
def sum(num1,num2):
      print(num1+num2)
sum(1,4)


# import json as js
# with open("C:/Users/AIA/Desktop/learn python/python-tasks/users.json", "r") as us:
#    data=js.load(us)
   


# user_name=input("Enter your name: ")
# user_pass=input("Enter you password: ")


# for i in data.values():
#       if user_name == i["username"] and user_pass==i["password"]:
#          print("Login done")
#       else:
#          print("Invalid username or password")









# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# x=filter(lambda n : n%2==0,numbers)
# y=list(x)
# # print(list(x))

# x2=map(lambda n2:n2**2,y)
# x3=list(x2)
# print(x3)

# def add(x3):
#          if len(x3)==0:
#             return 0
#          else:
#             x3[0]+add(x3[1:])

# print(add(x3))

   



# sentence = "Python is a powerful and beautiful programming language"
# words=sentence.split()
# print(words)
# long_words=filter(lambda l:len(l)>5,words)
# long_words_list=list(long_words)
# print(long_words_list)

# uppercase=map(lambda l2:l2.upper(),long_words_list)
# uppercase_list=list(uppercase)
# print(uppercase_list)

# def pr(uppercase_list):
#    if len(uppercase_list)==0:
#       return 0
#    else:
#       print(uppercase_list[0])
#       pr(uppercase_list[1:])
      

# pr(uppercase_list)















# #120
# # x = [1,7,9,87,4,4,8]

# # def sumfunction(sum):
# #    if len(sum)!=1:
# #       sum[0]+=sum[1]
# #       sum.pop(1)
# #       return sum
# #    else:
# #       print(sum[0])
# #       return sumfunction()

   
# # print(sumfunction([1,5,6,2,4])
# # )
# def sumfunction(sum):
#    for i in range(1,len(sum)):
#       sum[0] += sum[1]
#       sum.pop(1)
#       return sum

 
 
# print(sumfunction([1,2,5,4,7]))




# data = {'abdallah' : {'username' : 'abdallah', 'age' : 27, 'email' : 'abdallah@gmail.com', 'password' : '!Bdall8h'},
#       'ahmed' : {'username' : 'ahmed', 'age' : 28, 'email' : 'ahmed@gmail.com', 'password' : 222}
#    }

# for i in data:
#    print(data[i])
#i(in dictionary)=the keys
# x = [[1,6,9],8,10]
# for i in range (0,len(x)):#0 to 3 i=0,1,2
#    print(i)
# i=values of the range =0,1,2


# for i in x:
#    print(i)
# i=values of the items =1,5,10


# x = [[1,3,6],[4,5,8],[7,9,5],[1,6,9]]

# for i in x:
#    for u in i:
#       print(u)


# users = ["abdallah", "ahmed", "ali"]
# emailList = ["abdallah@gmail.com", "ahmed@gmail.com", "ali@gmail.com"]
# data = {
#     'abdallah' : {'username' : 'abdallah', 'age' : 27, 'email' : 'abdallah@gmail.com', 'password' : 1234},
#     'ahmed' : {'username' : 'ahmed', 'age' : 28, 'email' : 'ahmed@gmail.com', 'password' : 1234},
#     'ali' : {'username' : 'ali', 'age' : 23, 'email' : 'ahmed@gmail.com', 'password' : 15988963}
# }

# for check in range(0, 5):
#     username = input('Enter username : ').lower()
#     password = input('Enter Your Password : ')

#     if username in users :
#         if username == data[username]['username']:
#             if password == data[username]['password'] :
#                 print('Login Done :) ')
#                 break
#             else :
#                 print('Wrong Password :( ')
#         else :
#             print('Wrong Username :( ')
#     else :
#         print('User Not Found :( ')
   












# x=[1,5,10]
# for i in range (0,len(x)):
#    print(i)
# x=[1,5,10]
# for i in x:
#    print(i)


# for i in range(1,11):
#    for u in range(1,11):
      
#       for t in range(1,11):
         
#          for s in range(1,11):
         
#             print(f"({i},{u},{t},{s})")

   #125
# products={
#    'product1':{
#    'name':"milk",
#    'price':10,
#    'description':'Fresh and healthy milk',
#    'quantity': 40,
#    'on_sale' : False
# },

#    'product2':{
#    'name':"Rice",
#    'price':50,
#    'description':'Premium and pure rice',
#    'quantity': 60,
#    'on_sale' : True
# },


# 'product3':{
#    'name':"Bread",
#    'price':10,
#    'description':'Fresh bread',
#    'quantity': 100,
#    'on_sale' : False
# }

# }

# x=list(products.keys())
# print('=================Welcome===================')
# check=0
# while check<len(x):
#  print(f'{x[check]}:')
#  print(f'Name<={products[x[check]]['name']}')
#  print(f'Price<={products[x[check]]['price']}')

#  print(f'Description<={products[x[check]]['description']}')
#  print('!!!!!!!!!!!!!!!!!')
#  check+=1
# print('========================================')



# products_number=input("enter products number you want to order like this 1 2: ")
# products_quantity=input("enter products quantities you want to order like this 6 5: ")
# print('========================================')

# x2=products_number.split(' ')
# x3=products_quantity.split(' ')
# x_mix=dict(zip(x2,x3))
# x_mix_keys=list(x_mix.keys())
# x_mix_values=list(x_mix.values())

