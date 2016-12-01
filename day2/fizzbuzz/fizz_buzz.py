# FizzBuzz Lab. Function that returns "Fizz", "Buzz",
# "FizzBuzz", or passed argument depending on the number.

def fizz_buzz(number):
  if number % 3 == 0 and number % 5 == 0:
    return 'FizzBuzz'
  elif number % 3 == 0:
    return 'Fizz'
  elif (number % 5 == 0):
    return 'Buzz'
  else:
    return number
