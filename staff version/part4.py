# I declare that my work contains no examples of misconduct, such as plagiarism , or collusion.

#Any code taken from other sources is referenced within my code solution.

#Student ID: 20210914

#Date: 08/12/2021

def text_file():   #this function is used to produce a text file and then print that text file
    import part3
    from part3 import context_d
    global context_d
    length = len(context_d)
    for count in range(length):
        file1 = open("Progression.txt", "a")
        file1.write(context_d[count])
        file1.write("\n")
        file1.flush()
        file1.close()

    print("\n")
    file1 = open('Progression.txt', 'r')
    Lines = file1.readlines()
    count = 0
    for line in Lines:
        count = count + 1
        text = line.format(count, line.strip())
        print(text.strip())
