"""
Track daily cash spending with currency conversion.
"""
import datetime as dt

from ..calculator import Calculator
from ..record import Record


class CashCalculator(Calculator):
    """
    Class to track daily cash spending with currency conversion.
    Inherits from Calculator to manage records and calculate remaining cash.
    Supports USD, EUR, and RUB currencies with conversion rates.
    """
    RATES = {'USD': 79.34, 'EUR': 90.2, 'RUB': 1.0}

    def __init__(self, limit: int) -> None:
        """
        Initialize calculator with a daily spending limit.

        Args:
            limit: Daily limit in RUB.

        Raises:
            ValueError: If limit is invalid (via Calculator).
        """
        super().__init__(limit)
        self.supported_currencies = ['USD', 'EUR', 'RUB']

    def add_record(self, record: Record) -> None:
        """
        Add a record, preventing overspending.

        Args:
            record: Record object to add.

        Raises:
            TypeError: If record is not a Record instance.
            ValueError: If amount exceeds limit or date is invalid.
        """
        if not isinstance(record, Record):
            raise TypeError("Record must be an instance of Record")
        if record.date > dt.date.today():
            raise ValueError("Record date cannot be in the future")
        remained = self._get_today_remained()
        if record.date == dt.date.today() and record.amount > remained:
            raise ValueError("Record amount exceeds today's limit")
        self.records.append(record)

    def get_today_cash_remained(self, currency: str) -> str:
        """
        Get message about remaining cash for today in a currency.

        Args:
            currency: Currency code (USD, EUR, RUB).

        Returns:
            Message indicating remaining cash or debt.

        Raises:
            TypeError: If currency is not a string.
            ValueError: If currency is empty or unsupported.
        """
        if not isinstance(currency, str):
            raise TypeError("Currency must be a string")
        if not currency:
            raise ValueError("Currency cannot be empty")
        currency = currency.upper()
        if currency not in self.supported_currencies:
            raise ValueError("Unsupported currency")
        remained = self._convert_to_rate(self._get_today_remained(), currency)
        return self._get_cash_message(remained, currency)

    def _get_cash_message(self, remained: float, currency: str) -> str:
        """
        Format message based on remaining cash.

        Args:
            remained: Remaining amount in specified currency.
            currency: Currency code.

        Returns:
            Message for remaining cash or debt.
        """
        if remained == 0:
            return "No money left, hold on!"
        if remained < 0:
            msg = "No money left, hold on: your debt is "
            return f"{msg} {-remained:.2f} {currency}"
        return f"You have {remained:.2f} {currency} left for today"

    def _convert_to_rate(self, amount: int, currency: str) -> float:
        """
        Convert amount from RUB to specified currency.

        Args:
            amount: Amount in RUB.
            currency: Target currency (USD, EUR, RUB).

        Returns:
            Converted amount.

        Raises:
            ValueError: If currency is unsupported.
        """
        if currency not in self.RATES:
            raise ValueError("Unsupported currency")
        return amount / self.RATES[currency]
