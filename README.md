# NutrioBot Project

NutrioBot is a Telegram bot that provides nutritional information and recipe recommendations based on user input. The bot interacts with the Edamam API to fetch data and composes responses using a View class. The project follows the Singleton pattern for certain classes to ensure only one instance is created. Additionally, logging is implemented to keep track of bot interactions and user messages. The project is designed using the Model-View-Controller (MVC) architecture pattern to separate concerns and ensure maintainability.

## Files

The project consists of the following files:

1. **bot.py**: This file contains the main code for the Telegram bot. It sets up the conversation handlers, handles user commands and inputs, and manages the bot's responses.

2. **controller.py**: The controller file acts as an intermediary between the Model and the View. It handles user commands and communicates with the Edamam API to fetch nutritional information and recipe data.

3. **Model/edamam_API_connector.py**: This file contains the EdamameConnector class, which is responsible for handling communication with the Edamam API. It has methods to request nutritional information and recipe data based on user input.

4. **Model/logger.py**: The logger.py file defines the Logger class, which provides logging capabilities to record bot interactions and user messages. It stores the logs in the 'app.log' file.

5. **view.py**: The view.py file defines the View class, which composes responses for the bot. It contains methods to create different messages based on API responses and user commands.

## Implemented Design Patterns

The NutrioBot project utilizes the following design patterns:

1. **Singleton Pattern**: The Singleton pattern is used for the `View`, `EdamameConnector`, and `Bot` classes to ensure that only one instance of these classes is created. The pattern ensures that all interactions with these classes are handled through the same instance, avoiding unnecessary duplication.

## Implemented Architecture Pattern

The NutrioBot project follows the Model-View-Controller (MVC) architecture pattern. The MVC pattern is implemented as follows:

1. **Model**: The Model is represented by the `EdamameConnector` class, which handles communication with the Edamam API to fetch nutritional information and recipe data.

2. **View**: The View is represented by the `View` class, which composes responses for the bot based on the data received from the Model (Edamam API) and user commands.

3. **Controller**: The Controller is represented by the `Controller` class, which acts as an intermediary between the Model and the View. It handles user commands, communicates with the Edamam API, and composes responses using the View.

The MVC architecture pattern ensures a clear separation of concerns and promotes maintainability, as each component has its specific role and responsibilities.

## How to Run the Bot

To run the NutrioBot, follow these steps:

1. Clone the repository: `git clone https://github.com/bisera-ivanova/telegram_nutrio.git`

2. Install the required dependencies: `pip install -r requirements.txt`

3. Set up environment variables: Create a `.env` file and add the necessary credentials for the Edamam API and Telegram API.

4. Run the bot: Execute the `main()` function in the `bot.py` file.

5. Interact with the bot on Telegram: Start a chat with the bot and send commands like `/start`, or request nutritional information or recipe recommendations.


