class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32


temp = TemperatureConverter.celsius_to_fahrenheit(25)
print(temp)