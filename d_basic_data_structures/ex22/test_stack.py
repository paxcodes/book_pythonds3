from .stack import Stack


class Test_Stack:
    def test_stack_operations(self):
        givenStack = Stack()
        assert givenStack.is_empty

        givenStack.push(4)
        assert givenStack.contents == [4]

        givenStack.push("dog")
        assert givenStack.contents == [4, "dog"]

        actualTopItem = givenStack.peek()
        assert actualTopItem == "dog"
        assert givenStack.contents == [4, "dog"]

        givenStack.push(True)
        assert givenStack.contents == [4, "dog", True]
        assert givenStack.size == 3
        assert givenStack.is_empty is False

        givenStack.push(8.4)
        assert givenStack.contents == [4, "dog", True, 8.4]

        actualTopItem = givenStack.pop()
        assert actualTopItem == 8.4
        assert givenStack.contents == [4, "dog", True]

        actualTopItem = givenStack.pop()
        assert actualTopItem is True
        assert givenStack.contents == [4, "dog"]
        assert givenStack.size == 2
