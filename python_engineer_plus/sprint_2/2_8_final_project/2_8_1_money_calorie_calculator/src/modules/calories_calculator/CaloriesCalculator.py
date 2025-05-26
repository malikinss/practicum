"""
This module defines the CaloriesCalculator class for tracking daily calorie
intake.
It inherits from the Calculator class and provides methods to manage calorie
records, calculate remaining calories, and format messages based on calorie
limits.
"""
from ..calculator import Calculator


class CaloriesCalculator(Calculator):
    """
    Class to track daily calorie intake with a limit.
    Inherits from Calculator to manage records and calculate remaining
    calories.
    """

    def __init__(self, limit: int) -> None:
        """
        Initialize calculator with a daily calorie limit.

        Args:
            limit: Daily calorie limit (1000-3000 kcal).

        Raises:
            ValueError: If limit is not an integer, negative, or out of range.
        """
        if not isinstance(limit, int):
            raise ValueError("Limit must be an integer")
        if limit < 1000 or limit > 3000:
            raise ValueError("Limit must be between 1000 and 3000 kcal")
        super().__init__(limit)

    def get_today_calories_remained(self) -> str:
        """
        Get message about remaining calories for today.

        Returns:
            Message indicating remaining calories or to stop eating.
        """
        remained = self._get_today_remained()
        return self._get_calories_message(remained)

    def _get_calories_message(self, remained: int) -> str:
        """
        Format message based on remaining calories.

        Args:
            remained: Remaining calories.

        Returns:
            Message for remaining calories or to stop eating.
        """
        if remained > 0:
            return (
                f"Today you can eat something else, but with "
                f"a total caloric content of no more than {remained} kcal"
            )
        return "Stop eating!"
