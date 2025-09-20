class ManagePassenger:
    passenger_list = []
    
    # Takes user input for booking in name variable and validating if user has entered alphabets or number
    @staticmethod 
    def name():
        while True:
            name = input("Enter your name: ")
            if name.replace(" ", "").isalpha():
                return name
            else:
                print("Please enter a valid characters.")

    # Take user input for booking in phone_no variable and validating if its in digit(number) or not as well as a condition of 
    # user has entered less than 10 digit phone number
    @staticmethod
    def phone_no():
        while True:
            phone_no = input("Enter phone number: ")
            if phone_no.isdigit() and len(phone_no) == 10:
                return phone_no
            else:
                print("You have entered wrong character or your number length is less/more then 10.\n"
                      "Please enter numerical digit and correct 10 digit phone number.")
    
    # Takes user input for booking in gender variable and checks if the details are in alphabet or not converts into lower case
    @staticmethod
    def gender():
        while True:
            gender = input("Enter your gender (Male, Female, Not to mention): ").lower()
            if gender in ['male', 'female', 'not to mention']:
                return gender
            else:
                print("Invalid gender! Please enter Male, Female, or Not to mention.")

    # Take user input for booking in age variable and checks of age is digit or not and also a condition is added
    # age should not be more than 120 years
    @staticmethod
    def age():
        while True:
            age = input("Enter age: ")
            if age.isdigit() and (0 < int(age) <= 120):
                return age
            else:
                print("Please enter correct age")

    # here the method collects all the data of passenger and it is solely is used to call out all the date in a single list which
    # will show the passenger details
    def collect_passenger_data(self):
        print("\nBelow enter passenger details correctly as asked for booking:")
        passenger_list = []
        while True:
            obj_1 = ManagePassenger
            name_details = obj_1.name()
            phone_details = obj_1.phone_no()
            age_details = obj_1.age()
            gender_details = obj_1.gender()
            passenger_data = name_details, phone_details, age_details, gender_details
            self.passenger_list.append(passenger_data)
            more = input("Would you like to Add another passenger detail? (Yes/No): ").strip().lower()
            if more == "no":
                print("\n\n---Booking Done Successfully--- \nPassenger Details:")
                for idx, passenger in enumerate(passenger_list, 1):
                    print(f"Passenger {idx}: Name: {passenger[0]}, Phone: {passenger[1]}, Age: {passenger[2]}, Gender: {passenger[3]}")
                break
            else:
                continue
