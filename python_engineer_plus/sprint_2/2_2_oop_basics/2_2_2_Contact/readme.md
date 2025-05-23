# Contact Class Update Implementation

## Description 📝

The provided code extends the `Contact` class from the previous implementation by adding property decorators for `name`, `phone`, `address`, and `birthday`, including setters for `phone` and `address` to allow updates.

It also adds input validation in `__init__` to prevent empty values. The code updates the `mike` and `vlad` objects with new `address` and `phone` values for 1927, as specified, and prints their updated details using the `print_contact` method.

The updates reflect Mikhail Bulgakov’s move to Nashchokinsky Pereulok and Vladimir Mayakovsky’s move to Gendrikov Pereulok, along with their new phone numbers.

## Purpose 🎯

Intended for contact management systems, demonstrating property decorators, input validation, and object state updates in Python, or for educational examples of object-oriented programming.

## How It Works 🔍

-   **Module Import**:
    -   `import datetime as dt`: Imports `datetime` with alias `dt` for birthday parsing.
-   **Class Definition**:
    -   `Contact` class with enhanced features:
        -   `__init__`: Initializes `name`, `phone`, `address`, and `birthday` with validation.
        -   Properties: `name`, `phone`, `address`, `birthday` with getters; `phone` and `address` have setters.
        -   `_parse_birthday`: Parses birthday string to `dt.date`.
        -   `print_contact`: Prints contact details.
-   ****init** Method**:
    -   Takes `name: str`, `phone: str`, `address: str`, `birthday: str`.
    -   Validates non-empty `name`, `phone`, `address` using `if not all([name, phone, address])`.
    -   Stores attributes with private naming (`_name`, `_phone`, `_address`, `_birthday`).
    -   Parses `birthday` using `_parse_birthday`.
-   **Properties**:
    -   `name`, `phone`, `address`, `birthday`: Getters return respective values.
    -   `phone.setter`, `address.setter`: Allow updates, validate non-empty values.
    -   `birthday`: Read-only, returns `dt.date`.
-   **\_parse_birthday Method**:
    -   Parses `DD.MM.YYYY` string to `dt.date` using `dt.datetime.strptime`.
    -   Raises `ValueError` for invalid formats.
-   **print_contact Method**:
    -   Prints:
        -   `Name: <name>`
        -   `Phone: <phone>`
        -   `Address: <address>`
        -   `Birthday: <birthday>` (as `DD.MM.YYYY`).
-   **Main Code**:
    -   Creates `mike` and `vlad` with initial data (same as previous task).
    -   Updates:
        -   `mike.address`: "Russia, Moscow, Nashchokinsky Pereulok, Building 3, Apt. 44".
        -   `mike.phone`: "K-058-67".
        -   `vlad.address`: "Russia, Moscow, Gendrikov Pereulok, Building 15, Apt. 5".
        -   `vlad.phone`: "2-35-71".
    -   Calls `mike.print_contact()` and `vlad.print_contact()` with a blank line separator.
-   **Behavior**:

    -   For `mike`:
        -   Updated: Address and phone changed.
        -   Output:
            ```
            Name: Mikhail Bulgakov
            Phone: K-058-67
            Address: Russia, Moscow, Nashchokinsky Pereulok, Building 3, Apt. 44
            Birthday: 15.05.1891
            ```
    -   For `vlad`:
        -   Updated: Address and phone changed.
        -   Output:
            ```
            Name: Vladimir Mayakovsky
            Phone: 2-35-71
            Address: Russia, Moscow, Gendrikov Pereulok, Building 15, Apt. 5
            Birthday: 19.07.1893
            ```
    -   Full output:

        ```
        Name: Mikhail Bulgakov
        Phone: K-058-67
        Address: Russia, Moscow, Nashchokinsky Pereulok, Building 3, Apt. 44
        Birthday: 15.05.1891

        Name: Vladimir Mayakovsky
        Phone: 2-35-71
        Address: Russia, Moscow, Gendrikov Pereulok, Building 15, Apt. 5
        Birthday: 19.07.1893
        ```

## Verification ✅

Implementation satisfies requirements:

-   **Functionality**:
    -   Updates `mike`’s `address` and `phone` to new 1927 values.
    -   Updates `vlad`’s `address` and `phone` to new 1927 values.
    -   Prints updated details using `print_contact`.
-   **Correctness**:
    -   Property setters (`phone`, `address`) allow updates and validate non-empty values.
    -   `print_contact` displays updated `address` and `phone`, with unchanged `name` and `birthday`.
    -   Birthday remains `dt.date`, formatted as `DD.MM.YYYY` in output.
    -   Validation in `__init__` and setters ensures robustness.
-   **Output**:
    -   Matches expected format with updated values.
    -   Maintains consistent formatting (e.g., `Birthday: 15.05.1891`).
-   **Documentation**: Clear docstrings with type hints and validation details.

## Potential Considerations 🛠️

-   **Correctness**:
    -   Setters ensure non-empty `phone` and `address` (e.g., `mike.phone = "K-058-67"` is valid).
    -   Properties protect internal state (`_phone`, `_address`) while allowing controlled updates.
    -   `_parse_birthday` ensures valid birthdays, unchanged from creation.
    -   No need to update `name` or `birthday`, as task only specifies `address` and `phone`.
-   **Performance**:
    -   Property access/set: O(1).
    -   `print_contact`: O(1) for printing.
    -   Total: O(1), highly efficient.
-   **Design**:
    -   Property decorators provide clean access and update interface.
    -   Private attributes (`_name`, etc.) prevent direct modification.
    -   Validation in `__init__` and setters enhances robustness.
    -   Type hints clarify expected types.
-   **Alternatives**:
    -   Direct attribute access: Less safe, bypasses validation.
    -   No setters: Would require new objects for updates.
    -   Custom update method: Unnecessary, as properties suffice.
-   **Extensibility**:
    -   Easily add setters for `name` or other properties.
    -   Could validate `phone` format (e.g., regex for specific patterns).
    -   Could add methods for additional functionality (e.g., age calculation).
-   **Edge Cases**:
    -   Empty updates: `mike.phone = ""` raises `ValueError`.
    -   Invalid birthday: Handled at creation, not relevant for updates.
    -   Non-string updates: Type hints guide correct usage, enforced by Python.

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
mike.address = "Russia, Moscow, Nashchokinsky Pereulok, Building 3, Apt. 44"
mike.phone = "K-058-67"
vlad.address = "Russia, Moscow, Gendrikov Pereulok, Building 15, Apt. 5"
vlad.phone = "2-35-71"
mike.print_contact()
print()
vlad.print_contact()
# Output:
# Name: Mikhail Bulgakov
# Phone: K-058-67
# Address: Russia, Moscow, Nashchokinsky Pereulok, Building 3, Apt. 44
# Birthday: 15.05.1891
#
# Name: Vladimir Mayakovsky
# Phone: 2-35-71
# Address: Russia, Moscow, Gendrikov Pereulok, Building 15, Apt. 5
# Birthday: 19.07.1893

# Additional test case
try:
    mike.phone = ""  # Invalid update
except ValueError as e:
    print(e)  # Phone cannot be empty
```

## Conclusion 🚀

The `Contact` class implementation is precise, correctly updating `mike` and `vlad` objects with new `address` and `phone` values for 1927 and printing the updated details.

The use of property decorators and setters ensures controlled updates with validation, while maintaining the original functionality.

The implementation is efficient, robust, and fully compliant with the task’s requirements, making it ideal for contact management or teaching advanced object-oriented programming concepts like properties and validation.
