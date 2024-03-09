class Programmer:
    def __init__(self, name: str, title: str):
        self.name = name
        self.title = title
        self.work_time = 0
        self.skolko_denyag_zarabotal = 0

        match title:
            case "Junior":
                self.salary = 10
            case "Middle":
                self.salary = 15
            case "Senior":
                self.salary = 20

    def work(self, time):
        self.work_time += time
        self.skolko_denyag_zarabotal += self.salary * time

    def rise(self):
        match self.title:
            case "Junior":
                self.title = "Middle"
                self.salary += 5
            case "Middle":
                self.title = "Senior"
                self.salary += 5
            case "Senior":
                self.salary += 1

    def info(self) -> str:
        return f"{self.name} {self.work_time}ч. {self.skolko_denyag_zarabotal}тгр."
