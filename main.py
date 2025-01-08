import sys
import random
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGraphicsView, QGraphicsScene
from PyQt6.QtGui import QBrush, QColor


class CircleDrawer(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)
        self.circles = []
        self.basic_colors_rgb = [
            (0, 0, 0),  # black
            (255, 255, 255),  # white
            (255, 0, 0),  # red
            (0, 255, 0),  # green
            (0, 0, 255),  # blue
            (255, 255, 0),  # yellow
            (0, 255, 255),  # cyan
            (255, 0, 255),  # magenta
            (128, 128, 128),  # gray
            (192, 192, 192),  # light_gray
            (64, 64, 64),  # dark_gray
            (255, 165, 0),  # orange
            (128, 0, 128),  # purple
            (0, 255, 0),  # lime
            (0, 128, 128),  # teal
            (0, 0, 128),  # navy
            (128, 0, 0),  # maroon
            (128, 128, 0),  # olive
            (255, 105, 180),  # pink
            (210, 105, 30),  # chocolate
            (160, 82, 45),  # sienna
            (100, 149, 237),  # cornflowerblue
            (240, 128, 128),  # lightcoral
            (245, 222, 179),  # beige
            (220, 20, 60),  # crimson
            (255, 69, 0),  # orangered
            (153, 50, 204),  # darkorchid
            (70, 130, 180),  # steelblue
            (147, 112, 219),  # mediumpurple
            (0, 139, 139),  # darkcyan
            (0, 100, 0),  # darkgreen
            (139, 69, 19),  # saddlebrown
            (218, 112, 214),  # orchid
            (107, 142, 35),  # olivedrab
            (169, 169, 169),  # darkgrey
            (176, 196, 222),  # lightsteelblue
            (255, 215, 0),  # gold
            (244, 164, 96),  # sandybrown
            (230, 230, 250),  # lavender
            (240, 230, 140),  # khaki
            (255, 228, 196),  # bisque
            (95, 158, 160),  # cadetblue
            (25, 25, 112),  # midnightblue
            (248, 248, 255),  # ghostwhite
            (0, 128, 0),  # forestgreen
            (218, 165, 32),  # goldenrod
            (127, 255, 212),  # aquamarine
            (255, 248, 220),  # cornsilk
            (255, 228, 225),  # mistyrose
            (75, 0, 130),  # indigo
            (135, 206, 235),  # skyblue
            (72, 61, 139),  # darkslateblue
            (255, 20, 147),  # deeppink
            (240, 248, 255),  # aliceblue
            (240, 255, 240),  # honeydew
            (245, 255, 250),  # mintcream
            (250, 235, 215),  # antiquewhite
            (238, 232, 170),  # palegoldenrod
            (173, 216, 230),  # lightblue
            (175, 238, 238),  # paleturquoise
            (245, 245, 220),  # beige
            (188, 143, 143),  # rosybrown
            (216, 191, 216),  # plum
            (219, 112, 147),  # palevioletred
            (124, 252, 0),  # lawngreen
            (0, 250, 154),  # mediumspringgreen
            (253, 245, 230),  # ivory
            (176, 224, 230),  # powderblue
            (205, 92, 92),  # indianred
            (244, 164, 96),  # sandybrown
            (47, 79, 79),  # darkslategray
            (160, 32, 240),  # purple
            (127, 0, 255),  # blueviolet
            (255, 127, 80),  # coral
            (255, 99, 71),  # tomato
            (186, 85, 211),  # mediumorchid
            (0, 206, 209),  # darkturquoise
            (139, 0, 139),  # darkmagenta
            (107, 142, 35)  # olivedrab
        ]

    def add_circle(self):
        diameter = random.randint(20, 80)
        x = random.randint(0, self.width() - diameter)
        y = random.randint(0, self.height() - diameter)
        color = random.choice(self.basic_colors_rgb)
        self.circles.append((x, y, diameter, color))
        self.update_scene()

    def update_scene(self):
        self.scene.clear()
        for x, y, diameter, color in self.circles:
            brush = QBrush(QColor(color[0], color[1], color[2]))
            self.scene.addEllipse(x, y, diameter, diameter, brush=brush)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("Circle Drawer App")
        self.setGeometry(100, 100, 600, 400)

        self.circle_view = CircleDrawer(self)
        self.circle_view.setGeometry(10, 10, 580, 300)

        self.draw_button = QPushButton("Draw Circle", self)
        self.draw_button.setGeometry(10, 320, 100, 30)
        self.draw_button.clicked.connect(self.draw_circle)

    def draw_circle(self):
        self.circle_view.add_circle()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
