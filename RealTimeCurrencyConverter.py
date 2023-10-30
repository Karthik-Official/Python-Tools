from currency_converter import CurrencyConverter
from tkinter import *
from tkinter import font
from tkinter import messagebox

class RTCC:
    
    def __init__(self):
            
        self.mainscreen = Tk()
        self.mainscreen.title("Realtime Currency Converter")  
        
        # Create a bold font
        self.HeadingFont = font.Font(family="Helvetica", size=16, weight="bold")     
        self.MainFont = font.Font(family="Helvetica", size=12, weight="bold")    
        self.DropDownFont = font.Font(family="Helvetica", size=10, weight="bold")
        self.EntryFont = font.Font(family="Helvetica", size=10)    

        # Background colour of the window 
        self.mainscreen.configure(background="#6A6C6E")
        
        self.MainFrame = LabelFrame(self.mainscreen, padx=0, pady=0, borderwidth=5, relief='groove')
        self.MainFrame.pack(padx=10, pady=10)
        
        self.TitleFrame = LabelFrame(self.MainFrame, padx=150, pady=10, bg="#BFC3C6", borderwidth=1.20, relief='solid')
        self.TitleFrame.grid(row=0, column=0, sticky="nsew")
        self.MainFrame.grid_rowconfigure(0, weight=1)
        self.MainFrame.grid_columnconfigure(0, weight=1)
        
        self.TypeFrame = LabelFrame(self.MainFrame, text="Menu Types", padx=50, pady=10, borderwidth=2, relief='ridge')
        self.TypeFrame.grid(row=1, column=0, sticky="nsew")
        self.MainFrame.grid_rowconfigure(1, weight=1)
        self.MainFrame.grid_columnconfigure(0, weight=1)
        
        self.MenuFrame = LabelFrame(self.MainFrame, text="Menu", padx=50, pady=10, relief='groove')
        self.MenuFrame.grid(row=2, column=0, sticky="nsew")
        self.MainFrame.grid_rowconfigure(2, weight=1)
        self.MainFrame.grid_columnconfigure(0, weight=1)
        
        self.IOFrame = LabelFrame(self.MainFrame, text="Input and Output", padx=50, pady=10, relief='groove')
        self.IOFrame.grid(row=3, column=0, sticky="nsew")
        self.MainFrame.grid_rowconfigure(3, weight=1)
        self.MainFrame.grid_columnconfigure(0, weight=1)
        
        self.OptionFrame = LabelFrame(self.MainFrame, padx=50, pady=10, bg="#BFC3C6", borderwidth=2, relief='ridge')
        self.OptionFrame.grid(row=4, column=0, sticky="nsew", pady=10)
        self.MainFrame.grid_rowconfigure(4, weight=1)
        self.MainFrame.grid_columnconfigure(0, weight=1)
        
        #Title Frame
        Label(self.TitleFrame, text="CURRENCY CONVERTER", font=self.HeadingFont, bg="#BFC3C6", width=35).pack()
        
        #Type Frame and Menu Frame
        self.r = IntVar()
        self.r.set(1) 
        self.manual()
        
        self.ManualButton = Radiobutton(self.TypeFrame, text="Manual", font=self.MainFont, variable=self.r, value=1, command=self.manual)
        self.ManualButton.grid(row=0, column=0, sticky="nsew")
        self.TypeFrame.grid_rowconfigure(1, weight=1)
        self.TypeFrame.grid_columnconfigure(0, weight=1)
        self.DropdownButton = Radiobutton(self.TypeFrame, text="Dropdown", font=self.MainFont, variable=self.r, value=2, command=self.dropdown)
        self.DropdownButton.grid(row=0, column=1, sticky="nsew")
        self.TypeFrame.grid_rowconfigure(0, weight=1)
        self.TypeFrame.grid_columnconfigure(1, weight=1)
        
        #IOFrame
        self.InputLabel = Label(self.IOFrame, text="Input (Amount)", font=self.MainFont)
        self.InputLabel.grid(row=0, column=0, sticky="nsew")
        self.IOFrame.grid_rowconfigure(0, weight=1)
        self.IOFrame.grid_columnconfigure(0, weight=1)
        
        self.OutputLabel = Label(self.IOFrame, text="Output (Amount)", font=self.MainFont)
        self.OutputLabel.grid(row=0, column=2, sticky="nsew")
        self.IOFrame.grid_rowconfigure(0, weight=1)
        self.IOFrame.grid_columnconfigure(2, weight=1)
        
        self.CurrencyInput = Entry(self.IOFrame, width=30, borderwidth=3, font=self.EntryFont)
        self.CurrencyInput.grid(row=1,column=0, sticky="nsew")
        self.IOFrame.grid_rowconfigure(1, weight=1)
        self.IOFrame.grid_columnconfigure(0, weight=1)
        
        self.SwapButton = Button(self.IOFrame, text="Swap", bg="#BFC3C9", activebackground="#D5D9DC", command=lambda: self.swap(3))
        self.SwapButton.grid(row=1,column=1, sticky="nsew", padx=20)
        self.IOFrame.grid_rowconfigure(1, weight=1)
        self.IOFrame.grid_columnconfigure(1, weight=1)
        
        self.CurrencyOutput = Entry(self.IOFrame, width=30, borderwidth=3, font=self.EntryFont)
        self.CurrencyOutput.grid(row=1,column=2, sticky="nsew")
        self.IOFrame.grid_rowconfigure(1, weight=1)
        self.IOFrame.grid_columnconfigure(2, weight=1)
        
        #OptionFrame

        self.ClearButton = Button(self.OptionFrame, text="   Clear   ", font=self.MainFont, padx=10, command=self.clear, fg="blue")
        self.ClearButton.grid(row=0,column=1, sticky="nsew", padx=50)
        self.OptionFrame.grid_rowconfigure(0, weight=1)
        self.OptionFrame.grid_columnconfigure(1, weight=1)
        

        self.ConvertButton = Button(self.OptionFrame, text="Convert" , font=self.MainFont, padx=10, command=self.convert, fg="blue")
        self.ConvertButton.grid(row=0,column=2, sticky="nsew", padx=50)
        self.OptionFrame.grid_rowconfigure(0, weight=1)
        self.OptionFrame.grid_columnconfigure(2, weight=1)
        
        self.mainscreen.mainloop()  
        
    def swap(self, Flag):
        
        if(Flag==1):
            self.Temp = self.FromCurrencyTypeMan.get()
            self.FromCurrencyTypeMan.delete(0, END)    
            self.FromCurrencyTypeMan.insert(0,str(self.ToCurrencyTypeMan.get()))
            self.ToCurrencyTypeMan.delete(0, END)
            self.ToCurrencyTypeMan.insert(0,self.Temp)
            
        if(Flag==2):
            self.Temp = self.FromCurrencySelected.get()
            self.FromCurrencySelected.set(self.ToCurrencySelected.get())
            self.ToCurrencySelected.set(self.Temp)   
            
        if(Flag==3):    
            self.Temp = self.CurrencyInput.get()
            self.CurrencyInput.delete(0, END) 
            self.CurrencyInput.insert(0,str(self.CurrencyOutput.get()))
            self.CurrencyOutput.delete(0,END)
            self.CurrencyOutput.insert(0,self.Temp)            
        
    def clear(self):
        
        if(self.r.get()==1):
            self.FromCurrencyTypeMan.delete(0, END)
            self.ToCurrencyTypeMan.delete(0, END)
            self.CurrencyInput.delete(0, END)   
            self.CurrencyOutput.delete(0, END)     
            
        if(self.r.get()==2):
            self.dropdown()
            self.CurrencyInput.delete(0, END)   
            self.CurrencyOutput.delete(0, END)     
                           
    def convert(self):
        
        if(self.r.get()==1):
            try:
                # Getting user input values        
                self.FromCurrency = str(self.FromCurrencyTypeMan.get()).upper()
                self.ToCurrency = str(self.ToCurrencyTypeMan.get()).upper()
                self.InputCurrencyValue = float(self.CurrencyInput.get())
                self.output()
                
            except:
                messagebox.showinfo("error","1. Enter Data in Correct Format(example-INR, USD, EUR) in Types.\n2. Enter the Amount in Input Box")
                
        if(self.r.get()==2):
            try:
                # Getting user input values        
                self.FromCurrency = str(self.CurrenciesDict.get(self.FromCurrencySelected.get())).upper()
                self.ToCurrency = str(self.CurrenciesDict.get(self.ToCurrencySelected.get())).upper()
                self.InputCurrencyValue = float(self.CurrencyInput.get())
                self.output()
                
            except:
                messagebox.showinfo("error","\n1. Enter the Amount in Input Box")
                
    def output(self):
        
        # Using currency_converter package
        self.cc = CurrencyConverter()
        self.CurrencyOutput.delete(0, END)    
        # Generating Output 
        self.OutputCurrencyValue = self.cc.convert(self.InputCurrencyValue, self.FromCurrency, self.ToCurrency)
        self.CurrencyOutput.insert(0,round(self.OutputCurrencyValue, 2))
        print("The converted rate is:", self.OutputCurrencyValue) 
        
    def manual(self):
        
        # Clearing the MenuFrame
        for widget in self.MenuFrame.winfo_children():
            widget.destroy()
            
        self.FromLabel = Label(self.MenuFrame, text="From (Currency)", font=self.MainFont)
        self.FromLabel.grid(row=0,column=0, sticky="nsew")
        self.MenuFrame.grid_rowconfigure(0, weight=1)
        self.MenuFrame.grid_columnconfigure(0, weight=1)
        
        self.ToLabel = Label(self.MenuFrame, text="To (Currency)", font=self.MainFont)
        self.ToLabel.grid(row=0,column=2, sticky="nsew")
        self.MenuFrame.grid_rowconfigure(0, weight=1)
        self.MenuFrame.grid_columnconfigure(2, weight=1)
        
        self.FromCurrencyTypeMan = Entry(self.MenuFrame, width=30, borderwidth=3, font=self.EntryFont)
        self.FromCurrencyTypeMan.grid(row=1,column=0, sticky="nsew")
        self.MenuFrame.grid_rowconfigure(1, weight=1)
        self.MenuFrame.grid_columnconfigure(0, weight=1)
        
        self.SwapButton = Button(self.MenuFrame, text="Swap", bg="#BFC3C9", activebackground="#D5D9DC", command=lambda: self.swap(1))
        self.SwapButton.grid(row=1,column=1, sticky="nsew", padx=20)
        self.MenuFrame.grid_rowconfigure(1, weight=1)
        self.MenuFrame.grid_columnconfigure(1, weight=1)
        
        self.ToCurrencyTypeMan = Entry(self.MenuFrame, width=30, borderwidth=3, font=self.EntryFont)
        self.ToCurrencyTypeMan.grid(row=1,column=2, sticky="nsew")
        self.MenuFrame.grid_rowconfigure(1, weight=1)
        self.MenuFrame.grid_columnconfigure(2, weight=1)
            
    def dropdown(self):
        
        # Clearing the MenuFrame
        for widget in self.MenuFrame.winfo_children():
            widget.destroy()
            
        self.CurrenciesDict = {
            "Australian Dollar(AUD)":"AUD",
            "Brazilian Real(BRL)":"BRL",
            "Bulgarian Lev(BGN)":"BGN",
            "Canadian Dollar(CAD)":"CAD",
            "Chinese Yuan Renminbi(CNY)":"CNY",
            "Czech Koruna(CZK)":"CZK",	
            "Danish Krone(DKK)":"DKK",
            "European Euro (EUR)":"EUR",
            "Hong Kong Dollar(HKD)":"HKD",
            "Hungarian Forint(HUF)":"HUF",
            "US Dollar(USD)":"USD",
            "Indian Rupee(INR)":"INR",
            "Icelandic Krona(ISK)":"ISK",
            "Israeli Shekel(ILS)":"ILS",
            "Indonesian Rupiah(IDR)":"IDR",
            "Japanese Yen(JPY)":"JPY",
            "Mexican Peso(MXN)":"MXN",
            "Malaysian Ringgit(MYR)":"MYR",
            "Norwegian Krone(NOK)":"NOK",
            "New Zealand Dollar(NZD)":"NZD",
            "Pound Sterling(GBP)":"GBP",
            "Polish Zloty(PLN)":"PLN",
            "Philippine Peso(PHP)":"PHP",
            "Romanian Leu(RON)":"RON",	
            "Swedish Krona(SEK)":"SEK",
            "Swiss Franc(CHF)":"CHF",
            "South Korean Won(KRW)":"KRW",
            "Singapore Dollar(SGD)":"SGD",
            "South African Rand(ZAR)":"ZAR",
            "Turkish Lira(TRY)":"TRY",
            "Thai Baht(THB)":"THB",
        }
        self.CurrenciesList = list(self.CurrenciesDict.keys())
        
        self.FromCurrencySelected = StringVar()
        self.FromCurrencySelected.set(self.CurrenciesList[10])
        self.ToCurrencySelected = StringVar()
        self.ToCurrencySelected.set(self.CurrenciesList[11])
        
        self.FromLabel = Label(self.MenuFrame, text="From (Currency)", font=self.MainFont)
        self.FromLabel.grid(row=0, column=0, sticky="nsew")
        self.MenuFrame.grid_rowconfigure(0, weight=1)
        self.MenuFrame.grid_columnconfigure(0, weight=1)

        self.ToLabel = Label(self.MenuFrame, text="To (Currency)", font=self.MainFont)
        self.ToLabel.grid(row=0, column=2, sticky="nsew")
        self.MenuFrame.grid_rowconfigure(0, weight=1)
        self.MenuFrame.grid_columnconfigure(2, weight=1)
        
        self.FromCurrencyTypeDD = OptionMenu(self.MenuFrame, self.FromCurrencySelected, *self.CurrenciesList)
        self.FromCurrencyTypeDD.config(width=30, font=self.DropDownFont)
        self.FromCurrencyTypeDD.grid(row=1, column=0, sticky="nsew")
        self.MenuFrame.grid_rowconfigure(1, weight=1)
        self.MenuFrame.grid_columnconfigure(0, weight=1)
        
        self.SwapButton = Button(self.MenuFrame, text="Swap", bg="#BFC3C9", activebackground="#D5D9DC", command=lambda: self.swap(2))
        self.SwapButton.grid(row=1, column=1, sticky="nsew", padx=20)
        self.MenuFrame.grid_rowconfigure(1, weight=1)
        self.MenuFrame.grid_columnconfigure(1, weight=1)
        
        self.ToCurrencyTypeDD = OptionMenu(self.MenuFrame, self.ToCurrencySelected, *self.CurrenciesList)
        self.ToCurrencyTypeDD.config(width=30, font=self.DropDownFont)
        self.ToCurrencyTypeDD.grid(row=1, column=2, sticky="nsew")
        self.MenuFrame.grid_rowconfigure(1, weight=1)
        self.MenuFrame.grid_columnconfigure(2, weight=1)
        
if __name__ == "__main__":
    CC = RTCC()    
    