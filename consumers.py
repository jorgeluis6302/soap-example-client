# services
from services import PersonService, ArithmeticService

def person_service():
    print("***"*10, "Person Service", "***"*10)
    wsdl = "http://localhost:5075/PersonService.asmx"
    service = PersonService(wsdl=wsdl)
    _id = int(input("Id: "))
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    data = {
        "Id": _id,
        "FirstName": first_name,
        "LastName": last_name
    }
    print(service.greetings_message(data))


def arithmetic_service():
    print("***"*10, "Arithmetic Service", "***"*10)
    wsdl = "http://localhost:5075/ArithmeticService.asmx"
    service = ArithmeticService(wsdl=wsdl)
    a = float(input("Num a: "))
    b = float(input("Num b: "))
    data = {
        "a": a,
        "b": b
    }
    service.set_data(data)
    print(service.sum())
    print(service.substract())
    print(service.product())
    print(service.div())