# Contact Class with show_contact Method Implementation

## Description 📝

The provided code modifies the `Contact` class to include a new `show_contact` method, which replicates the functionality of the existing `print_contact` method but is named as specified in the task.

This method displays the contact’s details (`name`, `phone`, `address`, and `birthday`) in the same format as before, optimizing the code by encapsulating the display logic within the class.

The `print_contact` method is replaced by `show_contact` to avoid redundancy. The code creates `mike` and `vlad` objects with their initial 1927 contact details and calls `show_contact` to display their information, improving code reuse and adhering to object-oriented principles.

## Purpose 🎯

Intended for contact management systems, demonstrating encapsulation and method reuse in object-oriented programming, or for educational examples of class method implementation in Python.

## How It Works 🔍

-   **Module Import**:
    -   `import datetime as dt`: Imports `datetime` with alias `dt` for birthday parsing.
-   **Class Definition**:
    -   `Contact` class, updated to include `show_contact`:
        -   `__init__`: Initializes `name`, `phone`, `address`, and `birthday` with validation.
        -   Properties: `name`, `phone`, `address`, `birthday` with getters; `phone` and `address` have setters.
        -   `_parse_birthday`: Parses birthday string to `dt.date`.
        -   `show_contact`: Prints contact details, replacing `print_contact`.
-   ****init** Method**:
    -   Takes `name: str`, `phone: str`, `address: str`, `birthday: str`.
    -   Validates non-empty `name`, `phone`, `address` using `if not all([name, phone, address])`.
    -   Stores attributes privately (`_name`, `_phone`, `_address`, `_birthday`).
    -   Parses `birthday` using `_parse_birthday`.
-   **Properties**:
    -   `name`, `phone`, `address`, `birthday`: Getters for accessing values.
    -   `phone.setter`, `address.setter`: Allow updates with non-empty validation.
    -   `birthday`: Read-only, returns `dt.date`.
-   **\_parse_birthday Method**:
    -   Parses `DD.MM.YYYY` string to `dt.date` using `dt.datetime.strptime`.
    -   Raises `ValueError` for invalid formats.
-   **show_contact Method**:
    -   Prints:
        -   `Name: <name>`
        -   `Phone: <phone>`
        -   `Address: <address>`
        -   `Birthday: <birthday>` (formatted as `DD.MM.YYYY` using `strftime`).
    -   Identical in output to the previous `print_contact` method.
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
    -   Calls `mike.show_contact()` and `vlad.show_contact()`, with a blank line separator.
-   **Behavior**:

    -   For `mike`:
        -   Output:
            ```
            Name: Mikhail Bulgakov
            Phone: 2-03-27
            Address: Russia, Moscow, Bolshaya Pirogovskaya, 35b, apt. 6
            Birthday: 15.05.1891
            ```
    -   For `vlad`:
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
    -   Adds `show_contact` method to `Contact` class.
    -   `show_contact` displays `name`, `phone`, `address`, and `birthday` in the same format as the previous `print_contact`.
    -   Replaces separate print calls for `mike` and `vlad` with `show_contact`, optimizing code reuse.
-   **Correctness**:
    -   `show_contact` matches `print_contact` output format exactly.
    -   Uses properties (`self.name`, etc.) for consistent access.
    -   Formats birthday as `DD.MM.YYYY` using `strftime`.
    -   Maintains all existing functionality (validation, properties, setters).
-   **Output**:
    -   Matches expected format for `mike` and `vlad`.
    -   Displays all properties correctly, with proper formatting.
-   **Documentation**: Updated docstrings to reflect `show_contact`.

## Potential Considerations 🛠️

-   **Correctness**:
    -   `show_contact` uses the same logic as `print_contact`, ensuring identical output.
    -   Properties ensure safe access to attributes (`_name`, `_phone`, etc.).
    -   Birthday formatting (`%d.%m.%Y`) preserves `DD.MM.YYYY` format.
    -   No changes to validation or setters, as they remain functional.
-   **Performance**:
    -   `show_contact`: O(1) for accessing properties and printing.
    -   Overall: O(1), as efficient as `print_contact`.
-   **Design**:
    -   `show_contact` encapsulates display logic, adhering to OOP principles.
    -   Replaces redundant external print calls, improving maintainability.
    -   Type hints and private attributes remain consistent.
    -   Method name `show_contact` matches task specification.
-   **Alternatives**:
    -   Keep `print_contact`: Unnecessary, as `show_contact` serves the same purpose.
    -   Custom format: Could use a template, but current format is specified.
    -   Return string instead of printing: Not required by task.
-   **Extensibility**:
    -   Easily modify `show_contact` to include additional properties.
    -   Could add formatting options (e.g., different date formats).
    -   Could integrate with a contact list for bulk display.
-   **Edge Cases**:
    -   Invalid data: Handled at initialization (not relevant for display).
    -   Empty attributes: Prevented by `__init__` and setter validation.
    -   Special characters in `name` or `address`: Handled by string printing.

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
mike.show_contact()
print()
vlad.show_contact()
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
new_contact = Contact("Test User", "123-45", "Test Address", "01.01.2000")
new_contact.show_contact()
# Output:
# Name: Test User
# Phone: 123-45
# Address: Test Address
# Birthday: 01.01.2000
```

## Conclusion 🚀

The `Contact` class implementation successfully adds the `show_contact` method, replacing `print_contact` and optimizing the code by encapsulating display logic within the class.

It correctly displays the details of `mike` and `vlad` in the specified format, maintaining all existing functionality.

The implementation is efficient, adheres to OOP principles, and is fully compliant with the task’s requirements, making it ideal for contact management or teaching method encapsulation in Python.
