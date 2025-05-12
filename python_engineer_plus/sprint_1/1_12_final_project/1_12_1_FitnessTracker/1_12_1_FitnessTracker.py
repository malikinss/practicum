'''
TODO:
    Develop a software module for the "runaway" fitness tracker from Unicorn
    in the form of a FitnessTracker class that processes step data and
    displays a daily activity summary.

    The module must comply with the technical specifications.

    Input data:
        Data package in the form of a tuple package = (<time>, <steps>), where:
            - <time> is a string, the time the package was created in
            the "HH:MM:SS" format (e.g., "09:36:02").
            - <steps> is an integer, the number of steps since the last access.

    Example:
        package = ("09:36:02", 15000).

    Output data:
        - The storage_data dictionary, where the keys are time (str),
          the values are the number of steps (int).
        - Message to the terminal in the format:
            Time: <time from the package>.
            Number of steps for today:
                <sum of steps since the beginning of the day>.
            Distance was <distance in km> km.
            You burned <number of kilocalories> kcal.
            <motivational message>

    Example output:
        Time: 09:36:02.
        Steps today: 15302.
        Distance was 9.95 km.
        You burned 1512.00 kcal.
        Great result! Goal reached.

    Motivational message depends on distance:
        ≥ 6.5 km: "Great result! Goal reached"
        ≥ 3.9 km: "Not bad! It was a productive day."
        ≥ 2 km: "Not enough, but we'll make up for it tomorrow!"
        < 2 km: "Lying down is also good for you.
                 The main thing is to participate, not to win!"

    Requirements:
        - Implement the module as a FitnessTracker class with methods:
            __init__: initializes an empty storage_data dictionary.
            check_correct_data: checks the correctness of
                      the packet (length, types, non-empty values).
            check_correct_time: checks the time format and its order
                                (within a day).
            get_step_day: returns the total number of steps per day.
            get_distance: converts steps to kilometers.
            get_spent_calories: calculates burned kilocalories.
            get_achievement: returns a motivational message.
            show_message: generates and prints a summary.
            accept_package: entry point, accepts a packet, processes data and
                            returns storage_data.
        - Check the correctness of the packet:
            The tuple length must be equal to 2.
            No parameters must be empty.
            The time in the new packet must be greater than the previous one
            (within a day).
        - Save data to self.storage_data only after verification.
        - Calculate steps, distance (in km) and calories per day
          (from 00:00:00 to the time in the package).
        - Reset data for the next day (not implemented in the code,
          an external call is assumed).
        - Methods must be called in the correct order via accept_package.
'''
import datetime as dt
from decimal import Decimal
from typing import Dict, Tuple


