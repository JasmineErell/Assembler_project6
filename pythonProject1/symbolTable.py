class SymbolTable:
    def __init__(self):
        self.table = {
            "R0" : 0,
            "R1" : 1,
            "R2" : 2,
            "R3" : 3,
            "R4" : 4,
            "R5" : 5,
            "R6" : 6,
            "R7" : 7,
            "R8" : 8,
            "R9" : 9,
            "R10" : 10,
            "R11" : 11,
            "R12" : 12,
            "R13" : 13,
            "R14" : 14,
            "SCREEN": 16384,
            "KBD" : 24576,
            "SP" : 0,
            "LCL" : 1,
            "ARG" : 2,
            "THIS" : 3,
            "THAT" :4
        }
        self.first_empty_space = 15

    def addEntry(self, str, address):
        """
       Adding a symbol and its address (string) to the table
        """
        self.table[str] = address

    def contains(self, symbol):
        """
        Returns true if the symbol is already in the table, false if not
        """
        return symbol in self.table

    def getAdress(self, symbol):
        if(self.contains(symbol)):
            return int(self.table[symbol])
        else:
            return -1

    def print_table(self):
        print(self.table)


def test_symbol_table():
    # Create an instance of the SymbolTable
    symbol_table = SymbolTable()
    print(symbol_table.contains("YAS"))
    symbol_table.print_table()

if __name__ == "__main__":
    test_symbol_table()

