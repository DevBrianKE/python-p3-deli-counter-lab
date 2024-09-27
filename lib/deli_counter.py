# Initialize the deli queue as an empty list
katz_deli = []



# Function to display the current state of the line
def line(deli_line):
    # If the line is empty, inform the user
    if len(deli_line) == 0:
        print("The line is currently empty.")
    else:
        # Create a string that shows the current people in line with their positions
        line_status = "The line is currently: "
        line_status += " ".join([f"{index + 1}. {person}" for index, person in enumerate(deli_line)])
        print(line_status)



# Function to add a customer to the end of the line
def take_a_number(deli_line, name):
    # Add the new customer to the end of the line
    deli_line.append(name)
    print(f"Welcome, {name}. You are number {len(deli_line)} in line.")


# Function to serve the next person in line
def now_serving(deli_line):
    # If the line is empty, inform the user
    if len(deli_line) == 0:
        print("There is nobody waiting to be served!")
    else:
        # Serve the first person in the line (index 0) and remove them from the list
        print(f"Currently serving {deli_line.pop(0)}.")