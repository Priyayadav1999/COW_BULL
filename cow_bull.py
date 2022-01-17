import random

def create_list():
    list1 = [0,1,2,3,4,5,6,7,8,9]
    list2=[]
    n=5
    i=1
    while i<=n:
        a=random.choice(list1)
        list2.append(a)
        i+=1
    print(list2)
    return list2

def cow_bull():
    chances=10
    list2=create_list()
    list3=[]
    list4=[]

    for i in range(chances):
        guess_num=int(input("guess number in list2 = "))
        position=int(input("enter that guess number position = "))

        if guess_num in list2 and guess_num==list2[position]:
            list3.insert(position,guess_num)
            print("your number guess and position is right :- \n", list3)
        elif guess_num in list2:
            list4.append(guess_num)
            print("your number guesss is right but position is wrong :- \n ","you can use these numbers and try to guess right position \n", list4)
        
        print("you have chances left is :- ", chances-i+1)
        if len(list3)==len(list2):
            c=0
            for i in range(len(list2)):
                if list2[i]==list3[i]:
                    c+=1
            if c==len(list2):
                print("you won this game ")
                print("break")
                break
    if len(list3)!=len(list2):
        print("you lose this game")

cow_bull()

def try_again():
    check=input("you want to play again , yes or no :-")
    if check == "yes":
        cow_bull()
        
    else:
        print("you play very well , come again and play anytime ")

try_again()
