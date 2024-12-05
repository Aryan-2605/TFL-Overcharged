def amount_of_statements():
    is_amount_of_statements_valid = False
    while not is_amount_of_statements_valid:
        try:
            amount_of_statements = int(input("How many statements do have? "))
            if amount_of_statements <= 0:
                print("Invalid Input")
            else:
                is_amount_of_statements_valid = True
        except ValueError:
            print("Please enter an integer")




