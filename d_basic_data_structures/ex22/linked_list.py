from __future__ import annotations

from typing import Any, Optional, Tuple

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
        raise ValueError(f"The item, `{item}`, doesn't exist in LinkedList")

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
        currentNode, previousNode = self._get_node_and_previous_node(position)
        self._insert_item_between_current_and_previous(
            item, currentNode=currentNode, previousNode=previousNode
        )

    def _get_node_and_previous_node(
        self, position: int
    ) -> Tuple[Optional[Node], Optional[Node]]:
        """Return the node on {position} and the node before it.

        Returns:
            Tuple[Optional[Node], Optional[Node]]: The first `Optional[Node]` is the
                the node on {position}. It does not exist if it's an empty linked list
                or it's the {position} after the tail of the linked list.
                    The second `Optional[Node]` is the node before the node on
                {position}. It does not exist if the node on {position} is the
                head of the linked list.
        """
        if position < 0:
            raise ValueError(
                f"Invalid position {position}. "
                "Position should be 0 to list's size minus 1."
            )

        previousNode, currentPosition, currentNode = None, 0, self.head
        while currentPosition != position:
            if currentNode is None:
                raise ValueError(
                    f"Position {position} is out of range. "
                    f"Size of linked list is {self.size}."
                )
            currentPosition += 1
            previousNode, currentNode = currentNode, currentNode.next
        return currentNode, previousNode

    def _insert_item_between_current_and_previous(
        self,
        item: Any,
        *,
        currentNode: Optional[Node],
        previousNode: Optional[Node],
    ):
        newNode = Node(item)
        if previousNode:
            previousNode.next = newNode
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

    def pop(self, position: int) -> Any:
        """Remove the item in {position}, and returns it.

        As said in the book, "We will assume that position names are integers starting
        with 0."

        Raises:
            Exception: When {position} is out of range.
        """
        if self.head is None:
            raise ValueError(
                f"Position {position} is out of range. "
                f"Size of linked list is {self.size}."
            )

        # Let's set a constant so we can use 'is' comparison. Using '==' is not
        # sufficient since `False == 0` would return True, when we would want it to
        # be False. Although...there's only a tiny likelihood (super close to 0%) that
        # someone would use this class (found in a repo for book exercise)
        # would decide to pass `False` as `position`. 🤔
        # It might be a good idea anyway to implement it this way to reinforce the idea
        # in my own head that `False == 0` returns `True`. 😅
        # TODO do this for other `== position` conditions
        ZERO = 0
        item = None
        if position is ZERO:
            item = self.head.data
            self.head = self.head.next
            return item

        currentNode, prevNode = self._get_node_and_previous_node(position)
        if currentNode is None:
            raise ValueError(
                f"Position {position} is out of range. "
                f"Size of linked list is {self.size}."
            )
        prevNode.next = currentNode.next
        return currentNode.data
