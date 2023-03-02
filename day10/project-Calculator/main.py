from logo import logo
print(logo)

def add(n1, n2):
    return (n1 + n2)
def subtract(n1, n2):
    return (n1 - n2)
def multiply(n1, n2):
    return (n1 * n2)
def divide(n1, n2):
    return (n1 / n2)

calc_dictionary={
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    }

def calculator ():
    number1=int(input("Enter the 1st number: "))
    for op in calc_dictionary:
        print(op)
    operation = input("pick an operation from the above list to perform: ")
    number2=int(input("Enter the 2nd number: "))

    calc_fn=calc_dictionary[operation] 
    continue_input=(input("do you want to continue? yes or no: ").lower())
                
    continue_flag=True

    result=calc_fn(number1,number2)
    last_calc_value=result

    while continue_flag:
        if (continue_input == "yes"):
            operation = input("Enter the new operation to perform: ")
            nextnumber=int(input("Enter the next number you want to perform the new operation: "))
            result1=calc_fn(last_calc_value,nextnumber)
            
            continue_input=(input("do you want to continue? yes or no: ").lower())
            last_calc_value=result1
            
            if(continue_input == "no"):
                answer = last_calc_value
                continue_flag = False
        elif(continue_input == "no"):
            answer = last_calc_value
            continue_flag = False
        else:
            print ("provide a valid input")
            continue_flag = False

    print(f"final value: {answer}")

calculator()