# # # # # # # # # # # # # # # # # # c="ReD"
# # # # # # # # # # # # # # # # # # match c:
# # # # # # # # # # # # # # # # # #     case "ReD":
# # # # # # # # # # # # # # # # # #         print("R")
# # # # # # # # # # # # # # # # # #     case "Green":
# # # # # # # # # # # # # # # # # #         print("G")
# # # # # # # # # # # # # # # # # #     case _:
# # # # # # # # # # # # # # # # # #         print("NO COLOUR")
# # # # # # # # # # # # # # # # # t=20
# # # # # # # # # # # # # # # # # t+=2
# # # # # # # # # # # # # # # # # print(t)
# # # # # # # # # # # # # # # # # t*=2
# # # # # # # # # # # # # # # # # print(t)
# # # # # # # # # # # # # # # # marks1=90
# # # # # # # # # # # # # # # # marks2=90
# # # # # # # # # # # # # # # # marks3=90
# # # # # # # # # # # # # # # # marks4=90
# # # # # # # # # # # # # # # # marks5=90
# # # # # # # # # # # # # # # # total= marks1+marks2+marks3+marks4+marks5
# # # # # # # # # # # # # # # # percentage=total/5
# # # # # # # # # # # # # # # # print(percentage)
# # # # # # # # # # # # # # # # # if marks1>=90 and percentage>=90:
# # # # # # # # # # # # # # # # #     print("Grade A")
# # # # # # # # # # # # # # # # # if marks2>=75 and percentage>=80:
# # # # # # # # # # # # # # # # #     print("Grade B")
# # # # # # # # # # # # # # # # # if marks3>=50 and percentage>=70:
# # # # # # # # # # # # # # # # #     print("Grade C")
# # # # # # # # # # # # # # # # # if marks4>=35 and percentage>=50:
# # # # # # # # # # # # # # # # #     print("Grade D")
# # # # # # # # # # # # # # # # # if marks5>=20 and percentage>=30:
# # # # # # # # # # # # # # # # #     print("FAIL")    
# # # # # # # # # # # # # # # marks=91
# # # # # # # # # # # # # # # if marks>90:
# # # # # # # # # # # # # # #     if marks<100:
# # # # # # # # # # # # # # #         print("Grade A")
# # # # # # # # # # # # # # #     else:
# # # # # # # # # # # # # # #         print("PASS")
# # # # # # # # # # # # # # # else:
# # # # # # # # # # # #     print("Fail")
# # # # # # # # # # # # for i in range(1,10):
# # # # # # # # # # # #     print("Garv is a Good boy",i)
# # # # # # # # # # # # count=1
# # # # # # # # # # # # while count<6:
# # # # # # # # # # # # #     print("HELLO WOWRLD")
# # # # # # i=10
# # # # # # while i<=90:
# # # # # #     print(i)
# # # # # #     i+=1
# # # # # # # # # # # # sum=1
# # # # # # # # # # # # for i in range(11):
# # # # # # # # # # # #     sum=sum+i
# # # # # # # # # # # #     print(sum)
# # # # # # # # # # # # count=1
# # # # # # # # # # # # while count<=11:
# # # # # # # # # # # #     print(count)
# # # # # # # # # # # #     count+=2
# # # # # # # # # # # # count=160
# # # # # # # # # # # # while count>=33:
# # # # # # # # # # # #     print(count)
# # # # # # # # # # # #     count-=3
# # # # # num1=6
# # # # # num2=20
# # # # # if num1>num2:
# # # # #     num1,num2=num2,num1
# # # # # sum_even=0
# # # # # print("even numbers between",num1,"and",num2,"are:")
# # # # # for i in range(num1,num2+1):
# # # # #     if i%2==0:
# # # # #         print(i)
# # # # #         sum_even=sum_even+i
# # # # # print("sum of all even numbers is:",sum_even)
# # # # # for i in range(20):
# # # # #    if i==10:
# # # # #     continue
# # # # #    print(i)
# # # # # n=5
# # # # # for i in range(1,n+1):
# # # # #     print(' '*(n-i),end=" ")
# # # # #     for j in range(1,i+1):
# # # # #         print("*",end="")
# # # # #     print()
# # # # # n=5
# # # # # for i in range(n,0,-1):
# # # # #     for j in range(i,0,-1):
# # # # #         print(j,end=" ")
# # # # #     print()
# # # # # def sum(a,b):
# # # # #     sum=a+b
# # # # #     print("sum is=",sum)
# # # # # sum(69,1)
# # # # # sum(40,30)
# # # # # sum(90,80)
# # # # # sum(68,1)
# # # # # year=2024
# # # # # if(year%4==0 and year%100!=0) or (year%400==0):
# # # # #     print(year,"is a leap year")
# # # # # else:
# # # # #     print(year,"is not a leap year")
# # # # # # def addition():
# # # # # #     num1=2
# # # # # #     num2=2
# # # # # #     print("result=",num1+num2)
# # # # # def subtraction():
# # # # #     num1=5
# # # # #     num2=2
# # # # #     print("result=",num1-num2)
# # # # # #     if num2!=0:
# # # # # #        print("result=",num1/num2)
# # # # # #     else:
# # # # # #         print("division by zero is not allowed")
# # # # # # choice='a'
# # # # # # if choice=='a':
# # # # # #     addition()
# # # # # # elif choice=='s':
# # # # # #     subtraction()
# # # # # i=10
# # # # # while i<90:
# # # # #     print(i)
# # # # #     i+=10
# # # # # a=40
# # # # # b=80
# # # # # if a>b:
# # # # #     a,b=b,a
# # # # # sum=0
# # # # # print("sum of all numbers between",a, "and" ,b,"are:")
# # # # # for i in range(a,b+1):
# # # # #     if i%2==0:
# # # # #         print(i)
# # # # #     sum=sum+i
# # # # # print("Sum of all even numbers are",sum)
# # # # # n=8
# # # # # for i in range(n,0,-1):
# # # # #     for j in range(i,0,-1):
# # # # #         print(j,end=" ")
# # # # #     print()
# # # # # a=2
# # # # # b=10
# # # # # if a>b:
# # # # #     a,b=b,a
# # # # # sum_even=0
# # # # # print("all even number between",a,"and",b,"are:")
# # # # # for i in range(a,b+1):
# # # # #     if i%2==0:
# # # # #      print(i)
# # # # #      sum_even=sum_even+i
# # # # # print("sum of even numbers between",sum_even)
# n=5

