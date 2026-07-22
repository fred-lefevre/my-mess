# fizzbuzz-bug8.py
#
# Frederic Lefevre <fred.lefevre@gmail.com>

cpt = 0
while (cpt <= 100):
    cpt += 1
    if cpt % 15 == 0:
        print("FizzBuzz")
    elif cpt % 3 == 0:
        print("Fizz")
        cpt -= 1
    elif cpt % 5 == 0:
        print("Buzz")
        cpt -= 1
    else:
        print(cpt)
    cpt += 1
