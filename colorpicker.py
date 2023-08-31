import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QMainWindow, 
                               QLabel, QScrollBar, 
                               QVBoxLayout, QHBoxLayout, QWidget)

class MyApp(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setWindowTitle('Color Picker demo')
        #self.setWindowIcon()
        
        fixed_widget_width = 50
        
        self.__red_title = QLabel()
        self.__red_scroll_bar = QScrollBar()
        self.__red_value = QLabel()
        self.__red_color = QLabel()
        
        self.__red_title.setText('Red')
        self.__red_title.setFixedWidth(fixed_widget_width)
        
        self.__red_scroll_bar.setRange(0, 255)
        self.__red_scroll_bar.setValue(0)
        self.__red_scroll_bar.setOrientation(Qt.Horizontal)
        self.__red_scroll_bar.setMinimumWidth(4 * fixed_widget_width)
        
        self.__red_value.setNum(0)
        self.__red_value.setAlignment(Qt.AlignCenter)
        self.__red_value.setFixedWidth(fixed_widget_width)
        
        self.__red_color.setFixedWidth(fixed_widget_width)
        
        self.__red_scroll_bar.valueChanged.connect(self.__red_value.setNum)
        
        red_layout = QHBoxLayout()
        
        red_layout.addWidget(self.__red_title)
        red_layout.addWidget(self.__red_scroll_bar)
        red_layout.addWidget(self.__red_value)
        red_layout.addWidget(self.__red_color)
        
        central_widget = QWidget()
        central_widget.setLayout(red_layout)
        
        self.setCentralWidget(central_widget)
                
                
def main():
    app = QApplication(sys.argv)
    
    w = MyApp()
    w.show()
    sys.exit(app.exec())
    
    
if __name__ == '__main__':
    main()
