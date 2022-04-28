from typing import List, Set
from .Classes import Situation, Rule


def scan(multiple_situations: List[Set[Situation]], position: int, word: str):
    if position < 0:
        return
    for situation in multiple_situations[position]:
        try:
            if situation.rule.next_state[situation.dot_position] == word[position]:
                multiple_situations[position + 1].add(Situation(situation.rule, situation.dot_position + 1, situation.j_index))
        except Exception:
            pass


def complete(multiple_situations: List[Set[Situation]], position: int, situations: Set[Situation],
             new_situations: Set[Situation]):
    for situation in situations:
        for mult_situation in multiple_situations[situation.j_index]:
            try:
                if situation.rule.start_state == mult_situation.rule.next_state[mult_situation.dot_position]:
                    now_situation = Situation(mult_situation.rule, mult_situation.dot_position + 1, mult_situation.j_index)
                    if now_situation not in multiple_situations[position]:
                        new_situations.add(now_situation)
            except Exception:
                pass


def predict(multiple_situations: List[Set[Situation]], position: int, grammar: List[Rule], situations: Set[Situation],
            new_situations: Set[Situation]):
    for situation in situations:
        for rule in grammar:
            try:
                if rule.start_state == situation.rule.next_state[situation.dot_position]:
                    current_situation = Situation(rule, 0, position)
                    if current_situation not in multiple_situations[position]:
                        new_situations.add(current_situation)
            except Exception:
                pass


def check_input(grammar: List[Rule]):
    for i in range(len(grammar)):
        assert grammar[i].next_state != "S'" and grammar[i].start_state != "S'"


def earley(word: str, grammar: List[Rule]):
    word_len = len(word)
    multiple_situations = [set() for _ in range(word_len + 1)]
    multiple_situations[0].add(Situation(Rule("S'", "S"), 0, 0))  # начальное состояние
    for i in range(word_len + 1):
        new_situations: Set[Situation] = set()
        old_situations: Set[Situation] = set()
        scan(multiple_situations, i - 1, word)
        complete(multiple_situations, i, multiple_situations[i], new_situations)
        predict(multiple_situations, i, grammar, multiple_situations[i], new_situations)
        while True:
            if len(new_situations) <= 0:
                break
            for situation in new_situations:
                old_situations.add(situation)
                multiple_situations[i].add(situation)
            new_situations = set()
            complete(multiple_situations, i, old_situations, new_situations)
            predict(multiple_situations, i, grammar, old_situations, new_situations)
            old_situations = new_situations
        for situation in old_situations:
            multiple_situations[i].add(situation)
    if Situation(Rule("S'", "S"), 1, 0) in multiple_situations[word_len]:
        return True
    else:
        return False
