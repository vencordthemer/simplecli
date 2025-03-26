# CLIMenus

A simple and elegant framework for building interactive command-line menus in Python.

## Features

- Easy-to-use menu creation
- Customizable options and actions
- Clean and intuitive interface
- Simple integration with existing projects

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

## License

MIT License
