# fizzbuzz-bug1.py
#
# Frederic Lefevre <fred.lefevre@gmail.com>

cpt = 1
while (cpt <= 100):
    if cpt % 15 == 0:
        print("FizzBuzz")
    elif cpt % 3 == 0:
        print("Fizz")
    elif cpt % 5 == 0:
        print(Buzz")
    else:
        print(cpt)
    cpt += 1
