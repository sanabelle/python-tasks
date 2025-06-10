#login page
import tkinter as tk
#master
master = tk.Tk()
master.title('Login')
master.geometry("500x500")
master.maxsize(500, 500)
master.minsize(400, 400)
master['bg'] = "#adc178"

data={
      'ahmed':{'name':'ahmed','password':'123','phone':'1111','age':25}
   }







# for i in data:
#  print(data[i]['phone'])
#second page function
def open_second_page():
   
  
   
   
   
   
   master.destroy()

   master2 = tk.Tk()
   master2.title('Regestration')
   master2.geometry("500x500")
   master2.maxsize(500, 500)
   master2.minsize(400, 400)
   master2['bg'] = "#adc178"
   
   
      #regestration page
      #welcom label 
   welcome2 = tk.Label(master2, text='𝐑𝐄𝐆𝐄𝐒𝐓𝐑𝐀𝐓𝐈𝐎𝐍 𝐏𝐀𝐆𝐄', font=('Segoe UI', 25, "bold"), fg="#f0ead2", background="#adc178")
   welcome2.grid(row=0, column=0, columnspan=4,sticky='e', pady=25,padx=80)
        
        
         
   #username label and entry
   usernameLabel2 = tk.Label(master2, text='𝘂𝘀𝗲𝗿𝗻𝗮𝗺𝗲', font=('Segoe UI', 15, "bold"), fg="#f0ead2", background='#adc178')
   usernameLabel2.grid(row=1, column=0, sticky="e", padx=0, pady=10)

   username2 = tk.Entry(master2, width=30)
   username2.grid(row=1, column=1,sticky="e", padx=0, pady=5)

   #password label and entry
   passwordLabel2 = tk.Label(master2, text='𝗽𝗮𝘀𝘀𝘄𝗼𝗿𝗱', font=('Segoe UI', 15, "bold"), fg="#f0ead2", background='#adc178')
   passwordLabel2.grid(row=2, column=0, sticky="e", padx=0, pady=10)

   password2 = tk.Entry(master2, width=30)
   password2.grid(row=2, column=1,sticky="e", padx=0, pady=5)
   
      
      
      
   #username label and entry
   phonenumLabel = tk.Label(master2, text='𝙥𝙝𝙤𝙣𝙚 𝙣𝙪𝙢𝙗𝙚𝙧', font=('Segoe UI', 15, "bold"), fg="#f0ead2", background='#adc178')
   phonenumLabel.grid(row=3, column=0, sticky="e", padx=0, pady=10)

   phonenum = tk.Entry(master2, width=30)
   phonenum.grid(row=3, column=1,sticky="e", padx=0, pady=5)

   #password label and entry
   ageLabel = tk.Label(master2, text='𝘼𝙜𝙚', font=('Segoe UI', 15, "bold"), fg="#f0ead2", background='#adc178')
   ageLabel.grid(row=4, column=0, sticky="e", padx=0, pady=10)

   age = tk.Entry(master2, width=30)
   age.grid(row=4, column=1,sticky="e", padx=0, pady=5)
   
   
   
   
   #check regestration function:
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
      #check regestration function:
   def check_registration():
      #get username and password from entry fields
         new_user = username2.get()
         new_password = password2.get()
         new_phone=phonenum.get()
         new_age=age.get()
         for i in data:
            if new_user not in data[i]:
               if len(new_password)>8:
                  if new_phone not in data[i]['phone']:
                     data[new_user]={'name':new_user,'password':new_password,'age':new_age,'phone':new_phone,}
                     
<<<<<<< HEAD
               
                     break
            
=======
                     print("Rgestration Done")
                     print(data)
                     break
      
>>>>>>> 510ce5587147693d8de20ff9746f8660b47fb2f1
      
      
       
      
            master2.destroy()

         master3 = tk.Tk()
         master3.title('Welcom User')
         master3.geometry("500x500")
         master3.maxsize(500, 500)
         master3.minsize(400, 400)
         master3['bg'] = "#adc178"
      
      
      
         welcome3 = tk.Label(master3, text='𝗪𝗘𝗟𝗖𝗢𝗠 𝗨𝗦𝗘𝗥 ', font=('Segoe UI', 25, "bold"), fg="#f0ead2", background="#adc178")
         welcome3.grid(row=3, column=0, columnspan=4,sticky='e', pady=250,padx=150)
      
         # if new_user not in data:
         #    if new_password>8:
         #       if new_phone not in data['phone']:
   
   
   regestration2 = tk.Button(master2, text='Regestration', background="#7C9538", width=40, height=1,command=check_registration)
   regestration2.grid(row=5, column=0, sticky='s', columnspan=4,pady=20)
   master2.mainloop()
   
   










regestration = tk.Button(master, text='Or Regestration', background="#7C9538", width=40, height=1,command=open_second_page)
regestration.grid(row=5, column=0, sticky='s', columnspan=4,pady=20)









def check_login():
#get username and password from entry fields
         user = username.get()
         user_password = password.get()
      
         for i in data:
            if user == data[i]['name']:
               if user_password==data[i]['password']:
                  
                     
                     print("Login Done")
                     
                     break
               else:
                  print("Wrong Password")
            else:
               print("Invalid username")
#welcom label 
welcome = tk.Label(master, text='𝗟𝗢𝗚𝗜𝗡 𝗣𝗔𝗚𝗘', font=('Segoe UI', 25, "bold"), fg="#f0ead2", background="#adc178")
welcome.grid(row=0, column=0, columnspan=4,sticky='e', pady=25,padx=140)

#username label and entry
usernameLabel = tk.Label(master, text='𝘂𝘀𝗲𝗿𝗻𝗮𝗺𝗲', font=('Segoe UI', 15, "bold"), fg="#f0ead2", background='#adc178')
usernameLabel.grid(row=1, column=0, sticky="e", padx=0, pady=10)

username = tk.Entry(master, width=30)
username.grid(row=1, column=1,sticky="e", padx=0, pady=5)

#password label and entry
passwordLabel = tk.Label(master, text='𝗽𝗮𝘀𝘀𝘄𝗼𝗿𝗱', font=('Segoe UI', 15, "bold"), fg="#f0ead2", background='#adc178')
passwordLabel.grid(row=2, column=0, sticky="e", padx=0, pady=10)

password = tk.Entry(master, width=30)
password.grid(row=2, column=1,sticky="e", padx=0, pady=5)


#login button
login = tk.Button(master, text='Login', background="#7C9538", width=40, height=1,command=check_login )
login.grid(row=3, column=0, sticky='s', columnspan=4,pady=20)






master.mainloop()