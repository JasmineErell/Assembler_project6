from symbolTable import SymbolTable
from parser import Parser
from code import Code

class HackAssembler:
    def __init__(self, in_path, out_path):
        self.in_path = in_path
        self.out_path = out_path

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



    def read_and_write(self):
        """
        This function reads an .asm file and uses Parser and Code to create a corresponding .hack file.
        """
        parser = Parser(self.in_path)
        table = SymbolTable()
        code = Code()

        with open(self.out_path, "w") as f:
            while parser.hasMoreLines():
                parser.advance()  # Move to the next instruction
                instruction_type = parser.instructionType() # Determine the type of the current instruction

                if instruction_type == "A_INSTRUCTION":  # Handle @value
                    symbol = parser.symbol()
                    if symbol.isdigit():
                        # Convert the number to a 16-bit binary value
                        binary_instruction = format(int(symbol), '016b')
                    else:
                        if (not table.contains(symbol)):
                            table.addEntry(symbol, table.first_empty_space) ## if the symbol does not exist - add it in the free space
                            table.first_empty_space += 1


                # elif instruction_type == "C_INSTRUCTION":  # Handle dest=comp;jump
                    # Translate the C-instruction components
                    # comp_bits = code.comp(parser.comp())
                    # dest_bits = code.dest(parser.dest())
                    # jump_bits = code.jump(parser.jump())
                    # Combine into the final 16-bit instruction
                    # binary_instruction = "111" + comp_bits + dest_bits + jump_bits

                # else:
                #     continue  # Ignore labels or other lines

                # Write the translated binary instruction to the output file
                # f.write(binary_instruction + "\n")


assembler = HackAssembler("C:/secondYear/Nand2Tetris/MaxL.asm", "C:/secondYear/Nand2Tetris/res.txt")


# Run the read_and_write function
#assembler.read_and_write()

assembler.read_and_write()


