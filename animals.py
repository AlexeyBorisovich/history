# Создаю родительский класс Pets
class Pets:
    def __init__(self, name, birth_date):
        self.__name = name          # инкапсуляция
        self.__birth_date = birth_date  # инкапсуляция

    def get_name(self):
        return self.__name

    def get_birth_date(self):
        return self.__birth_date

# Создаю Класс Dogs, наследующий от Pets
class Dogs(Pets):
    def __init__(self, name, birth_date, command):
        super().__init__(name, birth_date)  # вызов конструктора родительского класса
        self.__command = command

    def perform_command(self):
        return f"{self.get_name()} says Woof!"

# Создаю Класс Cats, наследующий от Pets
class Cats(Pets):
    def __init__(self, name, birth_date, command):
        super().__init__(name, birth_date)
        self.__command = command

    def perform_command(self):
        return f"{self.get_name()} says Meow!"

# Создаю Класс Hamsters, наследующий от Pets
class Hamsters(Pets):
    def __init__(self, name, birth_date, command):
        super().__init__(name, birth_date)
        self.__command = command

    def perform_command(self):
        return f"{self.get_name()} squeaks!"

# Создаю Класс Horses, наследующий от Pets
class Horses(Pets):
    def __init__(self, name, birth_date, command):
        super().__init__(name, birth_date)
        self.__command = command

    def perform_command(self):
        return f"{self.get_name()} neighs!"

# Создаю Класс Donkeys, наследующий от Pets
class Donkeys(Pets):
    def __init__(self, name, birth_date, command):
        super().__init__(name, birth_date)
        self.__command = command

    def perform_command(self):
        return f"{self.get_name()} brays!"

# Созданию объекты
dog = Dogs("Buddy", "2021-01-01", "sit")
cat = Cats("Whiskers", "2022-06-15", "jump")
hamster = Hamsters("Nibbles", "2023-02-20", "run")
horse = Horses("Spirit", "2020-09-10", "gallop")
donkey = Donkeys("Eeyore", "2021-12-30", "stay")

# Вызываю методы
print(dog.perform_command())
print(cat.perform_command())
print(hamster.perform_command())
print(horse.perform_command())
print(donkey.perform_command())
