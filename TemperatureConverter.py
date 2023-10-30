class TC:
    def __init__(self):
        
        self.input = ""
        self.outputType = ""

    def converter(self, input):
        
        inputType = input[-1]
        degree = int(input[:-1])
        
        if inputType == 'C' or inputType == 'c':
            self.outputType = "Fahrenheit"
            return(int(round((9 * degree) / 5 + 32)))
            
        elif inputType == 'F' or inputType == 'f':
            self.outputType = "Celsius"
            return(int(round((degree - 32) * 5 / 9)))
            
        else:
            print("Input in Correct Method: (Example - 45C, 105F)")
            quit()
            
    def start(self):
        
        inputTemp = input("Enter the Temperature to Convert (Example - 45C, 105F): ")
        outputTemp = self.converter(inputTemp)    
        print("The temperature in", self.outputType, "is", outputTemp, "degrees.")

if __name__ == "__main__":
    Converter = TC()
    Converter.start()