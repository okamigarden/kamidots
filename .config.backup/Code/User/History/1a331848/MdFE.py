# Admin Class
from Doctor import Doctor
from Patient import Patient


class Admin:
    def __init__(self, username, password, address = ""):
        self.__username = username
        self.__password = password
        self.__address = address
    
    def view(self, a_list):
        for index, item in enumerate(a_list):
            print(f'{index+1:3}|{item}')
            
    def viewy(self, doctors):
        print("--------- List of Doctors -----------")
        print("ID |      Full Name           |    Speciality")
        for index, doctor in enumerate(doctors, start = 1):
            #call instance method on each object
            print(f"{index:3}|{doctor.get_first_name()} {doctor.get_surname():<30}|{doctor.get_speciality():<20}")
    
    def login(self):
        print("-----Login-----")
        #Get the details of the admin
        typed_username = input('Enter the username: ')
        typed_password = input('Enter the password: ')
        if typed_username == self.__username and typed_password == self.__password:
            print("You have logged in.")
            return True # Login successful
        else:
            return False # Login Incorrect
    
    def find_index(self, index, doctors):          
        if index in range(0,len(doctors)): # check that the doctor id exists
            return True
        else: # if the id is not in the list of doctors
            return False
    
    
    def get_doctor_details(self):
        """
        Get the details needed to add a doctor
        Returns:
            first name, surname and ...
                            ... the speciality of the doctor in that order.
        """
        return f"{print(Doctor.get_first_name())}, {print(Doctor.get_surname())}, {print(Doctor.get_speciality())}"
        pass

    def doctor_management(self, doctors):
        """
        A method that deals with registering, viewing, updating, deleting doctors
        Args:
            doctors (list<Doctor>): the list of all the doctors names
        """

        print("-----Doctor Management-----")
        # menu
        print('Choose the operation:')
        print(' 1 - Register')
        print(' 2 - View')
        print(' 3 - Update')
        print(' 4 - Delete')
        
        op = input("Enter Choice > ")
        
        # Register
        if op == "1":
            print("-----Register-----")
            
            # get the doctor details
            print('Enter the doctor\'s details:')
            typed_name = input("Enter the first name > ")
            typed_surname = input("Enter the surname > ")
            typed_speciality = input("Enter the speciality > ")
            new_doctor = Doctor(typed_name, typed_surname, typed_speciality)
            
            # check if the name is already registered
            name_exists = False
            for doctor in doctors:
                if typed_name == doctor.get_first_name() and typed_surname == doctor.get_surname():
                    print('Name already exists.')
                    name_exists = True
                    break
            if not name_exists:
                print("Doctor Registered.")
                

        # View
        elif op == "2":
            print("-----List of Doctors-----")
            header = "{:<10}|{:<40}|{:<20}".format("ID", "Full Name", "Specialty")
            for idx, doctor in enumerate(doctors, start=1):
                row = "{:<10}| {:<40}| {:<20}".format(
                idx, 
                f"{print(doctor.get_first_name())} {print(doctor.get_surname())}", 
                doctor.get_speciality()
            )
            
            # DISPLAYING TABLE
            print(header)
            print("-" * len(header))
            print(row)
        
        # Update
        elif op == '3':
            while True:
                print("-----Update Doctor`s Details-----")
                print('ID |          Full name           |  Speciality')
                self.view(doctors)
                try:
                    index = int(input('Enter the ID of the doctor: ')) - 1
                    doctor_index=self.find_index(index,doctors)
                    if doctor_index != False:
                        break
                    else:
                        print("Doctor not found")
                        # doctor_index is the ID minus one (-1)
                except ValueError: # the entered id could not be changed into an int
                    print("The ID entered is incorrect")

            # menu
            print("Choose the field to be updated:")
            print("1. First name")
            print("2. Surname")
            print("3. Speciality")
            op = int(input("Input > ")) # make the user input lowercase

            if op == 1:
                new_first_name = input("Enter new first name > ")
                Doctor.set_first_name(self, new_first_name)
                print(f"First name has been set to {Doctor.get_first_name()}")
            elif op == 2:
                new_surname = input("Enter new surname > ")
                Doctor.set_surname(self, new_surname)
                print(f"Surname has been set to {Doctor.get_surname()}")
            elif op == 3:
                new_speciality = input("Enter new Speciality > ")
                Doctor.set_speciality(self, new_speciality)
                print(f"Speciality has been set to {Doctor.get_speciality()}")
            else:
                print("Invalid Choice")

        # Delete
        elif op == '4':
            print("-----Delete Doctor-----")
            print('ID |          Full Name           |  Speciality')
            self.view(doctors)

            while True:
                try:
                    doctor_index = int(input("Enter the ID of the doctor to be deleted > ")) - 1
                    
                    if 0 <= doctor_index < len(doctors):
                        removed_doctor = doctors.pop(doctor_index)
                        print(f"Doctor {removed_doctor.get_first_name()} {removed_doctor.get_surname()} has been deleted.")
                        break
                    else:
                        print("The ID entered is incorrect")
                except ValueError:
                    print("Invalid Input. Please check spelling (Enter a Numeric Value)")


    def view_patient(self, patients):
        """
        print a list of patients
        Args:
            patients (list<Patients>): list of all the active patients
        """
        
        print("-----View Patients-----")
        
        header = "{:<5} | {:<30} | {:<30} | {:<3} | {:<15} | {:<10}".format(
        "ID", "Full Name", "Doctor's Full Name", "Age", "Mobile", "Postcode")
        
        for idx, patient in enumerate(patients, start=1):
            row = "{:<5} | {:<30} | {:<30} | {:<3} | {:<15} | {:<10}".format(
                idx,
                patient.get_full_name(),
                patient.get_doctor().full_name(), 
                patient.get_age(),
                patient.get_mobile(),
                patient.get_postcode(),
            )
        # DISPLAY FORMATTED TABLE
        print(header)
        print("-" * len(header))
        print(row)
        

    def assign_doctor_to_patient(self, patients, doctors):
        """
        Allow the admin to assign a doctor to a patient
        Args:
            patients (list<Patients>): the list of all the active patients
            doctors (list<Doctor>): the list of all the doctors
        """
        print("-----Assign-----")
        print("-----Patients-----")

        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(patients)
        
        patient_index = input('Please enter the patient ID: ')

        try:
            # patient_index is the patient ID mines one (-1)
            patient_index = int(patient_index) -1

            # check if the id is not in the list of patients
            if patient_index not in range(len(patients)):
                print('The ID entered was not found.')
                return # stop the procedure if the patient ID is invalid 

        except ValueError: # the entered id could not be changed into an int
            print('The ID entered is incorrect, check spelling!')
            return # stop the procedures

        print("-----Doctors Select-----")
        print('Select the doctor that fits these symptoms:')
        patients[patient_index].print_symptoms() # print the patient symptoms

        print('--------------------------------------------------')
        print('ID |          Full Name           |  Speciality   ')
        self.view(doctors)
        doctor_index = input('Please enter the doctor ID: ')

        try:
            # doctor_index is the patient ID mines one (-1)
            doctor_index = int(doctor_index) -1

            # check if the id is in the list of doctors
            if self.find_index(doctor_index,doctors) != False:
                # Link the patient to the doctor and the doctor to the patient
                doctor = doctors[doctor_index]
                patient = patients[patient_index]
                
                patient.link(doctor)
                print('The patient is now assigned to the doctor.')
            # if the id is not in the list of doctors
            else:
                print('The ID entered for the doctor was not found.')
        except ValueError: # the entered id could not be changed into an in
            print("The ID entered is incorrect")


    def discharge(self, patients, discharge_patients):
        """
        Allow the admin to discharge a patient when treatment is done
        Args:
            patients (list<Patients>): the list of all the active patients
            discharge_patients (list<Patients>): the list of all the non-active patients
        """
        print("-----Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(patients)
        discharge_y_n = input("Do you want to discharge a patient? (Y/N)")
        
        if discharge_y_n == "Y" or discharge_y_n == "y":
            print("-----Discharge Patient-----")
            try:
                patient_index = int(input("Please enter the patient ID: ")) -1
                
                if patient_index not in range(len(patients)):
                    print("The ID entered was not found")
                    return
                
                # Get selected patient
                patient_to_discharge = patients[patient_index]
                
                #Confirm Discharge
                confirm = input(f"Are you sure you want to discharge {patient_to_discharge.full_name()} (Y/N)")
                if confirm == "Y" or confirm == "y":
                    discharge_patients.append(patient_to_discharge)
                    
                    # Remove patient from active patient list
                    patients.pop(patient_index)
                    
                    print(f"{patient_to_discharge.full_name()} has been discharged successfully.")
                else:
                    print("Discharge Cancelled")
            
            except ValueError:
                print("The ID entered is incorrect")

    def view_discharge(self, discharged_patients):
        """
        Prints the list of all discharged patients
        Args:
            discharge_patients (list<Patients>): the list of all the non-active patients
        """
        
        if not discharged_patients:
            print("No patients have been discharged yet")
            return
        
        print("-----Discharged Patients-----")
        
        header = "{:<5} | {:<30} | {:<30} | {:<5} | {:<15} | {:<10}".format(
        "ID", "Full Name", "Doctor's Full Name", "Age", "Mobile", "Postcode")
        
        # DISPLAY FORMATTED TABLE
        print(header)
        print("-" * len(header))
        # ROWS CODE
        for idx, patient in enumerate(discharged_patients, start=1):
            row = "{:<5} | {:<30} | {:<30} | {:<5} | {:<15} | {:<10}".format(
                idx, 
                patient.full_name(), 
                patient.get_doctor().full_name(), 
                patient.get_age(), 
                patient.get_mobile(), 
                patient.get_postcode())
            
            print(row)

    def update_details(self):
        """
        Allows the user to update and change username, password and address
        """
        while True:
            print('Choose the field to be updated:')
            print('1. Username')
            print('2. Password')
            print('3. Address')
            op = int(input('Input: '))

            if op == 1:
                print(f"Current Username: {self.__username}")
                admin_new_user = input("Update Username > ")
                self.__username = admin_new_user
                print(f"Username has been changed to {self.__username}")
                break

            elif op == 2:
                password = input('Enter the new password: ')
                # validate the password
                if password == input('Enter the new password again: '):
                    self.__password = password
                print(f"Password has been changed to: {self.__password}")
                break

            elif op == 3:
                print(f"Current Address: {self.__address}")
                admin_new_address = input("Update Address > ")
                self.__address = admin_new_address
                print(f"Address has been changed to {self.__address}")
                break

            else:
                print("Incorrect Menu choice. Please try again.")
                
