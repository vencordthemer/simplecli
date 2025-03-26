import inspect
import argparse
from typing import Callable, List, Any, Dict, Optional, Union, Type, Sequence

class Option:
    """Represents a command-line option."""
    
    def __init__(self, *names, type=str, default=None, help="", required=False, 
                 choices=None, action=None, dest=None):
        self.names = names
        self.type = type
        self.default = default
        self.help = help
        self.required = required
        self.choices = choices
        self.action = action
        self.dest = dest or (names[0].lstrip('-').replace('-', '_') if names else None)
        
    def add_to_parser(self, parser: argparse.ArgumentParser) -> None:
        """Add this option to an argument parser."""
        kwargs = {
            'dest': self.dest,
            'help': self.help,
            'required': self.required
        }
        
        # Handle different types of options
        if self.action:
            kwargs['action'] = self.action
        elif isinstance(self.default, bool):
            kwargs['action'] = 'store_true' if not self.default else 'store_false'
        else:
            kwargs['type'] = self.type
            kwargs['default'] = self.default
            if self.choices:
                kwargs['choices'] = self.choices
        
        parser.add_argument(*self.names, **kwargs)

class Command:
    """Represents a CLI command with its arguments and options."""
    
    def __init__(self, name: str, func: Callable, description: str = "", 
                 global_options: List[Option] = None):
        self.name = name
        self.func = func
        self.description = description or func.__doc__ or ""
        self.global_options = global_options or []
        self.options: List[Option] = []
        self._parser = None  # Lazy initialization
    
    def option(self, *args, **kwargs) -> 'Command':
        """Add an option to this command and return self for chaining."""
        option = Option(*args, **kwargs)
        self.options.append(option)
        self._parser = None  # Reset parser so it will be rebuilt
        return self
    
    def _build_parser(self) -> argparse.ArgumentParser:
        """Build an argument parser based on the function signature and options."""
        parser = argparse.ArgumentParser(
            prog=self.name,
            description=self.description,
            add_help=False
        )
        
        # Add global options
        for option in self.global_options:
            option.add_to_parser(parser)
        
        # Add command-specific options
        for option in self.options:
            option.add_to_parser(parser)
        
        # Add options from function signature
        sig = inspect.signature(self.func)
        for param_name, param in sig.parameters.items():
            if param_name == 'self':  # Skip 'self' for class methods
                continue
                
            # Skip parameters that already have options defined
            if any(opt.dest == param_name for opt in self.options + self.global_options):
                continue
                
            # Handle positional arguments
            if param.default is inspect.Parameter.empty:
                parser.add_argument(param_name)
            else:
                # Handle optional arguments
                arg_name = f"--{param_name}"
                short_name = f"-{param_name[0]}"
                
                kwargs = {
                    "dest": param_name,
                    "default": param.default,
                    "help": f"Default: {param.default}"
                }
                
                # Handle boolean flags
                if isinstance(param.default, bool):
                    kwargs["action"] = "store_true" if not param.default else "store_false"
                    if param.default:
                        arg_name = f"--no-{param_name}"
                        short_name = None
                
                # Add the argument
                if short_name:
                    parser.add_argument(short_name, arg_name, **kwargs)
                else:
                    parser.add_argument(arg_name, **kwargs)
        
        return parser
    
    def get_parser(self) -> argparse.ArgumentParser:
        """Get the argument parser for this command, creating it if needed."""
        if self._parser is None:
            self._parser = self._build_parser()
        return self._parser
    
    def execute(self, args: List[str]) -> Any:
        """Execute the command with the given arguments."""
        parser = self.get_parser()
        
        if '-h' in args or '--help' in args:
            parser.print_help()
            return None
            
        parsed_args = parser.parse_args(args)
        kwargs = vars(parsed_args)
        
        return self.func(**kwargs)
