class Printer:
    @abstractmethod
    def print(self):
        pass

class Scanner:
    @abstractmethod
    def scan(self):
        pass

class Faxer:
    @abstractmethod
    def fax(self):
        pass

class MultiFunctionPrinter(Printer, Scanner, Faxer):
    def print(self):
        pass

    def scan(self):
        pass

    def fax(self):
        pass

def MultiFunctionMachine(Printer, Scanner):
    @abstractmethod
    def print(self):
        pass

    @abstractmethod
    def scan(self):
        pass

def PhotoCopier(MultiFunctionMachine):
    def print(self):
        pass

    def scan(self):
        pass

def OldPrinterMachine(Printer):
    def print(self):
        pass