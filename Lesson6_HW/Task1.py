# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.

# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.


from time import sleep


class TrafficLight:
    __color: str

    def running(self, timer):
        print("Светофор включен!")
        running_timer = 0
        while running_timer < timer:
            self.__color = "Красный"
            print(f"Свет: {self.__color}")
            running_timer += 7
            sleep(7)

            self.__color = "Желтый"
            print(f"Свет: {self.__color}")
            running_timer += 2
            sleep(2)

            self.__color = "Зеленый"
            print(f"Свет: {self.__color}")
            running_timer += 7
            sleep(7)
        print("Светофор выключен!")


traffic_light_instance = TrafficLight()
traffic_light_instance.running(20)
