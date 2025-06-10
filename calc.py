import tkinter as tk
master=tk.Tk()
master.title('Calculation')
master.geometry("460x460")

master.columnconfigure(0, weight=1)
master.columnconfigure(1, weight=1)
master.columnconfigure(2, weight=1)
master.columnconfigure(3, weight=1)
master['bg']="#00b39b"
opPlace=tk.Text(master,width=50,height=5,)
opPlace.grid(row=0,column=0,columnspan=4)

def addTextInScreen(value):
    opPlace.insert(tk.END, value)
   

row=1
column=0
text=['9','8','7','+','4','5','6','-','1','2','3','*','/','0','=']


for i in range (0,len(text)):
        if column == 4:
            column=0
            row+=1
        
        button=tk.Button(text=text[i],background='#efefd0',width=17,height=5,border=5, command=lambda val=text[i]: addTextInScreen(val))
        button.grid(row=row,column=column)
        column+=1   
            
        

master.mainloop()