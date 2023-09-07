fahrenheit_temps = [32, 68, 86, 104, 122]

celsius_temps = list(map(lambda x: (x - 32) * 5/9, fahrenheit_temps))

print(celsius_temps)
