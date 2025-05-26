










# student_mark=int(input("Enter your mark"))

# if(student_mark >=85):
#     print("A")
# elif(student_mark>=75 and student_mark<85 ) :
#     print("B")
# elif(student_mark>=65 and student_mark <75):
#     print("C")
# else:
#     print("fail")














# data={
#     'ahmed' : {'name' :'ahmed', 'age' : 27, 
#                'phone' : {'num1': [12587,36985,8], 
#                           'num2' : [1,8,933,[89,{'ed' : 1478, 
#                                                  "ed2" : [78569,9631]}]]}}
# }
# user_phone=int(input ("enter your phone:..."))
# data["ahmed"]['phone']['num2'][3][1]['ed2'][1]=user_phone
# print(data)



# data={
# 'name':'sanabel',
# 'phone':1021452,
# }
# data["name"]='soso'
# print(data['name'])






#Day_1 TASKS///////////////////////////////////////////////////
# 1)) Write a Python program that calculates the area of a circle based on the radius entered by the user.
Redias=int(input("enter the Redias of the Circle:..."))
print("the area of the circle is"," ",3.14*(Redias**2))

# 2)) Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.
f_name=str(input("Enter your first name.."))
l_name=str(input("Enter your last name.."))
print("your verse name is...",l_name,f_name)

# 3))  Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn
n=input("Enter a number: ") #n هتبقيstring
n2=n+n #n+n علشان هي بstring هتبقي 55
n3=n+n+n #n+n+n علشان هي بstring 555 هتبقي
print(int(n)+int(n2)+int(n3)) #هنا هتتحول لارقام ف هيبقي المجموع 5+55+555

# 4)) Write a Python program to display the examination schedule. (extract the date from exam_st_date).
exam_st_day =int(input("enter exam day:...."))
exam_st_month =int(input("enter exam month:...."))
exam_st_year =int(input("enter exam year:...."))
print("the examination schedule is...",exam_st_day,"/",exam_st_month,"/",exam_st_year)





#Day_2 TASKS//////////////////////////////
# 1)) Write a Python program to combine two lists into a dictionary.
com_dic={}
k_list=["name","age","phone","id"]
v_list=["John","25","123456"]

x=len(k_list)
print(x)
y=len(v_list)
print(y) #اذن هاخد اول 3 بس
com_dic[k_list[0]]=v_list[0]
com_dic[k_list[1]]=v_list[1]
com_dic[k_list[2]]=v_list[2]
print(com_dic)

# 2)) Write a Python program to display the first and last colors from the following list.
color_list = ["Red","Green","White" ,"Black"]
#print(color_list[0]," ",color_list[-1])
print(f'the first color is: {color_list[0]} and the last color is: {color_list[-1]} ')

# 3)) Ask the user for their name, age, city of residence, and job title.
# After obtaining the data and storing it in a dictionary, ask the user to enter their hobbies from the given options. They will enter numbers for each hobby, for example:
# 1. Swimming, 2. Climbing, 3. Horseback riding, 4. Cycling.
user_dic={}
user_name=input("Enter your name:...")
user_age=int(input("Enter your age:..."))
user_city=input("Enter your city:...")

user_dic['user_name']=user_name
user_dic['user_age']=user_age
user_dic['user_city']=user_city
print(f'hello {user_name} your age is:{user_age}')

user_job=input("Enter your job:...")
user_dic['user_job']=user_job

user_hobby_num=int(input("Enter your hobby number from these choices  (1-Swimming ,2-Climbing ,3-Horsebackriding ,4-Cycling) :..."))
y=len(user_hobby_num)
user_dic['user_hobby_num']=user_hobby_num
print(f'your job is: {user_job} your hobby is:{y}')







#Day_3 TASKS//////////////////////////////
#1)) Write a Python program that asks the user to enter a number and 
# tells him whether it is an even or odd number.
usernum1=int(input("Enter a number:..."))
usernum2=usernum1%2
if(usernum2==0):
    print("this is an even number")  
elif(usernum2==1):
    print("this is an odd number")
else:
    print("Error")
    
    
#2)) Write a Python program to check if a triangle is equilateral, isosceles or scalene.
first_side=int(input("Enter the first side:.... "))
second_side=int(input("Enter the second side:.... "))
third_side=int(input("Enter the third side:.... "))

if(first_side==second_side==third_side):
    print("It is An equilateral triangle")
elif(first_side==second_side)and first_side!=third_side:
    print("It is An isosceles triangle")
elif(second_side==third_side)and second_side!=first_side:
    print("It is An isosceles triangle")
elif(first_side==third_side)and first_side!=second_side:
    print("It is An isosceles triangle")
elif(first_side!=second_side!=third_side):    
    print("It is A scalene triangle")
else:
    print("Error")  
    
    
    
#3)) Write a Python program to find the median of three values.   
med_user_num=input("Enter three number each one followed by a space ")
med_user_num_sp=med_user_num.split(' ')
print(f'the meadian number is {med_user_num_sp[1]}')




