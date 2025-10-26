def read_number():
  user_input = input("enter a number: ")
  return int(user_input)

def calculate_factorial(number):
    result = 1
    for i in range(1,number + 1):
        result *= i
        

    return result



number = read_number()
print("!" , number, " = ", calculate_factorial(number))

