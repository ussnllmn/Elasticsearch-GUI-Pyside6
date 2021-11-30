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

        widgets.btn_google_search.clicked.connect(self.buttonClick)

        widgets.btn_search_doc_query.clicked.connect(self.buttonClick)
        widgets.btn_search_doc_id.clicked.connect(self.buttonClick)

        widgets.btn_index_doc.clicked.connect(self.buttonClick)
        widgets.btn_delete_doc_id.clicked.connect(self.buttonClick)

        widgets.btn_create_index.clicked.connect(self.buttonClick)
        widgets.btn_delete_index.clicked.connect(self.buttonClick)
        widgets.btn_search_doc_all.clicked.connect(self.buttonClick)
        widgets.btn_del_all.clicked.connect(self.buttonClick)

        widgets.Google_search.keyReleaseEvent = self.enter_Google
        widgets.Query_name.keyReleaseEvent = self.enter_Query
        widgets.Index_name_2.keyReleaseEvent = self.enter_searchALL
        widgets.ID_name.keyReleaseEvent = self.enter_ID
        widgets.Delete_doc_name.keyReleaseEvent = self.enter_delID
        widgets.Delete_doc_id.keyReleaseEvent = self.enter_delID
        widgets.Create_index.keyReleaseEvent = self.enter_creIn
        widgets.Delete_index.keyReleaseEvent = self.enter_delIn
        widgets.Password_del_all.keyReleaseEvent = self.enter_delALL

    def Search_Google(self):
        index_name = "no"
        search_text = self.ui.Google_search.text()

        BlueColor = QColor(130, 175, 255)
        WhiteColor = QColor(255, 255, 255)

        self.ui.Google_Result.setText("")
        query = {
          "query": {
            "multi_match": {
              "analyzer": "thai",
              "query": search_text,
              "fields": ["Title", "Content"]
            }
          }
        }
        if search_text == "":
            self.ui.Google_Result.setText("โปรดกรอกคำต้องการค้นหา")
        else:
            try:
                if search_text == "ทั้งหมด":
                    resp = client.search(index=index_name, query={"match_all": {}})
                else:
                    resp = client.search(index=index_name, body=query)
                self.ui.Google_Result.setFontUnderline(True)
                if resp['hits']['total']['value'] != 0:
                    self.ui.Google_Result.setText('พบ %d เอกสารสำหรับ "' % resp['hits']['total']['value'] + search_text + '"\n')
                else:
                    self.ui.Google_Result.setText('ไม่พบเอกสารที่เกี่ยวข้องกับ "' + search_text + '"')
                self.ui.Google_Result.setFontUnderline(False)
                for hit in resp['hits']['hits']:
                    self.ui.Google_Result.setTextColor(BlueColor)
                    self.ui.Google_Result.setFontPointSize(18)
                    self.ui.Google_Result.append("%(Title)s" % hit["_source"])

                    self.ui.Google_Result.setTextColor(WhiteColor)
                    self.ui.Google_Result.setFontPointSize(14)
                    self.ui.Google_Result.append("%(Content)s" % hit["_source"] + "\n")

            except:
                self.ui.Google_Result.setText("พบข้อผิดพลาดที่ไม่ทราบสาเหตุ")

    def Search_id(self):
        self.ui.response_text.setText("")
        index_name = self.ui.Index_name.text()
        ID = self.ui.ID_name.text()
        try:
            resp = client.get(index=index_name, id=self.ui.ID_name.text())
            json_resp = json.dumps(resp, indent=4)
            self.ui.response_json.setText(json_resp)
            self.ui.response_text.append("Index: " + index_name + "\nID: " + ID)
            self.ui.response_text.append("Title: %(Title)s\nContent: %(Content)s" % resp['_source'])
        except:
            self.ui.response_json.setText("Index: " + index_name + "\nID: " + ID + " not found.")
            self.ui.response_text.setText("Query not found.")

    def Search_query(self):
        self.ui.response_text.setText("")
        # pass the field name and query args to filter dict
        if self.ui.Field_combo.currentText() == "None":
            query = {
              "query": {
                "multi_match": {
                  "analyzer": "thai",
                  "query": self.ui.Query_name.text(),
                  "fields": ["Title", "Content"]
                }
              }
            }
        else:
            query = {
              "query": {
                "multi_match": {
                  "analyzer": "thai",
                  "query": self.ui.Query_name.text(),
                  "fields": [self.ui.Field_combo.currentText()]
                }
              }
            }

        index_name = self.ui.Index_name.text()
        # make sure that the user has entered an index name
        if index_name == "":
            self.ui.response_json.setText("Index name field cannot be empty")
            self.ui.response_text.setText("Got 0 Hits")
        else:
            try:
                resp = client.search(index=index_name, body=query)
                json_resp = json.dumps(resp, indent=4)
                self.ui.response_json.setText(json_resp)
                self.ui.response_text.setText("Got %d Hits:" % resp['hits']['total']['value'] + "\n")
                for hit in resp['hits']['hits']:
                    self.ui.response_text.append("ID: %(_id)s\nScore: %(_score)s" % hit)
                    self.ui.response_text.append("Title: %(Title)s\nContent: %(Content)s" % hit["_source"] + "\n")
            except:
                self.ui.response_text.setText("Query not found.")

    def Create_index(self):
        query = {
            "mappings": {
                "properties": {
                    "Title": {
                        "type": "text",
                        "analyzer": "thai"
                    },
                    "Content": {
                        "type": "text",
                        "analyzer": "thai"
                    }
                }
            }
        }
        try:
            resp = client.indices.create(index=self.ui.Create_index.text(), body=query)
            self.ui.Result_text_2.setText("Index: " + self.ui.Create_index.text() + " is created.")
            self.show_Indices()
            json_resp = json.dumps(resp, indent=4)
            self.ui.Result_text_2.append(json_resp)
        except:
            self.ui.Result_text_2.setText("Index: " + self.ui.Create_index.text() + " is already exists can't create.")

    def Delete_index(self):
        try:
            resp = client.indices.delete(index=self.ui.Delete_index.text())
            self.ui.Result_text_2.setText("Index: " + self.ui.Delete_index.text() + " is deleted.")
            self.show_Indices()
            json_resp = json.dumps(resp, indent=4)
            self.ui.Result_text_2.append(json_resp)
            # self.ui.Index_combo.removeItem(int(self.ui.Delete_index.text()))
        except:
            self.ui.Result_text_2.setText("Index: " + self.ui.Delete_index.text() + " is not found can't delete.")

    def Delete_doc(self):
        try:
            res = client.delete(index=self.ui.Delete_doc_name.text(), id=self.ui.Delete_doc_id.text())
            self.ui.Result_text.setText("ID: " + res['_id'] + " is " + res['result'])
        except:
            self.ui.Result_text.setText("ID: " + self.ui.Delete_doc_id.text() + " is not found can't delete.")

    def Index_doc(self):
        try:
            doc = {
                'Title': self.ui.Title_index_doc.toPlainText(),
                'Content': self.ui.Content_index_doc.toPlainText(),
            }
            resp = client.index(index=self.ui.Index_doc.text(), id=self.ui.ID_index_doc.text(), document=doc)
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

    def Delete_ALL(self):
        if self.ui.Password_del_all.text() == "123456":
            all_indices = client.indices.get_alias().keys()
            self.ui.Result_text_2.setText("Attempting to delete " + str(len(all_indices)) + " indexes.\n")
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

    def Search_ALL(self):
        self.ui.response_text.setText("")
        index_name = self.ui.Index_name_2.text()
        index_exists = client.indices.exists(index=index_name)
        if index_exists:
            try:
                resp = client.search(index=index_name, query={"match_all": {}})
                json_resp = json.dumps(resp, indent=4)
                self.ui.response_json.setText(json_resp)
                self.ui.response_text.setText("Got %d Hits:" % resp['hits']['total']['value'] + "\n")
                for hit in resp['hits']['hits']:
                    self.ui.response_text.append("ID: %(_id)s \nScore: %(_score)s" % hit)
                    self.ui.response_text.append("Title: %(Title)s \nContent: %(Content)s" % hit["_source"] + "\n")
            except:
                self.ui.response_text.setText("Query not found.")
        else:
            self.ui.response_json.setText("Index name: " + index_name + " does not exist.")
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

        if btnName == "btn_search_doc_query":
            self.Search_query()

        if btnName == "btn_search_doc_id":
            self.Search_id()

        if btnName == "btn_index_doc":
            self.Index_doc()

        if btnName == "btn_delete_doc_id":
            self.Delete_doc()

        if btnName == "btn_create_index":
            self.Create_index()

        if btnName == "btn_delete_index":
            self.Delete_index()

        if btnName == "btn_del_all":
            self.Delete_ALL()

        if btnName == "btn_search_doc_all":
            self.Search_ALL()

        if btnName == "btn_google_search":
            self.Search_Google()

    def enter_Google(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.Search_Google()

    def enter_searchALL(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.Search_ALL()

    def enter_Query(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.Search_query()

    def enter_ID(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.Search_id()

    def enter_delID(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.Delete_doc()

    def enter_creIn(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.Create_index()

    def enter_delIn(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.Delete_index()

    def enter_delALL(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.Delete_ALL()

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
