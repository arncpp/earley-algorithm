from .Classes import Rule
from .Functions import check_input, earley


def input_processing():
    grammar = []
    rules = []
    print("Введите количество правил: ")
    rule_numbers = int(input())
    print("\nВведите сами правила:")
    for i in range(rule_numbers):
        rules = input().split()
        if (len(rules) == 1):
            rules.append("")
        elif (rules[1] == "1"):
            rules[1] = ""
        grammar.append(Rule(rules[0], rules[1]))
    check_input(grammar)
    return grammar


def input_processing_for_tests():
    grammar = []
    rules = []
    rule_numbers = int(input())
    for i in range(rule_numbers):
        rules = input().split()
        if (len(rules) == 1):
            rules.append("")
        elif (rules[1] == "1"):
            rules[1] = ""
        grammar.append(Rule(rules[0], rules[1]))
    check_input(grammar)
    return grammar


def output_processing(word, grammar):
    if earley(word, grammar):
        print("YES")
    else:
        print("NO")
