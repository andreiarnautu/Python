def converter(original_unit, coefficient = 0.4012):
  return original_unit * coefficient

def string_length(my_string):
  if type(my_string) == int:
    return "Sorry, integers don't have length"
  else :
    return len(my_string)

print(converter(10, 0.5))
print(string_length("10"))