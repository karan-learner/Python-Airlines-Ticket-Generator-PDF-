from datetime import datetime

class HelperExtension:
    
    # Private method is created to convert a date string into a datetime object
    @staticmethod
    def __validate_date_format(date_input):
        try:
            HelperExtension.get_strptime(date_input)
            return True
        except ValueError:
                return False
    
    # converts the user input and changes it to string method
    @staticmethod
    def get_strptime(date_input):
        return datetime.strptime(date_input.strip(), "%d/%m/%Y")

    # Private Method Checks the date input given by the user is a past date or not
    @staticmethod    
    def __validate_date_if_past_date(date_input):
        valid_date = HelperExtension.get_strptime(date_input)
        if valid_date.date() < datetime.today().date():
            return False
        else:
            return True
    
    # Public method if the date format entered is correct or not also validates that past date is entered
    @staticmethod   
    def validate_travelling_date(date_input):
        if not HelperExtension.__validate_date_format(date_input):
            print("Wrong date format is entered.")
            return False
        
        if not HelperExtension.__validate_date_if_past_date(date_input):
            print("Entered past date")
            return False
        return True
    
    # public method used to convert date in day to fetch day from the FlightRoutes
    @staticmethod
    def get_day_from_date(date_input):
        try:
            date_input = HelperExtension.get_strptime(date_input)
            return date_input.strftime("%A")
        except ValueError:
            return None
    
    # this method gets the current time as a timestamp and converts it to a string
    @staticmethod    
    def get_time_stamp():
        return str(datetime.now().timestamp())
        