# # # age=25
# # # if age>13 and age<19:
# # #     print("You are a teenager")
# # # else:
# # #     print("you are not a teenager")
# # ch="h"
# # ch=ch.lower()
# # if ch in('a','e','i','o','u'):
# #     print("VOWEL")
# # else:
# #     print("consonent")
# # count=0
# # for i in range(5,101):
# #    if i%5==0:
# #     print(i)
# #     count+=1
# # print("total number divisible by 5 between 1 and 100 are:",count)
# n=5
# for i in range(1,n+1):
# def print_triangle(direction,rows):
#     if direction=='u':
#         for i in range(1,rows+1):
#             print("*" * i)
#     elif direction=='d':
#         for i in range(rows,0,-1):
#             print("*" * i)
#     else:
#         print("invalid input")
# ch='d'
# num=5
# print_triangle(ch,num)
# def sum_natural(n):
#     if n==0:
#         return 0
#     else:
#         return n+sum_natural(n-1)
# num=150
# result=sum_natural(num)
# print("sum of first",num,"natural number is:",result)
# n=5
# for i in range(1,n+1):
#     def print_triangle(direction,rows):
#         if direction=='u':
#             for i in range(1,1+rows+1):
#                 print("*" * i)
#         elif direction=='d':
#             for i in range(rows,0,-1):
#                 print("*" * i)
#         else:
#             print("Invalid Input")
# ch='d'
# num=5
# print_triangle(ch,num)

# def print_reverse(n):
#     if n==0:
#         return 
#     print(n)
#     print_reverse(n-1)
# print_reverse(2)
# def sum_n(n):
#     if n==0:
#         return 0
#     return n+sum_n(n-1)
# print(sum_n(14))
# num=10
# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(5-2))
# def fibonacci(n):
#     if n<=1:
#         return n  
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
# print(fibonacci(7))
# guns=["awm","kar98k","M24"]
# print(guns)
# a=[1,"hello",2,"garv"]
# print(a)
# a.insert(1,4)
# print(a)
# marks=10
# if marks>=90:
#     print("Grade A")
# elif marks>=80:
#     print("Grade B")
# elif marks>=70:
#     print("Grade C")
# else:
#     print("KYU NHI HO RHI PRAI")

