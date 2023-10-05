# Name:Brandon Council, SID: 009588480
import datetime
from hashTable import package_hash_table
from Truck import total

# Update the status of a package based on the time entered.
# Time complexity: O(1)
def set_package_status(package, time_entered):
    if package.time_delivered <= time_entered:
        package.status = "Delivered"
    elif package.time_left_hub <= time_entered:
        package.status = "En Route"
    else:
        package.status = "At Hub"


HEADER = "\n{:^15} ~ {:^65} ~ {:^12} ~ {:^10} ~ {:^15}".format("Package ID", "Address", "Weight (kgs)", "Deadline", "Status")

# Print information about packages based on user input time and choice.
# Time complexity: O(n)
def lookup_package_info(user_input_time, user_input_choice, package_select):
    packages = []
    hour, minute = map(int, user_input_time.split(':'))
    time_entered = datetime.timedelta(hours=hour, minutes=minute)

    for i in range(len(package_hash_table.table)):
        all_packages = package_hash_table.search(i + 1)
        packages.append(all_packages)

    print(HEADER)
    if user_input_choice == "1":
        print(f"\nShowing information for all packages at {user_input_time}")

        for package in packages:
            package_full_address = f"{package.address}, {package.city}, {package.zipcode}"
            set_package_status(package, time_entered)
            delivery_time = f"at {package.time_delivered}" if package.status == "Delivered" else ""
            print(f"{package.package_id:^15} ~ {package_full_address:<65} ~ {package.mass:^12} ~ {package.deadline:^10} ~ {package.status:<10} {delivery_time}")

    elif user_input_choice == "2":
        print(f"\nShowing information for package ID '{package_select}' at {user_input_time}")

        for package in packages:
            if package.package_id == int(package_select):
                package_full_address = f"{package.address}, {package.city}, {package.zipcode}"
                set_package_status(package, time_entered)
                delivery_time = f"at {package.time_delivered}" if package.status == "Delivered" else ""
                print(f"{package.package_id:^15} ~ {package_full_address:<65} ~ {package.mass:^12} ~ {package.deadline:^10} ~ {package.status:<10} {delivery_time}")


# Get user input for continuing the program or exiting.
# Time complexity: O(1)
def continue_or_exit():
    while True:
        continue_input = input("\nWould you like to: \n[1] Check for another option"
                               "\n[2] Go to main menu"
                               "\n[Exit] Exit the program\n")
        if continue_input == "1":
            return True
        elif continue_input == "2":
            main()
            return False
        elif continue_input.lower() == "exit":
            print("Goodbye!")
            exit()
        else:
            print("\nInvalid input, please try again using [1, 2, or 'exit']. ")


# Get a valid time input from the user.
# Time complexity: O(1)
def check_time_format():
    while True:
        try:
            time_input = input("\nEnter a time using 24-Hour time format [HH:mm]: ")
            hour, minute = map(int, time_input.split(":"))
            return time_input
        except ValueError:
            print("\nIncorrect time format! Tip: please include the ':' ")

# Handles user input for option 1 (status of all packages).
# Time complexity: O(1)
def option_one_input():
    while True:
        time_input = check_time_format()
        lookup_package_info(time_input, "1", package_select=None)
        if not continue_or_exit():
            break

# Handles user input for option 2 (status of a single package).
# Time complexity: O(1)
def option_two_input():
    while True:
        try:
            package_choice = int(input("\nEnter the package ID you want to search [1-40]: "))
            if package_choice > 40 or package_choice < 1:
                print("\nInvalid package ID. Choose an ID between 1-40.")
            else:
                time_choice = check_time_format()
                lookup_package_info(time_choice, "2", package_choice)
                if not continue_or_exit():
                    break
        except ValueError:
            print("\nInput error! Please enter an integer value.")

# Handles user input for option 1.
# Time complexity: O(1)
def handle_option_one():
    option_one_input()


# Handles user input for option 2.
# Time complexity: O(1)
def handle_option_two():
    option_two_input()


# Handles user input for option 3
# Time complexity: O(1)
def handle_option_three(total):
    print("\nTotal mileage travelled by all trucks: ", total, "miles")
    option_three_input = input("\nType [1] to return to the main menu. Type any other key to exit the program. ")
    if option_three_input != "1":
        print("Goodbye! Exiting program.")
        exit()

# Main function to control program flow.
def main():

    while True:
        print("\nWestern Governors University Parcel Service")
        first_input = input("\nPlease choose one of the following: "
                            "\n1. View the status of all packages at a specific time. "
                            "\n2. View the status of a single package at a specific time. "
                            "\n3. View the total mileage travelled by all trucks. "
                            "\n\nEnter [1, 2, or 3] or type 'Exit' to exit the program. ")

        if first_input == "1":
            handle_option_one()
        elif first_input == "2":
            handle_option_two()
        elif first_input == "3":
            handle_option_three(total)
        elif first_input.lower() == "exit":
            print("\nGoodbye! Exiting program.")
            exit()
        else:
            print("\nInput Invalid. Please try again.")

if __name__ == '__main__':
    main()
