#login page
import tkinter as tk
#master
master = tk.Tk()
master.title('Login')
master.geometry("500x500")
master.maxsize(500, 500)
master.minsize(400, 400)
master['bg'] = "#3c6e71"

<<<<<<< HEAD

import json
with open(r"C:\Users\AIA\Desktop\learn python\python-tasks\python-tasks-git\inventory_management_system.json","r") as file:
                    data=json.load(file)

=======
>>>>>>> 510ce5587147693d8de20ff9746f8660b47fb2f1
# master.columnconfigure(0, weight=1)
# master.columnconfigure(1, weight=1)
# master.columnconfigure(2, weight=1)
# master.columnconfigure(3, weight=1)



# master.rowconfigure(0, weight=1)
# master.rowconfigure(1, weight=1)
# master.rowconfigure(2, weight=1)
# master.rowconfigure(3, weight=1)

<<<<<<< HEAD
# import json
# with open(r"C:\Users\AIA\Desktop\learn python\python-tasks\python-tasks-git\inventory_management_system.json","r") as file:
#     data=json.load(file)
=======
import json
with open(r"C:\Users\AIA\Desktop\learn python\python-tasks\python-tasks-git\inventory_management_system.json","r") as file:
    data=json.load(file)
>>>>>>> 510ce5587147693d8de20ff9746f8660b47fb2f1
# data={
#       'ahmed':{'name':'ahmed','password':'123','phone':'1111','age':25}
#    }



def open_second_page():
    master.withdraw()  # يخفي النافذة الأولى بدل ما يقفلها
    master2 = tk.Toplevel()  # نافذة جديدة
    master2.title('Products')
    master2.geometry("500x500")
    master2.maxsize(500, 500)
    master2.minsize(400, 400)
    master2['bg'] = "#3c6e71"
    # i=0
    
    def edit_quantity():

        def save3():
<<<<<<< HEAD
            # import json
            # with open(r"C:\Users\AIA\Desktop\learn python\python-tasks\python-tasks-git\inventory_management_system.json","r") as file:
            #         data=json.load(file)
            
            usernewquantity_product=newquantityentry.get()
            data['products']['productquantity']=usernewquantity_product
            with open(r"C:\Users\AIA\Desktop\learn python\python-tasks\python-tasks-git\inventory_management_system.json","w") as file:
                json.dump(data,file,indent=4)
=======
            usernewquantity_product=newquantityentry.get()
            data['products']['productquantity']=usernewquantity_product
>>>>>>> 510ce5587147693d8de20ff9746f8660b47fb2f1
            print(data)
            open_second_page()
        
        master2.destroy()
        master3=tk.Tk()
        master3.title('Edit Products')
        master3.geometry("500x500")
        master3.maxsize(500, 500)
        master3.minsize(400, 400)
        master3['bg'] = "#3c6e71"
                    
        welcome3 = tk.Label(master3, text='Edit PAGE', font=('Segoe UI', 25, "bold"), fg="#052E2E", background="#3c6e71")
        welcome3.grid(row=0, column=0, columnspan=4,sticky='e', pady=10,padx=170)
        newquantitylabel=tk.Label(master3, text='new quantity price', font=('Segoe UI', 15, "bold"), fg="#ffffff", background='#3c6e71')
        newquantitylabel.grid(row=1, column=0, sticky="e", padx=0, pady=0)
        newquantityentry=tk.Entry(master3, font=('Arial', 10), width=20,)
        newquantityentry.grid(row=1, column=1, sticky="e", padx=0)
        newquantitybutton=tk.Button(master3, text='save quantity', background="#052E2E",fg="#ffffff",font=('Arial', 10), width=10, height=5,command=save3)
        newquantitybutton.grid(row=2,column=0,columnspan=4,sticky="e", padx=0)
    
    
    
    
    
    
    
    def edit_price():
    
        def save2():
<<<<<<< HEAD
            # import json
            # with open(r"C:\Users\AIA\Desktop\learn python\python-tasks\python-tasks-git\inventory_management_system.json","r") as file:
            #         data=json.load(file)
            usernewprice_product=newpriceentry.get()
            data['products']['productprice']=usernewprice_product
            with open(r"C:\Users\AIA\Desktop\learn python\python-tasks\python-tasks-git\inventory_management_system.json","w") as file:
                json.dump(data,file,indent=4)
