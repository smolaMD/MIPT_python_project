import sys
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

class Asset:
    def __init__(self, name, quantity, price_per_unit):
        self.name = name
        self.quantity = quantity
        self.price_per_unit = price_per_unit
    
    def price(self):
        return self.quantity * self.price_per_unit
    
    def __str__(self):
        return f'{self.name}: {self.quantity} units - {self.price_per_unit} per unit'
    
    def __eq__(self, other):
        if isinstance(other, Asset):
            return ((self.name == other.name) and (self.quantity == other.quantity) and (self.price_per_unit == other.price_per_unit))
        return False
    
class StockPortfolio:

    def __init__(self):
        self.assets = []

    def add_asset(self, asset: Asset):
        for i in range(len(self.assets)):
            if self.assets[i].name == asset.name:
                self.assets[i].quantity += asset.quantity
                return
        self.assets.append(asset)
        
    def remove_asset(self, asset: Asset):
        for i in range(len(self.assets)):
            if self.assets[i].name == asset.name:
                if self.assets[i].quantity > asset.quantity:
                    self.assets[i].quantity -= asset.quantity
                elif self.assets[i].quantity < asset.quantity:
                    print("Not enough assets to sell")
                elif self.assets[i].quantity == asset.quantity:
                    self.assets.remove(asset)
                return
        print("No asset in portfolio")

    def portfolio_price(self):
        portfolio_price = 0
        for i in range(len(self.assets)):
            portfolio_price += self.assets[i].quantity * self.assets[i].price_per_unit
        return portfolio_price

    def __str__(self):
        portfolio_str = "Your portfolio:\n"
        for i in range(len(self.assets)):
            portfolio_str += self.assets[i].__str__()
            portfolio_str += "\n"
        portfolio_str += f'Total price of portfolio: {self.portfolio_price()}'
        return portfolio_str

class PortfolioApp(QWidget):
    def __init__(self):
        super().__init__()
        
        self.portfolio = StockPortfolio()
        
        # Установка заголовка и размеров окна
        self.setWindowTitle("Stock Portfolio Manager")
        self.setGeometry(100, 100, 400, 400)

        # Создание вертикального компоновщика
        layout = QVBoxLayout()

        # Параметры ассета
        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText("Asset Name")
        layout.addWidget(self.name_input)

        self.quantity_input = QLineEdit(self)
        self.quantity_input.setPlaceholderText("Quantity")
        layout.addWidget(self.quantity_input)

        self.price_input = QLineEdit(self)
        self.price_input.setPlaceholderText("Price per Unit")
        layout.addWidget(self.price_input)

        # Реализация эдда и ремува
        self.add_button = QPushButton("Add Asset", self)
        self.add_button.clicked.connect(self.add_asset)
        layout.addWidget(self.add_button)

        self.remove_button = QPushButton("Remove Asset", self)
        self.remove_button.clicked.connect(self.remove_asset)
        layout.addWidget(self.remove_button)

        # __str__ portfolio
        self.portfolio_display = QTextEdit(self)
        self.portfolio_display.setReadOnly(True)
        layout.addWidget(self.portfolio_display)

        self.setLayout(layout)

    def add_asset(self):
        name = self.name_input.text()
        quantity = int(self.quantity_input.text())
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