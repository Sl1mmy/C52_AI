# Introduction à Qt (1/3)
#
# Cet exemple introductif présente comment créer une application de type sélection de couleur avec Qt.
#
# Le schéma suivant présente les widgets utilisé.
#   __________________________________________________________________
#  |__________________________________________________________________|
#  |             ________________________           _____     _____   |
#  |  Rouge     |__________________|_|___|   212   |_____|   |     |  |
#  |             ________________________           _____    |     |  |
#  |  Vert      |_|______________________|    0    |_____|   |     |  |
#  |             ________________________           _____    |     |  |
#  |  Bleu      |_____________|_|________|   188   |_____|   |_____|  |
#  |__________________________________________________________________|
# 
#    \____/     \________________________/  \____/ \_____/   \_____/
#      |                     |                |       |         |
#      |                     |                |       |         \_ QLabel : affiche une image de la couleur finale
#      |                     |                |        \_ QLabel : affiche une image pour chaque bande de couleur (intensité de rouge, vert, bleu)
#      |                     |                 \_ QLabel : affiche un texte pour la valeur de chaque bande de couleur (intensité de rouge, vert, bleu)
#      |                      \_ QScrollBar : sélection de la valeur pour chaque bande de couleur (intensité de rouge, vert, bleu)
#       \_ QLabel : affiche un titre pour chaque bande de couleur
#
#
# Cet exemple est constitué de plusieurs "layout" imbriqués les uns dans les autres. Les "layouts" permettent une gestion automatisée de la disposition à l'écran.
# Le schéma suivant présente quelle est la disposition des 6 "layouts" utilisés.
# 
#   _________________________________________________________________________________________
#  |_________________________________________________________________________________________|
#  |                                                                                         |
#  |   ___________________________________________________________________________________   |
#  |  6                                                                                   |  |
#  |  |   _____________________________________________________________________________   |  |
#  |  |  5                                                                             |  |  |
#  |  |  |   ______________________________________________________________            |  |  |
#  |  |  |  4                                                              |           |  |  |
#  |  |  |  |   ________________________________________________________   |           |  |  |
#  |  |  |  |  1             ________________________           _____   |  |   _____   |  |  |
#  |  |  |  |  |  Rouge     |__________________|_|___|   212   |_____|  |  |  |     |  |  |  |
#  |  |  |  |  |________________________________________________________|  |  |     |  |  |  |
#  |  |  |  |                                                              |  |     |  |  |  |     
#  |  |  |  |   ________________________________________________________   |  |     |  |  |  |     
#  |  |  |  |  2             ________________________           _____   |  |  |     |  |  |  |
#  |  |  |  |  |  Vert      |_|______________________|    0    |_____|  |  |  |     |  |  |  |
#  |  |  |  |  |________________________________________________________|  |  |     |  |  |  |
#  |  |  |  |                                                              |  |     |  |  |  |     
#  |  |  |  |   ________________________________________________________   |  |     |  |  |  |     
#  |  |  |  |  3             ________________________           _____   |  |  |     |  |  |  |
#  |  |  |  |  |  Bleu      |_____________|_|________|   188   |_____|  |  |  |_____|  |  |  |
#  |  |  |  |  |________________________________________________________|  |           |  |  |
#  |  |  |  |                                                              |           |  |  |
#  |  |  |  |______________________________________________________________|           |  |  |
#  |  |  |                                                                             |  |  |
#  |  |  |_____________________________________________________________________________|  |  |
#  |  |                                                                                   |  |
#  |  |___________________________________________________________________________________|  |
#  |                                          /                                              |
#  |                                         /                                               |
#  |                                         \                                               |
#  |                                          \  (stretch)                                   |
#  |                                           \                                             |
#  |                                           /                                             |
#  |__________________________________________/______________________________________________|
#
#  Informations sur les layouts :
#   - (1), (2) et (3) : 
#       - QHBoxLayout
#       - gère la disposition horizontale de 4 widgets : 
#           - le titre
#           - la barre de défilement
#           - la valeur de la couleur
#           - l'image de la couleur
#   - (4) :
#       - QVBoxLayout
#       - gère la disposition verticale des trois "layouts" (1), (2) et (3)
#   - (5) :
#       - QHBoxLayout
#       - gère la disposition horizontale entre le "layout" (4) et l'image de la couleur finale
#   - (6) :
#       - QHBoxLayout
#       - gère la disposition verticale du "layout" (5) et de l'application
#
# L'implémentation suivante est plutôt simple et vise une compréhension de base. Les exemples suivants pourront approfondir quelques aspects supplémentaires.


