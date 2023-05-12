# I declare that my work contains no examples of misconduct, such as plagiarism , or collusion.

#Any code taken from other sources is referenced within my code solution.

#Student ID: 20210914

#Date: 08/12/2021

credit_range = [0,20,40,60,80,100,120]    #this list contains acceptable input values
count1 = 0
count2 = 0
count3 = 0
count4 = 0
tot_count = 0
results = []    #an empty list is created to store the result(string)
pass_array = []    #an empty list is created to store the pass values
defer_array = []    #an empty list is created to store the defer values
fail_array = []      #an empty list is created to store the fail values
context_d = []   ##an empty list is created to store the data which is to be stored in text files
def pass_credit():    #this function is used to obtain the pass value
    global tot
    global pass_
    global pass_array
    tot = 0
    pass_ = 121
    while pass_ > 120 or pass_ not in credit_range:
        try:
            pass_ = int(input("\nPlease enter your credits at pass:"))
            if pass_ not in credit_range:
                print("Out of range")
                continue
            else:
                tot = tot + pass_
                pass_array.append(pass_)
        except ValueError:
            print("Integer required")
            continue
    return tot
    return pass_

def defer_credit():    #this function is used to obtain the defer value
    global tot
    global defer_
    global defer_array
    defer_ = 121
    while defer_ > 120 or defer_ not in credit_range:
        try:
            defer_ = int(input("Please enter your credits at defer:"))
            if defer_ not in credit_range:
                print("Out of range.")
                continue
            else:
                tot = tot + defer_
                defer_array.append(defer_)
        except ValueError:
            print("Integer required")
            continue
    return tot
    return defer_

def fail_credit():    #this function is used to obtain the fail value
    global tot
    global fail_
    global fail_array
    fail_ = 121
    while fail_ > 120 or fail_ not in credit_range:
        try:
            fail_ = int(input("Please enter your credits at fail:"))
            if fail_ not in credit_range:
                print("Out of range.")
                continue
            else:
                tot = tot + fail_
                fail_array.append(fail_)
        except ValueError:
            print("Integer required")
            continue
    return tot
    return fail_

def total():    #this function checks whether total in correct or incorrect
    global tot
    while tot > 120 or tot != 120:
        print("Total Incorrect")
        pass_credit()
        defer_credit()
        fail_credit()

def result():    #this function will print the progression of the student
    global pass_
    global defer_
    global fail_
    global count1
    global count2
    global count3
    global count4
    global tot_count
    global results
    if pass_ == 120:
        text = "Progress"
        print(text)
        count1 = count1 + 1
        results.append(text)
    else:
        if pass_ == 100 and (defer_ == 20 or fail_ == 20):
            text = "Progress(module trailer)"
            print(text)
            count2 = count2 + 1
            results.append(text)
        else:
            if pass_ < 100 and fail_ <= 60:
                text = "Module retriever"
                print(text)
                count3 = count3 +1
                results.append(text)
            else:
                if pass_ < 100 and fail_ >60:
                    text = "Exclude"
                    print(text)
                    count4 = count4 + 1
                    results.append(text)
    tot_count = count1 + count2 + count3 + count4
    return count1,count2,count3,count4,tot_count

def hori_histo1():   #this function will print horizontal histogram of all progression outcomes
    global count1
    global count2
    global count3
    global count4
    global tot_count
    while True:
        print("\nWould you like to enter another set of data?")
        Y_N = input("Enter 'y' for yes or 'q' to quit and view results:")
        if Y_N == "y" or Y_N == "Y":
            pass_credit()
            defer_credit()
            fail_credit()
            total()
            result()
        elif Y_N == "q" or Y_N == "Q":
            print("\n--------------------------------------------------")
            print("Horizontal Histogram")
            print("Progress ",str(count1)+":",count1*"*")
            print("Trailer  ",str(count2)+":",count2*"*")
            print("Retriever",str(count3)+":",count3*"*")
            print("Excluded ",str(count4)+":",count4*"*")
            print("\n"+str(tot_count)+" outcomes in total.")
            print("--------------------------------------------------")
            break
