from DataLayer.FlightRoutes import routes
from ModelLayer.Flight import Flight

class ManageFlightRoute:
        
    # Public method to check if the day, source_airport, destination_airport entered by user is available in the FlightRoutes
    def get_flight_route(self, travelling_day, source_airport, destination_airport):
        flight_list = []
        for flights in routes:
            if (flights["source_city"] == source_airport and
            flights["destination_city"] == destination_airport and 
            flights["weekday"] == travelling_day):
                flight_list.append(Flight.create_flight(flights))
                # print(flights)
        return flight_list

object_1 = ManageFlightRoute()

