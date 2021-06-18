class Subject:
    def register_observer():
        raise NotImplementedError

    def remove_observer():
        raise NotImplementedError

    def notify_observers():
        raise NotImplementedError


class Observer:
    def update():
        raise NotImplementedError


class DisplayElement:
    def display():
        raise NotImplementedError


class WeatherData(Subject):
    def __init__(self):
        self._observers = []

    def register_observer(self, observer: Observer):
        self._observers.append(observer)

    def remove_observer(self, observer: Observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._temperature, self._humidity, self._pressure)

    def set_measurements(self, temperature: float, humidity: float, pressure: float):
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.notify_observers()


class CurrentConditionsDisplay(DisplayElement, Observer):
    def __init__(self, weather_data):
        self._temperature = None
        self._humidity = None
        self._weather_data = weather_data
        weather_data.register_observer(self)

    def display(self):
        print(
            f"Current conditions: {self._temperature:.1f}F degrees and {self._humidity:.1f}% humidity"
        )

    def update(self, temperature: float, humidity: float, pressure: float):
        self._temperature = temperature
        self._humidity = humidity
        self.display()


def weather_station():
    weather_data = WeatherData()
    current_display = CurrentConditionsDisplay(weather_data)
    #   statistics_display = StatisticsDisplay(weather_data)
    weather_data.set_measurements(80, 65, 30.4)
    weather_data.set_measurements(82, 70, 29.2)
    weather_data.set_measurements(78, 90, 29.2)


if __name__ == "__main__":
    weather_station()
