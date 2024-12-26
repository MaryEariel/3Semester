class Browser:
    """Браузер"""
    def __init__(self, id, name, comp_id):
        self.id = id
        self.name = name
        self.comp_id = comp_id
class Computer:
    """Компьютер"""
    def __init__(self, id, name):
        self.id = id
        self.name = name
class BrowserComputer:
    """ для реализации связи многие-ко-многим"""
    def __init__(self, computer_id, browser_id, users_count):
        self.computer_id = computer_id
        self.browser_id = browser_id
        self.users_count = users_count

def create_one_to_many(Computers,Browsers):
     return [(brows.name, comp.id, comp.name)
                       for comp in Computers
                       for brows in Browsers
                       if brows.comp_id == comp.id]

def create_many_to_many(Browsers_Computers, Browsers, Computers):
    return [(brows.name, comp.name, cob.users_count)
                    for comp in Computers
                    for cob in Browsers_Computers
                    for brows in Browsers if brows.id == cob.browser_id and comp.id == cob.computer_id]

def task_1(one_to_many,string):
    return list(filter(lambda x: x[2].startswith(string), one_to_many))
def task_2(many_to_many):
    max_users={}
    for brows_name, comp_name, users_count in many_to_many:
        if comp_name not in max_users or max_users[comp_name]<users_count:
            max_users[comp_name]=users_count
    return sorted(max_users.items(),key=lambda x: x[1])
def task_3(many_to_many):
    return sorted(many_to_many, key=lambda x: (x[1],x[0]))

def main():
    # Список компьютеров
    Computers = [
        Computer(1, "AComputer"),
        Computer(2, "AComputer1"),
        Computer(3, "BComputer"),
    ]

    # Список браузеров
    Browsers = [
        Browser(1, "Chrome", 1),
        Browser(2, "Firefox", 3),
        Browser(3, "Safari", 2),
    ]

    # Связь браузеров и компьютеров
    Browsers_Computers = [
        BrowserComputer(1, 1, 1000),
        BrowserComputer(2, 4, 2000),
        BrowserComputer(3, 2, 1500),
    ]
    one_to_many=create_one_to_many(Computers, Browsers)
    many_to_many=create_many_to_many(Browsers_Computers, Browsers, Computers)

    # Г1: Выводим список всех компьютеров, которые начинаются с буквы «A»
    print('Задание Г1')
    result = task_1(one_to_many, 'A')
    for i in result:
        print(f"Компьютер: {i[2]}, Браузер: {i[0]}")

    # Г2: Список компьютеров с максимальным количеством пользователей для каждого браузера
    print('\nЗадание Г2')
    sorted_comp=task_2(many_to_many)
    for comp_name, users_count in sorted_comp:
        print(f"Компьютер: {comp_name}, Максимальное количество пользователей: {users_count}")

    # Г3: Список всех связанных браузеров и компьютеров
    print('\nЗадание Г3')
    sorted_browsers = task_3(many_to_many)
    for brows in sorted_browsers:
        print(f"Средство разработки: {brows[1]}, Язык программирования: {brows[0]}")

if __name__ == '__main__':
    main()