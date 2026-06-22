temps = [0, 20, 30, 40]

fahrenheit = list(
    map(
        lambda temp: (temp * 9/5) + 32,
        temps
    )
)

print(fahrenheit)