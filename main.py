from modules import health
from modules import input_reader 

def main():
    userInput = input(": ")
    compiledInput = input_reader.reader.decompileText(userInput)
    input_reader.reader.executeInput(compiledInput)
    main()
main()