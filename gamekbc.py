questions=[
    "1. who is known as the father of computers? ",
    "2. which language is used for AI?",
    "3. which app is best for software developers?",
    "4. which platform is best for freelancing?",
    "5. who introduced C language?" 
]

options=[
    ["A. Charles Babbage", "B. Isaac Newton", "C. Einstein", "D. Tesla"], 
    ["A.  Python", "B. HTML", "C. CSS", "D. JavaScript"], 
    ["A. WhatsApp", "B. Visual Studio Code", "C. Instagram" ,"D. YouTube"],
    ["A. Fiverr","B. Facebook","C. Linkedin","D. Instagram"],
    ["A. James Gosling","B. Dennis Ritchie","C. Bjarne Stroustrup","D. Guido van Rossum"]
]
answers=['A','A','B','A','B']
amount=0
n=len(questions)
for i in range(n):
    print("\n",questions[i])
    for opts in options:
        print(opts)

user=input("Enter your option (A/B/C/D):").upper()

if user==answers[i]:
    amount += 10000
    print("CORRECT,You've won 10000!!")
else:
    print("WRONG:( You've lostt")

print("\n Total amounnt won $:",amount)
print("THNAK YOU FOR PLAYING!....HOPE YOU ENJOYED THIS GAME:)")