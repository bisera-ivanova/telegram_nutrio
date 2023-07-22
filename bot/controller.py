from view import View

view = View()


class Controller:

    def __init__(self):
        pass

    def handle_start_command(self, update, context):
        return view.compose_start_message(update.message.chat.username)

    def handle_request_nutritional_information(self, update, context):
        return view.compose_nutritional_information_request_message()

    def handle_commands(self):
        pass

    def handle_messages(self):
        pass


class _ReminderSetter:
    def __init__(self):
        pass
