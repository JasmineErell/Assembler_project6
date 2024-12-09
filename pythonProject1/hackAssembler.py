from symbolTable import SymbolTable
from parser import Parser
from hack_code import Code
import os

class Assembler:
    def __init__(self, in_path):

        self.in_path = in_path

    def path_slicing(self, path):
        base, _ = os.path.splitext(path)  # Split the path into base and extension
        return base + ".hack"
    def first_loop(self):
        """
        Runs through each line and creates a symbol table
        """
        parser = Parser(self.in_path)
        table = SymbolTable()
        while parser.hasMoreLines():
            #Iterating each line in the file
            parser.advance()
            instruction_type = parser.instructionType()
            if (instruction_type == 'L_INSTRUCTION'):
                table.addEntry(parser.symbol(), parser.clean_line_pos-1) # Adding the symbol to the table
        return table


    def read_and_write(self, table):
        """
        This function reads an .asm file and uses Parser and Code to create a corresponding .hack file.
        """
        parser = Parser(self.in_path)
        code = Code()
        out_path = self.path_slicing(self.in_path)
        with open(out_path, "w", newline='\n') as f:
            while parser.hasMoreLines():
                parser.advance()  # Move to the next instruction
                instruction_type = parser.instructionType() # Determine the type of the current instruction

                if instruction_type == "A_INSTRUCTION":  # Handle @value
                    symbol = parser.symbol()
                    if symbol.isdigit():
                        binary_instruction = format(int(symbol), '016b')
                        f.write(binary_instruction + "\n")
                    else:
                        if table.contains(symbol):
                            binary_instruction = format((int)(table.getAdress(symbol)), '016b')
                            f.write(binary_instruction + "\n")
                        else:
                            table.addEntry(symbol, table.first_empty_space)
                            binary_instruction = format((int)(table.first_empty_space), '016b')
                            f.write(binary_instruction + "\n")
                            table.first_empty_space += 1



                elif instruction_type == "C_INSTRUCTION":  # Handle dest=comp;jump
                    comp_bits = code.comp(parser.comp())
                    dest_bits = code.dest(parser.dest())
                    jump_bits = code.jump(parser.jump())
                    binary_instruction = "111" + comp_bits + dest_bits + jump_bits
                    f.write(binary_instruction + "\n")







