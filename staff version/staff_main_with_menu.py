# I declare that my work contains no examples of misconduct, such as plagiarism , or collusion.

#Any code taken from other sources is referenced within my code solution.

#Student ID: 20210914

#Date: 08/12/2021

##this code displays a menu and gives results according to the selected option/type.

import part1
import part2
import part3
import part4
while True:
    print("---------------------------------------------------------------------------")
    print("Type 1 : To view the Horizontal Histogram\n")
    print("Type 2 : To view the Horizontal and Vertical Histogram\n")
    print("Type 3 : To view the Detailed Horizontal Histogram with other Histograms\n")
    print("Type 4 : To view all Histograms and Create, Save and display File\n")
    print("Type anything to exit\n")
    print("---------------------------------------------------------------------------")
    try:
        sel = int(input("Enter any type mentioned above:"))
        if sel == 1:
            part1.pass_credit()
            part1.defer_credit()
            part1.fail_credit()
            part1.total()
            part1.result()
            part1.hori_histo1()
        elif sel == 2:
            part1.pass_credit()
            part1.defer_credit()
            part1.fail_credit()
            part1.total()
            part1.result()
            part1.hori_histo1()
            part2.verti_histo()
        elif sel == 3:
            part1.pass_credit()
            part1.defer_credit()
            part1.fail_credit()
            part1.total()
            part1.result()
            part1.hori_histo1()
            part2.verti_histo()
            part3.hori_histo2()
        elif sel == 4:
            part1.pass_credit()
            part1.defer_credit()
            part1.fail_credit()
            part1.total()
            part1.result()
            part1.hori_histo1()
            part2.verti_histo()
            part3.hori_histo2()
            part4.text_file()
        break
    except ValueError:
        print("enter an integer")
