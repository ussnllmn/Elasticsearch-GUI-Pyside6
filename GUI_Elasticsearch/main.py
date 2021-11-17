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

# import the Elasticsearch client library
from elasticsearch import Elasticsearch
# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%
# define a function for the Elasticsearch query API call

# create a client instance of Elasticsearch
client = Elasticsearch("http://localhost:9200")

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
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

        # SHOW client.info()
        try:
            print("Connecting to http://localhost:9200")
            resp = client.info()
            json_resp = json.dumps(resp, indent=4)
            widgets.client_text.setText(json_resp)
            print("Connection complete")
        except:
            print("Connection error. is elasticsearch.bat running ?")
            widgets.client_text.setText("Connection error. is elasticsearch.bat running ?")

        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_search.clicked.connect(self.buttonClick)
        widgets.btn_add_data.clicked.connect(self.buttonClick)
        widgets.btn_send.clicked.connect(self.buttonClick)

        widgets.Q_name.keyReleaseEvent = self.check_enter

    def show_query(self):
        # pass the field name and query args to filter dict
        filter = {

            'match': {
                self.ui.Field_combo.currentText(): self.ui.Q_name.text()
            }
        }
        # get the index name and put into a string variable
        index_name = self.ui.Index_combo.currentText()

        # print("index_input", self.ui.Index_combo.currentText())
        # print("field_input", self.ui.Field_combo.currentText())
        # print("query_input", self.ui.Q_name.text())

        # make sure that the user has entered an index name
        if index_name == "":
            json_resp = '{"error", "index name field cannot be empty"}'
        else:
            # pass the filter dict to the make_query() function
            try:
                resp = self.make_query(filter, index_name)
                json_resp = json.dumps(resp, indent=4)
                print("Elasticsearch response:", resp)
            except:
                json_resp = "Cannot get response. is elasticsearch.bat running ?"
                print("Cannot get response. is elasticsearch.bat running ?")
        # change the label to match the Elasticsearch API response
        self.ui.response_json.setText(json_resp)
        try:
            self.ui.response_text.setText("Firstname: "+json.loads(json_resp)["hits"]["hits"][0]["_source"]["firstname"])
            self.ui.response_text.append("Lastname: "+json.loads(json_resp)["hits"]["hits"][0]["_source"]["lastname"])
            self.ui.response_text.append("Gender: "+json.loads(json_resp)["hits"]["hits"][0]["_source"]["gender"])
        except:
            self.ui.response_text.setText("Query not found.")
        # print(json.loads(json_resp)["hits"]["hits"][0]["_source"])

    def make_query(self, filter, index_name):

        # make an API call to check if the index exists
        index_exists = client.indices.exists(index=index_name)

        # if it exists then make the API call
        if index_exists:
            print("index_name:", index_name, "exists.")
            print("FILTER:", filter, "\n")

            # catch any exceptions and return them to Kivy app
            try:
                # pass filter query to the client's search() method
                response = client.search(index=index_name, query=filter, format='csv')

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

    # BUTTONS CLICK
    def buttonClick(self):
        btn = self.sender()
        btnName = btn.objectName()

        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)

        if btnName == "btn_search":
            widgets.stackedWidget.setCurrentWidget(widgets.Search)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "btn_add_data":
            widgets.stackedWidget.setCurrentWidget(widgets.Add_Data) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU

        if btnName == "btn_send":
            self.show_query()

    def check_enter(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.show_query()

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