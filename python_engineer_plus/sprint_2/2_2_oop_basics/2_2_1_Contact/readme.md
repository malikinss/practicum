# Contact Class Implementation

## Description 📝

The provided code implements the `Contact` class, which stores and displays contact information, including newly added `address` and `birthday` properties.

The class includes an initializer to set `name`, `phone`, `address`, and `birthday`, a helper method `_parse_birthday` to validate and parse the birthday string into a `datetime.date` object, and a `print_contact` method to display the contact's details.

Two contact objects, `mike` (Mikhail Bulgakov) and `vlad` (Vladimir Mayakovsky), are created with the specified data, and their details are printed using `print_contact`.

## Purpose 🎯

Intended for contact management systems, data storage, or educational examples of object-oriented programming, datetime parsing, and string formatting in Python.

## How It Works 🔍

-   **Module Import**:
    -   `import datetime as dt`: Imports the `datetime` module with alias `dt` for date handling.
-   **Class Definition**:
    -   `Contact` class with:
        -   `__init__`: Initializes attributes `name`, `phone`, `address`, and `birthday`.
        -   `_parse_birthday`: Parses birthday string (`DD.MM.YYYY`) to `dt.date`.
        -   `print_contact`: Prints contact details in a formatted manner.
-   ****init** Method**:
    -   Takes `name: str`, `phone: str`, `address: str`, `birthday: str`.
    -   Assigns `name`, `phone`, and `address` directly.
    -   Sets `birthday` by calling `_parse_birthday`.
-   **\_parse_birthday Method**:
    -   Takes a birthday string in `DD.MM.YYYY` format.
    -   Uses `dt.datetime.strptime(birthday, "%d.%m.%Y").date()` to parse.
    -   Raises `ValueError` for invalid formats.
    -   Returns a `dt.date` object.
-   **print_contact Method**:
    -   Prints:
        -   `Name: <name>`
        -   `Phone: <phone>`
        -   `Address: <address>`
        -   `Birthday: <birthday>` (formatted as `DD.MM.YYYY` using `strftime`).
-   **Main Code**:
    -   Creates `mike` with:
        -   Name: "Mikhail Bulgakov"
        -   Phone: "2-03-27"
        -   Address: "Russia, Moscow, Bolshaya Pirogovskaya, 35b, apt. 6"
        -   Birthday: "15.05.1891"
    -   Creates `vlad` with:
        -   Name: "Vladimir Mayakovsky"
        -   Phone: "73-88"
        -   Address: "Russia, Moscow, Lubyansky proezd, 3, apt. 12"
        -   Birthday: "19.07.1893"
    -   Calls `mike.print_contact()` and `vlad.print_contact()`, with a blank line separator.
-   **Behavior**:

    -   For `mike`:
        -   Birthday parsed: `1891-05-15`.
        -   Output:
            ```
            Name: Mikhail Bulgakov
            Phone: 2-03-27
            Address: Russia, Moscow, Bolshaya Pirogovskaya, 35b, apt. 6
            Birthday: 15.05.1891
            ```
    -   For `vlad`:
        -   Birthday parsed: `1893-07-19`.
        -   Output:
            ```
            Name: Vladimir Mayakovsky
            Phone: 73-88
            Address: Russia, Moscow, Lubyansky proezd, 3, apt. 12
            Birthday: 19.07.1893
            ```
    -   Full output:

        ```
        Name: Mikhail Bulgakov
        Phone: 2-03-27
        Address: Russia, Moscow, Bolshaya Pirogovskaya, 35b, apt. 6
        Birthday: 15.05.1891

        Name: Vladimir Mayakovsky
        Phone: 73-88
        Address: Russia, Moscow, Lubyansky proezd, 3, apt. 12
        Birthday: 19.07.1893
        ```

## Verification ✅

Implementation satisfies requirements:

-   **Functionality**:
    -   Adds `address` and `birthday` properties to `Contact` class.
    -   Creates `mike` and `vlad` objects with specified data.
    -   Calls `print_contact()` for both, displaying all properties.
-   **Correctness**:
    -   `__init__` correctly assigns `name`, `phone`, `address`, and parsed `birthday`.
    -   `_parse_birthday` validates and converts `DD.MM.YYYY` to `dt.date`.
    -   `print_contact` formats output correctly, with birthday as `DD.MM.YYYY`.
    -   No validation needed for `name`, `phone`, or `address`, as inputs are guaranteed valid.
-   **Output**:
    -   Matches expected format for both contacts.
    -   Birthday is formatted correctly (e.g., `15.05.1891`).
-   **Documentation**: Clear docstrings with type hints.

## Potential Considerations 🛠️

-   **Correctness**:
    -   `_parse_birthday` ensures valid `DD.MM.YYYY` format (e.g., handles `15.05.1891` correctly).
    -   `strftime('%d.%m.%Y')` in `print_contact` restores original format for output.
    -   Error handling in `_parse_birthday` prevents invalid dates (e.g., `32.13.1891`).
    -   Stores `birthday` as `dt.date` for potential future date operations.
-   **Performance**:
    -   `__init__`: O(1) for assignments and parsing.
    -   `_parse_birthday`: O(1) for fixed-length string parsing.
    -   `print_contact`: O(1) for printing.
    -   Total: O(1), highly efficient.
-   **Design**:
    -   Type hints (`str`, `dt.date`) clarify input/output.
    -   Private `_parse_birthday` method encapsulates parsing logic.
    -   Simple, focused class structure.
    -   Flexible `phone` and `address` as strings, allowing various formats.
-   **Alternatives**:
    -   Store birthday as string: Loses date functionality.
    -   Manual parsing: Split `DD.MM.YYYY` and construct `date` (error-prone).
    -   No error handling: Risks crashes on invalid dates.
-   **Extensibility**:
    -   Easily add more properties (e.g., email, notes).
    -   Could validate `phone` format or `address` structure.
    -   Could add methods to calculate age or format output differently.
-   **Edge Cases**:
    -   Invalid birthday: Caught by `ValueError` (not applicable with given inputs).
    -   Empty strings: Not validated, as inputs are guaranteed valid.
    -   Leap year birthdays (e.g., `29.02.1892`): Handled by `datetime`.

## Usage Example (For Clarity, Not Submission) 📦

```python
# Provided example
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
mike.print_contact()
print()
vlad.print_contact()
# Output:
# Name: Mikhail Bulgakov
# Phone: 2-03-27
# Address: Russia, Moscow, Bolshaya Pirogovskaya, 35b, apt. 6
# Birthday: 15.05.1891
#
# Name: Vladimir Mayakovsky
# Phone: 73-88
# Address: Russia, Moscow, Lubyansky proezd, 3, apt. 12
# Birthday: 19.07.1893

# Additional test case
try:
    invalid = Contact("Test", "123", "Test Address", "32.13.1891")
    invalid.print_contact()
except ValueError as e:
    print(e)  # Invalid birthday format: 32.13.1891
```

## Conclusion 🚀

The `Contact` class implementation is precise, correctly adding `address` and `birthday` properties, creating `mike` and `vlad` objects with the specified data, and printing their details using `print_contact`.

It parses birthdays into `dt.date` objects, handles errors, and formats output as required.

The implementation is efficient, robust, and fully compliant with the task’s requirements, making it ideal for contact management or teaching object-oriented programming and datetime handling.
