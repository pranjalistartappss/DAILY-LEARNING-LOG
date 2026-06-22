def count_details(**details):

    count = 0

    for key in details:
        count += 1

    print(count)

count_details(
    name="Rahul",
    age=25,
    city="Delhi"
)