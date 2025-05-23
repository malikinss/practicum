'''
TODO:
    Add the address and birthday properties to the Contact class

    Create a mike object of the Contact type with the following data:
        name: Mikhail Bulgakov
        phone: 2-03-27
        address: Russia, Moscow, Bolshaya Pirogovskaya, 35b, apt. 6
        birthday: 15.05.1891

    Create a vlad object of the Contact type with the following data:
        name: Vladimir Mayakovsky
        phone: 73-88
        address: Russia, Moscow, Lubyansky proezd, 3, apt. 12
        birthday: 19.07.1893

    Call the print_contact() function to print the properties of the created
    objects on the screen
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
            ValueError: If birthday format is invalid.
        """
        self.name = name
        self.phone = phone
        self.address = address
        self.birthday = self._parse_birthday(birthday)

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
            None, prints contact properties.
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

# Print contact details
mike.print_contact()
print()  # Separator for readability
vlad.print_contact()
