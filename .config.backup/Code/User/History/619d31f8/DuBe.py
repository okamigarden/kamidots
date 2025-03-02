# Doctor Class
class Doctor:
    
    def __init__(self, first_name, surname, speciality):
        self.__first_name = first_name
        self.__surname = surname
        self.__speciality = speciality
        self.__patient = "None"
    
    def full_name(self):
        return f"Doctor: {self.__first_name()} {self.__surname()}"
    
    def get_first_name(self):
        return self.__first_name()
    
    def set_first_name(self, new_name):
        self.__first_name = new_name
    
    def set_surname(self, new_surname):
        self.__surname = new_surname
    
    def get_speciality(self):
        return f"Speciality: {self.__speciality}"
    
    def set_speciality(self, new_speciality):
        self.__speciality = new_speciality
    
    def add_patient(self, patient):
        self.patients = []
        self.patients.append(patient)
    
    def __str__(self):
        return f"{self.full_name():^30}|{self.__speciality:^15}"
    
    