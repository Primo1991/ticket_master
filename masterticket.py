TICKET_PRICE = 10
SERVICE_PRICE = 2

tickets_remaining = 102

#Create the calculate_price function. It takes number of tickets and return
#num_ticets * TICKET_PRICE

def calculate_price(number_of_tickets):
    # Create a new constant for the $2 service charge
    return (number_of_tickets * TICKET_PRICE + SERVICE_PRICE)

while tickets_remaining >= 1:
    print("There are {} tikets remaining.".format(tickets_remaining))
    name = input("What is your name? ")
    num_tickets = input("How many tickets would you like, {}? ".format(name))
    try:
        num_tickets = int(num_tickets)
        if num_tickets > tickets_remaining:
            raise ValueError("there are only {} tickets remaining".format(tickets_remaining))
    except ValueError as err:
        print("Oh no, we ran into an issure. {}. Please try again".format(err))
    else:
        amount_due = calculate_price(num_tickets)
        print("The total due is ${}".format(amount_due))
        user_decidion = input("Do you whant to proceed, Y/N? ")
        if user_decidion.lower() == "y":
            #TODO: Gather credit card information and process it
            print("SOLD!")
            tickets_remaining -= num_tickets
        else:
            print("Thank you anyways, {}!".format(name))
print("Sorry the tickets are sold out!")