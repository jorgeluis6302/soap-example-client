from zeep import Client

class PersonService:
    _instance = None

    def greetings_message(self, data: dict):
        return self._instance.service.GreetingsMessage(**data)

    def __init__(self, wsdl):
        self._instance = Client(wsdl=wsdl)


class ArithmeticService:
    _instance = None
    _data: dict = None

    def set_data(self, data: dict):
        self._data = data

    def sum(self):
        return f"Sum Result = {self._instance.service.Sum(**self._data)}"

    def substract(self):
        return f"Substract Result = {self._instance.service.Substract(**self._data)}"

    def div(self):
        return f"Division Result = {self._instance.service.Div(**self._data)}"

    def product(self):
        return f"Product Result: {self._instance.service.Product(**self._data)}"

    def __init__(self, wsdl):
        self._instance = Client(wsdl=wsdl)
