"""
This module defines a Calculator class to track spending records
with a daily limit. It allows adding records, checking today's spending,
and calculating remaining budget for today and the last 7 days.
"""
import datetime as dt
from typing import List

from ..record import Record


class Calculator:
    """
    Class to track spending records with a daily limit.
    It allows adding records, checking today's spending,
    and calculating remaining budget for today and the last 7 days.
    """

    def __init__(self, limit: int) -> None:
        """
        Initialize calculator with a daily spending limit.

        Args:
            limit: Non-negative integer daily limit.

        Raises:
            ValueError: If limit is not a non-negative integer.
        """
        if not isinstance(limit, int):
            raise ValueError("Limit must be an integer")
        if limit < 0:
            raise ValueError("Limit cannot be negative")
        self.limit = limit
        self.records: List[Record] = []

    def add_record(self, record: Record) -> None:
        """
        Add a record if it doesn't exceed today's limit.

        Args:
            record: Record object to add.

        Raises:
            TypeError: If record is not a Record instance.
            ValueError: If amount exceeds limit or date is in the future.
        """
        if not isinstance(record, Record):
            raise TypeError("Record must be an instance of Record")
        if record.date > dt.date.today():
            raise ValueError("Record date cannot be in the future")
        if record.date == dt.date.today():
            if record.amount > self._get_today_remained():
                raise ValueError("Record amount exceeds today's limit")
        self.records.append(record)

    def _get_spent_by_date(self, date: dt.date) -> int:
        """
        Calculate total amount spent on a given date.

        Args:
            date: Date to check.

        Returns:
            Total amount spent.
        """
        return sum(record.amount for record in self.records
                   if record.date == date)

    def _get_today_spent(self) -> int:
        """
        Calculate total amount spent today.

        Returns:
            Total amount spent today.
        """
        return self._get_spent_by_date(dt.date.today())

    def _get_today_remained(self) -> int:
        """
        Calculate remaining limit for today.

        Returns:
            Remaining amount for today.
        """
        return self.limit - self._get_today_spent()

    def get_today_stats(self) -> str:
        """
        Get today's spending statistics.

        Returns:
            String with spent and remaining amounts.
        """
        spent = self._get_today_spent()
        remained = self._get_today_remained()
        return f"Today: spent {spent}, remained {remained}"

    def get_week_stats(self) -> str:
        """
        Get spending statistics for the last 7 days.

        Returns:
            String with total spent over the week.
        """
        total = sum(self._get_spent_by_date(date)
                    for date in self._get_week_dates())
        return f"Last 7 days: spent {total}"

    def _get_week_dates(self) -> List[dt.date]:
        """
        Get dates for today and the previous 6 days.

        Returns:
            List of dates.
        """
        today = dt.date.today()
        return [today - dt.timedelta(days=i) for i in range(7)]
