import os
import sys
import signal
from typing import List, Callable, Optional, Any, Dict, Union

# Check if running on Windows
is_windows = os.name == 'nt'

if is_windows:
    import msvcrt
else:
    import termios
    import tty

class Menu:
    """Interactive CLI menu with selectable options."""
    
    def __init__(self, title: str = "Select an option:"):
        self.title = title
        self.options: List[Dict[str, Any]] = []
        self.selected_index = 0
        self._running = False
        self._setup_terminal()
    
    def _setup_terminal(self):
        """Set up terminal handling."""
        if not is_windows:
            # Store original terminal settings on Unix systems
            self.original_settings = termios.tcgetattr(sys.stdin)
        
        # Handle Ctrl+C gracefully
        signal.signal(signal.SIGINT, self._handle_interrupt)
    
    def _handle_interrupt(self, sig, frame):
        """Handle keyboard interrupt."""
        self._restore_terminal()
        sys.exit(0)
    
    def _restore_terminal(self):
        """Restore original terminal settings."""
        if not is_windows:
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.original_settings)
    
    def add_option(self, label: str, callback: Optional[Callable] = None, 
                  data: Any = None) -> None:
        """Add an option to the menu."""
        self.options.append({
            "label": label,
            "callback": callback,
            "data": data
        })
    
    def _getch_windows(self):
        """Windows-specific implementation of getch."""
        ch = msvcrt.getch()
        
        # Check for special keys (arrow keys)
        if ch == b'\xe0':
            # It's a special key, get the second byte
            ch2 = msvcrt.getch()
            # Return a tuple to indicate special key
            return ('special', ch2)
        
        # For normal keys, try to decode as ASCII
        try:
            return ('normal', ch.decode('ascii'))
        except UnicodeDecodeError:
            # If we can't decode, just return the raw byte
            return ('normal', ch)
    
    def _getch_unix(self):
        """Unix-specific implementation of getch."""
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
            
            # Check for escape sequence (arrow keys)
            if ch == '\x1b':
                # Read the next two characters
                ch2 = sys.stdin.read(1)
                ch3 = sys.stdin.read(1)
                
                # Return a tuple to indicate special key
                if ch2 == '[':
                    return ('special', ch3)
            
            return ('normal', ch)
        finally:
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.original_settings)
    
    def _getch(self):
        """Get a single character from the user."""
        if is_windows:
            return self._getch_windows()
        else:
            return self._getch_unix()
    
    def _render(self) -> None:
        """Render the menu to the terminal."""
        # Clear screen
        os.system('cls' if is_windows else 'clear')
        
        # Print title
        print(f"{self.title}\n")
        
        # Print options
        for i, option in enumerate(self.options):
            if i == self.selected_index:
                print(f">{option['label']}")
            else:
                print(f" {option['label']}")
        
        # Move cursor to the beginning
        sys.stdout.flush()
    
    def run(self) -> Any:
        """Run the interactive menu and return the selected option's result."""
        if not self.options:
            raise ValueError("No options added to the menu")
        
        self._running = True
        
        while self._running:
            self._render()
            
            # Get user input
            key_type, key = self._getch()
            
            if key_type == 'special':
                # Handle special keys (arrow keys)
                if is_windows:
                    if key == b'H':  # Up arrow on Windows
                        self.selected_index = max(0, self.selected_index - 1)
                    elif key == b'P':  # Down arrow on Windows
                        self.selected_index = min(len(self.options) - 1, self.selected_index + 1)
                else:
                    if key == 'A':  # Up arrow on Unix
                        self.selected_index = max(0, self.selected_index - 1)
                    elif key == 'B':  # Down arrow on Unix
                        self.selected_index = min(len(self.options) - 1, self.selected_index + 1)
            else:
                # Handle normal keys
                if is_windows:
                    if key == b'\r' or key == '\r':  # Enter key
                        selected = self.options[self.selected_index]
                        self._running = False
                        self._restore_terminal()
                        
                        if selected['callback']:
                            return selected['callback'](selected['data'])
                        return selected['data']
                    elif key == b'q' or key == 'q':  # Quit
                        self._running = False
                        self._restore_terminal()
                        return None
                else:
                    if key in ['\r', '\n']:  # Enter key
                        selected = self.options[self.selected_index]
                        self._running = False
                        self._restore_terminal()
                        
                        if selected['callback']:
                            return selected['callback'](selected['data'])
                        return selected['data']
                    elif key.lower() == 'q':  # Quit
                        self._running = False
                        self._restore_terminal()
                        return None
        
        self._restore_terminal()
        return None
