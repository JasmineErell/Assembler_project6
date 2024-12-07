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

    # Test initialization of default symbols
    assert symbol_table.getAdress("R0") == 0, "R0 should map to 0"
    assert symbol_table.getAdress("SCREEN") == 16384, "SCREEN should map to 16384"
    assert symbol_table.getAdress("KBD") == 24576, "KBD should map to 24576"
    assert symbol_table.getAdress("NON_EXISTENT") == -1, "NON_EXISTENT should return -1"

    # Test adding a new entry
    symbol_table.addEntry("TEST", 100)
    assert symbol_table.getAdress("TEST") == 100, "TEST should map to 100"

    # Test contains method
    assert symbol_table.contains("R0") is True, "R0 should exist in the table"
    assert symbol_table.contains("TEST") is True, "TEST should exist in the table"
    assert symbol_table.contains("NON_EXISTENT") is False, "NON_EXISTENT should not exist in the table"

    # Test updating an existing symbol
    symbol_table.addEntry("R0", 500)
    assert symbol_table.getAdress("R0") == 500, "R0 should be updated to 500"

    symbol_table.print_table()

if __name__ == "__main__":
    test_symbol_table()

