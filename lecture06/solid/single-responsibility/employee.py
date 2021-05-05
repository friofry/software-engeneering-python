# SRP violation: hr, accounting and it buisness logic are managed by different departments/teams
class Employee:
    def calculate_pay(self) -> float:
        if self.role == "hr":
            # implement algorithm for hr
            pass
        if self.role == "accounting":
            # accounting
            pass
        if self.role == "it":
            # it
            pass
        # ...

    def report_hours(self) -> float:
        if self.role == "hr":
            pass
        if self.role == "accounting":
            pass
        if self.role == "it":
            pass
        # ...

    def save(self):
        if self.role == "hr":
            pass
        if self.role == "accounting":
            pass
        if self.role == "it":
            pass
        # ...
