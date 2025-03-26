# CLIMenus

A simple and elegant framework for building interactive command-line menus in Python.

## Features

- Easy-to-use menu creation
- Customizable options and actions
- Clean and intuitive interface
- Simple integration with existing projects
- Color-coded menus for better readability
- Nested menu support
- Keyboard navigation

## Installation

```
pip install climenus
```

## Quick Start

```python
from climenus import Menu

# Create a menu
menu = Menu("Main Menu")

# Add options
menu.add_option("Option 1", lambda: print("Option 1 selected"))
menu.add_option("Option 2", lambda: print("Option 2 selected"))
menu.add_option("Exit", lambda: exit())

# Display the menu
menu.run()
```

## Examples

### Basic Menu

```python
from climenus import Menu

# Create a menu
menu = Menu("Main Menu")

# Add options
menu.add_option("Option 1", lambda: print("Option 1 selected"))
menu.add_option("Option 2", lambda: print("Option 2 selected"))
menu.add_option("Exit", lambda: exit())

# Display the menu
menu.run()
```

### Nested Menus

```python
from climenus import Menu

# Create main menu
main_menu = Menu("Main Menu")

# Create submenu
submenu = Menu("Settings")
submenu.add_option("Change Theme", lambda: print("Theme changed"))
submenu.add_option("Change Language", lambda: print("Language changed"))
submenu.add_option("Back", lambda: main_menu.run())

# Add options to main menu
main_menu.add_option("Start", lambda: print("Starting..."))
main_menu.add_option("Settings", lambda: submenu.run())
main_menu.add_option("Exit", lambda: exit())

# Start with the main menu
main_menu.run()
```

### Customized Menu

```python
from climenus import Menu

# Create a customized menu
menu = Menu(
    title="My Application",
    prompt="Select an option: ",
    header_color="blue",
    option_color="green"
)

# Add options
menu.add_option("Start Application", lambda: print("Starting..."))
menu.add_option("Settings", lambda: print("Opening settings..."))
menu.add_option("Help", lambda: print("Showing help..."))
menu.add_option("Exit", lambda: exit())

# Display the menu
menu.run()
```

### Menu with Dynamic Options

```python
from climenus import Menu

def get_dynamic_options():
    # This could fetch options from a database, API, etc.
    return ["Option A", "Option B", "Option C"]

# Create a menu with dynamic options
menu = Menu("Dynamic Menu")

# Add static options
menu.add_option("Static Option", lambda: print("Static option selected"))

# Add dynamic options
for option in get_dynamic_options():
    menu.add_option(option, lambda opt=option: print(f"{opt} selected"))

menu.add_option("Exit", lambda: exit())

# Display the menu
menu.run()
```

### Menu with Input Validation

```python
from climenus import Menu

def validate_input(value):
    try:
        # Try to convert to integer
        int(value)
        return True
    except ValueError:
        print("Please enter a valid number")
        return False

# Create a menu with input validation
menu = Menu("Input Menu", input_validator=validate_input)

menu.add_option("Option 1", lambda: print("Option 1 selected"))
menu.add_option("Option 2", lambda: print("Option 2 selected"))
menu.add_option("Exit", lambda: exit())

# Display the menu
menu.run()
```

## API Reference

### Menu Class

```python
Menu(title, prompt="Enter your choice: ", header_color="yellow", option_color="white", input_validator=None)
```

- `title`: The title of the menu
- `prompt`: The prompt text shown when asking for input
- `header_color`: Color of the menu title
- `option_color`: Color of the menu options
- `input_validator`: Optional function to validate user input

### Methods

- `add_option(text, action=None)`: Add an option to the menu
- `run()`: Display the menu and handle user input
- `clear()`: Clear the terminal screen
- `set_header_color(color)`: Change the header color
- `set_option_color(color)`: Change the option color
- `set_input_validator(validator)`: Set a function to validate user input

### Available Colors

The following colors are available for customization:
- black
- red
- green
- yellow
- blue
- magenta
- cyan
- white
- bright_black
- bright_red
- bright_green
- bright_yellow
- bright_blue
- bright_magenta
- bright_cyan
- bright_white

## Advanced Usage

### Creating a Menu System

```python
from climenus import Menu, MenuSystem # MenuSystem coming soon

# Create a menu system
system = MenuSystem("My Application")

# Create menus
main_menu = Menu("Main Menu")
settings_menu = Menu("Settings")
help_menu = Menu("Help")

# Add menus to the system
system.add_menu("main", main_menu)
system.add_menu("settings", settings_menu)
system.add_menu("help", help_menu)

# Add options to main menu
main_menu.add_option("Start", lambda: print("Starting..."))
main_menu.add_option("Settings", lambda: system.show_menu("settings"))
main_menu.add_option("Help", lambda: system.show_menu("help"))
main_menu.add_option("Exit", lambda: exit())

# Add options to settings menu
settings_menu.add_option("Change Theme", lambda: print("Theme changed"))
settings_menu.add_option("Change Language", lambda: print("Language changed"))
settings_menu.add_option("Back", lambda: system.show_menu("main"))

# Add options to help menu
help_menu.add_option("View Tutorial", lambda: print("Showing tutorial..."))
help_menu.add_option("About", lambda: print("About this application..."))
help_menu.add_option("Back", lambda: system.show_menu("main"))

# Start the menu system
system.start()
```

### Creating a Progress Menu

```python
from climenus import Menu, ProgressMenu # ProgressMenu coming soon

# Create a progress menu
progress_menu = ProgressMenu("Installation Progress")

# Add steps
progress_menu.add_step("Downloading files...", lambda: time.sleep(2))
progress_menu.add_step("Installing dependencies...", lambda: time.sleep(3))
progress_menu.add_step("Configuring settings...", lambda: time.sleep(1))
progress_menu.add_step("Cleaning up...", lambda: time.sleep(1))

# Run the progress menu
progress_menu.run()
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Development Setup

1. Clone the repository
   ```
   git clone https://github.com/vencordthemer/climenus.git
   ```

2. Install development dependencies
   ```
   pip install -e ".[dev]"
   ```

3. Run tests
   ```
   pytest
   ```

## License

MIT License

Copyright (c) 2023 VencordThemer

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