#4)) Write a Python program to create the multiplication table (from 1 to 10) of a number.
usernumber=int(input("Enter a number:..."))
print(f'the multiplication table of {usernumber} is:')
print(f'1*{usernumber}={1*usernumber}')
print(f'2*{usernumber}={2*usernumber}')
print(f'3*{usernumber}={3*usernumber}')
print(f'4*{usernumber}={4*usernumber}')
print(f'5*{usernumber}={5*usernumber}')
print(f'6*{usernumber}={6*usernumber}')
print(f'7*{usernumber}={7*usernumber}')
print(f'8*{usernumber}={8*usernumber}')
print(f'9*{usernumber}={9*usernumber}')
print(f'10*{usernumber}={10*usernumber}')









#Day_4 TASKS//////////////////////////////( Products System)
#4))
# Write a supermarket management program.
# There is a database containing the following: the name of each product, 
# the quantity available in the warehouse, whether it is on sale, 
# the product's price, and the product's section.
# The program displays the product name, the price per item, 
# and a brief description. It displays all products in a simple and attractive way, 
# with each product having its own unique number.
# Then, the user is prompted to first select the product numbers they want to purchase. 
# After entering the numbers, a request appears, 
# specifying the required quantities for each product.
# Then, the purchase invoice displays the product name, 
# the price per item, the price per selected item, the quantity for each product, 
# and the total amount due. A discount is added to the product, 
# if applicable, and this is noted on the invoice. Example:
#
# ===============Welcome===============
# product 1 :
# Name -> milk
# Price -> 10$
# Description -> Fresh and healthy milk
# -----
# product 2 :
# Name -> Rice
# Price -> 20$
# Description -> Premium and pure rice
# -----
# product 3 :
# Name -> Bread
# Price -> 2$
# Description -> fresh bread
# =====================================
# Please write the numbers of the products you want to buy like this 1,2 : 1,3
# Please write the value of each product you want to purchase in order of your previous selection : 2,5
#
# ================Purchase Invoice================
# Product Name        Price per piece        Number of pieces        Total price
#
# milk                10$                    2                       20$
# Bread               2$                     5                       10$
#
# Total due before discount : 30$
# Total due after discount  : 25$

products={
   'product1':{
   'name':"milk",
   'price':10,
   'description':'Fresh and healthy milk',
   'quantity': 40,
   'on_sale' : False
},

   'product2':{
   'name':"Rice",
   'price':50,
   'description':'Premium and pure rice',
   'quantity': 60,
   'on_sale' : True
},


'product3':{
   'name':"Bread",
   'price':10,
   'description':'Fresh bread',
   'quantity': 100,
   'on_sale' : False
}

}

x=list(products.keys())
print('=================Welcome===================')
check=0
while check<len(x):
 print(f'{x[check]}:')
 print(f'Name<={products[x[check]]['name']}')
 print(f'Price<={products[x[check]]['price']}')

 print(f'Description<={products[x[check]]['description']}')
 print('!!!!!!!!!!!!!!!!!')
 check+=1
print('========================================')



products_number=input("enter products number you want to order like this 1 2: ")
products_quantity=input("enter products quantities you want to order like this 6 5: ")
print('========================================')

x2=products_number.split(' ')
x3=products_quantity.split(' ')
x_mix=dict(zip(x2,x3))
x_mix_keys=list(x_mix.keys())
x_mix_values=list(x_mix.values())

check3=0
# print(x[z])
while check3<len(x_mix_keys):
   y=x_mix_keys[check3]#2
   y2=x_mix_values[check3]
   z=int(y)-1#2-1=1
   print(f'you have ordered {products[x[z]]['name']} for quantites: {int(y2)}')
   


  
   check3+=1
   # total2=list(total)
   # print(total2)
print('========================================')

Purchase_Invoice=['Product Name','Price per piece','Number of pieces','Total price']#دي كل مرة بتتكرر
print(Purchase_Invoice)

check4=0
while check4<len(x_mix_keys):
   y=x_mix_keys[check4]#2
   y2=x_mix_values[check4]
   z=int(y)-1#2-1=1

   price=products[x[z]]['price']
# print(price)
   total=price*int(y2)
   Purchase_Invoice2=[products[x[z]]['name'],products[x[z]]['price'],int(y2),total]
   print(Purchase_Invoice2)
   check4+=1
print('========================================')









#Day_6 TASKS//////////////////////////////
#1)) Print only even numbers from 1 to n
n=input("enter a number: ")
for i in range(1,int(n),2):
    print(i)

#2))Write a function that adds all the numbers in a list.
numbers=[5,10,12,14,20]
total=0
for i in range(0,len(numbers)):
    total+=numbers[i]

print(total)


#3)) text = 'hello my name is abdallah' -> 4

# number of specific letters in a text
user_text=input("enter A text: ").lower() #any string is a list of its value (hello sanabel)<<=[h,e,l,l,o,s,a,n,a,b,e,l]
specifi_letter='a'
total=0
for i in user_text:
    if i==specifi_letter:
        total+=1
print(total)

#4)) Print triangle stars
#        *
#        **
#        ***
#        ****
#        *****
#        ******
#        *******
#        ********
#        **********
#        ***********
stars=['*',['*,*'],['*,*,*'],['*,*,*,*'],['*,*,*,*,*'],['*,*,*,*,*,*'],['*,*,*,*,*,*,*'],['*,*,*,*,*,*,*,*'],['*,*,*,*,*,*,*,*,*'],['*,*,*,*,*,*,*,*,*,*']]
for i in stars:
    for u in i:
        print(u)