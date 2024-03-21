#I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
#Any code taken from other sources is referenced within my code solution.
#Student ID : w1953254
#Date : 04/12/2022

#iterating variable for multiple inputs
user = "y"
                                
credits_list =[] 

progress =0
Exclude =0
trailer =0        
retriever =0

def creditsrangechecker(credits):           #To check the range
        if credits in range(0,121,20):
            return True
        print("out of range")
        return False



while True:
    try:
        mode=int(input("Enter mode 1 for student version or 2 for staff version: "))
        if mode==1:
            while True:
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
                    except ValueError:                  #Requiring a integer
                        print("integer required")
                total = pass_credit + defer_credit + fail_credit    #Total credits

                if total !=120:                         #Incorrect total                 
                    print("total incorrect")
                    continue            
                elif pass_credit ==120:
                    print("Progress")
                elif (fail_credit ==100) or (fail_credit==80) or (fail_credit==120):
                    print("Exclude")      
                elif pass_credit ==100:                                                                                                       
                    print("Progress (module trailer)")
                else:
                    print("Module retriever")

                break
            break

        
        elif mode ==2:
            while user !="q":                         #Iteration for multiple outcomes
                while True:
                    try:
                        pass_credit =int(input("Enter your total PASS credits :"))
                        if creditsrangechecker(pass_credit):
                            break
                    except ValueError:
                        print("integer required")       #Requiring a integer     
                
                while True:
                    try:    
                        defer_credit =int(input("Enter your total DEFER credits :"))
                        if creditsrangechecker(defer_credit):
                            break
                    except ValueError:
                        print("integer required")       #Requiring a integer
                
                while True:
                    try:
                        fail_credit =int(input("Enter your total FAIL credits :"))
                        if creditsrangechecker(fail_credit):
                            break
                    except ValueError:                  #Requiring a integer
                        print("integer required")
                total = pass_credit + defer_credit + fail_credit    #Total credits
                
                if total !=120:                         #Incorrect total                 
                    print("total incorrect")
                    continue            
                elif pass_credit ==120:
                    print("Progress")
                    credits_list.append("Progress - "+ str(pass_credit) + ", "  + str(defer_credit) + ", " + str(fail_credit))
                    print()
                    progress =progress+1
                elif (fail_credit ==100) or (fail_credit==80) or (fail_credit==120):
                    print("Exclude")
                    credits_list.append("Exclude - "+ str(pass_credit) + ", "  + str(defer_credit) + ", " + str(fail_credit))
                    print()
                    Exclude =Exclude +1        
                elif pass_credit ==100:                                                                                                                                      
                    print("Progress (module trailer)")
                    credits_list.append("Progress (module trailer) - "+ str(pass_credit) + ", "  + str(defer_credit) + ", " + str(fail_credit))
                    print()
                    trailer =trailer+1
                else:
                    print("Module retriever")
                    credits_list.append("Module retriever - "+ str(pass_credit) + ", "  + str(defer_credit) + ", " + str(fail_credit))
                    print()
                    retriever =retriever +1
                
                while True:  
                    user =input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results:")
                    if user=="y" or user=="q":
                        print()
                        break
                    else:
                        print("wrong input")
                    print()
            
            totaloutcomes = progress + trailer + retriever + Exclude
            
            def histrogram():                   #Histogram
                print("-------------------------------------------------------")
                print("Histogram")
                print(f"Progress {progress}\t: {progress * '*'}")
                print(f"Trailer {trailer}\t: {trailer * '*'}")
                print(f"Retriever {retriever}\t: {retriever * '*'}")
                print(f"Excluded {Exclude}\t: {Exclude * '*'}")
                print()
                print(totaloutcomes, "outcomes in total.")
                print("--------------------------------------------------------")
            histrogram()
#part 2 
            def datalist():                        #List
                    for i in credits_list:
                        print(i)
            datalist()
#part 3 
            def textfile():
                with open('textfile.txt','w') as x:
                    for i in credits_list:
                        x.write(i+"\n")
                with open('textfile.txt','r') as y:
                        print(y.read())
            textfile()
            break
        
        else:
            print("Enter the correct number")

    except ValueError:
        print("Enter the correct number")




