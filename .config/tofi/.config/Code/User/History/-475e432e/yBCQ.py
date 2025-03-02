# Patient Class
class Patient:
    def __init__(self, first_name, surname, age, mobile, postcode):
        self.__first_name = first_name
        self.__surname = surname
        self.__age = int(age)
        self.__mobile_num = mobile
        self.__postcode = postcode
        self.__doctor = "None"
        self.__symptoms = "None"
        
    def full_name(self):
        return f"{self.__first_name} {self.__surname}"
    
    def get_doctor(self):
        return self.__doctor
    
    def link(self, doctor):
        self.__doctor = doctor
        
    def print_symptoms(self):
        patient_symptoms = []
        self.__symptoms = patient_symptoms
        return self.__symptoms
    
    def get_age(self):
        return self.__age
    
    def get_postcode(self):
        return self.__postcode
    
    def get_mobile_num(self):
        return self.__mobile_num
    
    def __str__(self):
        return f"{self.full_name():^30}|{self.__doctor:^30}|{self.__age:^5}|{self.__mobile_num:^15}|{self.__postcode:^10}"
    