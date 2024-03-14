def hello():
    print("Hello")

hello()

def pack(arg_1, arg_2, arg_3):
    return[arg_1, arg_2, arg_3]

this_list = pack('lions', 'tigers', 'bears')
print(this_list)

def eat_lunch(lunch_list):

    if not lunch_list:
        print("My lunchbox is empty")
    else:
        print(f"First I eat {lunch_list[0]}")
        for next_element in lunch_list[1:]:
            print(f"Next I eat {next_element}")
   


eat_lunch(['sandwich', 'soup', 'salad'])
eat_lunch(['sandwich'])
eat_lunch([])

    


        
