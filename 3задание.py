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

        self.setWindowTitle("Закон охлаждения Ньютона")

        self.T0_label = QLabel("Начальная температура T0 (°C):")
        self.T0_input = QLineEdit("100")  # Значение по умолчанию

        self.Tenv_label = QLabel("Температура окружающей среды Tenv (°C):")
        self.Tenv_input = QLineEdit("20")  # Значение по умолчанию

        self.k_label = QLabel("Коэффициент теплообмена k (1/с):")
        self.k_input = QLineEdit("0.01")  # Значение по умолчанию

        self.plot_button = QPushButton("Построить")
        self.plot_button.clicked.connect(self.plot_cooling)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)  # 1 строка, 1 столбец, 1 график

        self.ax.set_xlabel("Время (с)")
        self.ax.set_ylabel("Температура тела (°C)")
        self.ax.grid(True)
        
        input_layout = QHBoxLayout()
        input_layout.addWidget(self.T0_label)
        input_layout.addWidget(self.T0_input)
        input_layout.addWidget(self.Tenv_label)
        input_layout.addWidget(self.Tenv_input)
        input_layout.addWidget(self.k_label)
        input_layout.addWidget(self.k_input)

        main_layout = QVBoxLayout()
        main_layout.addLayout(input_layout)
        main_layout.addWidget(self.plot_button)
        main_layout.addWidget(self.canvas)

        self.setLayout(main_layout)

    def plot_cooling(self):
        """Строит график охлаждения по закону Ньютона."""

        try:
            T0 = float(self.T0_input.text())
            Tenv = float(self.Tenv_input.text())
            k = float(self.k_input.text())
        except ValueError:
            print("Ошибка: Введите корректные числовые значения для T0, Tenv и k.")
            return 

        def temperature(t):
            return Tenv + (T0 - Tenv) * np.exp(-k * t)

        t = np.linspace(0, 300, 500) 
        T = temperature(t)

        self.ax.clear()

        # Построение графика
        self.ax.plot(t, T)
        self.ax.set_xlabel("Время (с)")
        self.ax.set_ylabel("Температура тела (°C)")
        self.ax.grid(True)

        self.canvas.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
