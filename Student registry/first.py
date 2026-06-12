def get_numbers(count):
    number_list = []

    for _ in range(count):
        while True:
            try:
                user_input = float(input("Please enter a number: "))
                number_list.append(user_input)
                break
            except ValueError:
                print("Please enter a valid input!")

    return number_list

def analyze_numbers(numbers):
    dict_list = {'min' : min(numbers), 'max' : max(numbers) , 'average' : round(sum(numbers) / len(numbers), 2) , 'count' :  len(numbers)} 
    return dict_list

def main():

    while True:
        try:
            numbers_count = int(input("Please enter how many numbers do you want: "))
            if numbers_count <= 0:
                print("must be positive number! ")
            else: 
                break
        except ValueError:
            print("Please put a valid input!")
    

    print(analyze_numbers(get_numbers(numbers_count)))

main()