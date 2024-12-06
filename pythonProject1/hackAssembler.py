from parser import Parser # Ensure your Parser class is implemented correctly
from code import Code  # Ensure your Code class is implemented correctly
class HackAssembler:
    def __init__(self, in_path, out_path):
        self.in_path = in_path
        self.out_path = out_path

    def read_and_write(self):
        """
        This function reads an .asm file and uses Parser and Code to create a corresponding .hack file.
        """
        parser = Parser(self.in_path)  # Initialize the Parser with the input file path
        code = Code()  # Initialize the Code class to translate instructions

        with open(self.out_path, "w") as f:
            while parser.hasMoreLines():
                parser.advance()  # Move to the next instruction

                # Determine the type of the current instruction
                instruction_type = parser.instructionType()

                if instruction_type == "A_INSTRUCTION":  # Handle @value
                    # Get the symbol or number from the instruction
                    symbol = parser.symbol()
                    if symbol.isdigit():
                        # Convert the number to a 16-bit binary value
                        binary_instruction = format(int(symbol), '016b')
                    else:
                        # If it's a symbol (e.g., variable/label), handle symbols here
                        raise ValueError(f"Symbol handling not implemented for '{symbol}'")

                elif instruction_type == "C_INSTRUCTION":  # Handle dest=comp;jump
                    # Translate the C-instruction components
                    comp_bits = code.comp(parser.comp())
                    dest_bits = code.dest(parser.dest())
                    jump_bits = code.jump(parser.jump())
                    # Combine into the final 16-bit instruction
                    binary_instruction = "111" + comp_bits + dest_bits + jump_bits

                else:
                    continue  # Ignore labels or other lines

                # Write the translated binary instruction to the output file
                f.write(binary_instruction + "\n")


assembler = HackAssembler("C:/secondYear/Nand2Tetris/MaxL.asm", "C:/secondYear/Nand2Tetris/res.txt")

# Run the read_and_write function
assembler.read_and_write()

print(f"Assembly completed! The .hack file is saved at {"C:/secondYear/Nand2Tetris/res.txt"}")