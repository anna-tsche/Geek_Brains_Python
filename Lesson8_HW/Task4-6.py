# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру, например словарь.
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.


class Warehouse:
    _inventory: list = []
    _transferred_to_departments: list = []

    def goods_receipt(self, item: "OfficeEquipment"):
        self._inventory.append({"ID": item.product_id, "бренд": item.brand})

    def transfer_to_department(self, requested_id: int, department: str):
        try:
            requested_object = None
            index_for_pop = None
            if type(requested_id) != int:
                if not requested_id.isdigit():
                    raise IDIsNotANumber
            for instance in range(len(self._inventory)):
                if self._inventory[instance]["ID"] == int(requested_id):
                    requested_object = self._inventory[instance]
                    index_for_pop = instance
            if requested_object is None:
                raise NoIDInInventory
            self._transferred_to_departments.append({"отдел": department,
                                                     "ID": requested_object["ID"],
                                                     "бренд": requested_object["бренд"]
                                                     })
            self._inventory.pop(index_for_pop)
        except NoIDInInventory as inventory_error:
            print(inventory_error)
        except IDIsNotANumber as id_error:
            print(id_error)

    def __str__(self):
        return f"На складе хранятся: {self._inventory}, в отделы переданы: {self._transferred_to_departments}."


class OfficeEquipment:
    def __init__(self, product_id: int, brand: str, price: float, purchase_year: int):
        self.product_id = product_id
        self.brand = brand
        self.price = price
        self.purchase_year = purchase_year


class Printer(OfficeEquipment):
    def __init__(self, product_id: int, brand: str, price: float, purchase_year: int, color: bool):
        super().__init__(product_id, brand, price, purchase_year)
        self.color = color

    def __str__(self):
        return f"Принтер {self.brand}."


class Scanner(OfficeEquipment):
    def __init__(self, product_id: int, brand: str, price: float, purchase_year: int, resolution: int):
        super().__init__(product_id, brand, price, purchase_year)
        self.resolution = resolution

    def __str__(self):
        return f"Сканер {self.brand}."


class Copier(OfficeEquipment):
    def __init__(self, product_id: int, brand: str, price: float, purchase_year: int, copies_per_minute: float):
        super().__init__(product_id, brand, price, purchase_year)
        self.copies_per_minute = copies_per_minute

    def __str__(self):
        return f"Ксерокс {self.brand}."


class NoIDInInventory(Exception):
    def __str__(self):
        return "Объект с таким инвентарным номером на складе не найден."


class IDIsNotANumber(ValueError):
    def __str__(self):
        return "Инвентарный номер должен быть числом."


printer = Printer(1, "Canon", 100, 2021, False)
scanner = Scanner(2, "Canon", 1000, 2021, 1024)
copier = Copier(3, "Xerox", 500, 2020, 70)
warehouse = Warehouse()

warehouse.goods_receipt(printer)
warehouse.goods_receipt(scanner)
warehouse.goods_receipt(copier)

print(warehouse)

warehouse.transfer_to_department(input("Пожалуйста, введите инвентарный номер объекта, который вы хотите получить >>> "),
                                 input("Пожалуйста, введите ваш отдел >>> "))
warehouse.transfer_to_department(input("Пожалуйста, введите инвентарный номер объекта, который вы хотите получить >>> "),
                                 input("Пожалуйста, введите ваш отдел >>> "))

print(warehouse)

warehouse.transfer_to_department(3, "Бухгалтерия")

print(warehouse)