import sys
from PySide6.QtCore import Qt, Slot, Signal
from PySide6.QtWidgets import (QApplication, QMainWindow, 
                               QWidget, QLabel, QScrollBar, 
                               QVBoxLayout, QHBoxLayout)
from PySide6.QtGui import QPixmap, QColor, QIcon


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__(None)
        
        self.setWindowTitle('Color picker demo')
        self.setWindowIcon(QIcon('color_picker_icon_1.png'))

        fixed_widget_width = 50
        
        self.__red_scroll_bar = QScrollBar()
        self.__red_color = QLabel()
        self.__green_scroll_bar = QScrollBar()
        self.__green_color = QLabel()
        self.__blue_scroll_bar = QScrollBar()
        self.__blue_color = QLabel()
        
        self.__mixed_color = QLabel()
        self.__mixed_color.setFixedWidth(fixed_widget_width)

        red_layout = self.__create_channel('Red', self.__red_scroll_bar, self.__red_color, fixed_widget_width)
        green_layout = self.__create_channel('Green', self.__green_scroll_bar, self.__green_color, fixed_widget_width)
        blue_layout = self.__create_channel('Blue', self.__blue_scroll_bar, self.__blue_color, fixed_widget_width)
        
        channel_layout = QVBoxLayout()
        channel_layout.addLayout(red_layout)
        channel_layout.addLayout(green_layout)
        channel_layout.addLayout(blue_layout)
        
        mixed_layout = QHBoxLayout()
        mixed_layout.addLayout(channel_layout)
        mixed_layout.addWidget(self.__mixed_color)
        
        central_layout = QVBoxLayout()
        central_layout.addLayout(mixed_layout)
        central_layout.addStretch()
        
        central_widget = QWidget()
        central_widget.setLayout(central_layout)
        
        self.setCentralWidget(central_widget)
        
        
    def __create_channel(self, title, color_sb, color_label, fixed_widget_width):
        title_label = QLabel()
        value_label = QLabel()
        
        title_label.setText(title)
        title_label.setFixedWidth(fixed_widget_width)
        color_sb.setRange(0, 255)
        color_sb.setValue(0)
        color_sb.setOrientation(Qt.Horizontal)
        color_sb.setMinimumWidth(2 * fixed_widget_width)
        value_label.setNum(0)
        value_label.setAlignment(Qt.AlignCenter)
        value_label.setFixedWidth(fixed_widget_width)
        color_label.setFixedWidth(fixed_widget_width)
        
        color_sb.valueChanged.connect(value_label.setNum)
        color_sb.valueChanged.connect(self.__update_color)
        
        layout = QHBoxLayout()
        layout.addWidget(title_label)
        layout.addWidget(color_sb)
        layout.addWidget(value_label)
        layout.addWidget(color_label)
        
        return layout
    
    def __update_label_color(self, label, red, green, blue):
        image = QPixmap(label.size())
        image.fill(QColor(red, green, blue))
        label.setPixmap(image)
    
    @Slot()
    def __update_color(self):
        r = self.__red_scroll_bar.value()
        g = self.__green_scroll_bar.value()
        b = self.__blue_scroll_bar.value()
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