# happy_new_year: countdown from 10 to 1 then prints "Happy New Year!"
def happy_new_year():
    i = 10
    while i > 0:
        print(i)
        i -= 1
    print("Happy New Year!")

# square_integers: square each element in the list and returns new list
def square_integers(int_list):
    return [num * num for num in int_list]

# fizzbuzz: print numbers 1 to 100 
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
