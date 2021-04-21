"""Self-Check: Using the code below,
```
word_list = ['cat', 'dog', 'rabbit']
letter_list = []
for a_word in word_list:
    for a_letter in a_word:
        letter_list.append(a_letter)
print(letter_list)
```

1. Modify the given code so that the final list only contains a single copy of each letter.
2. Redo the given code using list comprehensions. For an extra challenge, see if you can figure out how to remove the duplicates.
"""
from typing import List


def extract_letters(words: List[str]) -> List[str]:
    """Extract a single copy of the letters from the given {words}.

    Args:
        words (List[str]): List of words.

    Returns:
        List[str]: List which only contains a single copy of each letter.
    """
    letters = []
    for word in words:
        for char in word:
            if char not in letters:
                letters.append(char)
    return letters


def extract_letters_using_list_comprehension(words: List[str]) -> List[str]:
    """Extract a single copy of letters from the given {words} using comprehension.

    Args:
        words (List[str]): List of words.

    Returns:
        List[str]: List which only contains a single copy of each letter.
    """
    words_combined = "".join(words)
    return [
        words_combined[index]
        for index in range(len(words_combined))
        if words_combined.find(words_combined[index]) == index
    ]


def test_extract_letters():
    given_words = ["cat", "dog", "rabbit"]
    expected_result = ["c", "a", "t", "d", "o", "g", "r", "b", "i"]
    actual_result = extract_letters(given_words)
    assert actual_result == expected_result


def test_extract_letters_using_list_comprehension():
    given_words = ["cat", "dog", "rabbit"]
    expected_result = ["c", "a", "t", "d", "o", "g", "r", "b", "i"]
    actual_result = extract_letters_using_list_comprehension(given_words)
    assert actual_result == expected_result
