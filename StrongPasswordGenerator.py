import random
from tkinter import *
from tkinter import font
from tkinter import messagebox

class SPG:
    
    def __init__(self):
        
        self.charTypesDict = {
            "lowercase" : "abcdefghijklmnopqrstuvwxyz",
            "uppercase" : "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
            "numbers" : "0123456789",
            "symbols" : "!\"#$%&'()*+,-./\\:;<=>?@[]^_`{|}~",
        }
        self.secret = ""

    def generate(self, passLength, optionsList):
        
        # print(passLength, optionsList)
        selectedCharTypesStr = ""
        passwd = ""
        addedCharTypes = ""
        
        #Using string addedCharTypes = "0123" to check whether charset already included or not and adding the Charsets as string to a variable selectedCharTypesStr
        for option in optionsList:
            if str(option) not in addedCharTypes:
                key, value = (list(self.charTypesDict.items())[option])
                selectedCharTypesStr += value
                addedCharTypes += str(option)
        # print(selectedCharTypesStr)
        
        #Generating the Password using Random   
        for i in range(passLength):
            passwd += selectedCharTypesStr[random.SystemRandom().randint(0, len(selectedCharTypesStr)-1)];
        return passwd
            
    def cli(self):
        
        settingsIntList = []
        try:
            passLength = int(input("Enter the Length of Password to Generate (Default is 8): ") or "8")
        except:
            passLength = int(8)
            
        print("-" * 30)
        print("Enter the Options in comma seperated Format: (Example - 1,2,3)")
        print("1. Lowercase Letters \n2. Uppercase Letters \n3. Numbers \n4. Symbols")
        settingsOptions = input("Please Enter an Option (Default is 1(Lowercase)): ") or "1"
        print("=" * 30)
        
        #Split the input string into a list
        settingsStringList = settingsOptions.split(',')
        #Convert the values to integers
        for val in settingsStringList: 
            if val == '1' or val == '2' or val == '3' or val == '4' : 
                settingsIntList.append(int(val)-1)
         
        #Generating and Displaying the Password
        PasswdGenerated = self.generate(passLength, settingsIntList)
        print("Your Strong Password Generated:")
        print(PasswdGenerated)
        
    def gui(self):
        
        #Calling Tkinter Module to an Obj
        screen = Tk()
        screen.title("Strong Password Generator")  
        
        # Create a bold font
        HeadingFont = font.Font(family="Helvetica", size=16, weight="bold")     
        MainFont = font.Font(family="Helvetica", size=12, weight="bold")    
        EntryFont = font.Font(family="Helvetica", size=10)   

        # Background colour of the window 
        screen.configure(background="#6A6C6E")
        
        #Frames Defining
        MainFrame = LabelFrame(screen, padx=0, pady=0, borderwidth=5, relief='groove')
        MainFrame.pack(padx=10, pady=10)
        
        TitleFrame = LabelFrame(MainFrame, padx=50, pady=10, bg="#BFC3C6", borderwidth=1.20, relief='solid')
        TitleFrame.grid(row=0, column=0, sticky="nsew")
        MainFrame.grid_rowconfigure(0, weight=1)
        MainFrame.grid_columnconfigure(0, weight=1)
        
        GenFrame = LabelFrame(MainFrame, padx=50, pady=10, relief='groove')
        GenFrame.grid(row=1, column=0, sticky="nsew")
        MainFrame.grid_rowconfigure(1, weight=1)
        MainFrame.grid_columnconfigure(0, weight=1)
        
        OptionsFrame = LabelFrame(MainFrame, bg="#BFC3C6", borderwidth=2, relief='ridge')
        OptionsFrame.grid(row=2, column=0, sticky="nsew")
        MainFrame.grid_rowconfigure(2, weight=1)
        MainFrame.grid_columnconfigure(0, weight=1)
        
        OptionsFrame1 = LabelFrame(OptionsFrame, padx=30, pady=10, borderwidth=2, relief='ridge')
        OptionsFrame1.grid(row=0, column=0, sticky="nsew")
        OptionsFrame.grid_rowconfigure(0, weight=1)
        OptionsFrame.grid_columnconfigure(0, weight=1)

        OptionsFrame2 = LabelFrame(OptionsFrame, padx=10, pady=10, borderwidth=2, relief='ridge')
        OptionsFrame2.grid(row=0, column=1, sticky="nsew")
        OptionsFrame.grid_rowconfigure(0, weight=1)
        OptionsFrame.grid_columnconfigure(1, weight=1)
                
        #Title Frame
        Label(TitleFrame, text="Strong Password Generator", font=HeadingFont, bg="#BFC3C6", width=35).pack()

        #GenFrame
        GenLabel = Label(GenFrame, text="Instantly Create a Secure, Large, and Random Password", font=MainFont)
        GenLabel.grid(row=0, column=0, sticky="nsew", columnspan=2)
        GenFrame.grid_rowconfigure(0, weight=1)
        GenFrame.grid_columnconfigure(0, weight=1)
        
        self.OutputEntry = Entry(GenFrame, width=25, borderwidth=3, font=EntryFont)
        self.OutputEntry.grid(row=1, column=0, sticky="nsew", columnspan=2)
        GenFrame.grid_rowconfigure(1, weight=1)
        GenFrame.grid_columnconfigure(0, weight=1)
        
        GenerateButton = Button(GenFrame, text="Generate", bg="#BFC3C9", activebackground="#D5D9DC", font=MainFont, fg="blue", command = self.generateGUI)
        GenerateButton.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)
        GenFrame.grid_rowconfigure(2, weight=1)
        GenFrame.grid_columnconfigure(0, weight=1)
        
        CopyButton = Button(GenFrame, text="Copy", bg="#BFC3C9", font=MainFont, fg="blue", activebackground="#D5D9DC", command=self.copyPasswd)
        CopyButton.grid(row=2, column=1, sticky="nsew", padx=5, pady=5)
        GenFrame.grid_rowconfigure(2, weight=1)
        GenFrame.grid_columnconfigure(1, weight=1)

        #OptionsFrame1
        self.LengthNum = IntVar()
        OF1Label = Label(OptionsFrame1, text="Password Length\n(Default is 8)", font=MainFont)
        OF1Label.grid(row=0, column=0, sticky="nsew", columnspan=2)
        OptionsFrame1.grid_rowconfigure(0, weight=1)
        OptionsFrame1.grid_columnconfigure(0, weight=1)
        
        self.Length = Entry(OptionsFrame1, borderwidth=3, textvariable=self.LengthNum, justify='center')
        self.Length.grid(row=1, column=0, sticky="nsew", columnspan=2)
        OptionsFrame1.grid_rowconfigure(1, weight=1)
        OptionsFrame1.grid_columnconfigure(0, weight=1)
                
        Decrease = Button(OptionsFrame1, text="Decrease", font=MainFont, bg="#BFC3C9", activebackground="#D5D9DC", fg="blue", command=lambda: self.lengthIncDec(2))
        Decrease.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)
        OptionsFrame1.grid_rowconfigure(2, weight=1)
        OptionsFrame1.grid_columnconfigure(0, weight=1)
        
        Increase = Button(OptionsFrame1, text="Increase", font=MainFont, bg="#BFC3C9", activebackground="#D5D9DC", fg="blue", command=lambda: self.lengthIncDec(1))
        Increase.grid(row=2, column=1, sticky="nsew", padx=5, pady=5)
        OptionsFrame1.grid_rowconfigure(2, weight=1)
        OptionsFrame1.grid_columnconfigure(1, weight=1)

        #OptionsFrame2 
        self.opt1 = IntVar()
        self.opt2 = IntVar()
        self.opt3 = IntVar()
        self.opt4 = IntVar()

        OF1Labe2 = Label(OptionsFrame2, text="   Characters to Include in Password\n(Default is Lowercase)", font=MainFont)
        OF1Labe2.grid(row=0, column=0, sticky="nsew", columnspan=2)
        OptionsFrame1.grid_rowconfigure(0, weight=1)
        OptionsFrame1.grid_columnconfigure(0, weight=1)
        
        check1 = Checkbutton(OptionsFrame2, text="Lowercase", variable=self.opt1, onvalue="1", offvalue="0")
        check1.select()
        check1.grid(row=1, column=0, sticky="nsew")
        OptionsFrame1.grid_rowconfigure(1, weight=1)
        OptionsFrame1.grid_columnconfigure(0, weight=1)       

        check2 = Checkbutton(OptionsFrame2, text="Uppercase", variable=self.opt2, onvalue="2", offvalue="0")
        check2.deselect()
        check2.grid(row=1, column=1, sticky="nsew")
        OptionsFrame1.grid_rowconfigure(1, weight=1)
        OptionsFrame1.grid_columnconfigure(1, weight=1)    
        
        check3 = Checkbutton(OptionsFrame2, text=" Numbers ", variable=self.opt3, onvalue="3", offvalue="0")
        check3.deselect()
        check3.grid(row=2, column=0, sticky="nsew")
        OptionsFrame1.grid_rowconfigure(2, weight=1)
        OptionsFrame1.grid_columnconfigure(0, weight=1)    
        
        check4 = Checkbutton(OptionsFrame2, text=" Symbols  ", variable=self.opt4, onvalue="4", offvalue="0")
        check4.deselect()
        check4.grid(row=2, column=1, sticky="nsew")
        OptionsFrame1.grid_rowconfigure(2, weight=1)
        OptionsFrame1.grid_columnconfigure(1, weight=1)    
        
        screen.mainloop()  
             
    def generateGUI(self):
        
        value = 0
        opts = []
        opts.append(self.opt1.get())
        opts.append(self.opt2.get())
        opts.append(self.opt3.get())
        opts.append(self.opt4.get())
        
        #Check whether no option is selected
        DefaultFlag = False
        if opts[0] == 0 and opts[1] == 0 and opts[2] == 0 and opts[3] == 0:
            DefaultFlag = True
            
        #Removing all zeros from the List 
        while value in opts:
            opts.remove(0)
    
        #Making Default Lowercase Option
        if(DefaultFlag):
            opts.append(int(1)) 
        
        #Converting to correct format for generate function     
        for i in range(len(opts)):
            opts[i] = opts[i]-1
        
        #Checking the length to Default or Not:
        if(self.LengthNum.get() == 0):
            PassLength = 8
        else:
            PassLength = self.LengthNum.get() 
            
        #Calling the Generate Function and Displaying the Generated Password
        PasswdGenerated = self.generate(PassLength, opts)    
        self.OutputEntry.delete(0, END)  
        self.OutputEntry.insert(0, PasswdGenerated)
                  
    def lengthIncDec(self, flag):
        
        if (flag == 1):
            self.LengthNum.set(self.LengthNum.get() + 1)
        if (flag == 2):
            if self.LengthNum.get() != 0:
                self.LengthNum.set(self.LengthNum.get() - 1)

    def copyPasswd(self):
        
        self.OutputEntry.select_range(0,'end')
        self.OutputEntry.event_generate("<<Copy>>")
    
    def start(self):
        
        print("Welcome to Strong Password Generator")
        print("====================================")
        print("1. To Continue in CLI (Command Line Interface)")
        print("2. To Upgrade to GUI (Graphical User Interface)")
        
        try:
            self.interfaceOption = int(input("Please Enter an Option (Default is 1(CLI)): ") or "1")
        except:
            print("Enter the correct Option! Try Again")
            input("Press Enter to continue...")
            self.start()  
        print("-" * 30)
        
        if self.interfaceOption == 1:
            self.cli() 
        elif self.interfaceOption == 2:
            self.gui()
        else:
            print("Enter the correct Option! Try Again")
            input("Press Enter to continue...")
            self.start()

if __name__ == "__main__":
    Generator = SPG()
    Generator.start()
    
