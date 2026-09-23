class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        # додаємо у словник класу
        Person.people[self.name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    result = []

    # 1. створюємо всіх людей
    for person in people:
        new_person = Person(person["name"], person["age"])
        result.append(new_person)

    # 2. встановлюємо зв’язки
    for person in people:
        if "wife" in person and person["wife"] is not None:
            Person.people[person["name"]].wife = Person.people[person["wife"]]

        if "husband" in person and person["husband"] is not None:
            Person.people[person["name"]].husband = Person.people[person["husband"]]

    return result

