from typing import List, Dict, Set, Callable
import enum


class Parity(enum.Enum):
    ODD = 0
    EVEN = 1


def gen_list(start: int, stop: int, parity: Parity) -> List[int]:
    """
    Takes a starting number, and returns either the Odds or Evens depending on what Parity is. Does not include the stop input

    :param start:
    :param stop:
    :param parity:
    :return: A list of parity Value in the range of Start to Stop
    """
    new_list = list()
    for i in range(start, stop):
        if parity == Parity.EVEN and i % 2 == 0:
            new_list.append(i)
        elif parity == Parity.ODD and i % 2 != 0:
            new_list.append(i)

    return new_list


def gen_dict(start: int, stop: int, strategy: Callable) -> Dict:
    """
    Oh no some evil developer decided not to write docstrings. Maybe you can use the test cases to decipher
    what this method was supposed to do. Hey if you do, maybe you could do some good in this world by
    updating this here docstring to something useful.


    :param start:
    :param stop:
    :param strategy:
    :return:
    """
    pass


def gen_set(val_in: str) -> Set:
    """
    Oh no some evil developer decided not to write docstrings. Maybe you can use the test cases to decipher
    what this method was supposed to do. Hey if you do, maybe you could do some good in this world by
    updating this here docstring to something useful.

    :param val_in:
    :return:
    """
    pass
