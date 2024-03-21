#I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
#Any code taken from other sources is referenced within my code solution.
#Student ID : w1953254
#Date : 04/12/2022

#iterating variable for multiple inputs
user = "y"

dictionary_ ={}

StudentId_list =[]

def creditsrangechecker(credits):           #To check the range
        if credits in range(0,121,20):
            return True
        print("out of range")
        return False
                               
while user !="q":
    try:
        while True:
            Student_Id =input("Enter the Student_Id :")
            if Student_Id in StudentId_list : #check the student id is already in the data base
                print("The Student_Id is already in database please enter a another Student_Id")
                continue
            #student id check
            if len(Student_Id) ==8 and Student_Id[0]=="w" and int(Student_Id[1:8]):
                break
            else:
                print("Not valid Student Id")
    except ValueError:
        print("Not valid Student Id")
        continue
            
    
    while True:
        try:
            pass_credit =int(input("Please enter your credits at pass :"))
            if creditsrangechecker(pass_credit):
                break
        except ValueError:
            print("integer required")       #Requiring a integer     

    while True:
        try:    
            defer_credit =int(input("Please enter your credits at defer :"))
            if creditsrangechecker(defer_credit):
                break
        except ValueError:
            print("integer required")       #Requiring a integer

    while True:
        try:
            fail_credit =int(input("Please enter your credits at fail :"))
            if creditsrangechecker(fail_credit):
                break
        except ValueError:                  
            print("integer required")     #Requiring a integer

    total = pass_credit + defer_credit + fail_credit   #Total credits
    if total !=120:
        pass
    else:
        StudentId_list.append(Student_Id)    
    
    if total !=120:                         #Incorrect total                 
        print("total incorrect")
        continue           
    elif pass_credit ==120:
        print("Progress")
        dictionary_.update({Student_Id:"Progress - "+ str(pass_credit) + ", "  + str(defer_credit) + ", " + str(fail_credit)})
        print()

    elif (fail_credit ==100) or (fail_credit==80) or (fail_credit==120):
        print("Exclude")
        dictionary_.update({Student_Id:"Exclude - "+ str(pass_credit) + ", "  + str(defer_credit) + ", " + str(fail_credit)})
        print()
       
    elif pass_credit ==100:                                                                                                                                      
        print("Progress (module trailer)")
        dictionary_.update({Student_Id:"Progress (module trailer) - "+ str(pass_credit) + ", "  + str(defer_credit) + ", " + str(fail_credit)})
        print()

    else:
        print("Module retriever")
        dictionary_.update({Student_Id:"Module retriever - "+ str(pass_credit) + ", "  + str(defer_credit) + ", " + str(fail_credit)})
        print()
    
    while True:  
        user =input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results:")
        if user=="y" or user=="q":
            print()
            break
        else:
            print("wrong input")
        print()

for (k,v) in dictionary_.items():
        print(k,":",v,end=' ')
