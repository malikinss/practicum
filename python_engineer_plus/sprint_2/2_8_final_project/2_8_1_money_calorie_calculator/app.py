"""
Demonstrate usage of CashCalculator and CaloriesCalculator.
"""
from src.modules import (
    CaloriesCalculator,
    CashCalculator,
    Record,
)

# Cash spending example
cash_calc = CashCalculator(limit=5000)
print(cash_calc.get_today_cash_remained("RUB"))

cash_calc.add_record(Record(
    amount=145,
    date="2025-05-27",
    comment="Coffee"
))
print(cash_calc.get_today_cash_remained("RUB"))

cash_calc.add_record(Record(
    amount=300,
    date="2025-05-27",
    comment="Dinner with friends"
))
print(cash_calc.get_today_cash_remained("RUB"))

# Calorie tracking example
calories_calc = CaloriesCalculator(limit=2000)
calories_calc.add_record(Record(
    amount=500,
    date="2025-05-27",
    comment="Breakfast"
))
print(calories_calc.get_today_calories_remained())

calories_calc.add_record(Record(
    amount=700,
    date="2025-05-27",
    comment="Lunch"
))
print(calories_calc.get_today_calories_remained())

calories_calc.add_record(Record(
    amount=800,
    date="2025-05-27",
    comment="Dinner"
))
print(calories_calc.get_today_calories_remained())
