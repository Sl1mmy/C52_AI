import sys
from gol_engine import GOLEngine
from PySide6.QtCore import Qt, Slot, Signal, QTimer
from PySide6.QtWidgets import (QApplication, QMainWindow, QDockWidget,  
                               QWidget, QLabel, QScrollBar, QPushButton,
                               QVBoxLayout, QHBoxLayout, QSizePolicy)
from PySide6.QtGui import QImage, QPixmap, QPainter, QColor, QIcon

from __feature__ import snake_case, true_property


class QControlWidget(QWidget):
    
    def __init__(self, parent = None):
        super().__init__(parent)
        self.fixed_width = 100
        fixed_widget_width = 50
        
        self.__start_button = QPushButton("start")
        self.__stop_button = QPushButton("stop")
        
        self.__speed_scroll_bar = QScrollBar()
        self.__speed_value = QLabel()
        
        speed_layout = self.__create_channel(self.__speed_scroll_bar, self.__speed_value, fixed_widget_width)
        
        layout = QVBoxLayout()
        layout.add_widget(self.__start_button)
        layout.add_widget(self.__stop_button)
        layout.add_layout(speed_layout)
        
        self.set_layout(layout)
    
        
    def __create_channel(self, speed_sb, value_label, fixed_widget_width):

        speed_sb.set_range(0, 50)
        speed_sb.value = 0
        speed_sb.orientation = Qt.Horizontal
        speed_sb.minimum_width = 2 * fixed_widget_width
        value_label.set_num(0)
        value_label.alignment = Qt.AlignCenter
        value_label.set_fixed_width(fixed_widget_width)
        
        speed_sb.valueChanged.connect(value_label.set_num)
        speed_sb.valueChanged.connect(GOLApp.set_speed)

        layout = QHBoxLayout()
        layout.add_widget(speed_sb)
        layout.add_widget(value_label)

        
        return layout
        

class QInfoWidget(QWidget):
    
    #nb gen
    #nb cell vivant
    #nb cell mort
    def __init__(self, parent = None):
        super().__init__(parent)
        
        self.__generation_value = QLabel()
        self.__mort_value = QLabel()
        self.__vivant_value = QLabel()
        
    
        
    

class GOLApp(QMainWindow):
    def __init__(self):
        super().__init__(None)
        self.WindowWidth = 600
        self.WindowHeight = 300
        self.speed = 30
        
        self.minimum_width = self.width
        self.minimum_height = self.height
        self.__gol_engine = GOLEngine(100, 75)
        self.__gol_engine.randomize()
        
        self.__viewer = QLabel()
        self.__viewer.alignment = Qt.AlignCenter
        self.__viewer.size_policy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        #self.__viewer.scaled_contents = True
        
        self.__timer = QTimer()
        self.__timer.timeout.connect(self.__tic)
        self.__timer.start(self.speed)
        
        #layout
        control_widget = QControlWidget()
        control_widget.alignment = Qt.AlignLeft
        
        central_layout = QHBoxLayout()
        central_layout.add_widget(control_widget, stretch=1)
        central_layout.add_widget(self.__viewer, stretch=3)
        
        central_widget = QWidget()
        central_widget.set_layout(central_layout)
        
        self.set_central_widget(central_widget)
            
    @Slot()
    def set_speed(self, value):
        self.speed = value

    def __update_model(self):
        self.__gol_engine.tic()
        
    def __update_view(self):
        image = QImage(self.__gol_engine.width, self.__gol_engine.height, QImage.Format_ARGB32)
        painter = QPainter(image)
        painter.set_brush(Qt.black)
        painter.draw_rect(0, 0, image.width(), image.height())
        
        painter.set_pen(Qt.white)
        for x in range(self.__gol_engine.width):
            for y in range(self.__gol_engine.height):
                cell_value = self.__gol_engine.get_cell_value(x, y)
                if cell_value == 1:
                    painter.draw_point(x, y)
        painter.end()
                    
        self.__viewer.pixmap = QPixmap.from_image(image.scaled(self.__viewer.width, self.__viewer.height, Qt.KeepAspectRatio, Qt.FastTransformation))
        
    @Slot()
    def __tic(self):
        self.__update_model()
        self.__update_view()
        


def main():
    app = QApplication(sys.argv)

    w = GOLApp()
    #w = QControlWidget()
    w.show()
    sys.exit(app.exec())
    

if __name__ == '__main__':
    main()