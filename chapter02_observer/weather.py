class Subject:
    def register_observer(self, observer):
        raise NotImplementedError

    def remove_observer(self, observer):
        raise NotImplementedError

    def notify_observers(self):
        raise NotImplementedError


class Observer:
    def update(self, temp, humidity, pressure):
        raise NotImplementedError


class DisplayElement:
    def display(self):
        raise NotImplementedError


class WeatherData(Subject):
    def __init__(self):
        self._temperature = None
        self._humidity = None
        self._pressure = None
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
            f"Current conditions: "
            f"{self._temperature:.1f}F degrees and "
            f"{self._humidity:.1f}% humidity"
        )

    def update(self, temp: float, humidity: float, pressure: float):
        self._temperature = temp
        self._humidity = humidity
        self.display()


class StatisticsDisplay(DisplayElement, Observer):

    def __init__(self, weather_data):
        self._max_temp = 0.
        self._min_temp = 200.
        self._temp_sum = 0.
        self._num_readings = 0
        self._weather_data = None
        self._weather_data = weather_data
        weather_data.register_observer(self)

    def update(self, temp, humidity, pressure):
        self._temp_sum += temp
        self._num_readings += 1
        self._max_temp = max(temp, self._max_temp)
        self._min_temp = min(temp, self._min_temp)
        self.display()

    def display(self):
        print(f"Avg/Max/Min temperature = "
              f"{self._temp_sum / self._num_readings}"
              f"/{self._max_temp}"
              f"/{self._min_temp}"
              )


class ForecastDisplay(DisplayElement, Observer):

    def __init__(self, weather_data):
        self._current_pressure = 29.92
        self._last_pressure = None
        self._weather_data = weather_data
        weather_data.register_observer(self)

    def update(self, temp, humidity, pressure):
        self._last_pressure = self._current_pressure
        self._current_pressure = pressure
        self.display()

    def display(self):
        print("Forecast: ", end="")
        if self._current_pressure > self._last_pressure:
            print("Improving weather on the way!")
        elif self._current_pressure == self._last_pressure:
            print("More of the same")
        elif self._current_pressure < self._last_pressure:
            print("Watch out for cooler, rainy weather")


def weather_station():
    weather_data = WeatherData()

    current_display = CurrentConditionsDisplay(weather_data)
    statistics_display = StatisticsDisplay(weather_data)
    forecast_display = ForecastDisplay(weather_data)

    weather_data.set_measurements(80, 65, 30.4)
    weather_data.set_measurements(82, 70, 29.2)
    weather_data.set_measurements(78, 90, 29.2)

    weather_data.remove_observer(forecast_display)
    weather_data.set_measurements(62, 90, 28.1)


if __name__ == "__main__":
    weather_station()
