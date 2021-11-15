#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# import the JSON library to prettify the API response
import json

# import the Elasticsearch client library
from elasticsearch import Elasticsearch

# import the necessary UIX libraries for the Kivy app
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

# import the FloatLayout library for UIX widget's location
from kivy.uix.floatlayout import FloatLayout

# import the Config library to set window size
from kivy.config import Config

# create a client instance of Elasticsearch
client = Elasticsearch("http://localhost:9200")

# set the app's window size with Config
Config.set('graphics', 'width', '1024')
Config.set('graphics', 'height', '1536')

# define a function for the Elasticsearch query API call
def make_query(filter, index_name):

    # make an API call to check if the index exists
    index_exists = client.indices.exists(index=index_name)

    # if it exists then make the API call
    if index_exists == True:
        print ("index_name:", index_name, "exists.")
        print ("FILTER:", filter, "\n")

        # catch any exceptions and return them to Kivy app
        try:
            # pass filter query to the client's search() method
            response = client.search(index=index_name, body=filter)

            # print the query response for debugging purposes
            print ('response["hits"]:', len(response["hits"]))
            print ('response TYPE:', type(response))

        except Exception as err:
            print ("search() index ERROR", err)
            response = {"error": str(err)}

    # error text response if index doesn't exist
    else:
        # build a string for the index-does-not-exist response
        resp_text = "Elasticsearch index name '" + str(index_name)
        resp_text += "' does not exist."
        response = {"response": resp_text}

    # return the dict response to Kivy app
    return response

# declare the class for the Kivy app
class Elastic(FloatLayout):
    def __init__(self,**kwargs):
        #global es

        # use Python's built-in super() function to get class attr
        super(Elastic, self).__init__(**kwargs)

        # Button field to initiate the query to Elasticsearch
        label_pos = {'x': 0.05, 'y': 0.92}
        self.title_label = Label(
            text = "ObjectRocket Elasticsearch Query App",
            size_hint = (0.9, 0.07),
            pos_hint = label_pos,
            font_size ='36sp'
        )
        self.add_widget(self.title_label)

        # TextInput field for the Elasticsearch index name
        input_pos = {'x': 0.05, 'y': 0.87}
        self.index_input = TextInput(
            text = "Index Name",
            size_hint = (0.9, 0.05),
            pos_hint = input_pos,
            font_size ='38sp'
        )
        self.add_widget(self.index_input)

        # Button field to initiate the query to Elasticsearch
        button_pos = {'x': 0.05, 'y': 0.75}
        self.query_button = Button(
            text = "Make Query Request",
            size_hint = (0.9, 0.1),
            pos_hint = button_pos,
            font_size ='36sp',
            on_press = self.update
        )
        self.add_widget(self.query_button)

        # TextInput field for the Elasticsearch query match
        input_pos = {'x': 0.05, 'y': 0.66}
        self.field_input = TextInput(
            text = "Field name here..",
            size_hint = (0.45, 0.07),
            pos_hint = input_pos,
            font_size ='38sp'
        )
        self.add_widget(self.field_input)

        # TextInput field for the Elasticsearch query match
        input_pos = {'x': 0.50, 'y': 0.66}
        self.query_input = TextInput(
            text = "Query match here..",
            size_hint = (0.45, 0.07),
            pos_hint = input_pos,
            font_size ='38sp'
        )
        self.add_widget(self.query_input)

        # Label field for the Elasticsearch query results
        self.query_results = Label(
            text = "",
            font_size ='32sp',
            # change the color of response font
            color = [105, 106, 188, 1],
        )
        self.add_widget(self.query_results)

    def update(self, val):

        # pass the field name and query args to filter dict
        filter = {
            'query': {
                'match': {
                    self.field_input.text: self.query_input.text
                }
            }
        }

        # get the index name and put into a string variable
        index_name = self.index_input.text

        # make sure that the user has entered an index name
        if len(index_name) == 0 or index_name == "":
            json_resp = '{"error", "index name field cannot be empty"}'
        else:
            # pass the filter dict to the make_query() function
            resp = make_query(filter, index_name)
            json_resp = json.dumps(resp, indent=4)
            print ("Elasticsearch response:", resp)

        # change the label to match the Elasticsearch API response
        self.query_results.text = json_resp
        self.query_results.size_hint = (0.9, 0.4)
        self.query_results.pos_hint = {'x':0.01, 'y':0.10}

class ElasticApp(App):
    title = 'ObjectRocket Elasticsearch App'

    def build(self):
        return Elastic()

if __name__ == "__main__":
     ElasticApp().run()