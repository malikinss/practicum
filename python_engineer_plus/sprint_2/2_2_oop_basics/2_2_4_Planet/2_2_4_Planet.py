'''
TODO:
    The precode contains a Planet class, it describes planets and stores
    the properties:
        - name
        - surface_area (surface area in km²)
        - average_temp_celcius (average surface temperature of the planet
          in Celsius)
        - average_temp_fahrenheit (also in Fahrenheit).

    The class constructor takes three parameters as input:
        - the name of the planet
        - its radius in kilometers
        - the average surface temperature in degrees Celsius.

    In the constructor, calculate the surface area of the planet.

    For simplicity, consider the planets to be spherical.

    The surface area of a sphere with radius r is 4 * π * r² .

    In the constructor, calculate the surface temperature in Fahrenheit.

    To convert the temperature in Celsius to the Fahrenheit scale, multiply
    the value by 9/5 and add 32.
'''
import math


class Planet:
    """
    Class to store and display planet properties.
    """

    def __init__(
        self,
        name: str,
        radius: float,
        temp_celsius: float
    ) -> None:
        """
        Initialize planet with name, radius, and temperature.

        Args:
            name: Planet's name.
            radius: Radius in kilometers.
            temp_celsius: Average surface temperature in Celsius.

        Raises:
            ValueError: If name is empty or radius is negative.
        """
        if not name:
            raise ValueError("Name cannot be empty")
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.name = name
        self.radius = radius
        self.surface_area = self._get_surface_area()
        self.average_temp_celsius = temp_celsius
        self.average_temp_fahrenheit = self._get_fahrenheit(temp_celsius)

    def _get_surface_area(self) -> float:
        """
        Calculate surface area of the planet.

        Returns:
            Surface area in square kilometers.
        """
        # 4 * π * r²
        return 4 * math.pi * self.radius ** 2

    def _get_fahrenheit(self, celsius: float) -> float:
        """
        Convert Celsius to Fahrenheit.

        Args:
            celsius: Temperature in Celsius.

        Returns:
            Temperature in Fahrenheit.
        """
        # C * 9/5 + 32
        return celsius * 9 / 5 + 32

    def show_info(self) -> None:
        """
        Print planet details.

        Returns:
            None, prints name, surface area, and temperature.
        """
        print(f"Planet: {self.name} has surface area "
              f"{self.surface_area} square kilometers")
        print(f"Average temperature on the surface is "
              f"{self.average_temp_fahrenheit} Fahrenheit")
