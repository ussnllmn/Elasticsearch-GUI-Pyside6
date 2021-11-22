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

        self.show_Client()
        self.show_Indices()
        self.show_Health()

        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_search.clicked.connect(self.buttonClick)
        widgets.btn_document.clicked.connect(self.buttonClick)
        widgets.btn_index.clicked.connect(self.buttonClick)

        widgets.btn_send.clicked.connect(self.buttonClick)

        widgets.btn_add_doc.clicked.connect(self.buttonClick)
        widgets.btn_update_doc.clicked.connect(self.buttonClick)
        widgets.btn_delete_doc_id.clicked.connect(self.buttonClick)

        widgets.btn_create_index.clicked.connect(self.buttonClick)
        widgets.btn_delete_index.clicked.connect(self.buttonClick)

        widgets.Query_name.keyReleaseEvent = self.check_Enter

    def Create_index(self):
        try:
            client.indices.create(index=self.ui.Create_index.text())
            self.ui.Result_text_2.setText("Index: " + self.ui.Create_index.text() + " is created.")
        except:
            self.ui.Result_text_2.setText("Index: " + self.ui.Create_index.text() + " is already exists can't create.")

    def Del_index(self):
        try:
            client.indices.delete(index=self.ui.Delete_index.text(), ignore=[400, 404])
            self.ui.Result_text_2.setText("Index: " + self.ui.Create_index.text() + " is deleted.")
        except:
            self.ui.Result_text_2.setText("Index: " + self.ui.Create_index.text() + " is not found can't delete.")

    def Update_doc(self):
        # try:
        doc = {
            self.ui.Field_update_doc.currentText(): self.ui.Data_update_doc,
        }
        res = client.update(index=self.ui.Index_doc.currentText(), id=self.ui.ID_update_doc, body=doc)
        self.ui.Result_text.setText("ID: " + res['_id'] + " is " + res['result'] + ".")

        # except:
        #     self.ui.Result_text.setText("Unknown error please try again.")

    def Del_doc(self):
        try:
            res = client.delete(index=self.ui.Index_doc.currentText(), id=self.ui.Delete_doc_id.text())
            self.ui.Result_text.setText("ID: " + res['_id'] + " is " + res['result'])
        except:
            self.ui.Result_text.setText("ID: " + self.ui.Delete_doc_id.text() + " is not found can't delete.")

    def Add_doc(self):
        try:
            doc = {
                'Title': self.ui.Title_add_doc.toPlainText(),
                'Content': self.ui.Content_add_doc.toPlainText(),
            }
            res = client.index(index=self.ui.Index_doc.currentText(), document=doc)
            # self.ui.Result_label.setText("ID: " + res['_id'] + " is " + res['result'])
            self.ui.Result_text.setText("ID: " + res['_id'] + " is " + res['result'] + ".")
            print(res)
        except:
            self.ui.Result_text.setText("Unknown error please try again.")

    def show_Query(self):
        self.ui.response_text.setText("")
        # pass the field name and query args to filter dict
        query = {
            'match': {
                self.ui.Field_combo.currentText(): self.ui.Query_name.text()
                # "age": 30
            }
        }
        # get the index name and put into a string variable
        index_name = self.ui.Index_combo.currentText()
        # make sure that the user has entered an index name
        if index_name == "":
            json_resp = '{"error", "index name field cannot be empty"}'
        else:
            # pass the filter dict to the make_query() function
            try:
                resp = self.make_Query(query, index_name)
                json_resp = json.dumps(resp, indent=4)
                print("Elasticsearch response:", resp)
                print("total hits:", len(resp["hits"]["hits"]))
            except:
                json_resp = "Cannot get response. is elasticsearch.bat running ?"
                print("Cannot get response. is elasticsearch.bat running ?")
        # change the label to match the Elasticsearch API response
        self.ui.response_json.setText(json_resp)

        try:
            # returns 4 different keys: "took", "timed_out", "_shards", and "hits"
            all_hits = resp["hits"]["hits"]
            i = 0
            # iterate the nested dictionaries inside the ["hits"]["hits"] list
            for num, doc in enumerate(all_hits):
                # self.ui.response_text.append("DOC ID:" + str(doc["_id"]) + "--->" + str(doc) + str(type(doc)))

                # Use 'iteritems()` instead of 'items()' if using Python 2
                for key, value in doc.items():
                    if key != "_source":
                        self.ui.response_text.append(key + " = " + str(value))

                self.ui.response_text.append("Title: " + all_hits[i]["_source"]["Title"])
                self.ui.response_text.append("Content: " + all_hits[i]["_source"]["Content"])
                self.ui.response_text.append("")
                i += 1

        except:
            self.ui.response_text.setText("Query not found.")
        # print(json.loads(json_resp)["hits"]["hits"][0]["_source"])

    def make_Query(self, query, index_name):
        # make an API call to check if the index exists
        index_exists = client.indices.exists(index=index_name)

        # if it exists then make the API call
        if index_exists:
            print("Index_name:", index_name, "exists.")
            print("Query:", query, "\n")

            # catch any exceptions and return them to Kivy app
            try:
                # pass filter query to the client's search() method
                response = client.search(index=index_name, query=query)

                # print the query response for debugging purposes
                print('response["hits"]:', len(response["hits"]))
                print('response TYPE:', type(response))

            except Exception as err:
                print("search() index ERROR", err)
                response = {"error": str(err)}

        # error text response if index doesn't exist
        else:
            # build a string for the index-does-not-exist response
            resp_text = "Elasticsearch index name '" + str(index_name)
            resp_text += "' does not exist."
            response = {"response": resp_text}

        # return the dict response to Kivy app
        return response

    def show_Health(self):
        health = client.cluster.health()
        json_health = json.dumps(health, indent=4)
        self.ui.Health_text_2.setText(json_health)

    def show_Indices(self):
        indices = client.indices.get_alias().keys()
        sortIndices = sorted(indices)
        for index in sortIndices:
            self.ui.Indices_text.append(index)
            self.ui.Indices_text_2.append(index)

    def show_Client(self):
        try:
            print("Connecting to http://localhost:9200")
            resp = client.info()
            json_resp = json.dumps(resp, indent=4)
            widgets.client_text.setText(json_resp)
            print("Connection complete")
        except:
            print("Connection error. is elasticsearch.bat running ?")
            widgets.client_text.setText("Connection error. is elasticsearch.bat running ?")

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

        if btnName == "btn_send":
            self.show_Query()

        if btnName == "btn_add_doc":
            self.Add_doc()

        if btnName == "btn_delete_doc_id":
            self.Del_doc()

        if btnName == "btn_update_doc":
            self.Update_doc()

        if btnName == "btn_create_index":
            self.Create_index()

        if btnName == "btn_delete_index":
            self.Del_index()

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
