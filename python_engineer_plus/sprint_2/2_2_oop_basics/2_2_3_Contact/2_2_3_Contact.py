'''
TODO:
    In the previous task, to display data about each object on the screen, we
    wrote separate code for each object.

    This is cumbersome and irrational, OOP allows you to optimize the code.

    In the Contact class, create a show_contact() method that will display
    data for any Contact object in the same form as the print_contact function
    currently displays them.
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

    def show_contact(self) -> None:
        """
        Show contact details.

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

mike.show_contact()
print()  # Separator for readability
vlad.show_contact()
