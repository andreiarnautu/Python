address = ["Baker Street", "21", "London"]
pins = {"Mike":1234, "Joe":1111, "Jack":2222}

print(address[0], address[1])

pin = int(input("Enter your pin: "))


def find_in_file(f) :
    myFile = open("sample.txt")
    fruits = myFile.read()
    fruits = fruits.splitlines()

    if f in fruits :
        return "Got that shit"
    else :
        return "404 not found"


if pin in pins.values():
    fruit = input("Enter fruit: ")
    print(find_in_file(fruit))
else:
    print("Incorrect pin!")
    print("This info can only be accessed by: ")
    for key in pins.keys() :
        print(key)
