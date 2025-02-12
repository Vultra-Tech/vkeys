import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QSizePolicy
from PyQt6.QtCore import Qt
from pynput import keyboard

class VirtualKeyboard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Virtual Keyboard Highlighter")
        self.setFixedSize(900, 350)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)

        self.layout = QGridLayout()
        self.keys = {}
        self.create_keyboard()
        self.setLayout(self.layout)

        self.listener = keyboard.Listener(on_press=self.on_key_press, on_release=self.on_key_release)
        self.listener.start()

    def create_keyboard(self):
        key_layout = [
            ["Esc", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "Backspace"],
            ["Tab", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "|"],
            ["Caps", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Enter"],
            ["Shift", "Z", "X", "C", "V", "B", "N", "M", ",", ".", "/", "Shift"],
            ["Ctrl", "Alt", "Cmd", "Space"]
        ]

        key_sizes = {"Backspace": 120, "Tab": 90, "Caps": 100, "Enter": 100, "Shift": 120, "Space": 400}
        
        for row_idx, row in enumerate(key_layout):
            for col_idx, char in enumerate(row):
                label = QLabel(char)
                label.setStyleSheet("border: 2px solid white; font-size: 24px; padding: 10px; text-align: center;")
                label.setFixedSize(key_sizes.get(char, 60), 50)
                label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                label.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
                
                self.keys[char.lower()] = label
                self.layout.addWidget(label, row_idx, col_idx)

    def on_key_press(self, key):
        key_str = key.char.lower() if hasattr(key, 'char') and key.char else str(key).replace("Key.", "").lower()
        if key_str in self.keys:
            self.keys[key_str].setStyleSheet("background-color: yellow; border: 2px solid white; font-size: 24px; padding: 10px;")
    
    def on_key_release(self, key):
        key_str = key.char.lower() if hasattr(key, 'char') and key.char else str(key).replace("Key.", "").lower()
        if key_str in self.keys:
            self.keys[key_str].setStyleSheet("border: 2px solid white; font-size: 24px; padding: 10px;")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    keyboard_window = VirtualKeyboard()
    keyboard_window.show()
    sys.exit(app.exec())
