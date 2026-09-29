#Billing Software


data = {}

def total_amount(l1):
    sum = 0
    for j in l1:
        sum += j
    return sum

while True:
    note = '''
        1 for add an item.
        2 for remove an item.
        3 for final bill amount.

        '''
    try:
        choice = int(input("Enter a choice : "))

        if choice == 1:
            new_data = {}
            item_name = input("Enter Item Name : ")
            item_quantity = int(input("Enter Item Quantity : "))
            item_value = int(input("Enter Item Value : "))
            print("LENGTHHH", len(list(data)))
            if len(list(data)) > 0:
                item_id = list(data)[-1] + 1

            else:
                item_id = 1
            print(item_id)
            
            new_data['item_name'] = item_name
            new_data['item_quantity'] = item_quantity
            new_data['item_value'] = item_value

            data[item_id] = new_data
            
            print(data)
        elif choice == 2:
            num = int(input("Enter a id to remove item : "))

            if data[num] :
                data.pop(num)
            else:
                print("Item does not exists")


        elif choice == 3:
            temp_list = []

            for i in data:
                temp_val = data[i]['item_value'] * data[i]['item_quantity']
                temp_list.append(temp_val)
                print("Item Val : ", temp_val)
            final = total_amount(temp_list)

            print("Your Final Bill is : ", final)
            break

        else:
            print("Invalid Choice")
            break
    except:
        print("Invalid Input")

