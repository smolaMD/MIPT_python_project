import sys
from PyQt6.QtWidgets import QApplication
from visualization import PortfolioApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PortfolioApp()
    window.show()
    sys.exit(app.exec())

"""
Launches the widget
"""