# i=15
# while i<51:
#     print(i)
#     i+=1
# i=10
# for i in range(90):
#     if i==60:
#         continue
#     print(i)
# for i in range(1,30+1):
#     if i%2!=0: 
#      print(i)
# day=4
# match day:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case 5:
#         print("Friday")
#     case 6:
#         print("Saturday")
#     case 7:
#         print("Sunday")
# def sum_natural(n):
#     if n==0:
#         return 0
#     else:
#         return n+sum_natural(n-1)
# num=14
# result=sum_natural(sum)
# print("sum of first",num,"natural number is:",result)
# def power(a,b):
#     if b==0:
#         return 1
#     return a*power(a,b-1)
# print(power(3,4))
# print(" *")
# print("***")
# print(" *")
# num=1 
# rows=4
# for i in range(1,rows+1):
#     for j in range(i):
#         print(num,end=" ")
#         num+=1
#     print()
# rows=5
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         if i==1 or i==rows or j==1 or j==i:
#             print("*",end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# rows=5
# for i in range(rows,0,-1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()
# class person:
#     def insert(self,name,age):
#         self.name="Garv"
#         self.age=age
#     def introduce(self):
#         print("My name is",self.name,"and my age is",self.age)
import random
QUESTIONS = [
    {
        "question": "What is the output of: print(2 ** 3)?",
        "options": {"A": "6", "B": "8", "C": "9", "D": "5"},
        "answer": "B",
        "category": "Operators",
        "difficulty": "easy",
    },
    {
        "question": "Which data type stores True or False?",
        "options": {"A": "str", "B": "int", "C": "bool", "D": "float"},
        "answer": "C",
        "category": "Data Types",
        "difficulty": "easy",
    },
    {
        "question": "What does len('hello') return?",
        "options": {"A": "4", "B": "5", "C": "6", "D": "7"},
        "answer": "B",
        "category": "Built-in Functions",
        "difficulty": "easy",
    },
    {
        "question": "Which keyword is used to create a function?",
        "options": {"A": "func", "B": "define", "C": "function", "D": "def"},
        "answer": "D",
        "category": "Functions",
        "difficulty": "easy",
    },
    {
        "question": "What symbol is used for comments in Python?",
        "options": {"A": "//", "B": "#", "C": "--", "D": "**"},
        "answer": "B",
        "category": "Syntax",
        "difficulty": "easy",
    },
    {
        "question": "What does 'str(123)' return?",
        "options": {"A": "123", "B": "'123'", "C": "Error", "D": "None"},
        "answer": "B",
        "category": "Data Types",
        "difficulty": "medium",
    },
    {
        "question": "Which method adds an item to the end of a list?",
        "options": {"A": "add()", "B": "insert()", "C": "append()", "D": "push()"},
        "answer": "C",
        "category": "Data Types",
        "difficulty": "medium",
    },
    {
        "question": "What is the output of: 10 // 3?",
        "options": {"A": "3.33", "B": "3", "C": "4", "D": "1"},
        "answer": "B",
        "category": "Operators",
        "difficulty": "medium",
    },
    {
        "question": "What does 'break' do inside a loop?",
        "options": {
            "A": "Skips current iteration",
            "B": "Ends the program",
            "C": "Exits the loop",
            "D": "Restarts the loop",
        },
        "answer": "C",
        "category": "Syntax",
        "difficulty": "medium",
    },
    {
        "question": "What is the output of: list(range(3))?",
        "options": {
            "A": "[1, 2, 3]",
            "B": "[0, 1, 2]",
            "C": "[0, 1, 2, 3]",
            "D": "[1, 2]",
        },
        "answer": "B",
        "category": "Built-in Functions",
        "difficulty": "medium",
    },
    {
        "question": "What does 'pass' do in Python?",
        "options": {
            "A": "Exits the function",
            "B": "Skips the block",
            "C": "Does nothing (placeholder)",
            "D": "Returns None",
        },
        "answer": "C",
        "category": "Syntax",
        "difficulty": "hard",
    },
    {
        "question": "What is the output of: type([])?",
        "options": {
            "A": "<class 'tuple'>",
            "B": "<class 'dict'>",
            "C": "<class 'list'>",
            "D": "<class 'set'>",
        },
        "answer": "C",
        "category": "Data Types",
        "difficulty": "hard",
    },
]
    
   
        
      
   

 
def get_categories(questions):
    categories=[]
    for q in questions:
        if q["category"] not in categories:
            categories.append(q["category"])
    categories.sort()
    return categories

def filter_questions(questions,category=None,difficulty=None):
    filtered=[]
    for q in questions:
        match=True
        if category and q["category"]!=category:
            match=False
        if difficulty and q["difficulty"]!=difficulty:
            match=False
        if match:
            filtered.append(q)
    return filtered

