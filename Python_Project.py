
from BusinessLayer.ManageTicketBooking import ManageTicketBooking
from BusinessLayer.ManagePassenger import ManagePassenger
from BusinessLayer.ManageFlightRoute import ManageFlightRoute 
from BusinessLayer.ManageTicketGenerator import ManageTicketGenerator
from BusinessLayer.HelperExtension import HelperExtension
from ModelLayer.Constants import Constants

# Here object flight holds the class Flights
ticket_booking = ManageTicketBooking() 

# collect and validate source_airport input
ticket_booking.get_and_validate_source_airport()

# collect and validate destination_airport input
ticket_booking.get_and_validate_destination_airport()

# collect and validate date input
ticket_booking.get_and_validate_travelling_date()

# class is assigned to an object
manage_flight_route = ManageFlightRoute()

# Get flight routes available for that day
available_flights = manage_flight_route.get_flight_route(ticket_booking.travelling_day,
                                    ticket_booking.source_city, 
                                    ticket_booking.destination_city)

# Show flight routes to user
print(f"\n---List of Flights available on {ticket_booking.travelling_date}---")
ticket_booking.print_flight_details(available_flights)
ticket_booking.book_flight(available_flights)

# Since the method is a staticmethod we are calling it directly without object initialization
# Collects passenger like name age and validates it
manage_passenger = ManagePassenger()
manage_passenger.collect_passenger_data()

# booking confirmed message
print("\n---The booking has been confirmed for the mentioned flight details---")
ticket_booking.confirmed_flight_booked(available_flights, len(manage_passenger.passenger_list))

# Show the booked ticket to user
time_stamp = HelperExtension.get_time_stamp()

# this class and method is used to generate the ticket in pdf format and for the selected flight
ManageTicketGenerator.generate_ticket_pdf(ticket_booking.selected_flight.__dict__,
                                          manage_passenger.passenger_list, 
                                          time_stamp + Constants.file_name)


