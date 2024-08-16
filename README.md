Overview
This project is a simple Telegram bot built using the pyTelegramBotAPI library (telebot). The bot performs basic user registration by storing user details in a PostgreSQL database. It allows users to send their contact details (phone number) and stores them in a database. The bot also provides basic interaction and logging.

Features
User Registration: New users are prompted to share their contact details, which are then stored in the PostgreSQL database.
Database Management: The bot checks whether the user is already registered, and if not, it inserts the user's details into the database.
Logging: Application events and errors are logged to both a file (bot.log) and the console.
Project Structure
bot.py: The main file containing the bot's logic and functionality.
core/settings.py: Contains sensitive data such as the bot's API token (TOKEN) and the PostgreSQL connection (PGCONN).
Setup
Prerequisites
Python .10.12
PostgreSQL database
pip for managing Python packages
Installation
Clone the repository:

bash
Копировать код
git clone <repository_url>
cd <repository_directory>
Install required Python packages:

bash
Копировать код
pip install pyTelegramBotAPI psycopg2-binary
Set up PostgreSQL:

Create a PostgreSQL database.
Create a user with the necessary privileges.
Update the core/settings.py file with the TOKEN and PGCONN settings.
Running the Bot
Run the bot using the following command:

bash
Копировать код
python bot.py
Usage
Start the bot: Send the /start command to the bot. If you are not registered, the bot will prompt you to share your contact information.
Register: Share your phone number with the bot. The bot will store your details in the database and confirm the registration.
Logging
All logs are stored in the bot.log file and also displayed in the console. The logs include information about user registrations, database operations, and any errors that occur.

Error Handling
The bot is designed to catch exceptions during its operation and log them for debugging purposes. If any error occurs, it will be logged in the bot.log file.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Contributing
Feel free to contribute to this project by submitting pull requests or opening issues.