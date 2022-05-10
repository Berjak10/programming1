from datetime import datetime

class furniture:
    def __init__(self, type, amount, weight, color, dimensions, time = datetime.now()):
        self.type = type
        self.amount = int(amount)
        self.weight = float(weight)
        self.color = color
        self.dimensions = dimensions
        self.time = datetime.now()
        self.time = time

    def to_string(self):
        return (":|:" + self.type
                + ":|:" + self.amount
                + ":|:" + self.weight
                + ":|:" + self.color
                + ":|:" + self.dimensions
                + ":|:" + self.time
                + ":|:\n")


def add_furniture():
    type = input("Input the furniture type: ")
    amount = input("Input the amount: ")
    weight = input("Input the weight of the furniture in kg: ")
    width = input("Input the furniture width in m: ")
    height = input("Input the furniture height in m : ")
    length = input("Input the furniture length in m: ")
    color = input("Input the furniture color: ")
    dimensions = (width, length, height)
    add_new_furniture = furniture(type, amount, weight, color, dimensions)
    furniture_list.append(add_new_furniture)



def list_furniture():
    print("\n"*100)
    for furniture in furniture_list:
        print(f"Type: {furniture.type}")
        print(f"Amount: {furniture.amount} ")
        print(f"Weight: {furniture.weight}kg ")
        print(f"Dimensions: {furniture.dimensions[0]}m / {furniture.dimensions[1]}m / {furniture.dimensions[2]}m ")
        print(f"Color: {furniture.color}")
        print(f"Color: {furniture.time.ctime()}")


def store_furniture():
    with open(file_name , 'w' ) as f:
        for furniture in furniture_list:
            f.write(f"{furniture.type};")
            f.write(f"{furniture.amount};")
            f.write(f"{furniture.weight};")
            f.write(f"{furniture.dimensions[0]}/{furniture.dimensions[1]}/{furniture.dimensions[2]};")
            f.write(f"{furniture.color};")
            f.write(f"{furniture.time.timestamp()}\n")

def restore_furniture():
    with open (file_name, 'r') as f:
        for line in f.readlines():
            fields = line.split(":|:")
            dimensions = (i for i in fields[4].split("/"))
            time = datetime.fromtimestamp(float(fields[5]))
            furniture_list.append(furniture(fields[0], fields[1], fields[2], dimensions, fields[4], time))

def full_text_search(match):
    print("\n" * 100)
    for furniture in furniture_list:
        if furniture.to_string().lower() in match.lower():
            print(f"Type: {furniture.type}")
            print(f"Amount: {furniture.amount} ")
            print(f"Weight: {furniture.weight}")
            print(f"Dimensions: {furniture.dimensions[0]}/{furniture.dimensions[1]}/{furniture.dimensions[2]}")
            print(f"Color:{furniture.color}")
            print(f"Time:{furniture.time.ctime()}")


def delete_furniture(delete):
    print("\n" * 100)
    for index, furniture in enumerate(furniture_list):
        if delete.lower() in furniture.to_string().lower():
            print(f"Type: {furniture.type}")
            print(f"Amount: {furniture.amount} ")
            print(f"Weight: {furniture.weight}")
            print(f"Dimensions: {furniture.dimensions[0]}/{furniture.dimensions[1]}/{furniture.dimensions[2]}")
            print(f"Color:{furniture.color}")
            print(f"Time:{furniture.time.ctime()}")
    delete_option = input("which one you want to delete: ")
    try:
        deleted_item = furniture_list.pop(int(delete_option))
        print(f"deleted {deleted_item.destination} trip")
    except IndexError:
        print("Wrong input")

file_name = "inventar.txt"
household_inventory_list = []
while True:
    print("Main Menu")
    print("What do you want to do next?")
    print("1: add a new furniture")
    print("2: list all furniture")
    print("3: Reading all furniture from file")
    print("4: Save the data")
    print("5: Find the data")
    print("6: Delete furniture")
    print("x: exit the problem")
    option = input("Your selection: ")
    if(option == "1"):
        add_furniture()
    elif(option == "2"):
        list_furniture()
    elif(option =="3"):
        restore_furniture()
    elif(option == "4"):
        store_furniture()
    elif(option == "5"):
        full_text_search(input("please provide the cupboards amount: "))
    elif(option == "6"):
        delete_furniture(input("Please provide the search string: "))
    elif(option == "x"):
        store_furniture()
        quit()
    else:
        print("Wrong Input, try again!")

