# fizzbuzz-bug4.py
#
# Frederic Lefevre <fred.lefevre@gmail.com>

cpt = 1
while (cpt <= 100):
    if cpt % 15 == 0:
        echo("FizzBuzz")
    elif cpt % 3 == 0:
        echo("Fizz")
    elif cpt % 5 == 0:
        echo("Buzz")
    else:
        echo(cpt)
    cpt += 1
