numbers = ['1', '2', '3', '4']

integer_numbers = list(
    map(
        lambda num: int(num),
        numbers
    )
)

print(integer_numbers)