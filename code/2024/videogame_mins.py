minsplayed = [
    [60,30,45,0],
    [180,60,0,60],
    [200,30,0,20],
    [60,10,15,15],
    [100,35,30,45]
]
total = 0
kids = {"stuart":0, "wes":1,"victoria":2, "dan":3}
while True:
    try:
        who = input("Who do you want to know about? ")
        break
    except:
        print("please enter a valid name")
        continue
kid = kids.get(who)
for row in range(0,len(minsplayed)):
    for col in range(kid,kid+1):

        total = minsplayed[row][kids[who]] + total
        hours = total/60
print(f"{who} has played {total} minutes or {hours} hours of video games this week")
