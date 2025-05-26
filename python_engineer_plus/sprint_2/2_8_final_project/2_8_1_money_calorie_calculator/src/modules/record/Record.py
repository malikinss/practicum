"""
This module defines a Record class to store and display records
with attributes for amount, date, and comment.
It includes methods for initialization, date parsing,
and string representation.
"""
import datetime as dt


class Record:
    """
    Class to store and display a record with amount, date, and comment.
    """

    def __init__(
        self,
        amount: int,
        date: str = '',
        comment: str = 'No comment'
    ) -> None:
        """
        Initialize record with amount, date, and comment.

        Args:
            amount: Non-negative integer amount.
            date: Date in YYYY-MM-DD format, defaults to today if empty.
            comment: Optional comment, defaults to 'No comment'.

        Raises:
            ValueError: If amount is not an integer, negative, or comment
                        is empty.
        """
        if not isinstance(amount, int):
            raise ValueError("Amount must be an integer")
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        if not comment:
            raise ValueError("Comment cannot be empty")
        self.amount = amount
        self.date = self._parse_str_to_date(date)
        self.comment = comment

    @staticmethod
    def _parse_str_to_date(date_str: str) -> dt.date:
        """
        Parse date string to date object.

        Args:
            date_str: Date in YYYY-MM-DD format.

        Returns:
            Parsed date or today's date if invalid/empty.
        """
        if not date_str:
            return dt.date.today()
        try:
            return dt.datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError:
            return dt.date.today()

    @staticmethod
    def _parse_date_to_str(date: dt.date) -> str:
        """
        Format date object to string.

        Args:
            date: Date object.

        Returns:
            Date in YYYY-MM-DD format.
        """
        return date.strftime('%Y-%m-%d')

    def __str__(self) -> str:
        """
        Return readable string representation.

        Returns:
            String in format '<amount> on <date> - <comment>'.
        """
        date_str = self._parse_date_to_str(self.date)
        return f"{self.amount} on {date_str} - {self.comment}"

    def __repr__(self) -> str:
        """
        Return detailed string representation.

        Returns:
            String in format:
                'Record(amount=<amount>, date=<date>, comment=<comment>)'.
        """
        return (f"Record(amount={self.amount}, "
                f"date={self.date.strftime('%Y-%m-%d')}, "
                f"comment={self.comment})")
