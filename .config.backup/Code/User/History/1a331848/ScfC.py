# Admin Class
from Doctor import Doctor



class Admin:
    def __init__(self, username, password, address = ""):
        self.__username = username
        self.__password = password
        self.__address = address
    
    def view(self, a_list):
        for index, item in enumerate(a_list):
            print(f'{index+1:3}|{item}')
    
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
    
    
    def get_doctor_details(self) :
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
                if typed_name == Doctor.get_first_name() and typed_surname == Doctor.get_surname():
                    print('Name already exists.')
                    name_exists = True
                    break
                else:
                    print("Doctor Registered.")
                    doctors.append(new_doctor)

        # View
        elif op == "2":
            print("-----List of Doctors-----")
            header = "{:<10}|{:<40}|{:<20}".format("ID", "Full Name", "Specialty")
            for idx, doctor in enumerate(doctors, start=1):
                row = "{:<10}| {:<40}| {:<20}".format(
                idx, 
                f"{print(Doctor.get_first_name())} {print(Doctor.get_surname())}", 
                Doctor.get_speciality()
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
                    if doctor_index!=False:
                
                        break
                        
                    else:
                        print("Doctor not found")

                    
                        # doctor_index is the ID mines one (-1)
                        

                except ValueError: # the entered id could not be changed into an int
                    print("The ID entered is incorrect")

            # menu
            print("Choose the field to be updated:")
            print("1. First name")
            print("2. Surname")
            print("3. Speciality")
            op = int(input("Input > ")) # make the user input lowercase

            #ToDo8
            pass

        # Delete
        elif op == '4':
            print("-----Delete Doctor-----")
            print('ID |          Full Name           |  Speciality')
            self.view(doctors)

            doctor_index = input('Enter the ID of the doctor to be deleted: ')
            #ToDo9
            pass

           
            print('The id entered is incorrect')

        # if the id is not in the list of patients
        else:
            print('Invalid operation choosen. Check your spelling!')


    def view_patient(self, patients):
        """
        print a list of patients
        Args:
            patients (list<Patients>): list of all the active patients
        """
        print("-----View Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        #ToDo10
        pass

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
                print('The id entered was not found.')
                return # stop the procedures

        except ValueError: # the entered id could not be changed into an int
            print('The id entered is incorrect')
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
            if self.find_index(doctor_index,doctors)!=False:
                    
                # link the patients to the doctor and vice versa
                #ToDo11
                pass
                
                print('The patient is now assign to the doctor.')

            # if the id is not in the list of doctors
            else:
                print('The id entered was not found.')

        except ValueError: # the entered id could not be changed into an in
            print('The id entered is incorrect')


    def discharge(self, patients, discharge_patients):
        """
        Allow the admin to discharge a patient when treatment is done
        Args:
            patients (list<Patients>): the list of all the active patients
            discharge_patients (list<Patients>): the list of all the non-active patients
        """
        print("-----Discharge Patient-----")

        patient_index = input('Please enter the patient ID: ')

        #ToDo12
        pass

    def view_discharge(self, discharged_patients):
        """
        Prints the list of all discharged patients
        Args:
            discharge_patients (list<Patients>): the list of all the non-active patients
        """

        print("-----Discharged Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        #ToDo13
        pass

    def update_details(self):
        """
        Allows the user to update and change username, password and address
        """

        print('Choose the field to be updated:')
        print(' 1 Username')
        print(' 2 Password')
        print(' 3 Address')
        op = int(input('Input: '))

        if op == 1:
            #ToDo14
            pass

        elif op == 2:
            password = input('Enter the new password: ')
            # validate the password
            if password == input('Enter the new password again: '):
                self.__password = password

        elif op == 3:
            #ToDo15
            pass

        else:
            #ToDo16
            pass
