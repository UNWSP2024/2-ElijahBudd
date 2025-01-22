def average_age():
    # Get User Input
    age1 = int(input("Enter age of Friend 1: "))
    age2 = int(input("Enter age of Friend 2: "))
    age3 = int(input("Enter age of Friend 3: "))
    age4 = int(input("Enter age of Friend 4: "))
    age5 = int(input("Enter age of Friend 5: "))

    # Sum ages
    sum_age = (age1 + age2 + age3 + age4 + age5)

    # Average the ages
    average_age = sum_age / 5
    # Print the results
    print("Average Age of Friends:", average_age)


# Line which calls the above function.
average_age()
