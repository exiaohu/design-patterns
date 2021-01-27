from abc import abstractmethod
from typing import Set


class Observer(object):
    @abstractmethod
    def update(self, temp: float, humidity: float, pressure: float):
        raise NotImplementedError()


class Subject(object):
    @abstractmethod
    def register_observer(self, o: Observer) -> None:
        raise NotImplementedError()

    @abstractmethod
    def remove_observer(self, o: Observer) -> None:
        raise NotImplementedError()

    @abstractmethod
    def notify_observers(self) -> None:
        raise NotImplementedError()


class DisplayElement(object):
    @abstractmethod
    def display(self):
        raise NotImplementedError()


class WeatherData(Subject):
    def __init__(self):
        self.__observers: Set[Observer] = set()
        self.__temperature: float = 0.
        self.__humidity: float = 0.
        self.__pressure: float = 0.

    def register_observer(self, o: Observer):
        self.__observers.add(o)

    def remove_observer(self, o: Observer):
        if o in self.__observers:
            self.__observers.remove(o)

    def notify_observers(self):
        for o in self.__observers:
            o.update(self.__temperature, self.__humidity, self.__pressure)

    def measurements_changed(self):
        self.notify_observers()

    def set_measurements(self, temp: float, humidity: float, pressure: float) -> None:
        self.__temperature = temp
        self.__humidity = humidity
        self.__pressure = pressure
        self.measurements_changed()


class CurrentConditionsDisplay(Observer, DisplayElement):
    def __init__(self, weather_data: Subject):
        self.__temperature: float = 0.
        self.__humidity: float = 0.
        self.__weather_data: Subject = weather_data

        weather_data.register_observer(self)

    def update(self, temp: float, humidity: float, pressure: float):
        self.__temperature: float = temp
        self.__humidity: float = humidity

        self.display()

    def display(self):
        print(f'Current conditions: {self.__temperature} F degrees and {self.__humidity} % humidity.')


class StatisticsDisplay(Observer, DisplayElement):

    def __init__(self, weather_data: Subject):
        self.__max_temp: float = 0.
        self.__min_temp: float = 200.
        self.__temp_sum: float = 0.
        self.__num_readings: int = 0

        self.__weather_data = weather_data
        weather_data.register_observer(self)

    def update(self, temp: float, humidity: float, pressure: float):
        self.__temp_sum += temp
        self.__num_readings += 1

        self.__max_temp = max(self.__max_temp, temp)
        self.__min_temp = min(self.__min_temp, temp)

        self.display()

    def display(self):
        print(f'Avg/Max/Min temperature = {self.__temp_sum / self.__num_readings}/{self.__max_temp}/{self.__min_temp}')


class ForecastDisplay(Observer, DisplayElement):

    def __init__(self, weather_data: Subject):
        self.__current_pressure: float = 29.92
        self.__last_pressure: float = 0.

        self.__weather_data = weather_data
        weather_data.register_observer(self)

    def update(self, temp: float, humidity: float, pressure: float):
        self.__last_pressure = self.__current_pressure
        self.__current_pressure = pressure

        self.display()

    def display(self):
        print("Forecast: ", end='')
        if self.__current_pressure > self.__last_pressure:
            print("Improving weather on the way!")
        elif self.__current_pressure == self.__last_pressure:
            print("More of the same")
        elif self.__current_pressure < self.__last_pressure:
            print("Watch out for cooler, rainy weather")


def test():
    weather_data = WeatherData()

    CurrentConditionsDisplay(weather_data)
    StatisticsDisplay(weather_data)
    ForecastDisplay(weather_data)

    weather_data.set_measurements(80, 65, 30.4)
    weather_data.set_measurements(82, 70, 29.2)
    weather_data.set_measurements(78, 90, 29.2)


if __name__ == '__main__':
    test()
