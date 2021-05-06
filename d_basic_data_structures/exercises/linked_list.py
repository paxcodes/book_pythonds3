from __future__ import annotations

from typing import Any, Optional

"""
Linked Lists are discussed in
https://runestone.academy/runestone/books/published/pythonds3/BasicDS/ImplementinganUnorderedListLinkedLists.html
"""


class Node:
    _next: Optional[Node]
    _data: Any

    def __init__(self, data: Any) -> None:
        self._next = None
        self._data = data

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new_data: Any) -> None:
        self._data = new_data

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, new_next: Node):
        self._next = new_next


class LinkedList:
    head: Optional[Node]

    def __init__(self):
        self.head = None

    @property
    def is_empty(self):
        pass  # TODO

    def add(self, item: Any):
        """Adds the item at the beginning of the list (i.e. as the new head).

        As mentioned in the book,
        > ...place the new item in the easiest location possible. ... the easiest place
        > to add the new node is right at the head, or beginning, of the list.
        """
        pass  # TODO

    @property
    def size(self):
        pass  # TODO

    def search(self, item: Any):
        pass  # TODO

    def remove(self, item: Any):
        pass  # TODO

    def append(self, item: Any):
        pass  # TODO

    def insert(self, item: Any, position: int):
        """
        Inserts the {item} in {position}.

        Args:
            item (Any): The data to be inserted.
            position (int): The position where the {item} is to be inserted. As said in
                the book, "We will assume that position names are integers starting
                with 0."
        """
        # TODO

    def index(self, item: Any) -> int:
        """Returns the position of the {item} in the list.

        As said in the book, "We will assume that position names are integers starting
        with 0."
        """
        # TODO

    def pop(self, position: int):
        """Remove the item in {position}.

        As said in the book, "We will assume that position names are integers starting
        with 0."
        """
        # TODO


class Test_Linked_List:
    pass
