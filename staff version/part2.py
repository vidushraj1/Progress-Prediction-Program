# I declare that my work contains no examples of misconduct, such as plagiarism , or collusion.

#Any code taken from other sources is referenced within my code solution.

#Student ID: 20210914

#Date: 08/12/2021

def verti_histo():   #this function will print vertical histogram of all progression outcomes
    import part1
    from part1 import count1
    from part1 import count2
    from part1 import count3
    from part1 import count4
    from part1 import tot_count
    global count1
    global count2
    global count3
    global count4
    global tot_count

    #References
    ##this logic expression is learnt from a website called stackoverflow
    ###webaddress"https://stackoverflow.com/questions/53285446/how-do-i-make-print-vertically-on-python-loops?answertab=oldest#tab-top"

    print("\n")
    progress_value = str(count1)
    trailer_value = str(count2)
    retriever_value = str(count3)
    excluded_value = str(count4)
    topics=['Progress',progress_value,"|",'Trailer',trailer_value,"|",'Retriever',retriever_value,"|",'Excluded',excluded_value]
    print(' '.join(topics))
    for i in range(max(count1,count2,count3,count4)):
        print("     {0}          {1}            {2}             {3}" . format(
            '*' if i<count1 else " ",
            '*' if i<count2 else " ",
            '*' if i<count3 else " ",
            '*' if i<count4 else " "))
    print("\n"+str(tot_count),"number of outcomes in total")
