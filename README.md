# SimpleCLI

A simple, intuitive framework for building interactive command-line menus in Python.

## Installation

```bash
pip install simplecli
```

## Usage

### Basic Menu

```python
from interactivecli import Menu

# Create a menu
menu = Menu("Welcome to the CLI!")

# Add options
menu.add_option("Option1")
menu.add_option("Option2")
menu.add_option("Option3")

# Run the menu
result = menu.run()
```

### Menu with Callbacks

```python
from interactivecli import Menu

def option1_action(data):
    print("You selected Option 1!")
    return "Option 1 result"

def option2_action(data):
    print("You selected Option 2!")
    return "Option 2 result"

# Create a menu
menu = Menu("Select an action:")

# Add options with callbacks
menu.add_option("Run Option 1", option1_action)
menu.add_option("Run Option 2", option2_action)
menu.add_option("Exit")

# Run the menu
result = menu.run()
print(f"Result: {result}")
```

### Simple Menu Helper

```python
from interactivecli import create_simple_menu

options = ["Red", "Green", "Blue", "Yellow"]
selected_index = create_simple_menu("Choose a color:", options)

print(f"You selected: {options[selected_index]}")
```

### Other Utilities

```python
from interactivecli import prompt, confirm, clear_screen

# Clear the terminal
clear_screen()

# Get user input
name = prompt("Enter your name")
age = prompt("Enter your age", default="30")

# Get confirmation
if confirm("Are you sure you want to continue?"):
    print("Continuing...")
else:
    print("Operation cancelled.")
```

## Features

- Interactive arrow-key navigation
- Customizable menu titles and options
- Support for callbacks on selection
- Helper functions for common CLI tasks
- Clean, intuitive API

## License

MIT
```

## Example Usage

Here's a complete example of how to use your module:

```python
# example_menu.py
from interactivecli import Menu, clear_screen

def main():
    # Create the main menu
    main_menu = Menu("Welcome to the CLI!")
    
    # Add options
    main_menu.add_option("Show Information", show_info)
    main_menu.add_option("Configure Settings", configure_settings)
    main_menu.add_option("Run Process", run_process)
    main_menu.add_option("Exit")
    
    # Run the menu
    result = main_menu.run()
    
    if result is None:
        print("Goodbye!")

def show_info(data):
    clear_screen()
    print("Application Information")
    print("======================")
    print("Version: 1.0.0")
    print("Author: Your Name")
    print("License: MIT")
    print("\nPress Enter to return to the main menu...")
    input()
    return main()

def configure_settings(data):
    # Create a submenu for settings
    settings_menu = Menu("Configure Settings:")
    
    settings_menu.add_option("General Settings", lambda d: handle_setting("General"))
    settings_menu.add_option("User Settings", lambda d: handle_setting("User"))
    settings_menu.add_option("Advanced Settings", lambda d: handle_setting("Advanced"))
    settings_menu.add_option("Back to Main Menu")
    
    result = settings_menu.run()
    return main()

def handle_setting(setting_type):
    clear_screen()
    print(f"{setting_type} Settings")
    print("=" * (len(setting_type) + 9))
    print(f"You are now configuring {setting_type.lower()} settings.")
    print("\nPress Enter to return...")
    input()

def run_process(data):
    clear_screen()
    print("Running Process...")
    print("=================")
    
    # Simulate a process
    for i in range(10):
        print(f"Step {i+1}/10 completed...")
        import time
        time.sleep(0.5)
    
    print("\nProcess completed successfully!")
    print("\nPress Enter to return to the main menu...")
    input()
    return main()

if __name__ == "__main__":
    main()
```

To run this example:

```bash
python example_menu.py
```

This will display an interactive menu that looks like:

```
Welcome to the CLI!

>Show Information
 Configure Settings
 Run Process
 Exit
