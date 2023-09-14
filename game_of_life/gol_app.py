import sys
from gol_engine import GOLEngine
from PySide6.QtCore import Qt, Slot, Signal, QTimer
from PySide6.QtWidgets import (QApplication, QMainWindow, 
                               QWidget, QLabel, QScrollBar, 
                               QVBoxLayout, QHBoxLayout, QSizePolicy)
from PySide6.QtGui import QImage, QPixmap, QPainter, QColor, QIcon


class GOLApp(QMainWindow):
    def __init__(self):
        super().__init__(None)
        
        self.__gol_engine = GOLEngine(100, 75)
        self.__gol_engine.randomize()
        
        self.__viewer = QLabel()
        self.__viewer.setAlignment(Qt.AlignCenter)
        self.__viewer.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        # self.__viewer.setScaledContents(True)
        self.setCentralWidget(self.__viewer)
        
        self.__timer = QTimer()
        self.__timer.timeout.connect(self.__tic)
        self.__timer.start(30)
        
    
    def __update_model(self):
        self.__gol_engine.tic()
        
    def __update_view(self):
        image = QImage(self.__gol_engine.width, self.__gol_engine.height, QImage.Format_ARGB32)
        painter = QPainter(image)
        painter.setBrush(Qt.black)
        painter.drawRect(0, 0, image.width(), image.height())
        
        painter.setPen(Qt.white)
        for x in range(self.__gol_engine.width):
            for y in range(self.__gol_engine.height):
                cell_value = self.__gol_engine.get_cell_value(x, y)
                if cell_value == 1:
                    painter.drawPoint(x, y)
        painter.end()
                    
        self.__viewer.setPixmap(QPixmap.fromImage(image.scaled(self.__viewer.width(), self.__viewer.height(), Qt.KeepAspectRatio, Qt.FastTransformation)))
        
    @Slot()
    def __tic(self):
        self.__update_model()
        self.__update_view()
        


def main():
    app = QApplication(sys.argv)

    w = GOLApp()
    w.show()
    sys.exit(app.exec())
    

if __name__ == '__main__':
    main()