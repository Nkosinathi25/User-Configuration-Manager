test_settings = {
    'theme': 'white',
    'notifications': 'enabled',
    'volume': 'low',
    'language': 'english'   
}

def add_setting(settings, new_setting):
    key, value = new_setting
    key = key.lower()
    value = value.lower()

    if key in settings:
       return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
       settings[key] = value
       return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings, new_setting):
    key, value = new_setting
    key = key.lower()
    value = value.lower()

    if key in settings:
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings, key):
    key = key.lower()
    
    if key in settings:
        del settings[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"

def view_settings(settings):
    if not settings:
        return "No settings available."

    settings_str = "Current User Settings:\n"
    for key, value in settings.items():
        settings_str += f"{key.capitalize()}: {value}\n"
    return settings_str

print(add_setting(test_settings, ('Brightness', 'High')))
print(update_setting(test_settings, ('Language', 'Spanish')))
print(delete_setting(test_settings, 'Volume'))
print(view_settings(test_settings))