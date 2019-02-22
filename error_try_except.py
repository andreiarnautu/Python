def divide(a, b):
  try:
    return a / b
  except ZeroDivisionError:
    return "Zero division can not be done, you idiot. :P"

a = int(input("Give a number: "))
b = int(input("Give a number: "))
print(divide(a, b))
