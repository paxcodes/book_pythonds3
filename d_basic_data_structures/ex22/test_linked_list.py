from typing import Any, Tuple

from pytest import fixture, raises

from .linked_list import ZERO, LinkedList


def _generate_linked_list(size: int) -> LinkedList:
    """
    Helper function that generates a linked list of a certain {size}.

    Each item's data is {position} * 200.
    """
    ll = LinkedList()
    for i in range(size):
        ll.add((size - i - 1) * 200)
    return ll


class Test_Linked_List:
    def test_fresh_linked_list_should_be_empty(self):
        givenLinkedList = LinkedList()
        assert givenLinkedList.is_empty

    def test_position_of_first_item_in_linked_list_should_be_zero(self):
        givenLinkedList = LinkedList()
        givenLinkedList.add(1)
        assert givenLinkedList.index(1) is ZERO

    class Test_Adding_Items:
        def test_adding_item_to_fresh_linked_list_should_make_linked_list_not_empty(
            self,
        ):
            givenLinkedList = LinkedList()
            givenLinkedList.add(1)
            assert not givenLinkedList.is_empty

        def test_position_of_last_item_added_in_linked_list_should_be_zero(self):
            givenLinkedList = LinkedList()
            givenLinkedList.add(1)
            givenLinkedList.add("Num")
            assert givenLinkedList.index("Num") is ZERO

        def test_position_of_first_item_added_in_linked_list_should_be_size_minus_one(
            self,
        ):
            givenLinkedList = LinkedList()
            givenFirstItemAdded = "Data"
            givenLinkedList.add(givenFirstItemAdded)
            givenLinkedList.add("Num")
            givenLinkedList.add("Py")
            assert (
                givenLinkedList.index(givenFirstItemAdded) == givenLinkedList.size - 1
            )

    class Test_3_Item_Linked_List:
        @fixture(scope="class")
        def givenLinkedList(self):
            return _generate_linked_list(3)

        def test_size_prop_should_return_size_of_linked_list(
            self, givenLinkedList: LinkedList
        ):
            """`size` property should return the number of items in the Linked List."""
            assert givenLinkedList.size == 3

        def test_index_method_should_return_position_of_items_in_linked_list(
            self, givenLinkedList: LinkedList
        ):
            assert givenLinkedList.index(400) == 2
            assert givenLinkedList.index(200) == 1
            assert givenLinkedList.index(0) is ZERO

        def test_search_method_should_return_True_for_items_in_the_linked_list(
            self, givenLinkedList: LinkedList
        ):
            givenItemsInLinkedList = [0, 200, 400]
            for itemInLinkedList in givenItemsInLinkedList:
                assert givenLinkedList.search(itemInLinkedList)

        def test_search_method_should_return_False_for_items_not_in_the_linked_list(
            self, givenLinkedList: LinkedList
        ):
            givenItemsNotInLinkedList = ["One", 8, "Pandas"]
            for itemNotInLinkedList in givenItemsNotInLinkedList:
                assert givenLinkedList.search(itemNotInLinkedList) is False

    class Test_Removing_Item:
        ITEM_TO_BE_REMOVED = 200

        @fixture(scope="class")
        def givenLinkedList(self):
            givenSize = 3
            givenLinkedList = _generate_linked_list(givenSize)
            assert givenLinkedList.size == givenSize
            givenLinkedList.remove(self.ITEM_TO_BE_REMOVED)
            return givenLinkedList

        def test_removing_an_item_should_decrease_size_of_linked_list(
            self, givenLinkedList: LinkedList
        ):
            assert givenLinkedList.size == 2

        def test_removing_an_item_should_adjust_indices_of_items_in_linked_list(
            self, givenLinkedList: LinkedList
        ):
            assert givenLinkedList.index(400) == 1
            assert givenLinkedList.index(0) is ZERO

        def test_item_removed_should_not_be_in_the_linked_list_anymore(
            self, givenLinkedList: LinkedList
        ):
            givenRemovedItem = self.ITEM_TO_BE_REMOVED
            assert givenLinkedList.search(givenRemovedItem) == False

        def test_removing_a_non_existent_item_should_raise_an_error(self):
            givenLinkedList = LinkedList()
            givenLinkedList.add(1)
            with raises(ValueError, match="The item, `Num`, doesn't exist."):
                givenLinkedList.remove("Num")

    class Test_Appending_an_Item:
        def test_item_should_be_at_the_tail_of_the_linked_list(self):
            givenLinkedList = LinkedList()
            givenLinkedList.append(1)
            givenLinkedList.append("Num")
            assert givenLinkedList.index(1) is ZERO
            assert givenLinkedList.index("Num") == 1

        def test_item_should_be_added_the_head_of_an_empty_linked_list(self):
            givenItem = 1
            givenLinkedList = LinkedList()
            givenLinkedList.append(givenItem)
            givenLinkedList.head.data == givenItem

    class Test_Inserting_an_Item:
        @fixture(scope="class")
        def givenLinkedList(self):
            ll = _generate_linked_list(3)
            assert ll.size == 3
            ll.insert("Pandas", 1)
            return ll

        def test_size_should_increase(self, givenLinkedList: LinkedList):
            assert givenLinkedList.size == 4

        def test_item_should_be_at_position_specified(
            self, givenLinkedList: LinkedList
        ):
            assert givenLinkedList.index("Pandas") == 1

        def test_index_of_previous_items_should_be_the_same(
            self, givenLinkedList: LinkedList
        ):
            assert givenLinkedList.index(0) is ZERO

        def test_index_of_following_items_should_be_adjusted(
            self, givenLinkedList: LinkedList
        ):
            assert givenLinkedList.index(200) == 2
            assert givenLinkedList.index(400) == 3

        def test_inserting_at_position_0_should_change_head(self):
            givenLinkedList = LinkedList()
            givenLinkedList.add("Pyjamas")
            givenLinkedList.insert("Sleepers", 0)
            assert givenLinkedList.head.data == "Sleepers"
            assert givenLinkedList.index("Pyjamas") == 1
            assert givenLinkedList.index("Sleepers") is ZERO

        def test_inserting_at_a_position_that_is_out_of_range_raises_an_error(self):
            givenLinkedList = LinkedList()
            givenSize = givenLinkedList.size
            givenOutOfRangePositions = [1, 9]
            for outOfRangePosition in givenOutOfRangePositions:
                expectedErrorMsg = (
                    f"Position {outOfRangePosition} is out of range. "
                    f"Size of linked list is {givenSize}."
                )
                with raises(ValueError, match=expectedErrorMsg):
                    givenLinkedList.insert("Banana", outOfRangePosition)

    class Test_Popping_an_Item:
        # TODO Refactor by passing HEAD, MID, and TAIL positions as test parameters

        @fixture(scope="class")
        def poppedItemAndList(self) -> Tuple[Any, LinkedList]:
            MID_POSITION = 2
            ll = _generate_linked_list(4)
            actualTailItem = ll.pop(MID_POSITION)
            return actualTailItem, ll

        def test_item_popped_should_not_be_in_linked_list_anymore(
            self, poppedItemAndList: Tuple[Any, LinkedList]
        ):
            actualPoppedItem, givenLinkedList = poppedItemAndList
            assert actualPoppedItem == 400
            assert givenLinkedList.search(actualPoppedItem) is False

        def test_linked_list_should_decrease_in_size(
            self, poppedItemAndList: Tuple[Any, LinkedList]
        ):
            _, givenLinkedList = poppedItemAndList
            assert givenLinkedList.size == 3

        class Test_When_popping_the_tail:
            @fixture(scope="class")
            def poppedItemAndList(self) -> Tuple[Any, LinkedList]:
                TAIL_POSITION = 3
                ll = _generate_linked_list(4)
                actualTailItem = ll.pop(TAIL_POSITION)
                return actualTailItem, ll

            def test_item_popped_should_not_be_in_linked_list_anymore(
                self, poppedItemAndList: Tuple[Any, LinkedList]
            ):
                actualPoppedItem, givenLinkedList = poppedItemAndList
                assert actualPoppedItem == 600
                assert givenLinkedList.search(actualPoppedItem) is False

            def test_linked_list_should_decrease_in_size(
                self, poppedItemAndList: Tuple[Any, LinkedList]
            ):
                _, givenLinkedList = poppedItemAndList
                assert givenLinkedList.size == 3

        class Test_When_position_is_out_of_bounds:
            def test_it_should_raise_an_error(
                self,
            ):
                ## Test: Attempt popping on an empty list
                givenLinkedList = LinkedList()
                givenOutOfRangePositions = [0, 3]
                for outOfRangePosition in givenOutOfRangePositions:
                    expectedErrorMsg = (
                        f"Position {outOfRangePosition} is out of range. "
                        "Size of linked list is 0."
                    )
                    with raises(ValueError, match=expectedErrorMsg):
                        givenLinkedList.pop(outOfRangePosition)

                givenSize = 3
                givenLinkedList = _generate_linked_list(givenSize)
                givenOutOfRangePositions = [3, 5, 10]
                for outOfRangePosition in givenOutOfRangePositions:
                    expectedErrorMsg = (
                        f"Position {outOfRangePosition} is out of range. "
                        f"Size of linked list is {givenSize}."
                    )
                    with raises(ValueError, match=expectedErrorMsg):
                        givenLinkedList.pop(outOfRangePosition)

                givenOutOfRangePositions = [-1, -3]
                for outOfRangePosition in givenOutOfRangePositions:
                    expectedErrorMsg = (
                        f"Invalid position {outOfRangePosition}. "
                        "Position should be 0 to list's size minus 1."
                    )
                    with raises(ValueError, match=expectedErrorMsg):
                        givenLinkedList.pop(outOfRangePosition)

        class Test_When_popping_the_head:
            @fixture(scope="class")
            def givenLinkedList(self) -> LinkedList:
                ll = _generate_linked_list(2)
                assert ll.head.data == 0
                ll.pop(0)
                return ll

            def test_linked_list_should_decrease_in_size(
                self, givenLinkedList: LinkedList
            ):
                assert givenLinkedList.size == 1

            def test_popping_an_item_at_position_0_should_change_head(
                self, givenLinkedList: LinkedList
            ):
                assert givenLinkedList.head.data == 200

            def test_item_popped_should_not_be_in_linked_list_anymore(
                self, givenLinkedList: LinkedList
            ):
                assert givenLinkedList.search(0) is False
