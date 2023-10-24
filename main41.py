import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog
from main322 import get_data_for_date

class DataViewerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("CSV Data Viewer")
        self.setGeometry(100, 100, 400, 200)


        self.dataset_file_input = QLineEdit(self)
        self.dataset_file_input.setPlaceholderText("Выберите файл датасета")
        self.browse_dataset_button = QPushButton("Выбрать файл датасета", self)
        self.browse_dataset_button.clicked.connect(self.browse_dataset)




        self.date_input = QLineEdit(self)
        self.date_input.setPlaceholderText("Введите дату в формате YYYY-MM-DD")
        self.get_data_button = QPushButton("Получить данные", self)
        self.get_data_button.clicked.connect(self.get_data)


        self.data_label = QLabel(self)

        # Размещаем элементы в вертикальном макете
        layout = QVBoxLayout()
        layout.addWidget(self.dataset_file_input)
        layout.addWidget(self.browse_dataset_button)
        layout.addWidget(self.date_input)
        layout.addWidget(self.get_data_button)
        layout.addWidget(self.data_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def browse_dataset(self):
        filepath, _ = QFileDialog.getOpenFileName(self, 'Выберите файл датасета', '', 'CSV Files (*.csv)')
        if filepath:
            self.dataset_file_input.setText(filepath)



    def get_data(self):
        input_date = self.date_input.text()
        dataset_file_path = self.dataset_file_input.text()
        result = get_data_for_date(input_date, dataset_file_path)

        if result is not None:
            self.data_label.setText(f"Данные для {input_date}: {result}")
        else:
            self.data_label.setText(f"Данные для {input_date} не найдены.")

def main():
    app = QApplication(sys.argv)
    window = DataViewerApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
