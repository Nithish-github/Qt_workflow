import sys
from PySide6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout

class HelloWorldApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello PySide6")
        self.setMinimumSize(300, 150)

        layout = QVBoxLayout()
        label = QLabel("Hello, World!")
        label.setStyleSheet("font-size: 24px;")
        layout.addWidget(label)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HelloWorldApp()
    window.show()
    sys.exit(app.exec())
