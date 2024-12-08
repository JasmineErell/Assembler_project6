import sys
from hackAssembler import Assembler

def main():
    input_path = sys.argv[1]
    assembler = Assembler(input_path)
    table = assembler.first_loop()
    assembler.read_and_write(table)
    print("Success! The hack file is in the entered input path")

if __name__ == '__main__':
    main()