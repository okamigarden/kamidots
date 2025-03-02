#Patient Class
class Patient:
    def __init__(self, first_name, surname, age, mobile, postcode):
        self.__first_name = first_name
        self.__surname = surname
        self.__age = int(age)
        self.__mobile_num = mobile
        self.__postcode = postcode
        self.__doctor = "None"
        
    def full_name(self):
        return f"Full Name: {self.__first_name()} {self.__surname()}"
    
    def get_doctor(self):
        return f"Doctor: {self.__doctor}"
    
    def link(self, doctor):
        self.__doctor = doctor
        
    def print_symptoms(self):
        