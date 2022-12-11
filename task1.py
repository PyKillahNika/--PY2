import doctest


class PlayerUnit:
    """
    Создание и подготовка к работе объекта "Юнит Игрока"

    :param name: Имя юнита
    :param race: Раса юнита (Человек/Орк/Рептилоид/Эльф)
    :param unitclass: Класс юнита (Лучник/Воин/Маг)

    Созданный объект получает:

    exp - Опыт юнита (0)
    lvl - Уровень юнита (1)
    Примеры:
    >>> Unit = PlayerUnit("Сергей","Рептилоид", "Маг") #инициализация экземпляра класса
    """
    def __init__(self, name: str, race: str, unitclass: str):
        if not isinstance(name, str):
            raise TypeError("Имя юнита должно быть str()")
        if not isinstance(race, str):
            raise TypeError("Раса юнита должна быть str()")
        elif race not in ["Человек", "Орк", "Рептилоид", "Эльф"]:
            raise ValueError("Допустимые расы: Человек, Орк, Рептилоид, Эльф")
        if not isinstance(unitclass, str):
            raise TypeError("Класс юнита должен быть str()")
        elif unitclass not in ["Лучник", "Воин", "Маг"]:
            raise ValueError("Допустимые классы: Лучник, Воин, Маг")
        self.name = name
        self.race = race
        self.unitclass = unitclass
        self.exp = 0
        self.lvl = 1

    def getting_exp(self, exp: int):
        """
        Метод получения опыта и повышения уровня юнита
        :param exp: полученный опыт
        после увеличения опыта до необходимого значения
        "lvl" повышается автоматически
        Пример:
        >>> Unit = PlayerUnit("Александр","Орк", "Воин")
        >>> Unit.getting_exp(2200)
        Опыт юнита Александр увеличен на 2200 единиц
        Уровень юнита Александр увеличен до 2
        """
        if type(exp) is not int:
            raise TypeError("Опыт должен быть int()")
        elif exp < 1:
            raise ValueError("Опыт не может быть меньше 1")

        self.exp += exp
        print("Опыт юнита " + self.name + " увеличен на " + str(exp) + " единиц")
        while self.exp >= self.lvl*1000:
            self.exp -= self.lvl*1000
            self.lvl += 1
            print("Уровень юнита " + self.name + " увеличен до " + str(self.lvl))

    def move(self):
        """
        Метод движения игрока
        Пример:
        >>> Unit = PlayerUnit("VLADIMIR", "Эльф", "Лучник")
        >>> Unit.move()
        """
        ...

    def show_info(self):
        """Метод, отображающий информацию о герое
        Пример:
        >>> Unit = PlayerUnit("Джайна", "Человек", "Маг")
        >>> Unit.show_info()
        Имя юнита: Джайна Раса юнита: Человек Класс юнита: Маг Уровень юнита: 1 Текущий опыт:  0
        """
        print("Имя юнита:", self.name, "Раса юнита:", self.race, "Класс юнита:", self.unitclass, "Уровень юнита:",
              self.lvl, "Текущий опыт: ", self.exp)
        ...


class Weapon:
    """
    Создание и подготовка к работе объекта "оружие"
    :param name: название оружия
    :param level: уровень оружия
    :param weapon_class: тип оружия
    :param attack: сила атаки
    Пример:
    >>> Drobitel = Weapon("Дробитель", 3, "Двуручное", 10) #создание объекта
    """
    def __init__(self, name, level: int, weapon_class: str, attack: int):
        self.name = name
        self.level = level
        self.weapon_class = weapon_class
        self.attack = attack

    def sharpen(self):
        """
        Метод заточки оружия, увеличивающий атаку
        Пример:
        >>> Destroyer = Weapon("Дестроер", 5, "Лук", 29)
        >>> Destroyer.sharpen()
        """
        self.attack += 1

    def test_weapon(self):
        """
        Метод проверки силы оружия
        Пример:
        >>> Nightmare = Weapon("Найтмэйр", 10, "Одноручное", 45)
        >>> Nightmare.test_weapon()
        В результате проверки оружия Найтмэйр типа Одноручное было уничтожено 450 противников
        """
        print("В результате проверки оружия", self.name, "типа", self.weapon_class,
              "было уничтожено", self.attack*10, "противников")

    def show_info(self):
        """
        Метод, отображающий параметры объекта
        Пример:
        >>> CheesyStaff = Weapon("Нечестное колдунство", 1, "Посох", 99)
        >>> CheesyStaff.show_info()
        Название оружия: Нечестное колдунство Тип оружия: Посох Сила атаки: 99
        """
        print("Название оружия:", self.name, "Тип оружия:", self.weapon_class, "Сила атаки:", self.attack)


class Car:
    """
    Создание и подготовка к работе объекта типа "Машина"
    :param name: марка автомобиля
    :param color: цвет автомобиля
    :param horse_power: количество лошадиных сил
    :param max_speed: максимальная скорость км/ч
    """
    def __init__(self, name: str, color: str, horse_power: int, max_speed: int):
        self.name = name
        self.color = color
        self.horse_power = horse_power
        self.max_speed = max_speed

    def change_color(self, new_color: str):
        """
        Метод изменения цвета автомобиля
        :param new_color: новый цвет
        """
        self.color = new_color

    def upgrade_engine(self):
        """
        Метод улучшения двигателя автомобиля
        """
        self.horse_power += 50
        self.max_speed += 10

    def go_race(self):
        """
        Метод начала заезда
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
    pass
