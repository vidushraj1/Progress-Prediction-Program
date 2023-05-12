# I declare that my work contains no examples of misconduct, such as plagiarism , or collusion.

#Any code taken from other sources is referenced within my code solution.

#Student ID: 20210914

#Date: 08/12/2021

def hori_histo2():   #this function will print histogram where all outcomes will appear with the values for pass, defer and fail
    import part1
    from part1 import results
    from part1 import pass_array
    from part1 import defer_array
    from part1 import fail_array
    from part1 import context_d
    global results
    global pass_array
    global defer_array
    global fail_array
    global context_d
    print("\n")
    length = len(pass_array)
    for count in range(length):
        context = results[count]+" "+"-"+" "+str(pass_array[count])+","+" "+str(defer_array[count])+","+" "+str(fail_array[count])
        context_d.append(context)
        print(context)
