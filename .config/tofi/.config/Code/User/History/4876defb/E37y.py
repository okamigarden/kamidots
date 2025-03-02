class Customer:
    def __init__(self, cID, first_name, second_name, address, balance):
        self.__cID = cID
        self.__first_name = first_name
        self.__second_name = second_name
        self.__address = address # Expects an Address object
        self.__balance = balance
    
    def get_cID(self):
        return self.__cID
        
    
    def set_cID(self, c_id):
        self.__cID = c_id
    
    def get_first_name(self):
        return self.__first_name
        
    
    def set_first_name(self, f_name):
        self.__first_name = f_name
    
    def get_second_name(self):
        return self.__second_name
    
    def set_second_name(self, s_name):
        self.__second_name = s_name
    
    def get_address(self):
        return self.__address
    
    def set_address(self, addObj):
        self.__address = addObj
        
    def get_balance(self):
        return self.__balance
    
    def set_balance(self, value):
        self.__balance = value

    def deposit(self,value):
        self.__balance += value

    def withdraw(self,value):
        self.__balance -= value

    def check_balance(self):
        return self.__balance 

class Address:
    def __init__(self, number, street, town, post_code):
        self.__number = number
        self.__street = street
        self.__town = town
        self.__post_code = post_code
        
    def get_number(self):
        return self.__number
    
    def set_number(self, value):
        self.__number = value

    def get_street(self):
        return self.__street
    
    def set_street(self, street_name):
        self.__street = street_name

    def get_town(self):
        return self.__town

    def set_town(self, town_name):
        self.__town = town_name

    def get_post_code(self):
        return self.__post_code
    
    def set_post_code(self, value):
        self.__post_code = value

    def change_address(self, new_address):
        self.number = new_address.number
        self.street = new_address.street
        self.town = new_address.town
        self.post_code= new_address.post_code

    def __str__(self):
        return f"{self.__number},{self.__street},{self.__town},{self.__post_code}"

def new_customer():

    cid = int(input("Enter customer id number: "))
    f_name= input( "Enter first name: ")
    s_name= input("Enter second name: ")
    address = input("Enter address (number, street, town, postCode): ")
    while len(address.split(',')) != 4:
        address = input( "Please re-enter address (number, street, town, postCode): ")
    number, street, town, post_code = address.split(',')
    address_object_instance = Address(number.strip(), street.strip(), town.strip(), post_code.strip()) # __address attribute has to store a Address Instance (created instance using command)
    
    try:
        balance = float(input( "Enter balance: "))
    except ValueError:
        print("Invalid Input for Balance, setting balance to 0.00")
        balance = 0.0
    
    return Customer(cid, f_name, s_name, address_object_instance, balance)

c = Customer('12A','Anna','Duka',Address(42,'Curzon Street','Birmingham', 'B4 2SU'),888)


def save_cRecords(lst):
    success = False # assume failure initially
    with open(r"/home/fabian/Documents/Univesity/customerList.txt", "w") as records: # with statement makes sure the file is closed properly after writing instead of records.close()
        for customer in lst:
            # Extract Customer Details
            cID = customer.get_cID()
            first_name = customer.get_first_name()
            second_name = customer.get_second_name()
            address = str(customer.get_address())
            balance = customer.get_balance()
            
            # Formatting the text to save
            record = f"{cID}, {first_name}, {second_name}, {address}, {balance}\n"
            # Write the text to file
            records.write(record)
            
            
            success = True # If code reaches here, file write was successful, if not it will return False
    return success

c1 = Customer('12A','Rea','Koci',Address('42','Curzon Street','Birmingham', 'B4 2SU'),888)
c2 = Customer('11A','Liora','Koci',Address('42b','Curzon Street2','Birmingham2', 'B4 2SU'),33)

save_cRecords([c1,c2])

def read_customerRecords(data_file):
    with open(r"/home/fabian/Documents/Univesity/customerList.txt", "r") as cRecords:
        line = cRecords.readline()
        while line != "":
            print(line)
            line = cRecords.readline()


#read_customerRecords("/home/fabian/Documents/Univesity/customerList.txt")

read_customerRecords("lalalalalal.txt")
