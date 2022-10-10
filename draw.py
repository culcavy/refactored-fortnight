from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton

import sys

import logging

logging.basicConfig(level=logging.INFO)

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("My App")
        button = QPushButton("Press me!")
        self.setCentralWidget(button)

def startApp():
    logging.info("初始化 Application")
    app: QApplication = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    startApp()