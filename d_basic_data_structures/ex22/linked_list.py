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
    def next(self, new_next: Optional[Node]):
        self._next = new_next


class LinkedList:
    head: Optional[Node]

    def __init__(self):
        self.head = None

    @property
    def is_empty(self):
        return self.head is None

    def add(self, item: Any):
        """Adds the item at the beginning of the list (i.e. as the new head).

        As mentioned in the book,
        > ...place the new item in the easiest location possible. ... the easiest place
        > to add the new node is right at the head, or beginning, of the list.
        """
        newNode = Node(item)
        newNode.next = self.head
        self.head = newNode

    @property
    def size(self):
        numOfItems = 0
        currentNode = self.head
        while currentNode is not None:
            numOfItems += 1
            currentNode = currentNode.next
        return numOfItems

    def search(self, item: Any) -> bool:
        """Searches for the item in the list.

        Returns:
            bool: `True` if the item is found. Otherwise, `False`.
        """
        currentNode = self.head
        while currentNode:
            if currentNode.data == item:
                return True
            currentNode = currentNode.next
        return False

    def remove(self, item: Any):
        prevNode, currentNode = None, self.head
        while currentNode:
            if currentNode.data == item:
                if prevNode:
                    prevNode.next = currentNode.next
                else:
                    self.head = currentNode.next
                return
            prevNode, currentNode = currentNode, currentNode.next
        raise Exception(f"{item} doesn't exist in LinkedList")

    def append(self, item: Any):
        """Adds the item at the end of the list (i.e. at the tail)."""
        if self.head is None:
            self.head = Node(item)
            return

        currentNode = self.head
        while currentNode.next:
            currentNode = currentNode.next
        currentNode.next = Node(item)

    def insert(self, item: Any, position: int):
        """python
        Inserts the {item} in {position}.

        Args:
            item (Any): The data to be inserted.
            position (int): The position where the {item} is to be inserted. As said in
                the book, "We will assume that position names are integers starting
                with 0."
        """
        prevNode, currentPosition, currentNode = None, 0, self.head
        # TODO refactor: get node in {position}
        while currentPosition != position:
            currentPosition += 1
            prevNode, currentNode = currentNode, currentNode.next

        # TODO refactor: adjust nodes / insert newNode
        newNode = Node(item)
        if prevNode:
            prevNode.next = newNode
        else:
            self.head = newNode

        if currentNode:
            newNode.next = currentNode

    def index(self, item: Any) -> Optional[int]:
        """Returns the position of the {item} in the list.

        Returns:
            Optional[int]: The position of the item. As said in the book, "We will assume that
                position names are integers starting with 0." If the position is not
                found, returns `None`
        """
        position = 0
        currentNode = self.head
        while currentNode:
            if currentNode.data == item:
                return position
            else:
                currentNode = currentNode.next
            position += 1
        return None

    def pop(self, position: int):
        """Remove the item in {position}.

        As said in the book, "We will assume that position names are integers starting
        with 0."
        """
        # TODO
