import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qtc
from canvas import Canvas
from toolbar import Toolbar
from textbox import ChatBoxWidget

class MainWindow(qtw.QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle('CS 839 Project')
        self.showMaximized()
        
        # Create a layout
        layout = qtw.QHBoxLayout()
        
        # Create a canvas instance
        self.canvas = Canvas()
        
        # Create Chatbox
        self.promptbox_widget = ChatBoxWidget(self.canvas)
        screen_width = qtw.QApplication.desktop().screenGeometry().width()
        self.promptbox_widget.setFixedWidth(screen_width // 7)
        
        # Create Toolbar
        self.toolbar = Toolbar(self.canvas)
        
        # Set maximum width for canvas to prevent it from going beyond the promptbox widget
        #self.canvas.setMinimumWidth(screen_width - self.promptbox_widget.width())
        
        # Add the canvas to the layout
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        layout.addStretch(2)
        layout.addWidget(self.promptbox_widget)
        
        # Set the layout to the main window
        self.setLayout(layout)

if __name__ == '__main__':
    app = qtw.QApplication([])
    mw = MainWindow()
    app.exec_()