class FitnessTracker:
    """
    Fitness tracker module for processing step data.
    """
    WEIGHT = 75
    HEIGHT = 175
    K_1 = 0.035
    K_2 = 0.029
    STEP_M = 0.65
    TIME_FORMAT = '%H:%M:%S'
    MOTIVATIONS = [
        'Отличный результат! Цель достигнута',
        'Неплохо! День был продуктивным.',
        'Маловато, но завтра наверстаем!',
        'Лежать тоже полезно. Главное — участие, а не победа!',
    ]

    def __init__(self) -> None:
        """
        Initialize the fitness tracker with empty storage.
        """
        self.storage_data: Dict[dt.datetime, int] = {}

    def check_correct_data(self, data: Tuple[str, int]) -> bool:
        """
        Check if the data package is valid.

        Args:
            data: Tuple of (time: str, steps: int).

        Returns:
            True if data is valid, False otherwise.
        """
        if len(data) != 2 or not all(data):
            return False
        time, steps = data
        if not isinstance(time, str) or not isinstance(steps, int):
            return False
        try:
            dt.datetime.strptime(time, self.TIME_FORMAT)
            return True
        except ValueError:
            return False

    def check_correct_time(self, time: str) -> bool:
        """
        Check if the time is later than previous entries.

        Args:
            time: Time string in HH:MM:SS format.

        Returns:
            True if time is valid and later, False otherwise.
        """
        try:
            current_time = dt.datetime.strptime(time, self.TIME_FORMAT)
        except ValueError:
            return False
        for stored_time in self.storage_data:
            if stored_time >= current_time:
                return False
        return True

    def get_step_day(self, steps: int) -> int:
        """
        Calculate total steps for the current day.

        Args:
            steps: Steps from the current package.

        Returns:
            Total steps including current package.
        """
        total_steps = sum(self.storage_data.values()) + steps
        return total_steps

    def get_distance(self, steps: int) -> float:
        """
        Convert steps to distance in kilometers.

        Args:
            steps: Total steps.

        Returns:
            Distance in kilometers, rounded to 2 decimals.
        """
        distance = (steps * self.STEP_M) / 1000
        return round(float(distance), 2)

    def get_decimal(self, data: float) -> Decimal:
        """
        Convert data to Decimal.

        Args:
            data: Numeric data to convert.

        Returns:
            Decimal representation of data.
        """
        return Decimal(str(data))

    def get_spent_calories(self, dist: float, current_time: str) -> float:
        """
        Calculate calories burned based on distance and time.

        Args:
            dist: Distance in kilometers.
            current_time: Time string in HH:MM:SS format.

        Returns:
            Calories burned, rounded to 2 decimals.
        """
        time_obj = dt.datetime.strptime(current_time, self.TIME_FORMAT)
        k_1 = self.get_decimal(self.K_1)
        k_2 = self.get_decimal(self.K_2)
        weight = self.get_decimal(self.WEIGHT)
        height = self.get_decimal(self.HEIGHT)
        d_dist = self.get_decimal(dist)
        hours = self.get_decimal(time_obj.hour + time_obj.minute / 60)
        mean_speed = d_dist / hours
        minutes = hours * 60
        calories_per_min = (
            (k_1 * weight + (mean_speed ** 2 / height))
            * (k_2 * weight)
        )
        return round(float(calories_per_min * minutes), 2)

    def get_achievement(self, dist: float) -> str:
        """
        Determine motivational message based on distance.

        Args:
            dist: Distance in kilometers.

        Returns:
            Motivational message.
        """
        if dist >= 6.5:
            return self.MOTIVATIONS[0]
        if dist >= 3.9:
            return self.MOTIVATIONS[1]
        if dist >= 2:
            return self.MOTIVATIONS[2]
        return self.MOTIVATIONS[3]

    def show_message(
        self,
        time: str,
        steps: int,
        distance: float,
        calories: float,
        achievement: str
    ) -> None:
        """
        Print summary message for the current day.

        Args:
            time: Time string in HH:MM:SS format.
            steps: Total steps.
            distance: Distance in kilometers.
            calories: Calories burned.
            achievement: Motivational message.

        Returns:
            None, prints the summary.
        """
        print(f"Время: {time}.")
        print(f"Количество шагов за сегодня: {steps}.")
        print(f"Дистанция составила {distance} км.")
        print(f"Вы сожгли {calories} ккал.")
        print(achievement)

    def accept_package(
        self, package: Tuple[str, int]
    ) -> Dict[dt.datetime, int]:
        """
        Process fitness tracker data package and return storage.

        Args:
            package: Tuple of (time: str, steps: int).

        Returns:
            Dictionary with stored data.
        """
        if not self.check_correct_data(package):
            return self.storage_data
        time, steps = package
        if not self.check_correct_time(time):
            return self.storage_data
        time_obj = dt.datetime.strptime(time, self.TIME_FORMAT)
        total_steps = self.get_step_day(steps)
        distance = self.get_distance(total_steps)
        calories = self.get_spent_calories(distance, time)
        achievement = self.get_achievement(distance)
        self.show_message(time, total_steps, distance, calories, achievement)
        self.storage_data[time_obj] = steps
        return self.storage_data


# Example usage
if __name__ == "__main__":
    tracker = FitnessTracker()
    package = ("09:36:02", 15000)
    tracker.accept_package(package)
