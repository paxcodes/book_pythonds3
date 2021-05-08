from __future__ import annotations

from typing import Any, Optional

from pytest import fixture

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


class Test_Linked_List:
    def test_fresh_linked_list_should_be_empty(self):
        givenLinkedList = LinkedList()
        assert givenLinkedList.is_empty

    def test_adding_item_to_fresh_linked_list_should_make_linked_list_not_empty(self):
        givenLinkedList = LinkedList()
        givenLinkedList.add(1)
        assert not givenLinkedList.is_empty

    def test_position_of_first_item_in_linked_list_should_be_zero(self):
        givenLinkedList = LinkedList()
        givenLinkedList.add(1)
        assert givenLinkedList.index(1) == 0

    def test_position_of_last_item_added_in_linked_list_should_be_zero(self):
        givenLinkedList = LinkedList()
        givenLinkedList.add(1)
        givenLinkedList.add("Num")
        assert givenLinkedList.index("Num") == 0

    def test_position_of_first_item_added_in_linked_list_should_be_size_minus_one(self):
        givenLinkedList = LinkedList()
        givenFirstItemAdded = "Data"
        givenLinkedList.add(givenFirstItemAdded)
        givenLinkedList.add("Num")
        givenLinkedList.add("Py")
        assert givenLinkedList.index(givenFirstItemAdded) == givenLinkedList.size - 1

    @fixture(scope="class")
    def givenLinkedList(self):
        ll = LinkedList()
        ll.add(1)
        ll.add("Num")
        ll.add("Py")
        return ll

    def test_size_prop_should_return_size_of_linked_list(
        self, givenLinkedList: LinkedList
    ):
        """`size` property should return the number of items in the Linked List."""
        assert givenLinkedList.size == 3

    def test_index_method_should_return_position_of_items_in_linked_list(
        self, givenLinkedList: LinkedList
    ):
        assert givenLinkedList.index(1) == 2
        assert givenLinkedList.index("Num") == 1
        assert givenLinkedList.index("Py") == 0

    def test_search_method_should_return_True_for_items_in_the_linked_list(
        self, givenLinkedList: LinkedList
    ):
        givenItemsInLinkedList = [1, "Num", "Py"]
        for itemInLinkedList in givenItemsInLinkedList:
            assert givenLinkedList.search(itemInLinkedList)

    def test_search_method_should_return_False_for_items_not_in_the_linked_list(
        self, givenLinkedList: LinkedList
    ):
        givenItemsNotInLinkedList = ["One", 2, "Pandas"]
        for itemNotInLinkedList in givenItemsNotInLinkedList:
            assert givenLinkedList.search(itemNotInLinkedList) == False
