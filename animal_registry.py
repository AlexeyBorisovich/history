class Pets:
    def __init__(self, name, birth_date):
        self.__name = name
        self.__birth_date = birth_date
        self.__commands = []

    def get_name(self):
        return self.__name

    def get_birth_date(self):
        return self.__birth_date

    def add_command(self, command):
        self.__commands.append(command)

    def get_commands(self):
        return self.__commands


class Dogs(Pets):
    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)


class Cats(Pets):
    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)


class Hamsters(Pets):
    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)


class AnimalRegistry:
    def __init__(self):
        self.animals = []

    def add_animal(self):
        name = input("Введите имя животного: ")
        birth_date = input("Введите дату рождения животного (YYYY-MM-DD): ")
        animal_type = input("Введите тип животного (dog/cat/hamster): ").lower()

        if animal_type == "dog":
            animal = Dogs(name, birth_date)
        elif animal_type == "cat":
            animal = Cats(name, birth_date)
        elif animal_type == "hamster":
            animal = Hamsters(name, birth_date)
        else:
            print("Неправильный тип животного.")
            return

        self.animals.append(animal)
        print(f"{animal.get_name()} успешно добавлено в реестр!")

    def view_commands(self):
        name = input("Введите имя животного, чтобы увидеть команды: ")
        for animal in self.animals:
            if animal.get_name() == name:
                commands = animal.get_commands()
                if commands:
                    print(f"Команды для {name}: {', '.join(commands)}")
                else:
                    print(f"{name} еще не обучено ни одной команде.")
                return
        print(f"Животное с именем {name} не найдено.")

    def train_animal(self):
        name = input("Введите имя животного, которое хотите обучить: ")
        for animal in self.animals:
            if animal.get_name() == name:
                command = input("Введите новую команду для обучения: ")
                animal.add_command(command)
                print(f"{name} обучено новой команде: {command}")
                return
        print(f"Животное с именем {name} не найдено.")

    def list_all_animals(self):
        if not self.animals:
            print("Реестр животных пуст.")
            return
        
        print("\nСписок всех животных:")
        for animal in self.animals:
            print(f"- {animal.get_name()} (Тип: {type(animal).__name__}, Дата рождения: {animal.get_birth_date()})")

    def display_menu(self):
        while True:
            print("\n--- Реестр домашних животных ---")
            print("1. Завести новое животное")
            print("2. Увидеть список команд животного")
            print("3. Обучить животное новым командам")
            print("4. Посмотреть список всех животных")
            print("5. Выход")
            choice = input("Выберите действие: ")

            if choice == '1':
                self.add_animal()
            elif choice == '2':
                self.view_commands()
            elif choice == '3':
                self.train_animal()
            elif choice == '4':
                self.list_all_animals()
            elif choice == '5':
                print("Выход из программы.")
                break
            else:
                print("Неправильный выбор. Пожалуйста, попробуйте снова.")


# Запуск программы
if __name__ == "__main__":
    registry = AnimalRegistry()
    registry.display_menu()
