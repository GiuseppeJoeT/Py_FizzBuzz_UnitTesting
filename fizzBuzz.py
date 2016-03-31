def fizzBuzz(n):
    if n % 15 == 0:
        return "FizzBuzz"
    elif (n % 3) == 0:
        return "Fizz"
    elif (n % 5) == 0:
        return "Buzz"
    return n


numbersArray = range(1, 100)

for n in numbersArray:
    if (n % 3) == 0:
        print "Fizz"
    elif (n % 5) == 0:
        print "Buzz"
    elif (n % 3) == 0 & (n % 5) == 0:
        print "FizzBuzz"
    else:
        print n
