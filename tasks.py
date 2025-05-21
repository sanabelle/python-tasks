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



