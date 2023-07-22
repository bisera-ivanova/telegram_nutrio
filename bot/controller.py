import sys
from view import View

from telegram_nutrio.Model.edamam_API_connection import EdamameConnector

view = View()


class Controller:

    def __init__(self):
        self.api_connector = EdamameConnector()

    def handle_start_command(self, update, context):
        return view.compose_start_message(update.message.chat.username)

    def handle_request_nutritional_information_command(self, update, context):
        return view.compose_nutritional_information_request_message()

    def handle_user_input_nutritional_information(self, update, context):

        nutritional_information_json = self.api_connector.request_nutritional_information(update.message.text)
        response_message = view.compose_nutritional_information_response_message(nutritional_information_json)
        return response_message

    def handle_recipe_request(self, update, context):
        recipe_information = self.api_connector.request_recipe_information(update.message.text)
        for recipe in recipe_information['hits']:
            response_message = view.compose_returned_recipe_response_message(recipe_information, recipe)
            return response_message



    def handle_commands(self):
        pass

    def handle_messages(self):
        pass


