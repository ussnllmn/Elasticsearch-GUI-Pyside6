# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

import sys
import os
import json

from elasticsearch import Elasticsearch
from modules import *
from widgets import *

os.environ["QT_FONT_DPI"] = "96"  # FIX Problem for High DPI and Scale above 100%

# create a client instance of Elasticsearch
client = Elasticsearch("http://localhost:9200")

widgets = None

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))
        UIFunctions.uiDefinitions(self)

        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)

        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)
        self.show()
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))

        try:
            self.show_Client()
            self.show_Indices()
            self.show_Health()
            self.ui.Status_text.setText("Status: Connected")
        except:
            error_text = "Connection error. is elasticsearch.bat running ?"
            self.ui.Status_text.setText("Status: Disconnected")
            self.ui.client_text.setText(error_text)
            self.ui.Indices_text.setText(error_text)
            self.ui.Indices_text_2.setText(error_text)
            self.ui.Health_text_2.setText(error_text)

        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_search.clicked.connect(self.buttonClick)
        widgets.btn_document.clicked.connect(self.buttonClick)
        widgets.btn_index.clicked.connect(self.buttonClick)

        widgets.btn_search_doc.clicked.connect(self.buttonClick)

        widgets.btn_index_doc.clicked.connect(self.buttonClick)
        widgets.btn_delete_doc_id.clicked.connect(self.buttonClick)

        widgets.btn_create_index.clicked.connect(self.buttonClick)
        widgets.btn_delete_index.clicked.connect(self.buttonClick)

        widgets.btn_del_all.clicked.connect(self.buttonClick)

        widgets.Query_name.keyReleaseEvent = self.check_Enter

    def Create_index(self):
        try:
            resp = client.indices.create(index=self.ui.Create_index.text())
            self.ui.Result_text_2.setText("Index: " + self.ui.Create_index.text() + " is created.")
            self.show_Indices()
            json_resp = json.dumps(resp, indent=4)
            self.ui.Result_text_2.append(json_resp)
        except:
            self.ui.Result_text_2.setText("Index: " + self.ui.Create_index.text() + " is already exists can't create.")

    def Del_index(self):
        try:
            resp = client.indices.delete(index=self.ui.Delete_index.text())
            self.ui.Result_text_2.setText("Index: " + self.ui.Delete_index.text() + " is deleted.")
            self.show_Indices()
            json_resp = json.dumps(resp, indent=4)
            self.ui.Result_text_2.append(json_resp)
        except:
            self.ui.Result_text_2.setText("Index: " + self.ui.Delete_index.text() + " is not found can't delete.")

    def Del_doc(self):
        try:
            res = client.delete(index=self.ui.Index_doc.currentText(), id=self.ui.Delete_doc_id.text())
            self.ui.Result_text.setText("ID: " + res['_id'] + " is " + res['result'])
        except:
            self.ui.Result_text.setText("ID: " + self.ui.Delete_doc_id.text() + " is not found can't delete.")

    def Index_doc(self):
        try:
            doc = {
                'Title': self.ui.Title_index_doc.toPlainText(),
                'Content': self.ui.Content_index_doc.toPlainText(),
            }
            resp = client.index(index=self.ui.Index_doc.currentText(), id=self.ui.ID_index_doc.text(), document=doc)
            self.ui.Result_text.setText("ID: " + resp['_id'] + " is " + resp['result'] + ".")
            json_resp = json.dumps(resp, indent=4)
            self.ui.Result_text.append(json_resp)

        except:
            self.ui.Result_text.setText("Unknown error please try again.")

    def show_Health(self):
        health = client.cluster.health()
        json_health = json.dumps(health, indent=4)
        self.ui.Health_text_2.setText(json_health)

    def show_Indices(self):
        self.ui.Indices_text.setText("")
        self.ui.Indices_text_2.setText("")
        indices = client.indices.get_alias().keys()
        sortIndices = sorted(indices)
        for index in sortIndices:
            self.ui.Indices_text.append(index)
            self.ui.Indices_text_2.append(index)

    def show_Client(self):
        resp = client.info()
        json_resp = json.dumps(resp, indent=4)
        self.ui.client_text.setText(json_resp)

    def Del_ALL(self):
        if self.ui.Password_del_all.text() == "123456":
            all_indices = client.indices.get_alias().keys()
            self.ui.Result_text_2.setText("Attempting to delete " + str(len(all_indices)) + " indexes.")
            # iterate the list of indexes
            for _index in all_indices:
                # attempt to delete ALL indices in a 'try' and 'catch block
                try:
                    if "." not in _index: # avoid deleting indexes like `.kibana`
                        client.indices.delete(index=_index)
                        self.ui.Result_text_2.append("Successfully deleted: "+_index)
                except Exception as error:
                    self.ui.Result_text_2.append('indices.delete error: ' + str(error) + 'for index: ' + _index)
            self.show_Indices()
        elif self.ui.Password_del_all.text() == "":
            self.ui.Result_text_2.setText("Password field can't be empty.")
        else:
            self.ui.Result_text_2.setText("Incorrect password please try again.")

    def show_Query(self):
        self.ui.response_text.setText("")
        # pass the field name and query args to filter dict
        query = {
            'match': {
                self.ui.Field_combo.currentText(): self.ui.Query_name.text()
            }
        }
        index_name = self.ui.Index_name.text()
        # make sure that the user has entered an index name
        if index_name == "":
            self.ui.response_json.setText('{"error", "index name field cannot be empty"}')
        else:
            try:
                resp = client.search(index=index_name, query=query)
                json_resp = json.dumps(resp, indent=4)
                self.ui.response_json.setText(json_resp)
                self.ui.response_text.setText("Got %d Hits:" % resp['hits']['total']['value']+"\n")
                for hit in resp['hits']['hits']:
                    self.ui.response_text.append("ID: %(_id)s \nScore: %(_score)s" % hit)
                    self.ui.response_text.append("Title: %(Title)s \nContent: %(Content)s" % hit["_source"]+"\n")
            except:
                self.ui.response_text.setText("Query not found.")

    # BUTTONS CLICK
    def buttonClick(self):
        btn = self.sender()
        btnName = btn.objectName()

        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "btn_search":
            widgets.stackedWidget.setCurrentWidget(widgets.Search)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "btn_document":
            widgets.stackedWidget.setCurrentWidget(widgets.Document)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU

        if btnName == "btn_index":
            widgets.stackedWidget.setCurrentWidget(widgets.Index)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU

        if btnName == "btn_search_doc":
            self.show_Query()

        if btnName == "btn_index_doc":
            self.Index_doc()

        if btnName == "btn_delete_doc_id":
            self.Del_doc()

        if btnName == "btn_create_index":
            self.Create_index()

        if btnName == "btn_delete_index":
            self.Del_index()

        if btnName == "btn_del_all":
            self.Del_ALL()

    def check_Enter(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.show_Query()

    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPosition().toPoint()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("ES_icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())
