def process(data):
    total = 0
    c = 0
    for i in data:
        if i > 0:
            total += i
            c += 1
    print("avg:", total / c)


def get_average(numbers):

    total_value = sum(numbers)
    length_numbers= len(numbers)
    return total_value/length_numbers