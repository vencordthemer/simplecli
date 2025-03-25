import os
from typing import List, Any, Optional

def clear_screen() -> None:
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def create_simple_menu(title: str, options: List[str]) -> int:
    """
    Create and run a simple menu with string options.
    Returns the index of the selected option.
    """
    from .menu import Menu
    
    menu = Menu(title)
    for option in options:
        menu.add_option(option)
    
    result = menu.run()
    return menu.selected_index

def prompt(message: str, default: Optional[str] = None) -> str:
    """Prompt the user for input with an optional default value."""
    if default:
        result = input(f"{message} [{default}]: ") or default
    else:
        result = input(f"{message}: ")
    return result

def confirm(message: str, default: bool = True) -> bool:
    """Ask the user for confirmation."""
    if default:
        prompt_str = f"{message} [Y/n]: "
        result = input(prompt_str).lower()
        return result not in ('n', 'no')
    else:
        prompt_str = f"{message} [y/N]: "
        result = input(prompt_str).lower()
        return result in ('y', 'yes')
