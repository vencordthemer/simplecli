import inquirer
from typing import List, Dict, Any, Union, Optional

def select(message: str, choices: List[str], default: Optional[str] = None) -> str:
    """
    Display an interactive selection menu and return the selected option.
    
    Args:
        message: The prompt message to display
        choices: List of choices to select from
        default: Default selected option
        
    Returns:
        The selected option as a string
    """
    questions = [
        inquirer.List('result',
                      message=message,
                      choices=choices,
                      default=default)
    ]
    
    answers = inquirer.prompt(questions)
    return answers['result']

def checkbox(message: str, choices: List[str], default: Optional[List[str]] = None) -> List[str]:
    """
    Display an interactive checkbox menu and return the selected options.
    
    Args:
        message: The prompt message to display
        choices: List of choices to select from
        default: Default selected options
        
    Returns:
        List of selected options
    """
    questions = [
        inquirer.Checkbox('result',
                          message=message,
                          choices=choices,
                          default=default)
    ]
    
    answers = inquirer.prompt(questions)
    return answers['result']

def confirm(message: str, default: bool = True) -> bool:
    """
    Display a confirmation prompt and return the result.
    
    Args:
        message: The prompt message to display
        default: Default value (True/False)
        
    Returns:
        Boolean result of the confirmation
    """
    questions = [
        inquirer.Confirm('result',
                         message=message,
                         default=default)
    ]
    
    answers = inquirer.prompt(questions)
    return answers['result']

def text(message: str, default: str = "") -> str:
    """
    Display a text input prompt and return the entered text.
    
    Args:
        message: The prompt message to display
        default: Default text value
        
    Returns:
        Entered text
    """
    questions = [
        inquirer.Text('result',
                      message=message,
                      default=default)
    ]
    
    answers = inquirer.prompt(questions)
    return answers['result']

def password(message: str) -> str:
    """
    Display a password input prompt and return the entered password.
    
    Args:
        message: The prompt message to display
        
    Returns:
        Entered password
    """
    questions = [
        inquirer.Password('result',
                          message=message)
    ]
    
    answers = inquirer.prompt(questions)
    return answers['result']
