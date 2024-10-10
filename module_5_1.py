class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        if type(number_of_floors) != int:
            print('Ошибка ввода данных')


    def go_to(self, new_floor):
        self.new_floor = new_floor
        if isinstance(new_floor, int):
            if self.new_floor <= self.number_of_floors and self.new_floor >= 1:
                for i in range(1, self.new_floor + 1):
                    print(f'Лифт прибыл на {i} этаж')
            else:
                print('Такого этажа не существует')
        else:
            print('Ошибка ввода данных')


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
