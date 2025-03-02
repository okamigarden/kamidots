# Doctor Class
class Doctor:
    
    def __init__(self, first_name, surname, speciality):
        self.first_name = first_name
        self.surname = surname
        self.speciality = speciality
    
    def full_name(self):
        return f"Doctor: {self.first_name} {self.surname}"
    
    def get_first_name(self):
        return self.first_name
    
    def set_first_name(self, new_name):
        self.first_name = new_name
    
    def set_surname(self, new_surname):
        self.surname = new_surname
    
    def get_surname(self):
        return self.surname
    
    def get_speciality(self):
        return self.speciality
    
    def set_speciality(self, new_speciality):
        self.speciality = new_speciality
    
    def add_patient(self, patient):
        self.patients = []
        self.patients.append(patient)
    
    def __str__(self):
        return f"{self.full_name():^30}|{self.speciality:^15}"
    
    