def get_tuple():
    numbers = eval(input("Enter a tuple with integers: "))
    return numbers


def split_positions(numbers):
    even_pos = numbers[0::2]
    odd_pos = numbers[1::2]
    return (even_pos, odd_pos)


numbers = get_tuple()
print("Original tuple:", numbers)
print("Result:", split_positions(numbers))