from Model.edamam_API_connection import EdamameConnector
import view


class Controller:
    """The Controller class acts as an intermediary between the Model (EdamameConnector) and the View (view).
    It handles user commands and responses to provide appropriate messages to the user."""

    def __init__(self):
        """Initialize the Controller.

        The Controller creates instances of EdamameConnector for API communication
        and view.View for composing responses.
        """
        self.api_connector = EdamameConnector()
        self.view = view.View()

    def handle_start_command(self, update):
        """
        Handle the /start command.
        Args:
            update (object): Update object containing the user message information.

        Returns:
            str: The composed message for the /start command response.
        """
        return self.view.compose_start_message(update.message.chat.username)

    def handle_request_nutritional_information_command(self):
        """Handle the command to request nutritional information.

        Returns:
            str: The composed message to request nutritional information from the user.
        """
        return self.view.compose_nutritional_information_request_message()

    def handle_user_input_nutritional_information(self, update):
        """Handle the user input for nutritional information.

        Args:
            update (object): Update object containing the user message information.

        Returns:
            str: The composed message with nutritional information or a message indicating no data was found.
        """
        try:
            nutritional_information_json = self.api_connector.request_nutritional_information(update.message.text)
            response_message = self.view.compose_nutritional_information_response_message(nutritional_information_json)
            return response_message
        except Exception:
            return self.view.compose_nutrition_information_not_found_message()

    def handle_request_recipe_command(self):
        """Handle the command to request recipe information.

        Returns:
            str: The composed message to request recipe information from the user.
        """
        return self.view.compose_recipe_request_message()

    def handle_recipe_request(self, update):
        """Handle the user input for recipe information.

        Args:
            update (object): Update object containing the user message information.

        Returns:
            str: The composed message with recipe information or a message indicating no recipes were found.
        """
        recipe_information = self.api_connector.request_recipe_information(update.message.text)
        if recipe_information["count"] == 0:
            return self.view.compose_recipe_not_found_message()
        recipe_list = recipe_information['hits']
        return self.view.compose_returned_recipe_response_message(recipe_information, recipe_list)

    def handle_cancel_message(self):
        """Handle the cancel message.

        Returns:
            str: The composed message to bid farewell to the user and suggest further actions.
        """
        return self.view.compose_cancel_message()
