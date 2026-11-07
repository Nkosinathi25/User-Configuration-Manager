# User-Configuration-Manager
Users get to store, update, delete and view their settings and manage default configuration values. Developed as part of my freeCodeCamp Python learning journey.
User Configuration Manager 🛠️

Project Overview

The User Configuration Manager is a Python project developed as part of my freeCodeCamp learning journey.

This application allows users to manage configuration settings by adding new settings, updating existing ones, deleting settings, and viewing all available settings.

The project demonstrates my understanding of Python programming fundamentals and dictionary manipulation.

Features

- Add Settings: Add new configuration settings.
- Update Settings: Modify existing configuration values.
- Delete Settings: Remove unwanted configuration settings.
- View Settings: Display all currently stored settings.
- Input Handling: Convert setting keys and values to lowercase for consistency.
- Error Handling: Provide feedback when attempting to add duplicate settings or update settings that do not exist.

Technologies Used

- Python 3
- Python Dictionaries
- Functions
- Conditional Statements
- For Loops
- String Methods

Example

test_settings = {
    "theme": "dark",
    "notifications": "enabled",
    "volume": "high",
    "language": "english"
}

Example operations:

add_setting(test_settings, ("Brightness", "High"))

update_setting(test_settings, ("Language", "Spanish"))

delete_setting(test_settings, "volume")

print(view_settings(test_settings))

What I Learned

Through this project, I improved my understanding of:

1. Creating and calling Python functions.
2. Working with dictionaries and key-value pairs.
3. Using conditional statements.
4. Iterating through dictionaries.
5. Updating and deleting dictionary elements.
6. Using Python string methods.
7. Writing reusable and organised code.

How to Run

1. Clone this repository.
2. Make sure Python 3 is installed.
3. Open the project folder in your code editor.
4. Run the Python file:

python main.py

Author

Developed as part of my Python programming journey and practical software development learning through freeCodeCamp.

Acknowledgements

Thanks to freeCodeCamp for providing practical programming exercises that help develop my Python programming skills.
