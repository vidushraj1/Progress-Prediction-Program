# I declare that my work contains no examples of misconduct, such as plagiarism , or collusion.

#Any code taken from other sources is referenced within my code solution.

#Student ID: 20210914

#Date: 08/12/2021

credit_range = [0,20,40,60,80,100,120]  #this list contains acceptable input values
def pass_credit():   #this function is used to obtain the pass value
    global tot
    global pass_
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
        except ValueError:
            print("Integer required")
            continue
    return tot
    return pass_

def defer_credit():    #this function is used to obtain the defer value
    global tot
    global defer_
    defer_ = 121
    while defer_ > 120 or defer_ not in credit_range:
        try:
            defer_ = int(input("Please enter your credits at defer:"))
            if defer_ not in credit_range:
                print("Out of range.")
                continue
            else:
                tot = tot + defer_
        except ValueError:
            print("Integer required")
            continue
    return tot
    return defer_

def fail_credit():   #this function is used to obtain the fail value
    global tot
    global fail_
    fail_ = 121
    while fail_ > 120 or fail_ not in credit_range:
        try:
            fail_ = int(input("Please enter your credits at fail:"))
            if fail_ not in credit_range:
                print("Out of range.")
                continue
            else:
                tot = tot + fail_
        except ValueError:
            print("Integer required")
            continue
    return tot
    return fail_

def total():   #this function checks whether total in correct or incorrect
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
    if pass_ == 120:
        print("Progress")
    else:
        if pass_ == 100 and (defer_ == 20 or fail_ == 20):
            print("Progress(module trailer)")
        else:
            if pass_ < 100 and fail_ <= 60:
                print("Module retriever")
            else:
                if pass_ < 100 and fail_ >60:
                    print("Exclude")

