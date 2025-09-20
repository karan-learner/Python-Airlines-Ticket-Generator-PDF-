from DataLayer.Airports import cities

class ManageAirport:
    # Class-level attribute (shared across all instances)
    list_of_cities = cities

    # Private method to check if the city is available in the list of cities 
    @staticmethod
    def __validate_city_name(city_name):
        if city_name in ManageAirport.list_of_cities:
            return True
        else:
            return False

    # Private method to check if user input of source and destination cities are same or not
    @staticmethod
    def __validate_source_destination_name(source_city_name, destination_city_name):
        if source_city_name == destination_city_name:
            return False
        else:
            return True

    # Public method to validate/check the source city name using the private method that checks if the source city
    # is available or not in the cities list
    @staticmethod
    def validate_source(source_city_name):
        return ManageAirport.__validate_city_name(source_city_name)
    
    
    # Public method to validate/check the destination city name using the private method that checks if the destination city
    # is available or not in the cities list
    @staticmethod
    def validate_destination(source_city_name, destination_city_name):
        if not ManageAirport.__validate_source_destination_name(source_city_name, destination_city_name):
            print("❌ Source and destination cities cannot be the same.")
            return False
        
        if not ManageAirport.__validate_city_name(destination_city_name):
            print(f"❌ Destination '{destination_city_name}' is not a valid city.")
            return False
        return True