import json
import os

# Определение классов животных
class Animal:
    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date
        self.commands = []

    def perform_command(self):
        return f"{self.name} выполняет команды: {', '.join(self.commands)}"

    def add_command(self, command):
        self.commands.append(command)


class Dog(Animal):
    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)


class Cat(Animal):
    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)


class Hamster(Animal):
    def __init__(self, name, birth_date):
        super().__init__(name, birth_date)


class AnimalCounter:
    def __init__(self):
        self.count = 0
        self.filename = 'counter.json'
        self.load_count()

    def add(self):
        self.count += 1

    def save_to_file(self):
        with open(self.filename, 'w') as f:
            json.dump({'count': self.count}, f)
        print(f"Счетчик сохранен: {self.count}")

    def load_count(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                data = json.load(f)
                self.count = data.get('count', 0)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            raise Exception("Работа с ресурсом была некорректной")
        self.save_to_file()


# Реализация реестра животных
class AnimalRegistry:
    def __init__(self):
        self.animals = []
        self.filename = 'animals.json'
        self.load_animals()

    def add_animal(self, animal):
        self.animals.append(animal)

    def list_animals(self):
        return [(idx + 1, animal.name) for idx, animal in enumerate(self.animals)]

    def show_commands(self, animal_name):
        for animal in self.animals:
            if animal.name == animal_name:
                return animal.perform_command()
        return "Животное не найдено."

    def train_animal(self, animal_name, command):
        for animal in self.animals:
            if animal.name == animal_name:
                animal.add_command(command)
                return f"{animal.name} обучен команде: {command}"
        return "Животное не найдено."

    def save_animals(self):
        with open(self.filename, 'w') as f:
            for animal in self.animals:
                data = {
                    'type': animal.__class__.__name__.lower(),
                    'name': animal.name,
                    'birth_date': animal.birth_date,
                    'commands': animal.commands  # Сохранение команд
                }
                json.dump(data, f)
                f.write('\n')  # Добавляем новую строку после каждого животного
        print("Список животных сохранен.")

    def load_animals(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                for line in f:
                    data = json.loads(line.strip())
                    animal_type = data.get('type', 'unknown')
                    if animal_type == 'dog':
                        animal = Dog(data['name'], data['birth_date'])
                    elif animal_type == 'cat':
                        animal = Cat(data['name'], data['birth_date'])
                    elif animal_type == 'hamster':
                        animal = Hamster(data['name'], data['birth_date'])
                    else:
                        print(f"Неизвестный тип животного: {animal_type}")
                        continue
                    animal.commands = data['commands']  # Загрузка команд из файла
                    self.add_animal(animal)
                    print(f"Загружено животное: {animal.name}, Тип: {animal_type}")

def main():
    registry = AnimalRegistry()
    
    with AnimalCounter() as counter:
        while True:
            print("\nМеню:")
            print("1. Завести новое животное")
            print("2. Посмотреть список животных")
            print("3. Посмотреть команды животного")
            print("4. Обучить животное новым командам")
            print("5. Выход")

            choice = input("Выберите опцию: ")

            if choice == '1':
                name = input("Введите имя животного (с заглавной буквы): ").capitalize()
                birth_date = input("Введите дату рождения животного (формат: YYYY-MM-DD): ")
                animal_type = input("Введите тип животного (dog, cat, hamster): ").lower()

                if animal_type == 'dog':
                    animal = Dog(name, birth_date)
                elif animal_type == 'cat':
                    animal = Cat(name, birth_date)
                elif animal_type == 'hamster':
                    animal = Hamster(name, birth_date)
                else:
                    print("Неизвестный тип животного.")
                    continue

                registry.add_animal(animal)
                counter.add()
                registry.save_animals()  # Сохранение списка животных
                print(f"{animal.name} добавлен в реестр.")
            
            elif choice == '2':
                print("Список животных:")
                animals_list = registry.list_animals()
                if animals_list:
                    for idx, animal_name in animals_list:
                        print(f"{idx}. {animal_name}")
                else:
                    print("Реестр животных пуст.")

            elif choice == '3':
                animal_name = input("Введите имя животного: ")
                commands = registry.show_commands(animal_name)
                print(commands)

            elif choice == '4':
                animal_name = input("Введите имя животного: ")
                command = input("Введите команду для обучения: ")
                result = registry.train_animal(animal_name, command)
                print(result)
                registry.save_animals()  # Сохраняем обновленный список после обучения

            elif choice == '5':
                print("Выход из программы.")
                break

            else:
                print("Неверный выбор. Пожалуйста, попробуйте снова.")


if __name__ == "__main__":
    main()
