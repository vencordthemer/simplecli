import sys
import inspect
from typing import Dict, List, Callable, Optional, Any, Union, Type
from .command import Command, Option
from .utils import format_help

class CLI:
    """Main CLI class that manages commands and handles command execution."""
    
    def __init__(self, name: str, description: str = ""):
        self.name = name
        self.description = description
        self.commands: Dict[str, Command] = {}
        self.default_command: Optional[str] = None
        self.global_options: List[Option] = []
    
    def command(self, name: Optional[str] = None, description: str = "", 
                default: bool = False) -> Callable:
        """Decorator to register a function as a CLI command."""
        def decorator(func: Callable) -> Callable:
            cmd_name = name or func.__name__
            cmd = Command(cmd_name, func, description, self.global_options)
            self.commands[cmd_name] = cmd
            
            if default:
                self.default_command = cmd_name
                
            return func
        return decorator
    
    def get_command(self, name: str) -> Optional[Command]:
        """Get a command by name."""
        return self.commands.get(name)
    
    def option(self, *args, **kwargs) -> Callable:
        """Add a global option that applies to all commands."""
        option = Option(*args, **kwargs)
        self.global_options.append(option)
        
        def decorator(func: Callable) -> Callable:
            return func
        return decorator
    
    def run(self, args: Optional[List[str]] = None) -> Any:
        """Run the CLI with the given arguments."""
        if args is None:
            args = sys.argv[1:]
        
        if not args and self.default_command:
            return self.commands[self.default_command].execute([])
        
        if not args or args[0] in ['-h', '--help']:
            return self._show_help()
        
        command_name = args[0]
        if command_name not in self.commands:
            print(f"Unknown command: {command_name}")
            return self._show_help()
        
        return self.commands[command_name].execute(args[1:])
    
    def _show_help(self) -> None:
        """Display help information for the CLI."""
        print(format_help(self.name, self.description, self.commands, self.global_options))


