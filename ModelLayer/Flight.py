from ModelLayer.Constants import Constants

class Flight:
    
    # this method is a constructor which holds the value inside the objects
    def __init__(self, flight_number, source_city, destination_city, start_time, end_time, distance_km, weekday):
        self.flight_number = flight_number
        self.source_city = source_city
        self.destination_city = destination_city
        self.start_time = start_time
        self.end_time = end_time
        self.distance_km = distance_km
        self.weekday = weekday
        self.fare =  distance_km * Constants.base_fare

    # this method where the string is getting place to object to fetch data from flight_routes
    # Encapsulates object creation logic outside the class.
    def create_flight(flight_data):
        return Flight(flight_data["flight_number"], flight_data["source_city"], flight_data["destination_city"],
                flight_data["start_time"], flight_data["end_time"], flight_data["distance_km"], flight_data["weekday"])