def ask_question(q_number,q_dict):
    print(f"\nQ{q_number}.{q_dict['question']}")
    print(f"[difficulty: {q_dict['difficulty'].upper()}]    [category:{q_dict['category']}]")
    for letter,text in q_dict["options"].items():
        print(f"{letter}. {text}")
        valid_choices=list(q_dict["options"].keys())
        answer=input("Your answer (A/B/C/D): ").strip().upper()
    while answer not in valid_choices:
        print("Invalid! Please enter A,B,C or D.")
        answer=input("Your answer (A/B/C/D):").strip().upper()
    if answer== q_dict["answer"]:
        print("Correct!")
        return 1
    else:
        correct_letter=q_dict["answer"]
        correct_text=q_dict["options"][correct_letter]
        print(f"Wrong! The correct answer was {correct_letter}.{correct_text}")
        return 0
    
def show_result(score,total,category_scores):
    print("\n"+ "="*45)
    print("           QUIZ COMPLETE!")
    print("="*45)
    percentage=round((score/total)*100)if total>0 else 0

    print(f" Score     : {score}/{total}")
    print(f" Percentage: {percentage}%")

    if percentage>=80:
        grade="Excellent !"
    elif percentage>=60:
        grade="Good job !"
    elif percentage>=40:
        grade="Keep learning !"
    else:
        grade="Try again !"

    print(f"Grade      :{grade}")   

    print("\n category breakdown:")
    print("  "+ "-" * 35)   
    for cat, scores in sorted(category_scores.items()):
        cat_correct=scores["correct"]
        cat_total= scores["total"]
        cat_pct= round((cat_correct/cat_total)* 100) if cat_total>0 else 0
        print(f"      {cat:<20} {cat_correct}/{cat_total}  ({cat_pct}%)")
    print("="  * 45)
    return {"score": score, "total": total, "percentage":percentage,"grade":grade}
def show_menu():
    print("\n--- Quiz Settings---")
    categories = get_categories(QUESTIONS)
    print("\nCategories:")
    print("  0.All categories")
    for i, cat in enumerate(categories,1):
        count= len (filter_questions(QUESTIONS, category=cat))
        print(f"{i}. {cat} ({count} questions)")
        
    cat_choice=input("\nPick a category (number):").strip()
    chosen_category=None
    if cat_choice.isdigit() and 1 <= int(cat_choice) <= len(categories):
        chosen_category=categories[int(cat_choice)-1]

    print("\nDifficulty:")
    print("0.All")
    print("1.Easy")
    print("2.Medium")
    print("3.Hard")

    diff_map={"1": "easy","2":"medium","3":"hard"}
    diff_choice=input("Pick difficulty(number):").strip()
    chosen_diffculty=diff_map.get(diff_choice,None)
    shuffle_choice=input("shuffle questions?(yes/no):").strip().lower()
    shuffle=shuffle_choice=="yes"
    return chosen_category, chosen_diffculty,shuffle
def show_history(history):
    if not history:
        print("\nNo rounds played yet")
        return
    print("\n" + "=" * 45)
    print("      Score History")
    print("=" * 45)
    for i, record in enumerate(history,1):
        print(f"  Round{i}: {record['score']}/{record['total']}"
              f"({record['percentage']}%) - {record['grade']}")
    print("=" * 45)
def run_quiz():
    history=[]
    playing=True
    while playing:
        print("\n" + "=" * 45)
        print("     Welcome to the python quiz!!")
        print("=" * 45)
        chosen_category, chosen_difficulty, shuffle= show_menu()
        quiz_questions=filter_questions(QUESTIONS, chosen_category, chosen_difficulty)

        if not quiz_questions:
            print("\nNo questions match those filters.try again!")
            continue

        if shuffle:
            random.shuffle(quiz_questions)
        print(f"\n---Starting quiz:{len(quiz_questions)} questions ---")
        print("Answer each question by typing A,B,C or D.\n")

        score=0
        category_scores={}
        for i,q in enumerate(quiz_questions,1):
            cat=q["category"]
            if cat not in category_scores:
                category_scores[cat]={"correct":0,"total":0}
            category_scores[cat]["total"]+=1
            result = ask_question(i,q) 
            score+=result
            category_scores[cat]["correct"]+=result
        round_result=show_result(score,len(quiz_questions),category_scores)
        history.append(round_result)
        print("\nWhat next?")
        print(" 1. Play Again")
        print(" 2. View score history")
        print(" 3. Quit")
        choice=input("choice(1/2/3):").strip()
        if choice =="2":
            show_history(history)
            again=input("\nPlay another round? (yes/no):").strip().lower()
            if again !="yes":
                playing=False
        elif choice=="1":
            continue
        else:
            playing=False
    if len(history)>1:
        show_history(history)
    print("\nThanks for playing!")
run_quiz()