# check3=0
# # print(x[z])
# while check3<len(x_mix_keys):
#    y=x_mix_keys[check3]#2
#    y2=x_mix_values[check3]
#    z=int(y)-1#2-1=1
#    print(f'you have ordered {products[x[z]]['name']} for quantites: {int(y2)}')
   


  
#    check3+=1
#    # total2=list(total)
#    # print(total2)
# print('========================================')

# Purchase_Invoice=['Product Name','Price per piece','Number of pieces','Total price']#دي كل مرة بتتكرر
# print(Purchase_Invoice)

# check4=0
# while check4<len(x_mix_keys):
#    y=x_mix_keys[check4]#2
#    y2=x_mix_values[check4]
#    z=int(y)-1#2-1=1

#    price=products[x[z]]['price']
# # print(price)
#    total=price*int(y2)
#    Purchase_Invoice2=[products[x[z]]['name'],products[x[z]]['price'],int(y2),total]
#    print(Purchase_Invoice2)
#    check4+=1
# print('========================================')











# num1=input("enter the first number:  ")
# num2=input("enter the second number:  ")
# opr=input("enter the operation:  ")
# if opr=="+":
#    print(num1,"+",num2,"=",int(num1)+int(num2))
# else:
#    choice=input("do you want to do another operation")
# while choice=='yes' :
#  num1=int(input("enter the first number:  "))
#  num2=int(input("enter the second number:  "))
# opr=input("enter the operation:  ")
# if opr=="-":
#    print(num1,"-",num2,"=",num1-num2)
# elif opr=="/":
#  print(num1,"/",num2,"=",num1/num2)
# elif opr=="*":
#  print(num1,"*",num2,"=",num1*num2)
# else:
#    print("invalid operation") 

# if choice=='no':
#    print("thank you")
   

   











#num1=int(input("enter the first number"))
#opr=(input("enter the operation"))
#num2=int(input("enter the second number"))



#['meta']['qrCode'])
#list methods
#x=[1,2,3,4]

#x.append() #بيضيفها ف الاخر
#x = ["apple", "banana", "cherry"]
#x.append(1)
#print(x)
#x.insert() #بيضيفها ف اي مكان انت عايزة
#x = [1,9,8]
#x.insert(1,55)
#print(x) 
#x.extend(y)
#x.extend(1,2,3,5,8,14) #بيضيف اكتر من حاجه 
#x = ["apple", "banana", "cherry"]
#x.extend([1,2])
#print(x)
#x=[1,2,3,4,5]
#x.pop(1) #  بديله (index)بيمسح من المكان اللي انت عايزة
#print(x)
#x = [1,9,8]
#x.clear()
#print(x)
#x.sort() #بيرتبها
#x.reverse() #بيعكسها
#x[1:3] #معناها من رقم واحد حتي رقم اتنين 
#x.remove("abdallah") #بديله الحاجه نفسها مش الindex
#x = ["w", "s", "e", "p"]
#x.remove("p")
#print(x) 
#len()  x[1:3] #الطول وعلاقته بالlist وعلاقته بالمدي
#x = [1,5,9,8,5,55,99,5,'ffff',5,9]
#y = int(len(x) / 2)
#print(y)
#print(x[y])
#print(x[-3])
#print(x[5:-1])

#y=x.coby()
#التبديل في ال list
#x = [1,5,"6",10]
#x[2]="35"
#print(x) 

#تبديل المدي في الlist
#x = ["abdallah", "ahmed","ali", "yasser", "sara", "mohamed"]
#x[1:3]=['sanabel','asss','mmmm']
#print(x)

# index fun

# x = [1, 3, 7, 8, 7, 5, 4, 6, 8, 5,3]

# print(x.index(3))

# count fun
# x = [1, 3, 7, 8, 7, 5, 4, 6, 8, 5]

# print(x.count(3))

# x =  'hello my name is abdallah'

# print(x.find('my'))

#x = ['a','d','c','g'] list
#y = [1,5,9,8] list
#z = dict(zip(x,y)) zip بتحولها الي ازواج dictبتحول الازواج الي  كييز وفاليو جوا الديكشنري 
#print(z)

#Username = input('1. Swimming, 2. Climbing, 3. Horseback riding, 4. Cycling. : ')
#x = Username.split(' , ')
#print(x)
#///////////////////////////////////////////////////////////////////////////////////



#DICTIONARY

#data = {
   # 'name' : 'abdallah',
#   'age' : 27,
#    'phone' : 11111,
#}
#data['age']=55
#print(data['age'])

#UserData = {

#}
#username = input('Please enter Username : ')
#age = int(input('Please enter Your Age : '))
#phone = input('Please enter Your Phone : ')

#UserData['username'] = username
#UserData['age'] = age
#UserData['phone'] = phone
#print(UserData)
#print(f'hello {username} your age is {age} and phone number is {phone}')

#Tuple (الزوج المرتب شبه الlist)
#x=[1,2,3,4] list
#x=(1,2,3,4) tuple لا يمكن التعديل بها او اضافه اي عنصر
#ف يا اما احولها الي قائمه يا اما استخدم الطريقه دي
#x = ("abdallah", "ahmed", "ali")

#y = ('ali',)

#x += y
#print(x)

#///////////////////////////////////////////


#Conditions




