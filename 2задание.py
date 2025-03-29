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

        self.setWindowTitle("График гармонического колебания")

        self.amplitude_label = QLabel("Амплитуда (м):")
        self.amplitude_input = QLineEdit("1.0")  # Значение по умолчанию

        self.frequency_label = QLabel("Частота (Гц):")
        self.frequency_input = QLineEdit("1.0")  # Значение по умолчанию

        self.phase_label = QLabel("Фаза (градусы):")
        self.phase_input = QLineEdit("0.0")  # Значение по умолчанию

        self.plot_button = QPushButton("Построить")
        self.plot_button.clicked.connect(self.plot_harmonic)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)  # 1 строка, 1 столбец, 1 график
        
        self.ax.set_xlabel("Время (с)")
        self.ax.set_ylabel("Смещение (м)")
        self.ax.grid(True)
        
        input_layout = QHBoxLayout()
        input_layout.addWidget(self.amplitude_label)
        input_layout.addWidget(self.amplitude_input)
        input_layout.addWidget(self.frequency_label)
        input_layout.addWidget(self.frequency_input)
        input_layout.addWidget(self.phase_label)
        input_layout.addWidget(self.phase_input)

        main_layout = QVBoxLayout()
        main_layout.addLayout(input_layout)
        main_layout.addWidget(self.plot_button)
        main_layout.addWidget(self.canvas)

        self.setLayout(main_layout)

    def plot_harmonic(self):
        """Строит график гармонического колебания."""

        try:
            amplitude = float(self.amplitude_input.text())
            frequency = float(self.frequency_input.text())
            phase = float(self.phase_input.text())
        except ValueError:
            print("Ошибка: Введите корректные числовые значения для амплитуды, частоты и фазы.")
            return  # Прерываем выполнение функции, если ввод некорректный

        phase_rad = np.radians(phase)  # Преобразование фазы в радианы
        t = np.linspace(0, 5, 500)  # Время от 0 до 5 секунд, 500 точек для плавности
        x = amplitude * np.sin(2 * np.pi * frequency * t + phase_rad)

        self.ax.clear()

        self.ax.plot(t, x)
        self.ax.set_xlabel("Время (с)")
        self.ax.set_ylabel("Смещение (м)")
        self.ax.grid(True)

        self.canvas.draw()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