=======
            usernewprice_product=newpriceentry.get()
            data['products']['productprice']=usernewprice_product
>>>>>>> 510ce5587147693d8de20ff9746f8660b47fb2f1
            print(data)
            open_second_page()
        
        master2.destroy()
        master3=tk.Tk()
        master3.title('Edit Products')
        master3.geometry("500x500")
        master3.maxsize(500, 500)
        master3.minsize(400, 400)
        master3['bg'] = "#3c6e71"
        
        welcome3 = tk.Label(master3, text='Edit PAGE', font=('Segoe UI', 25, "bold"), fg="#052E2E", background="#3c6e71")
        welcome3.grid(row=0, column=0, columnspan=4,sticky='e', pady=40,padx=170)
        newpricelabel=tk.Label(master3, text='new product price', font=('Segoe UI', 15, "bold"), fg="#ffffff", background='#3c6e71')
        newpricelabel.grid(row=1, column=0, sticky="e", padx=0, pady=0)
        newpriceentry=tk.Entry(master3, font=('Arial', 10), width=20,)
        newpriceentry.grid(row=1, column=1, sticky="e", padx=0)
        newpricebutton=tk.Button(master3, text='save price', background="#052E2E",fg="#ffffff",font=('Arial', 10), width=10, height=5,command=save2)
        newpricebutton.grid(row=2,column=0,columnspan=4,sticky="e", padx=0)
            
    
    
        
    def edit_name():
        

            


        def save():
<<<<<<< HEAD
            # import json
            # with open(r"C:\Users\AIA\Desktop\learn python\python-tasks\python-tasks-git\inventory_management_system.json","r") as file:
            #         data=json.load(file)
            usernewname_product=newnameentry.get()
            data['products']['productname']=usernewname_product
            
            with open(r"C:\Users\AIA\Desktop\learn python\python-tasks\python-tasks-git\inventory_management_system.json","w") as file:
                json.dump(data,file,indent=4)
            print(data)
            
=======
            usernewname_product=newnameentry.get()
            data['products']['productname']=usernewname_product
            print(data)
>>>>>>> 510ce5587147693d8de20ff9746f8660b47fb2f1
            open_second_page()
        
        master2.destroy()
        master3=tk.Tk()
        master3.title('Edit Products')
        master3.geometry("500x500")
        master3.maxsize(500, 500)
        master3.minsize(400, 400)
        master3['bg'] = "#3c6e71"
        
        welcome3 = tk.Label(master3, text='Edit PAGE', font=('Segoe UI', 25, "bold"), fg="#052E2E", background="#3c6e71")
        welcome3.grid(row=0, column=0, columnspan=4,sticky='e', pady=40,padx=170)
        newnamelabel=tk.Label(master3, text='new product name', font=('Segoe UI', 15, "bold"), fg="#ffffff", background='#3c6e71')
        newnamelabel.grid(row=1, column=0, sticky="e", padx=0, pady=0)
        newnameentry=tk.Entry(master3, font=('Arial', 10), width=20,)
        newnameentry.grid(row=1, column=1, sticky="e", padx=0)
        newnamesave=tk.Button(master3, text='save name', background="#052E2E",fg="#ffffff",font=('Arial', 10), width=10, height=5,command=save)
        newnamesave.grid(row=2,column=0,columnspan=4,sticky="e", padx=0)
    

    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    welcome2 = tk.Label(master2, text='PROGUCTS PAGE', font=('Segoe UI', 25, "bold"), fg="#052E2E", background="#3c6e71")
    welcome2.grid(row=0, column=0, columnspan=4,sticky='e', pady=40,padx=120)
        #name label and entry and button
    nameLabel = tk.Label(master2, text='product name', font=('Segoe UI', 15, "bold"), fg="#ffffff", background='#3c6e71')
    nameLabel.grid(row=1, column=0, sticky="e", padx=0, pady=0)
    prduct_nameLabel = tk.Label(master2, text=data['products']['productname'], font=('Segoe UI', 15, "bold"), fg="#ffffff", background='#3c6e71')
    prduct_nameLabel.grid(row=1, column=1,sticky="e", padx=0, pady=0)
    namebutton = tk.Button(master2, text='edit', background="#052E2E",fg="#ffffff",font=('Arial', 10), width=5, height=1,command=edit_name )
    namebutton.grid(row=1, column=2, sticky='s',pady=0)
        #price label and entry and button
    pricedLabel = tk.Label(master2, text='product price', font=('Segoe UI', 15, "bold"), fg="#ffffff", background='#3c6e71')
    pricedLabel.grid(row=2, column=0, sticky="e", padx=0, pady=0)
    prduct_priceLabel = tk.Label(master2, text=data['products']['productprice'], font=('Segoe UI', 15, "bold"), fg="#ffffff", background='#3c6e71')
    prduct_priceLabel.grid(row=2, column=1,sticky="e", padx=0, pady=0)
    pricebutton = tk.Button(master2, text='edit', background="#052E2E",fg="#ffffff",font=('Arial', 10), width=5, height=1,command=edit_price )
    pricebutton.grid(row=2, column=2, sticky='s',pady=0)
        #quantity label and entry and button
    quantityLabel = tk.Label(master2, text='product quantity', font=('Segoe UI', 15, "bold"), fg="#ffffff", background='#3c6e71')
    quantityLabel.grid(row=3, column=0, sticky="e", padx=0, pady=0)
    prduct_quantityLabel = tk.Label(master2, text=data['products']['productquantity'], font=('Segoe UI', 15, "bold"), fg="#ffffff", background='#3c6e71')
    prduct_quantityLabel.grid(row=3, column=1,sticky="e", padx=0, pady=0)
    quantitybutton = tk.Button(master2, text='edit', background="#052E2E",fg="#ffffff",font=('Arial', 10), width=5, height=1,command=edit_quantity )
    quantitybutton.grid(row=3, column=2, sticky='s',pady=0)
    

        
        
        
        
        
        # i+=1
