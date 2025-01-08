import sys
import random
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGraphicsView, QGraphicsScene
from PyQt6.QtGui import QBrush, QColor


class CircleDrawer(QGraphicsView):
    def __init__(self) -> None:
        super().__init__()
        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)
        self.circles = []

    def _add_circle(self) -> None:
        diameter = random.randint(20, 80)
        x = random.randint(0, self.width() - diameter)
        y = random.randint(0, self.height() - diameter)
        self.circles.append((x, y, diameter))
        self._update_scene()

    def _update_scene(self) -> None:
        self.scene.clear()
        for x, y, diameter in self.circles:
            brush = QBrush(QColor(255, 255, 0))
            self.scene.addEllipse(x, y, diameter, diameter, brush=brush)


class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setObjectName("Circle Drawer App")
        self.setGeometry(100, 100, 600, 400)

        self.circle_view = CircleDrawer(self)
        self.circle_view.setGeometry(10, 10, 580, 300)

        self.draw_button = QPushButton("Draw Circle", self)
        self.draw_button.setGeometry(10, 320, 100, 30)
        self.draw_button.clicked.connect(self._draw_circle)

    def _draw_circle(self) -> None:
        self.circle_view._add_circle()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
