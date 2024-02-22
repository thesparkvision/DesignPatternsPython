class Machine:
    def print(self):
        raise Error("Method Not Implemented")

    def scan(self):
        raise Error("Method Not Implemented")

    def fax(self):
        raise Error("Method Not Implemented")

class MultiFunctionPrinter(Machine):
    def print(self):
        pass

    def scan(self):
        pass

    def fax(self):
        pass

def OldPrinterMachine(Machine):
    def print(self):
        pass

    ## Supports only printing