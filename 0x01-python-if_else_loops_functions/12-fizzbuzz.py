def fizzbuzz():
    result = []
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            result.append("FizzBuzz")
        elif number % 3 == 0:
            result.append("Fizz")
        elif number % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(number))
    return " ".join(result)


print(fizzbuzz(), end=" $\n")  # Changed from end=" $$"
