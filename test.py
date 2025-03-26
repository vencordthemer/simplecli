from cli import Menu, MenuSystem

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