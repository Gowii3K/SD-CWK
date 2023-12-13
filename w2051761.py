# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code soluƟon.
# Student ID:  20517618
# IIT ID: 20230763
# Date: 08/12/2023

from graphics import *

def main():
    version=input("Type in 's' if you are a student or type in 't' if you are staff :")
    # enter student version if input is for student
    if version.lower()=="s":  
        entered_marks=get_credits()
        if entered_marks!=None:
            result=check_results(entered_marks)

    #enter staff version if input is t
    elif version.lower()=="t":
        while True:
            entered_marks=get_credits()
            if entered_marks!=None:
                    result=check_results(entered_marks)
                    histogram(result)
                    lst_extension(entered_marks,result)
                    retry=confirmation()
                    if retry==False:
                        ans=choice()
                        if ans==None:
                            break

        
            elif entered_marks== None:
                retry=confirmation()
                if retry==False:
                    ans=choice()
                    if ans==None:
                        break




    
#get credit details from user and check if all of them are integers
def get_credits():
    try:
        print("input should be in the range of 0,20,40,60,80,100,120")
        #reprompt if any input is not in valid range
        pass_cred=int(input("Enter pass credits :"))
        if pass_cred not in mark_range:
            print("out of range")
            return None
        defer_cred=int(input("Enter defer credits :"))
        if defer_cred not in mark_range:
            print("out of range")
            return None
        fail_cred=int(input("Enter fail credits :"))
        if fail_cred not in mark_range:
            print("Out of range")
            return None
    except ValueError:
        #repromt if any input is not an integer
        print("Integer required")
        return None
    entered_marks=[pass_cred,defer_cred,fail_cred]

    total=0

    for mark in entered_marks:
        total+=mark
        # check if mark total is acceptable if not reprompt
    if total!=120:
        print("Total incorrect")
        return None
    return entered_marks
    #return entered marks if all inputs are valid


def check_results(marks):
    if marks[0]==120:
        print("Progress")
        return "Progress"
    elif marks[0]>=100 and marks[0]<120:
        print("Progress (module trailer)")
        return "Progress (module trailer)"
    elif marks[2]>=80:
        print("Exclude")
        return "Exclude"
    else:
        print("Do not progress(module retriever)")
        return "Do not progress(module retriever)"
#update dictionary
def histogram(result):
    if result in results:
        results[result]+=1
#create result list
def lst_extension(marks,result):
    outcome.append([result,marks[0],marks[1],marks[2]])
# print result list
def display_lst():
    for i in outcome:       
        for j in i[0:3]:
            if j in results:
                print(j,end=" - ")
            else:
                print(j,end=", ")
        print(i[3])

# create the histogram
def output():
    totaloutcomes=len(outcome)
    win=GraphWin("Histogram",750,700)
    
    hisres=Text(Point(150,100),"Histogram Results")
    hisres.setStyle("bold")
    hisres.draw(win)

    totout=Text(Point(150,635),str(totaloutcomes)+" Outcomes in Total")
    totout.setStyle("bold")
    totout.draw(win)

    l1=Text(Point(150,600),"Progress")
    l1.draw(win)
    l2=Text(Point(300,600),"Trailer")
    l2.draw(win)
    l3=Text(Point(450,600),"Retriever")
    l3.draw(win)
    l4=Text(Point(600,600),"Excluded")
    l4.draw(win)
    point1=(550-(results["Progress"])*15)
    point2=(550-(results["Progress (module trailer)"])*15)
    point3=(550-(results["Do not progress(module retriever)"])*15)
    point4=(550-(results["Exclude"])*15) 




    box1=Rectangle(Point(100,550),Point(200,point1))
    box1.setFill("palegreen")
    box2=Rectangle(Point(250,550),Point(350,point2))
    box2.setFill("forestgreen")
    box3=Rectangle(Point(400,550),Point(500,point3))
    box3.setFill("darkolivegreen")
    box4=Rectangle(Point(550,550),Point(650,point4))
    box4.setFill("lightpink")

    box1.draw(win)
    box2.draw(win)
    box3.draw(win)  
    box4.draw(win)

    boxcount1=Text(Point(150,(point1-20)),results["Progress"])
    boxcount1.draw(win)
    boxcount2=Text(Point(300,(point2-20)),results["Progress (module trailer)"])
    boxcount2.draw(win)
    boxcount3=Text(Point(450,(point3-20)),results["Do not progress(module retriever)"])
    boxcount3.draw(win)
    boxcount4=Text(Point(600,(point4-20)),results["Exclude"])
    boxcount4.draw(win)

    win.getMouse()
    win.close()                          
#create text file with result list
def txtfile():
    resfile=open("results.txt","w")
    for i in outcome:
        for j in i[0:3]:
            if j in results:
                resfile.write(str(j))
                resfile.write(" - ")

            else:
                resfile.write(str(j))

                resfile.write(" , ")
        resfile.write(str(i[3]))
    resfile.close()
# reprompt for confirmation
def confirmation():
    confirmation="y"
    #keep repromtiing is user doesnt input y or q
    while confirmation!="y" or confirmation!="q":
        confirmation=input("'q' to quit or 'y' key to try again")
        if confirmation.lower()=="q":
            return False
        elif confirmation=="y":
            return True

#ask preferred method of output
def choice():
    while True:
        n=int(input("How do you want your output? Part1 (Histogram Only), Part2 (Histogram & List) or Part3 (Histogram,List & Text File)"))
        if n in choices:
            if n==1:
                output()            
                return
            elif n==2:
                output()
                display_lst()
                return
            elif n==3:
                output()
                display_lst()
                txtfile()
                return 


        


        
choices=[1,2,3]
mark_range=[0,20,40,60,80,100,120]   
results={"Progress":0,"Progress (module trailer)":0,"Exclude":0,"Do not progress(module retriever)":0}
outcome=[]
main()

