from test import Asset, Stock, Currency, Obligation, StockPortfolio
from assets import SBER, AFLT, MGNT, GMKN, VKCO, YDEX, OZON, ROSN, AMZN, AAPL, MSFT, TSLA, NVDA, INTC, NFLX, MOEX, VTBR, CSCO, ADBE, PYPL, TCSG
from datetime import datetime
from PyQt6.QtWidgets import (
    QComboBox,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QTextEdit,
    QMessageBox,
    QHBoxLayout
)

class PortfolioApp(QWidget):

    """
    Initializes an instance of the PortfolioApp class.

    Sets up the user interface for managing a stock portfolio, including inputs
    for stock names, prices, and quantities. Initializes the portfolio and
    sets up layout and widgets.
    """

    def __init__(self):
        super().__init__()
        
        self.portfolio = StockPortfolio()
        
        self.setWindowTitle("Stock Portfolio Manager")
        self.setGeometry(100, 100, 400, 400)

        main_layout = QHBoxLayout()

        left_layout = QVBoxLayout()

        self.name_input = QComboBox(self)
        self.name_input.addItems(["SBER", "AFLT", "MGNT", "GMKN", "VKCO", "YDEX", "OZON", "ROSN", "AMZN", "AAPL", "MSFT", "TSLA", "NVDA", "INTC", "NFLX", "MOEX", "VTBR", "CSCO", "ADBE", "PYPL", "TCSG"])
        left_layout.addWidget(self.name_input)

        self.asset_prices = {
            "SBER": SBER,
            "AFLT": AFLT,
            "MGNT": MGNT,
            "GMKN": GMKN,
            "VKCO": VKCO,
            "YDEX": YDEX,
            "OZON": OZON,
            "ROSN": ROSN,
            "AMZN": AMZN,
            "AAPL": AAPL,
            "MSFT": MSFT,
            "TSLA": TSLA,
            "NVDA": NVDA,
            "INTC": INTC,
            "NFLX": NFLX,
            "MOEX": MOEX,
            "VTBR": VTBR,
            "CSCO": CSCO,
            "ADBE": ADBE,
            "PYPL": PYPL,
            "TCSG": TCSG
        }

        self.price_input = QLineEdit(self)
        self.price_input.setPlaceholderText("Price per Unit")
        self.price_input.setReadOnly(True)
        left_layout.addWidget(self.price_input)

        self.quantity_input = QLineEdit(self)
        self.quantity_input.setPlaceholderText("Number of lots (1 lot = 10 stocks)")
        left_layout.addWidget(self.quantity_input)

        self.name_input.currentIndexChanged.connect(self.update_price)

        self.add_button = QPushButton("Add Asset", self)
        self.add_button.clicked.connect(self.add_asset)
        left_layout.addWidget(self.add_button)

        self.remove_button = QPushButton("Remove Asset", self)
        self.remove_button.clicked.connect(self.remove_asset)
        left_layout.addWidget(self.remove_button)

        self.portfolio_display = QTextEdit(self)
        self.portfolio_display.setReadOnly(True)
        left_layout.addWidget(self.portfolio_display)

        main_layout.addLayout(left_layout)

        right_layout = QVBoxLayout()

        self.history_display = QTextEdit(self)
        self.history_display.setReadOnly(True)
        right_layout.addWidget(QLabel("History of Requests:"))
        right_layout.addWidget(self.history_display)

        main_layout.addLayout(right_layout)

        self.setLayout(main_layout)

        self.update_price()

    def update_price(self):
        name = self.name_input.currentText()
        price = self.asset_prices.get(name, 0.0)
        self.price_input.setText(str(price))
        self.price_input.setPlaceholderText('per unit')

    """
    Updates the price input field based on the selected asset.

    Retrieves the price of the selected asset from the asset_prices dictionary
    and displays it in the price_input field.
    """

    def add_asset(self):
        name = self.name_input.currentText()
        quantity = int(self.quantity_input.text()) * 10

        if name and quantity > 0:
            try:
                price_per_unit = float(self.price_input.text())
        
                asset = Stock(name, quantity, price_per_unit)
                self.portfolio.add_asset(asset)
        
                self.update_portfolio_display()
                self.log_history(f"Added {quantity} shares of {name} at {price_per_unit} each.")

            except:
                QMessageBox.warning(self, "Error", "Please enter valid asset details")

        else:
            QMessageBox.warning(self, "Input Error", "Please enter valid asset details")

    """
    Handles adding a new asset to the portfolio.

    Validates the input data and adds the asset to the portfolio. If the data
    is invalid, it displays an error message.
    """

    def remove_asset(self):
        name = self.name_input.currentText()
        quantity = int(self.quantity_input.text()) * 10

        if name and quantity > 0:
            try:
                asset = Stock(name, quantity, 0)
                self.portfolio.remove_asset(asset)
        
                self.update_portfolio_display()
                self.log_history(f"Removed {quantity} shares of {name}.")

            except:
                QMessageBox.warning(self, "Error", "Please enter valid asset details")

        else:
            QMessageBox.warning(self, "Input Error", "Please enter valid asset details")

    """
    Handles removing an asset from the portfolio.

    Removes the specified asset from the portfolio. If the asset is not found,
    it displays an error message.
    """

    def update_portfolio_display(self):
        self.portfolio_display.setPlainText(str(self.portfolio))

    """
    Updates the display of the portfolio in the user interface.

    Sets the text area to show the current state of the portfolio.
    """

    def log_history(self, message):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        current_text = self.history_display.toPlainText()
        new_text = f"{current_text}\n{current_time} - {message}" if current_text else f"{current_time} - {message}"
        self.history_display.setPlainText(new_text)

    """
    Logs a message to the history display with a timestamp.

    This method retrieves the current time, formats it as a string, and appends
    the provided message to the history display. Each log entry is prefixed with
    the current date and time, ensuring that all logged messages are timestamped.
    """