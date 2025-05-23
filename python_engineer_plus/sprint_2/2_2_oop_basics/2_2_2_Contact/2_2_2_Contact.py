'''
TODO:
    In 1927, Bulgakov moved to a new address:
        Russia, Moscow, Nashchokinsky Pereulok, Building 3, Apt. 44
    his phone number changed to:
        K-058-67.

    And Mayakovsky went from Lubyanka to his apartment at the address:
        Russia, Moscow, Gendrikov Pereulok, Building 15, Apt. 5
    you can call him there at:
        2-35-71.

    Access the required properties of the mike and vlad objects and write new
    values to them.

    Run the code and check what happened: new data will be displayed on
    the screen.
'''
import datetime as dt


class Contact:
    """
    Class to store and display contact information.
    """

    def __init__(
        self,
        name: str,
        phone: str,
        address: str,
        birthday: str
    ) -> None:
        """
        Initialize contact with name, phone, address, and birthday.

        Args:
            name: Contact's full name.
            phone: Contact's phone number.
            address: Contact's address.
            birthday: Birthday in DD.MM.YYYY format.

        Raises:
            ValueError: If birthday format is invalid or inputs are empty.
        """
        if not all([name, phone, address]):
            raise ValueError("Name, phone, and address cannot be empty")
        self._name = name
        self._phone = phone
        self._address = address
        self._birthday = self._parse_birthday(birthday)

    @property
    def name(self) -> str:
        """
        Get contact name.
        """
        return self._name

    @property
    def phone(self) -> str:
        """
        Get contact phone.
        """
        return self._phone

    @phone.setter
    def phone(self, value: str) -> None:
        """
        Set contact phone.

        Args:
            value: New phone number.

        Raises:
            ValueError: If phone is empty.
        """
        if not value:
            raise ValueError("Phone cannot be empty")
        self._phone = value

    @property
    def address(self) -> str:
        """
        Get contact address.
        """
        return self._address

    @address.setter
    def address(self, value: str) -> None:
        """
        Set contact address.

        Args:
            value: New address.

        Raises:
            ValueError: If address is empty.
        """
        if not value:
            raise ValueError("Address cannot be empty")
        self._address = value

    @property
    def birthday(self) -> dt.date:
        """
        Get contact birthday.
        """
        return self._birthday

    def _parse_birthday(self, birthday: str) -> dt.date:
        """
        Parse birthday string to date.

        Args:
            birthday: Birthday in DD.MM.YYYY format.

        Returns:
            Parsed date object.

        Raises:
            ValueError: If format is invalid.
        """
        try:
            return dt.datetime.strptime(birthday, "%d.%m.%Y").date()
        except ValueError as e:
            raise ValueError(f"Invalid birthday format: {birthday}") from e

    def print_contact(self) -> None:
        """
        Print contact details.

        Returns:
            None, prints name, phone, address, and birthday.
        """
        print(f"Name: {self.name}")
        print(f"Phone: {self.phone}")
        print(f"Address: {self.address}")
        print(f"Birthday: {self.birthday.strftime('%d.%m.%Y')}")


# Create contacts
mike = Contact(
    name="Mikhail Bulgakov",
    phone="2-03-27",
    address="Russia, Moscow, Bolshaya Pirogovskaya, 35b, apt. 6",
    birthday="15.05.1891"
)
vlad = Contact(
    name="Vladimir Mayakovsky",
    phone="73-88",
    address="Russia, Moscow, Lubyansky proezd, 3, apt. 12",
    birthday="19.07.1893"
)

# Update contact details
mike.address = (
    "Russia, Moscow, Nashchokinsky Pereulok, "
    "Building 3, Apt. 44"
)
mike.phone = "K-058-67"
vlad.address = (
    "Russia, Moscow, Gendrikov Pereulok, "
    "Building 15, Apt. 5"
)
vlad.phone = "2-35-71"

# Print updated contact details
mike.print_contact()
print()  # Separator for readability
vlad.print_contact()
