import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit,
                             QPushButton, QVBoxLayout, QHBoxLayout)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Траектория броска тела под углом к горизонту")
        
        self.speed_label = QLabel("Начальная скорость (м/с):")
        self.speed_input = QLineEdit("10") 

        self.angle_label = QLabel("Угол броска (градусы):")
        self.angle_input = QLineEdit("45")  

        self.plot_button = QPushButton("Построить траекторию")
        self.plot_button.clicked.connect(self.plot_trajectory)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)  

        self.ax.set_xlabel("Расстояние (м)")
        self.ax.set_ylabel("Высота (м)")
        self.ax.grid(True)

        input_layout = QHBoxLayout()
        input_layout.addWidget(self.speed_label)
        input_layout.addWidget(self.speed_input)
        input_layout.addWidget(self.angle_label)
        input_layout.addWidget(self.angle_input)

        main_layout = QVBoxLayout()
        main_layout.addLayout(input_layout)
        main_layout.addWidget(self.plot_button)
        main_layout.addWidget(self.canvas)

        self.setLayout(main_layout)

    def plot_trajectory(self):
        """Строит траекторию движения тела."""

        try:
            speed = float(self.speed_input.text())
            angle = float(self.angle_input.text())
        except ValueError:
            print("Ошибка: Введите корректные числовые значения для скорости и угла.")
            return 

        angle_rad = np.radians(angle)
        g = 9.81 

        t_flight = (2 * speed * np.sin(angle_rad)) / g

        t = np.linspace(0, t_flight, 100)

        x = speed * np.cos(angle_rad) * t
        y = speed * np.sin(angle_rad) * t - 0.5 * g * t**2

        self.ax.clear()

        self.ax.plot(x, y)
        self.ax.set_xlabel("Расстояние (м)")
        self.ax.set_ylabel("Высота (м)")
        self.ax.grid(True)

        self.canvas.draw()

if name == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
