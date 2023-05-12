import os
import re
import sys
from abc import ABC, abstractmethod
from time import perf_counter

def Timer(function: callable) -> callable:
    """
    Timer decorator
    :param function: callable
    :return: callable
    """
    def wrapper(*args, **kwargs) -> callable:
        """
        Wrapper function
        :param args: list
        :param kwargs: dict
        :return: callable
        """
        start = perf_counter()
        result = function(*args, **kwargs)
        end = perf_counter()
        print("Time elapsed: {} seconds.".format(end - start))
        return result
    return wrapper


class Content(ABC):
    """Abstract class for Content topics"""

    @abstractmethod
    def topics(self) -> list[str]:
        pass


class DesignPatterns(Content):
    """
    Design Patterns content strategy
    Implements Content abstract class
    """

    def topics(self) -> list[str]:
        """
        Design Patterns topics
        :return list[str]
        """
        return [
            "observer",
            "strategy",
            "decorator",
            "singleton",
            "builder",
            "factory"
        ]


class DataStructures(Content):
    """
    Data Structures content strategy
    Implements Content abstract class
    """

    def topics(self) -> list[str]:
        """
        Data Structures topics
        :return list[str]
        """
        return [
            "linked-list",
            "stack",
            "queue"
        ]


class Algorithms(Content):
    """
    Algorithms content strategy
    Implements Content abstract class
    """

    def topics(self) -> list[str]:
        """
        Algorithms topics
        :return list[str]
        """
        return [
            "bubble-sort",
            "merge-sort",
            "quick-sort",
            "insertion-sort",
            "selection-sort"
        ]


class ContentFactory:
    """Content factory for the desired strategy."""

    def __init__(self, date: str, topic: str) -> None:
        """"""
        if not date and not topic:
            raise ValueError("Date and topic cannot be empty")
        if re.match("^design", topic, re.IGNORECASE):
            self.content = DesignPatterns().topics()
        elif re.match("^data", topic, re.IGNORECASE):
            self.content = DataStructures().topics()
        elif re.match("^algo", topic, re.IGNORECASE):
            self.content = Algorithms().topics()
        else:
            raise ValueError("{} is not a valid topic".format(topic))
        self.topic = topic
        self._date = date

    @property
    def date(self) -> str:
        """
        Date property
        :return: str
        """
        return self._date

    @staticmethod
    def default_content(pattern: str) -> str:
        """
        Produces 3 exercises with default content for each pattern
        :param pattern: str
        :return: str
        """
        if not pattern:
            raise ValueError("Pattern cannot be empty")
        return f"""
# {pattern} exercises
from abc import ABC, abstractmethod

if __name__ == "__main__":
    print("Exercise 1\\n———————————")
    print()

    print("Exercise 2\\n———————————")
    print()

    print("Exercise 3\\n———————————")
    print()
        """

    @Timer
    def run(self) -> None:
        """
        Runs Content factory
        :return: None
        """
        print("Making directory for {}.".format(self.date))
        os.makedirs(f"{self.date}/{self.topic}", exist_ok=True)
        print("Changing directory to {}.".format(self.date))
        os.chdir(f"{self.date}/{self.topic}")
        for topic in self.content:
            print("Producing {} content.".format(topic))
            with open(f"{topic}.py", "w") as file:
                file.write(self.default_content(topic))
        os.chdir("../..")
        print("Done.")


if __name__ == '__main__':

    factory = ContentFactory(sys.argv[1], sys.argv[2])
    factory.run()
