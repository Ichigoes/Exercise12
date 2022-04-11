command = input().split()
bakery_dict = dict()
sold_goods = 0

while command[0] != "Complete":

    if command == "Complete":
        break

    if command[0] == "Receive":
        quantity = int(command[1])
        food = command[2]
        if food not in bakery_dict:
            bakery_dict[food] = quantity
        elif food in bakery_dict:
            bakery_dict[food] += quantity
        elif quantity <= 0:
            continue

    elif command[0] == "Sell":
        quantity = int(command[1])
        food = command[2]
        if food not in bakery_dict:
            print(f"You do not have any {food}.")
        elif quantity > bakery_dict[food]:
            bakery_dict.update(food = "")
            print(f"There aren't enough {food}. You sold the last {quantity} of them.")
        elif quantity <= bakery_dict[food]:
            bakery_dict[food] -= quantity
            sold_goods += quantity
            print(f"You sold {quantity} {food}.")
            if bakery_dict[food] == 0:
                del bakery_dict[food]

    command = input().split()

for food in bakery_dict:
    print(f"{food}: {bakery_dict[food]}")
print(f"All sold: {sold_goods} goods")