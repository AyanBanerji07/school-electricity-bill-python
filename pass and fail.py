board = input("enter your board: ")
if board=="CBSE" or board=="cbse":
    marks_prac = float(input("enter your practical marks: "))
    if marks_prac>20:
        print("marks cant exceed maximum marks")
    else:
        pass
    marks_theory = float(input("enter your theory marks: "))

    if marks_theory>80:
        print("marks cant exceed maximum marks")
    else:
        pass

    if (marks_prac/20)*100>=35:
        print("you have passed in practical")
    else:
        print("you have failed in practical")

    if (marks_theory/80)*100>=35:
        print("you have passed in theory")
    else:
        print("you have failed theory")

elif board=="HSC" or board=="hsc":
    marks_prac_2 = float(input("enter your marks: "))
    marks_theory_2 = float(input("enter your marks: "))
    if marks_prac_2>20:
        print("marks cant exceed maximum marks")
    else:
        pass

    if marks_theory_2>80:
        print("marks cant exceed maximum marks")
    else:
        pass
    if ((marks_prac_2+marks_theory_2)/100)*100>=35:
        print("you have passed")
    else:
        print("you have failed")