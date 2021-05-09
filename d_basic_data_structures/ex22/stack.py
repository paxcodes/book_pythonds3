from typing import Any, List

from .linked_list import LinkedList


class Stack(LinkedList):
    """The stack abstract data type implemented using linked lists.

    > A stack is An ordered collection of items where items are added to and removed
    > from the end called the “top.” Stacks are ordered LIFO.

    `size` and `is_empty` properties are already provided by the linked list.
    """

    def push(self, item: Any) -> None:
        """Adds a new item to the top of the stack."""
        super().add(item)

    def pop(self) -> Any:
        """Removes the top item from the stack."""
        return super().pop(0)

    def peek(self) -> Any:
        """Returns the top item from the stack but does not remove it."""
        if self.head:
            return self.head.data
        raise Exception("Stack is empty!")

    @property
    def contents(self) -> List[Any]:
        """
        Not part of a stack's definition. Get contents without modifying the stack.

        Created as a helper function for testing stack operations as how they are
        listed in the book under,
        "4.4. The Stack Abstract Data Type" > "Table 1: Sample Stack Operations":
        https://runestone.academy/runestone/books/published/pythonds3/BasicDS/TheStackAbstractDataType.html

        Returns:
            List[Any]: Where the "top" of the stack is at the end of the list.
        """
        currentNode = self.head
        stackContents = []
        while currentNode:
            stackContents.append(currentNode.data)
            currentNode = currentNode.next

        # Reverse the list so the "top" of the stack / "head" of the list
        # is at the end of the list.
        return stackContents[::-1]
