from .base import Predicate
from .explanation import Explanation


class is_lt(Predicate):
    """
    Generates a predicate that checks if the data is lower than the given
    value. The optional keyword argument ``rep`` specifies what the value
    should be called in the explanation. If no value for ``rep`` is given it
    will just use ``repr(value)``.
    """

    def __init__(self, value, rep=None):
        if rep is None:
            rep = repr(value)
        self._value = value
        self._valid_exp = Explanation(
            True, 'lower_than', 'data is lower than {}'.format(rep)
        )
        self._not_valid_exp = Explanation(
            False, 'not_lower_than', 'data is not lower than {}'.format(rep)
        )

    def _evaluate(self, data, explain, context):
        return (
            (self._valid_exp if explain else True)
            if data < context(self._value) else
            (self._not_valid_exp if explain else False)
        )
