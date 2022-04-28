import pytest
from src.Functions import earley
from src.Classes import Rule


def create_grammar(rules):
    grammar = []
    for i in range(len(rules)):
        if (len(rules)) == 0:
            break
        if rules[1] == "1":
            rules[1] = ""
        grammar.append(Rule(rules[0], rules[1]))
        del rules[0]
        del rules[0]
    return grammar


def test_earley():
    rules = ["S", "a", "S", "aS"]
    grammar = create_grammar(rules)
    word = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    assert earley(word, grammar) is True

    rules = ["S", "aSb", "S", "c", "S", "1"]
    grammar = create_grammar(rules)
    word = "aaaacbbbb"
    assert earley(word, grammar) is True
    word = "aaabbb"
    assert earley(word, grammar) is True
    word = "aaabbbb"
    assert earley(word, grammar) is False
    word = ""  # пустое слово
    assert earley(word, grammar) is True

    rules = ["S", "aB", "A", "Ba", "A", "a", "B", "ABC", "B", "b", "C", "BA", "C", "c"]
    grammar = create_grammar(rules)
    word = "ababba"
    assert earley(word, grammar) is True

    rules = ["S", "aSbS", "S", "1"]
    grammar = create_grammar(rules)
    word = "aababb"
    assert earley(word, grammar) is True

    rules = ["S", "aSbS", "S", "1"]
    grammar = create_grammar(rules)
    word = "aabbba"
    assert earley(word, grammar) is False



