# Introduction à Qt (2/4)
#
# Ajuster Qt à la norme PEP 8
#  - snake_case
#  - true_property
#  - ATTENTION : 
#     - snake_case a quelques exceptions (signaux)
#     - lire la doc pour connaître les vraies property


import sys
from PySide6.QtCore import Qt, Slot, Signal
from PySide6.QtWidgets import (QApplication, QMainWindow, 
                               QWidget, QLabel, QScrollBar, 
                               QVBoxLayout, QHBoxLayout)
from PySide6.QtGui import QPixmap, QColor, QIcon

from __feature__ import snake_case, true_property

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__(None)
        
        self.set_window_title('Color picker demo')
        self.window_icon = QIcon('color_picker_icon_1.png')

        fixed_widget_width = 50
        
        self.__red_scroll_bar = QScrollBar()
        self.__red_color = QLabel()
        self.__green_scroll_bar = QScrollBar()
        self.__green_color = QLabel()
        self.__blue_scroll_bar = QScrollBar()
        self.__blue_color = QLabel()
        
        self.__mixed_color = QLabel()
        self.__mixed_color.set_fixed_width(fixed_widget_width)

        red_layout = self.__create_channel('Red', self.__red_scroll_bar, self.__red_color, fixed_widget_width)
        green_layout = self.__create_channel('Green', self.__green_scroll_bar, self.__green_color, fixed_widget_width)
        blue_layout = self.__create_channel('Blue', self.__blue_scroll_bar, self.__blue_color, fixed_widget_width)
        
        channel_layout = QVBoxLayout()
        channel_layout.add_layout(red_layout)
        channel_layout.add_layout(green_layout)
        channel_layout.add_layout(blue_layout)
        
        mixed_layout = QHBoxLayout()
        mixed_layout.add_layout(channel_layout)
        mixed_layout.add_widget(self.__mixed_color)
        
        central_layout = QVBoxLayout()
        central_layout.add_layout(mixed_layout)
        central_layout.add_stretch()
        
        central_widget = QWidget()
        central_widget.set_layout(central_layout)
        
        self.set_central_widget(central_widget)
        
        
    def __create_channel(self, title, color_sb, color_label, fixed_widget_width):
        title_label = QLabel()
        value_label = QLabel()
        
        title_label.text = title
        title_label.set_fixed_width(fixed_widget_width)
        color_sb.set_range(0, 255)
        color_sb.value = 0
        color_sb.orientation = Qt.Horizontal
        color_sb.minimum_width = 2 * fixed_widget_width
        value_label.set_num(0)
        value_label.alignment = Qt.AlignCenter
        value_label.set_fixed_width(fixed_widget_width)
        color_label.set_fixed_width(fixed_widget_width)
        
        color_sb.valueChanged.connect(value_label.set_num)
        color_sb.valueChanged.connect(self.__update_color)
        
        layout = QHBoxLayout()
        layout.add_widget(title_label)
        layout.add_widget(color_sb)
        layout.add_widget(value_label)
        layout.add_widget(color_label)
        
        return layout
    
    def __update_label_color(self, label, red, green, blue):
        image = QPixmap(label.size)
        image.fill(QColor(red, green, blue))
        label.pixmap = image
    
    @Slot()
    def __update_color(self):
        r = self.__red_scroll_bar.value
        g = self.__green_scroll_bar.value
        b = self.__blue_scroll_bar.value
        self.__update_label_color(self.__red_color, r, 0, 0)
        self.__update_label_color(self.__green_color, 0, g, 0)
        self.__update_label_color(self.__blue_color, 0, 0, b)
        self.__update_label_color(self.__mixed_color, r, g, b)
        



def main():
    app = QApplication(sys.argv)

    w = MyApp()
    w.show()
    sys.exit(app.exec())
    

if __name__ == '__main__':
    main()