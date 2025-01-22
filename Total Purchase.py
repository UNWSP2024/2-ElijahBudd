def calculate_total_purchase():
    # ask for item prices
    item1 = int(input("Enter price of item 1: "))
    item2 = int(input("Enter price of item 2: "))
    item3 = int(input("Enter price of item 3: "))
    item4 = int(input("Enter price of item 4: "))
    item5 = int(input("Enter price of item 5: "))

    # find and print subtotal
    subtotal = (item1 + item2 + item3 + item4 + item5)
    print("Subtotal:", subtotal)

    # find and print sales_tax
    sales_tax = float(1.07)
    print("Sales tax: 0.07")

    #find and print total
    total = subtotal * sales_tax
    print("Total:", total)
    
calculate_total_purchase()
