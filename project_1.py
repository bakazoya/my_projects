print("welcome to my computer quiz")
playing=input("do you want to play? ")

if playing.lower()!="yes":
    quit()
print("okay! let's play :)")
score=0

answer=input("what does cpu stand for? ").lower()
if answer=="central processing unit":
    print("correct! ")
    score+=1
else:
    print("incorrect! ")

answer=input("what does gpu stands for? ").lower()
if answer=="graphical processing unit":
    print("correct! ")
    score+=1
else:
    print("incorrect! ")


answer=input("what does ram stand for? ").lower()
if answer=="random access memory":
    print("correct! ")
    score+=1
else:
    print("incorrect! ")   


answer=input("what does psu stand for? ").lower()
if answer=="power supply":
    print("correct! ")
    score+=1
else:
    print("incorrect! ")    
print("you got "+str(score)+ " questions correct")
print("you got "+str((score/4)*100)+ " %")

