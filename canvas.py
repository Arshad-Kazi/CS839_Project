import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from PyQt5.QtGui import QPainter, QPen, QPixmap, QMouseEvent
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QDesktopWidget
import numpy as np
from PyQt5.QtGui import QImage
import cv2




class Canvas(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background-color: white;")  # Set canvas background
        self.setFixedSize(QDesktopWidget().availableGeometry(self).size())  # Set canvas size to screen size
        self.image = QPixmap(self.size())  # Create a pixmap to store the drawing
        self.image.fill(Qt.white)  # Fill the pixmap with white
        self.last_point = QPoint()
        self.drawing = False
        self.pen_color = Qt.black  # Default pen color
        self.canvas_width = self.size().width()
        self.canvas_height = self.size().height()
        
        
        




    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.last_point = event.pos()

    def mouseMoveEvent(self, event: QMouseEvent):
        if event.buttons() & Qt.LeftButton and self.drawing:
            painter = QPainter(self.image)  # Draw on the pixmap
            pen = QPen(self.pen_color, 9, Qt.SolidLine)  # Set pen to black with thickness 5
            pen.setCapStyle(Qt.RoundCap)  # Set pen cap to round for smoother edges
            pen.setJoinStyle(Qt.RoundJoin)  # Set pen join style to round for smoother connections
            painter.setPen(pen)
            painter.drawLine(self.last_point, event.pos())
            self.last_point = event.pos()
            painter.end()
            self.update()  # Trigger a repaint of the widget

    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.drawing = False

    def paintEvent(self, event):
        super().paintEvent(event)  # Call the base class's paintEvent method
        
        canvas_painter = QPainter(self)
        canvas_painter.drawPixmap(0, 0, self.image)  # Draw the pixmap onto the widget
        
    def clear_canvas(self):
        self.image.fill(Qt.white)
        self.update()
        
    def convert_pixmap_to_numpy(self):

        image = self.image.toImage()
        width = image.width()
        height = image.height()
        ptr = image.bits()
        ptr.setsize(image.byteCount())
        arr = np.array(ptr).reshape(height, width, 4)  # Assuming the image has 4 channels (RGBA)
        arr = arr[:, :, :3]  # Remove the alpha channel
        arr = np.uint8(arr)  # Convert the data type to uint8
        return arr
    
    def update_image(self, image):
        image = np.uint8(image)
        image = cv2.resize(image, (self.canvas_width, self.canvas_height))
        height, width, channel = image.shape
        qimage = QImage(image.data, width, height, channel * width, QImage.Format_RGB888)
        self.image = QPixmap(qimage)
        self.update()
        
        


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Drawing Canvas")
        self.setGeometry(100, 100, 800, 600)

        canvas = Canvas(self)
        layout = QVBoxLayout()
        layout.addWidget(canvas)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
