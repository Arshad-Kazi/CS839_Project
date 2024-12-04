import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLineEdit, QPushButton, QTextEdit, QLabel
)
from PyQt5.QtCore import Qt
from model_binding import prompt_model
from canvas import Canvas


class ChatBoxWidget(QWidget):
    def __init__(self, canvas, parent=None):
        super().__init__(parent)

        # Create UI components
        self.layout = QVBoxLayout()

        # Chat area (non-editable QTextEdit)
        self.chat_area = QTextEdit()
        self.chat_area.setReadOnly(True)  # Make chat area read-only
        self.chat_area.setStyleSheet("background-color: #f4f4f4;")

        # Input area with a QLineEdit and QPushButton
        self.input_layout = QHBoxLayout()
        self.text_box = QLineEdit()
        self.text_box.setPlaceholderText("Prompt ....")
        self.send_button = QPushButton("Draw")

        # Add components to input layout
        self.input_layout.addWidget(self.text_box)
        self.input_layout.addWidget(self.send_button)

        # Add components to the main layout
        self.layout.addWidget(QLabel("Prompt Box:"))
        self.layout.addWidget(self.chat_area)
        self.layout.addLayout(self.input_layout)
        

        # Set layout for the widget
        self.setLayout(self.layout)

        # Connect signals
        self.send_button.clicked.connect(self.handle_send)
        self.text_box.returnPressed.connect(self.handle_send)  # Press Enter to send
        
        # Canvas
        self.canvas = canvas
        
    

    def handle_send(self):
        message = self.text_box.text().strip()  # Get the input text
        if message:  # Check if the message is not empty
            self.chat_area.append(f"Prompt: {message}")  # Add message to chat area
            self.text_box.clear()  # Clear the input box
            
            # INFER YOUR MODEL HERE
            canvas_sketch = self.canvas.convert_pixmap_to_numpy()
            generated_image = prompt_model(message,canvas_sketch)
            self.canvas.update_image(generated_image)
            


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chatbox Example")
        self.setGeometry(100, 100, 500, 400)

        # Embed the ChatBoxWidget
        chat_widget = ChatBoxWidget(self)
        self.setCentralWidget(chat_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
