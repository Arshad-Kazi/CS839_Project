import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton,
    QColorDialog, QHBoxLayout, QLabel
)
from PyQt5.QtGui import QPainter, QPen, QPixmap
from PyQt5.QtCore import Qt, QPoint

class Toolbar(QWidget):
    def __init__(self, canvas, parent=None):
        super().__init__(parent)

        # Toolbar layout
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)

        # Clear button
        clear_button = QPushButton("Clear")
        clear_button.clicked.connect(canvas.clear_canvas)
        layout.addWidget(clear_button)

        # Color selection button
        color_button = QPushButton("Select Color")
        color_button.clicked.connect(self.open_color_dialog)
        layout.addWidget(color_button)

        # Spacer for alignment
        spacer = QWidget()
        #spacer.setSizePolicy(QPushButton.Expanding, QPushButton.Expanding)
        layout.addWidget(spacer)

        # Save reference to canvas
        self.canvas = canvas

        self.setLayout(layout)

    def open_color_dialog(self):
        color = QColorDialog.getColor(self.canvas.pen_color, self, "Select Color")
        if color.isValid():
            self.canvas.pen_color = color