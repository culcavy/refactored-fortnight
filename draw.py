from PySide6.QtWidgets import QApplication, QWidget

import sys

import logging

logging.basicConfig(level=logging.INFO)

def showWindow():
    logging.info("初始化 window")
    window: QWidget = QWidget()
    logging.info("显示 window")
    window.show()

def startApp():
    logging.info("初始化 Application")
    app: QApplication = QApplication(sys.argv)
    logging.info("初始化 window")
    window: QWidget = QWidget()
    logging.info("显示 window")
    window.show()
    logging.info("启动 App")
    app.exec()

if __name__ == "__main__":
    startApp()