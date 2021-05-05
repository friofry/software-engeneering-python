from abc import ABC, abstractmethod


class Employee(ABC):
    @abstractmethod
    def calculate_pay(self) -> float:
        pass

    @abstractmethod
    def report_hours(self) -> float:
        pass

    def save(self):         # <-- shared implementation
        # Let's assume THIS is going to be the
        # same algorithm for each employee - it can
        # be shared here.
        pass


class HR(Employee):
    def calculate_pay(self) -> float:
        # implement own algorithm for HR
        pass

    def report_hours(self) -> float:
        # implement own algorithm for HR
        pass


class Accounting(Employee):
    def calculate_pay(self) -> float:
        # implement own algorithm for Accounting
        pass

    def report_hours(self) -> float:
        # ...
        pass


class IT(Employee):
    def calculate_pay(self) -> float:
        # ...
        pass

    def report_hours(self) -> float:
        # ...
        pass
