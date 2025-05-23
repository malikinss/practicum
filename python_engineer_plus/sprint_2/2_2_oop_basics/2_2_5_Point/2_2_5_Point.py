'''
TODO:
    The code describes the Point class (a point on the map), it has
    properties - latitude and longitude, and the distance(self, other) method
    is the distance between two points in kilometers (the other parameter must
    receive another Point object).

    Create two classes that inherit the Point class:
        - City(Point, name, population) - describes the city, the city
                                          coordinates (an object of the Point
                                          class), its name and population are
                                          passed to the constructor.
        - Mountain(Point, name, height) - describes the mountain, the mountain
                                          coordinates (an object of the Point
                                          class), its name and height in
                                          meters are passed to the constructor.

    Your task is to display the distance from Moscow to Everest.
'''
from math import radians, sin, cos, acos


class Point:
    """
    Class for a point on Earth with latitude and longitude.
    """

    def __init__(self, latitude: float, longitude: float) -> None:
        """
        Initialize point with latitude and longitude.

        Args:
            latitude: Latitude in degrees (-90 to 90).
            longitude: Longitude in degrees (-180 to 180).

        Raises:
            ValueError: If latitude or longitude is out of range.
        """
        if not -90 <= latitude <= 90:
            raise ValueError("Latitude must be between -90 and 90")
        if not -180 <= longitude <= 180:
            raise ValueError("Longitude must be between -180 and 180")
        self.latitude = radians(latitude)
        self.longitude = radians(longitude)

    def distance(self, other: 'Point') -> float:
        """
        Calculate distance to another point in kilometers.

        Args:
            other: Another Point object.

        Returns:
            Distance in kilometers.
        """
        cos_d = (sin(self.latitude) * sin(other.latitude) +
                 cos(self.latitude) * cos(other.latitude) *
                 cos(self.longitude - other.longitude))
        # Clamp cos_d to [-1, 1] to avoid acos domain errors
        cos_d = min(1.0, max(-1.0, cos_d))
        return 6371 * acos(cos_d)


class City(Point):
    """
    Class for a city with name and population.
    """

    def __init__(
        self,
        latitude: float,
        longitude: float,
        name: str,
        population: int
    ) -> None:
        """
        Initialize city with coordinates, name, and population.

        Args:
            latitude: Latitude in degrees.
            longitude: Longitude in degrees.
            name: City name.
            population: City population.

        Raises:
            ValueError: If name is empty or population is negative.
        """
        super().__init__(latitude, longitude)
        if not name:
            raise ValueError("Name cannot be empty")
        if population < 0:
            raise ValueError("Population cannot be negative")
        self.name = name
        self.population = population

    def show(self) -> None:
        """
        Print city details.

        Returns:
            None, prints name and population.
        """
        print(f"City: {self.name}")
        print(f"Population: {self.population}")


class Mountain(Point):
    """
    Class for a mountain with name and height.
    """

    def __init__(
        self,
        latitude: float,
        longitude: float,
        name: str,
        height: float
    ) -> None:
        """I
        nitialize mountain with coordinates, name, and height.

        Args:
            latitude: Latitude in degrees.
            longitude: Longitude in degrees.
            name: Mountain name.
            height: Height in meters.

        Raises:
            ValueError: If name is empty or height is negative.
        """
        super().__init__(latitude, longitude)
        if not name:
            raise ValueError("Name cannot be empty")
        if height < 0:
            raise ValueError("Height cannot be negative")
        self.name = name
        self.height = height

    def show(self) -> None:
        """
        Print mountain details.

        Returns:
            None, prints name and height.
        """
        print(f"Mountain: {self.name}")
        print(f"Height: {self.height} meters")


# Create Moscow and Everest
moscow = City(
    latitude=55.75,
    longitude=37.62,
    name="Moscow",
    population=12_600_000
)
everest = Mountain(
    latitude=27.99,
    longitude=86.93,
    name="Everest",
    height=8848
)

# Display distance
distance = moscow.distance(everest)
print(f"Distance from {moscow.name} to {everest.name}: {distance:.2f} km")
