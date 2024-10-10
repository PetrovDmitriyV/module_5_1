class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = int(number_of_floors)

    def go_to(self, new_floor):
        self.new_floor = int(new_floor)
        if new_floor <= self.number_of_floors and self.new_floor >= 1:
            for i in range(1, self.new_floor + 1):
                print(i)
        else:
            print('Такого этажа не существует')


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
