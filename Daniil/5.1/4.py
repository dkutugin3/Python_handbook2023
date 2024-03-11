class Programmer:
    def __init__(self, name: str, grade: str) -> None:
        self.name = name
        self.grade = grade
        self.work_timer = 0
        self.salary = 0
        self.rises = 0

    def work(self, time: int):
        self.work_timer += time
        if self.grade == "Junior":
            self.salary += time * 10
        elif self.grade == "Middle":
            self.salary += time * 15
        else:
            self.salary += time * (20 + self.rises)

    def rise(self):
        if self.grade == "Junior":
            self.grade = "Middle"
            self.rises = 0
        elif self.grade == "Middle":
            self.grade = "Senior"
            self.rises = 0
        else:
            self.rises += 1

    def info(self):
        return f"{self.name} {self.work_timer}ч. {self.salary}тгр."
