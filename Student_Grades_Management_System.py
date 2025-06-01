

print("____________ Student Grades Management System______________")
data={}
st_name={}
st_id=""


#Add function
def add_student():
        
        print("**********ADD STUDENT**********")
        st_name = input("Enter new student name: ")
        st_id=input("Enter student id: ")
        arabic_grade=int(input("Enter arabic grade: "))
        math_grade=int(input("Enter math grade: "))
        english_grade=int(input("Enter english grade: "))
        science_grade=int(input("Enter science grade: "))

        data[st_name]={'name':st_name,'id':st_id,'arabic':arabic_grade,'math':math_grade,'english':english_grade,'science':science_grade}
        print(data)
        print(f'the total grades is {arabic_grade+math_grade+ english_grade+science_grade}')
        admin_panel()
        # print("Back To Admin Panel Or Back To Login Page???")
        # print("1.Back To Admin Panel")
        # print("2.Back To Log in Page")
        # ask_again=input("Enter number: ")
        # if ask_again=="1":
        #     admin_panel()
        # elif ask_again=="2":
        #     login()
        # else:
        #     print("Invalid input")
# add_student()
# delete function
def delete_student():
    print("**********DELETE STUDENT**********")
    st_name = input("Enter student name to delete: ")
    if st_name in data:
        del data[st_name]
    else:
        print("Student not found")
    print(data)
    admin_panel()
        
# delete_student()
#edit function
# def edit_student():
#     print("**********EDIT STUDENT**********")
#     for i in data.values():
#         st_id = input("Enter student id to edit: ")
#         if st_id == data[i]['id']:
#             print("valid id")
            
#         else:
#             print("Invalid id")
#             admin_panel()
        


# #admin panel function
def admin_panel():
    print("**********ADMIN PANEL**********")
    print("1. Add Student")
    print("2. Delete Student")
    print("3. Edit Student")
    print("4. Log Out")
    choice = input("Enter your choice: ")
    if choice=="1":
        add_student()
    elif choice=="2":
        delete_student()
    # elif choice=="3":
    #     edit_student()
    elif choice=="4":
        login()
    else:
        print("Invalid choice")
        
#student panal
def student_panal():
    print("**********STUDENT INFORMATION**********")
    student_name=input("Enter your name:  ")
    if student_name in data:
        print(f"your name is {data[student_name]['name']} and your id is {data[student_name]['id']}")
        # for student_name in data:
        print(f'your Arabic grade is {data[student_name]['arabic']}')
        print(f'your Math grade is {data[student_name]['math']}')
        print(f'your English grade is {data[student_name]['english']}')
        print(f'your Science grade is {data[student_name]['science']}')
        total=data[student_name]['arabic']+data[student_name]['math']+data[student_name]['english']+data[student_name]['science']
        print(f'the total grades is {data[student_name]['arabic']+data[student_name]['math']+data[student_name]['english']+data[student_name]['science']}')
        if total>=300:
            print("PASSED")
        else:
            print("FAILED")

    else:
        print("student not found")

#login function
def login():
    print("**********LOGIN**********")
    username = input("Enter your username: ").lower()
    password = input("Enter your password: ").lower()
    if username=="admin":
        print("You are an Admin")
        admin_panel()
    elif username=="student":
        print("You are a Student")
        student_panal()
    else:
        print("Invalid username or password")
    login()
        
login()
