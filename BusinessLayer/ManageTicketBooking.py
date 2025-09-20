from BusinessLayer.ManageAirport import ManageAirport
from BusinessLayer.HelperExtension import HelperExtension

class ManageTicketBooking:
    
    # global variable declared to call it around all the project for classes and methods
    def __init__(self):
        self.source_city = None
        self.destination_city = None
        self.travelling_date = None
        self.travelling_day = None
        self.selected_flight_number = None
        self.selected_flight = None
        
    print("\t \t \t \t \t -----Welcome to the Domestic Ticket Booking System!-----\n")

    # Taking source city(airport) input from the user and checking/validating using the ManageAirport business layer 
    # and assigns the city to a global variable declared
    def get_and_validate_source_airport(self):
        while True:
            source_airport = input("Enter City name From/Source (Airport): ").title()
            if ManageAirport.validate_source(source_airport):
                self.source_city = source_airport
                return
            else:
                print("Please enter correct From/Source Airport.")

    # Taking destination city(airport) input from the user and checking/validating using the ManageAirport business layer 
    # and assigns the city to a global variable declared
    def get_and_validate_destination_airport(self):
        while True:
            destination_airport = input("Enter City name To/Destination (Airport): ").title()
            if ManageAirport.validate_destination(self.source_city, destination_airport):
                self.destination_city = destination_airport
                return
            else:
                print("Please enter correct To/Destination Airport.")

    # Taking date input from the user and checking/validating using the ManageDateValidation business layer 
    # and the date gets converted to day using the get_day_from_date method of ManageDateValidation
    # and both day and date gets assigned to a global variable declared
    def get_and_validate_travelling_date(self):
        while True:
            date_input = input("Enter Travelling Date in DD/MM/YYYY format: ")
            if HelperExtension.validate_travelling_date(date_input):
                # assigning user date input to global variable
                self.travelling_date = date_input
                # getting day from date to check if the day is available in the list of flight routes
                self.travelling_day = HelperExtension.get_day_from_date(date_input)
                return                  
            else:
                print("Please enter correct Date format.")
    
    # method fetches all the details flight number which is stored in a jason file and prints the list of available flights
    def print_flight_details(self, flights):  # Accepts a list of flight objects
        for flight in flights:  # Loop through each flight object
            placeholder = f"""
            🛫 Flight Details:
            --------------------------------
            ✈ Flight Number: {flight.flight_number}
            🌍 From: {flight.source_city} → 🏙 To: {flight.destination_city}
            📅 Travel Day: {self.travelling_date, flight.weekday}
            ⏰ Departure: {flight.start_time} → 🛬 Arrival: {flight.end_time}
            📏 Distance: {flight.distance_km} km
            --------------------------------
            """
            print(placeholder)
            
    # the below method asks the user to enter flight number from the give list
    # and fetches the flight number from the list of available flights 
    def book_flight(self, available_flights):
        self.selected_flight_number = input("Enter the Flight Number from the list: ")
        for flight in available_flights:
            if flight.flight_number == self.selected_flight_number:
                print(f"Selected Flight Number has all seats available: ",{self.selected_flight_number})
                print(f"""\n
                        🛫 Flight Details:
                        --------------------------------
                        ✈ Flight Number: {flight.flight_number}
                        🌍 From: {flight.source_city} → 🏙 To: {flight.destination_city}
                        📅 Travel Day: {self.travelling_date, flight.weekday}
                        ⏰ Departure: {flight.start_time} → 🛬 Arrival: {flight.end_time}
                        📏 Distance: {flight.distance_km} km
                        --------------------------------
                        """)
                
    # this method finds the selected flight from the available flights, update its travel date, and print the flight details      
    def confirmed_flight_booked(self, available_flights, number_of_passengers = 1):       
        for flight in available_flights:
            if flight.flight_number == self.selected_flight_number:
                self.selected_flight = flight
                self.selected_flight.travel_date = self.travelling_date
                self.selected_flight.fare = self.selected_flight.fare * number_of_passengers
                print(f"""\n
                        🛫 Flight Details:
                        --------------------------------
                        ✈ Flight Number: {flight.flight_number}
                        🌍 From: {flight.source_city} → 🏙 To: {flight.destination_city}
                        📅 Travel Day: {self.travelling_date} ({flight.weekday})
                        ⏰ Departure: {flight.start_time} → 🛬 Arrival: {flight.end_time}
                        📏 Distance: {flight.distance_km} km
                        --------------------------------
                        """)


                    