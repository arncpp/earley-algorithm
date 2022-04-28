class Rule:
    """
    Правило КС-грамматики
    """

    def __init__(self, start_state: str, next_state: str):
        self.start_state = start_state
        self.next_state = next_state

    def __eq__(self, other):
        return self.start_state == other.start_state and self.next_state == other.next_state

    def __ne__(self, other):
        return self.start_state != other.start_state and self.next_state != other.next_state

    def __gt__(self, other):
        return self.start_state > other.start_state and self.next_state > other.next_state


class Situation:
    """
    Ситуации
    """

    def __init__(self, rule: Rule, dot_position: int, j_index: int):
        self.rule = rule
        self.dot_position = dot_position
        self.j_index = j_index

    def __eq__(self, other):
        return self.rule == other.rule and self.dot_position == other.dot_position and self.j_index == other.j_index

    def __ne__(self, other):
        return self.rule != other.rule and self.dot_position != other.dot_position and self.j_index != other.j_index

    def __gt__(self, other):
        return self.rule > other.rule and self.dot_position > other.dot_position and self.j_index > other.j_index

    def __hash__(self):
        return hash(
            (str(hash(self.rule.start_state)) + str(hash(self.rule.next_state)) + str(hash(self.dot_position)) + str(hash(
                self.j_index))))
