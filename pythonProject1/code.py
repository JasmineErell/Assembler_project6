class Code:
    def __init__(self):
        self.dest_table = {
            None: "000",
            "M": "001",
            "D": "010",
            "MD": "011",
            "A": "100",
            "AM": "101",
            "AD": "110",
            "AMD": "111"
        }

        self.jump_table = {
            None: "000",
            "JGT": "001",
            "JEQ": "010",
            "JGE": "011",
            "JLT": "100",
            "JNE": "101",
            "JLE": "110",
            "JMP": "111"
        }

        self.comp_table = {
            "0": "101010",
            "1": "111111",
            "-1": "111010",
            "D": "001100",
            "A": "110000",
            "!D": "001101",
            "!A": "110001",
            "-D": "001111",
            "-A": "110011",
            "D+1": "011111",
            "A+1": "110111",
            "D-1": "001110",
            "A-1": "110010",
            "D+A": "000010",
            "D-A": "010011",
            "A-D": "000111",
            "D&A": "000000",
            "D|A": "010101",

            # When a=1 (operations using M register)
            "M": "110000",
            "!M": "110001",
            "-M": "110011",
            "M+1": "110111",
            "M-1": "110010",
            "D+M": "000010",
            "D-M": "010011",
            "M-D": "000111",
            "D&M": "000000",
            "D|M": "010101"
        }

    def dest(self, insruction):
        return self.dest_table[insruction]

    def jump(self, instruction):
        return self.jump_table[instruction]

    def comp(self, instruction):
        if ('M' in instruction):
            a=1
        else:
            a=0
        return  str(a) + self.comp_table[instruction]

def test_code_class():
    code = Code()

    # Testing dest() method
    assert code.dest("M") == "001", "dest('M') failed"
    assert code.dest("D") == "010", "dest('D') failed"
    assert code.dest("MD") == "011", "dest('MD') failed"
    assert code.dest("A") == "100", "dest('A') failed"
    assert code.dest("AM") == "101", "dest('AM') failed"
    assert code.dest("AD") == "110", "dest('AD') failed"
    assert code.dest("AMD") == "111", "dest('AMD') failed"
    assert code.dest(None) == "000", "dest(None) failed"

    # Testing comp() method
    assert code.comp("A+1") == "0110111", "comp('0') failed"
    assert code.comp("D&M") == "1000000", "comp('D+M') failed"

    # Testing jump() method
    assert code.jump("JGT") == "001", "jump('JGT') failed"
    assert code.jump("JEQ") == "010", "jump('JEQ') failed"
    assert code.jump("JGE") == "011", "jump('JGE') failed"
    assert code.jump("JLT") == "100", "jump('JLT') failed"
    assert code.jump("JNE") == "101", "jump('JNE') failed"
    assert code.jump("JLE") == "110", "jump('JLE') failed"
    assert code.jump("JMP") == "111", "jump('JMP') failed"
    assert code.jump(None) == "000", "jump(None) failed"

    print("All passed!")

# Run the test
test_code_class()