import sys
from main import Asset, StockPortfolio
from assets import SBER, AFLT, MGNT, GMKN
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
    QTextEdit
)

class PortfolioApp(QWidget):
    def __init__(self):
        super().__init__()
        
        self.portfolio = StockPortfolio()
        
        self.setWindowTitle("Stock Portfolio Manager")
        self.setGeometry(100, 100, 400, 400)

        layout = QVBoxLayout()

        self.name_input = QComboBox(self)
        self.name_input.addItems(["SBER", "AFLT", "MGNT", "GMKN"])
        layout.addWidget(self.name_input)

        self.asset_prices = {
            "SBER": SBER,
            "AFLT": AFLT,
            "MGNT": MGNT,
            "GMKN": GMKN
        }

        self.price_input = QLineEdit(self)
        self.price_input.setPlaceholderText("Price per Unit")
        self.price_input.setReadOnly(True)
        layout.addWidget(self.price_input)

        self.quantity_input = QLineEdit(self)
        self.quantity_input.setPlaceholderText("Number of lots (1 lot = 10 stocks)")
        layout.addWidget(self.quantity_input)

        self.name_input.currentIndexChanged.connect(self.update_price)

        self.add_button = QPushButton("Add Asset", self)
        self.add_button.clicked.connect(self.add_asset)
        layout.addWidget(self.add_button)

        self.remove_button = QPushButton("Remove Asset", self)
        self.remove_button.clicked.connect(self.remove_asset)
        layout.addWidget(self.remove_button)

        self.portfolio_display = QTextEdit(self)
        self.portfolio_display.setReadOnly(True)
        layout.addWidget(self.portfolio_display)

        self.setLayout(layout)

        self.update_price()

    def update_price(self):
        name = self.name_input.currentText()
        price = self.asset_prices.get(name, 0.0)
        self.price_input.setText(str(price))
        self.price_input.setPlaceholderText('per unit')

    def add_asset(self):
        name = self.name_input.currentText()
        quantity = int(self.quantity_input.text()) * 10
        price_per_unit = float(self.price_input.text())
        
        asset = Asset(name, quantity, price_per_unit)
        self.portfolio.add_asset(asset)
        
        self.update_portfolio_display()

    def remove_asset(self):
        name = self.name_input.text()
        quantity = int(self.quantity_input.text())

        asset = Asset(name, quantity, 0)
        self.portfolio.remove_asset(asset)
        
        self.update_portfolio_display()

    def update_portfolio_display(self):
        self.portfolio_display.setPlainText(str(self.portfolio))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PortfolioApp()
    window.show()
    sys.exit(app.exec())