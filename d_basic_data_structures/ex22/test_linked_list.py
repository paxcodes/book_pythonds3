from pytest import fixture, raises

from .linked_list import LinkedList


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

    class Test_3_Item_Linked_List:
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

    class Test_Removing_Item:
        ITEM_TO_BE_REMOVED = "Num"

        @fixture(scope="class")
        def givenLinkedList(self):
            givenLinkedList = LinkedList()
            givenLinkedList.add(1)
            givenLinkedList.add(self.ITEM_TO_BE_REMOVED)
            givenLinkedList.add("Py")
            assert givenLinkedList.size == 3
            givenLinkedList.remove(self.ITEM_TO_BE_REMOVED)
            return givenLinkedList

        def test_removing_an_item_should_decrease_size_of_linked_list(
            self, givenLinkedList: LinkedList
        ):
            assert givenLinkedList.size == 2

        def test_removing_an_item_should_adjust_indices_of_items_in_linked_list(
            self, givenLinkedList: LinkedList
        ):
            assert givenLinkedList.index(1) == 1
            assert givenLinkedList.index("Py") == 0

        def test_item_removed_should_not_be_in_the_linked_list_anymore(
            self, givenLinkedList: LinkedList
        ):
            givenRemovedItem = self.ITEM_TO_BE_REMOVED
            assert givenLinkedList.search(givenRemovedItem) == False

        def test_removing_a_non_existent_item_should_raise_an_error(self):
            givenLinkedList = LinkedList()
            givenLinkedList.add(1)
            with raises(Exception):
                givenLinkedList.remove("doesn't exist")

    class Test_Appending_an_Item:
        def test_item_should_be_at_the_tail_of_the_linked_list(self):
            givenLinkedList = LinkedList()
            givenLinkedList.append(1)
            givenLinkedList.append("Num")
            assert givenLinkedList.index(1) == 0
            assert givenLinkedList.index("Num") == 1

        def test_item_should_be_added_the_head_of_an_empty_linked_list(self):
            givenItem = 1
            givenLinkedList = LinkedList()
            givenLinkedList.append(givenItem)
            givenLinkedList.head.data == givenItem
