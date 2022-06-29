Number_of_Classes_Abel_is_taking=None
while Number_of_Classes_Abel_is_taking==None:
    try:
        Number_of_Classes_Abel_is_taking=int(input("How many subjects are you taking? "))
    except:
        print("Error, Please enter number!\n")
output=0
i=0
while i<Number_of_Classes_Abel_is_taking:
    grade=input("Enter your grade in letter for the %s class "%(str(i+1) ))
    grade=grade.upper()
    if grade=='A+' or grade== 'A' or grade== 'A-' or grade== 'B+' or grade== 'B' or grade== 'B-' or grade=='C+' or grade== 'C' or grade== 'C-' or grade== 'D' or grade== 'F':
        i+=1
        if grade== 'A+':
            output+=4
        elif grade== 'A':
            output+=4
        elif grade=='A-':
            output+=3.75
        elif grade== 'B+':
            output+=3.5
        elif grade== 'B':
            output+=3.0
        elif grade== 'B-':
            output+=2.75
        elif grade== 'C+':
            output+=2.5
        elif grade== 'C':
            output+=2.0
        elif grade== 'C-':
            output+=1.75
        elif grade== 'D':
            output+=1
        elif grade== 'F':
            output+=0
        print (output)
    else:
        print ("invalid grade, PLEASE ENTER : A+, A, A-, B+, B, B-, C+, C, C-, D, F!\n")
average="%.2f" % (float(output)/float(Number_of_Classes_Abel_is_taking))
print("Your GPA is: %s" %(str(average)))