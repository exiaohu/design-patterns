#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Set


class Observer(object):
    def update(self, temp: float, humidity: float, pressure: float):
        raise NotImplementedError()


class Subject(object):
    def register_observer(self, o: Observer) -> None:
        raise NotImplementedError()

    def remove_observer(self, o: Observer) -> None:
        raise NotImplementedError()

    def notify_observers(self) -> None:
        raise NotImplementedError()


class DisplayElement(object):
    def display(self):
        raise NotImplementedError()


class WeatherData(Subject):
    def __init__(self):
        self.observers: Set[Observer] = set()
        self.temperature: float = 0.
        self.humidity: float = 0.
        self.pressure: float = 0.

    def register_observer(self, o: Observer):
        self.observers.add(o)

    def remove_observer(self, o: Observer):
        if o in self.observers:
            self.observers.remove(o)

    def notify_observers(self):
        for o in self.observers:
            o.update(self.temperature, self.humidity, self.pressure)

    def measurements_changed(self):
        self.notify_observers()

    def set_measurements(self, temp: float, humidity: float, pressure: float) -> None:
        self.temperature = temp
        self.humidity = humidity
        self.pressure = pressure
        self.measurements_changed()


class CurrentConditionsDisplay(Observer, DisplayElement):
    def __init__(self, weather_data: Subject):
        self.temperature: float = 0.
        self.humidity: float = 0.
        self.weather_data: Subject = weather_data

        weather_data.register_observer(self)

    def update(self, temp: float, humidity: float, pressure: float):
        self.temperature: float = temp
        self.humidity: float = humidity

        self.display()

    def display(self):
        print(
            f'Current conditions: {self.temperature} F degrees and {self.humidity} % humidity.')


class StatisticsDisplay(Observer, DisplayElement):

    def __init__(self, weather_data: Subject):
        self.max_temp: float = 0.
        self.min_temp: float = 200.
        self.temp_sum: float = 0.
        self.num_readings: int = 0

        self.weather_data = weather_data
        weather_data.register_observer(self)

    def update(self, temp: float, humidity: float, pressure: float):
        self.temp_sum += temp
        self.num_readings += 1

        self.max_temp = max(self.max_temp, temp)
        self.min_temp = min(self.min_temp, temp)

        self.display()

    def display(self):
        print(
            f'Avg/Max/Min temperature = {self.temp_sum / self.num_readings}/{self.max_temp}/{self.min_temp}')


class ForecastDisplay(Observer, DisplayElement):

    def __init__(self, weather_data: Subject):
        self.current_pressure: float = 29.92
        self.last_pressure: float = 0.

        self.weather_data = weather_data
        weather_data.register_observer(self)

    def update(self, temp: float, humidity: float, pressure: float):
        self.last_pressure = self.current_pressure
        self.current_pressure = pressure

        self.display()

    def display(self):
        print("Forecast: ", end='')
        if self.current_pressure > self.last_pressure:
            print("Improving weather on the way!")
        elif self.current_pressure == self.last_pressure:
            print("More of the same")
        elif self.current_pressure < self.last_pressure:
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
