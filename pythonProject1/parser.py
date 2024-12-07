from pconst import const

const.A_INSTRUCTION = "A_INSTRUCTION"
const.L_INSTRUCTION = "L_INSTRUCTION"
const.C_INSTRUCTION = "C_INSTRUCTION"

class Parser(object):
    def __init__(self, file_path):
        self.file_path = file_path
        self.file = open(self.file_path)
        self.lts_lines = self.file.readlines()
        self.current_line = None
        self.clean_line_pos = 0
        self.pos = 0

    def line_cleaner(self, string):
        """
        Cleans comments and whitespace from a line
        """
        return string.split("//")[0].strip()

    def hasMoreLines(self):
        # Checks if there are more lines to process
        return self.pos < len(self.lts_lines)

    def advance(self):
        while self.hasMoreLines():
            raw_line = self.lts_lines[self.pos]  # Read the next line
            current_line = self.line_cleaner(raw_line)  # Clean the line
            self.pos +=1
            if current_line:  # Return the first non-empty, cleaned line
                self.clean_line_pos +=1
                self.current_line = current_line
                return
        self.current_line = None  # Set to None if no valid lines are found

    def instructionType(self):
        ### takes a single line and tells us if its an A,C or L instruction according to the rules ###
        raw_line = self.line_cleaner(self.current_line)
        if not raw_line:
            return None
        if (raw_line[0] == '@'):
            return "A_INSTRUCTION"
        if ((raw_line[0] == '(') and (raw_line[-1] == ')')):
            return "L_INSTRUCTION"
        else:
            return "C_INSTRUCTION"

    def symbol(self):
        if (self.instructionType() == const.L_INSTRUCTION):
            return str(self.line_cleaner(self.current_line)[1:-1]) #returns the symbol without ( , ) as a string
        if (self.instructionType() == const.A_INSTRUCTION):
            return str(self.line_cleaner(self.current_line)[1:]) #returns the symbol without @ as a string
        else:
            return None


    def dest(self):
        str = self.line_cleaner(self.current_line)
        if ('=' in str ):
            return str.split('=')[0]
        else:
            return None

    def comp(self):
        str = self.line_cleaner(self.current_line)
        if ('=' in str):
            str = str.split('=')[1]
        if (';' in str):
            str = str.split(';')[0]
        return str


    def jump(self):
        str = self.line_cleaner(self.current_line)
        if ( ';' in str):
            return str.split(';')[1]
        else:
            return None





# Test function defined outside the class
def test_parser():
    # Test file content
    test_lines = [
        "// This is a comment",
        "@2",          # A-instruction
        "(LOOP)",      # L-instruction
        "D=D+1;JLE",   # C-instruction with dest, comp, and jump
        "M=-1"         # C-instruction with dest and comp only
    ]

    # Write the test content to a temporary file
    with open("test.asm", "w") as f:
        f.write("\n".join(test_lines))

    # Initialize parser
    parser = Parser("test.asm")

    # Test line_cleaner and hasMoreLines
    assert parser.hasMoreLines(), "hasMoreLines() failed before advancing"
    parser.advance()  # Skip the comment line

    # Test A-instruction
    # parser.advance()
    assert parser.instructionType() == "A_INSTRUCTION", "instructionType() failed for A-instruction"
    assert parser.symbol() == "2", f"symbol() failed for A-instruction: {parser.symbol()}"

    # Test L-instruction
    parser.advance()
    assert parser.instructionType() == "L_INSTRUCTION", "instructionType() failed for L-instruction"
    assert parser.symbol() == "LOOP", f"symbol() failed for L-instruction: {parser.symbol()}"

    # Test C-instruction with dest, comp, and jump
    parser.advance()
    assert parser.instructionType() == "C_INSTRUCTION", "instructionType() failed for C-instruction"
    assert parser.dest() == "D", f"dest() failed: {parser.dest()}"
    assert parser.comp() == "D+1", f"comp() failed: {parser.comp()}"
    assert parser.jump() == "JLE", f"jump() failed: {parser.jump()}"

    # Test C-instruction with only dest and comp
    parser.advance()
    assert parser.instructionType() == "C_INSTRUCTION", "instructionType() failed for C-instruction"
    assert parser.dest() == "M", f"dest() failed: {parser.dest()}"
    assert parser.comp() == "-1", f"comp() failed: {parser.comp()}"
    assert parser.jump() is None, f"jump() failed: {parser.jump()}"

    # Ensure all lines were processed
    assert not parser.hasMoreLines(), "hasMoreLines() failed after processing all lines"

    print("All parser tests passed.")

# Run the test


# Main block
if __name__ == "__main__":
    test_parser()