def check_login():
    #get username and password from entry fields
<<<<<<< HEAD
            # import json
            # with open(r"C:\Users\AIA\Desktop\learn python\python-tasks\python-tasks-git\inventory_management_system.json","r") as file:
            #         data=json.load(file)
=======
>>>>>>> 510ce5587147693d8de20ff9746f8660b47fb2f1
            user = username.get()
            user_password = password.get()
        
            
            if user == data['users']['username']:
                    if user_password==data['users']['password']:
                    
                        
                        print("Login Done")
                        open_second_page()
                        
                    else:
                        print("Wrong Password")
            else:
                    print("Invalid username")







#welcom label 
welcome = tk.Label(master, text='𝗟𝗢𝗚𝗜𝗡 𝗣𝗔𝗚𝗘', font=('Segoe UI', 25, "bold"), fg="#052E2E", background="#3c6e71")
welcome.grid(row=0, column=0, columnspan=4,sticky='e', pady=40,padx=140)


#login page(username,pasword)
#username(label,entry)
#label(tk,grid)
#entry(tk,grid)
usernameLabel = tk.Label(master, text='𝘂𝘀𝗲𝗿𝗻𝗮𝗺𝗲', font=('Segoe UI', 15, "bold"), fg="#ffffff", background='#3c6e71')
usernameLabel.grid(row=1, column=0, sticky="e", padx=0, pady=0)

username = tk.Entry(master, width=30)
username.grid(row=1, column=1,sticky="e", padx=0, pady=0)


#password(label,entry)
#label(tk,grid)
#entry(tk,grid)
passwordLabel = tk.Label(master, text='𝗽𝗮𝘀𝘀𝘄𝗼𝗿𝗱', font=('Segoe UI', 15, "bold"), fg="#ffffff", background='#3c6e71')
passwordLabel.grid(row=2, column=0, sticky="e", padx=0, pady=0)

password = tk.Entry(master, width=30)
password.grid(row=2, column=1,sticky="e", padx=0, pady=0)



login = tk.Button(master, text='Login', background="#052E2E",fg="#ffffff",font=('Arial', 10), width=40, height=4,command=check_login )
login.grid(row=3, column=0, sticky='s', columnspan=4,pady=70)
master.mainloop()