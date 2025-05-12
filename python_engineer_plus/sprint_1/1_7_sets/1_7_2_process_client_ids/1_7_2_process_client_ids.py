'''
TODO:
    Anton received a list of client ids in response from the server as
    a string, where the ids are separated by spaces.

    His task is to remove duplicates and sort the list of ids in ascending
    order.

    Write a program that will help Anton form such lists.

    If a duplicate id is found in the list, the program should output
    the message:
        "Duplicate id <id_value> found"
'''
from typing import List


def process_client_ids(ids: str) -> List[int]:
    """
    Process client IDs, remove duplicates, and sort.

    Args:
        ids: String of space-separated client IDs.

    Returns:
        Sorted list of unique IDs.
    """
    id_list = [int(id) for id in ids.split()]
    seen = set()
    for id_val in id_list:
        if id_val in seen:
            print(f"Duplicate id {id_val} found")
        else:
            seen.add(id_val)
    return sorted(seen)


ids = "1 2 2 3"
result = process_client_ids(ids)
print(result)
