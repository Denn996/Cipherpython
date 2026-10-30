# for loop
for i in range(1,11):
    print(f"Welcome to my shop customer {i}")

students = ["Dennis", "Samuel", "Lucy", "Jackie", "Eugene"]

for s in students:
    print(f"Welcome to our today's class {s}")

#calculate expense that you bought
#bread ksh 90
#milk ksh 120
#sugar ksh 160

my_shopping = [90,120,160]
total = 0
for m in my_shopping:
    total = total + m
    print(f"My total shopping cost is {total}")


#imagine you have five
#customer and each pay you 100. create a
#script to get the total

total = 0
for num in range(1,6):
    total = total + 100
    print(f"Total money collected : Ksh {total}")

# while loop
x=0
while x<=10:
    print(f"Loops {x}")
    x+=2

#imagine you want to save starting 0 balance
#and save 100 daily until you hit 1000.

money=0
while money<1000:
    money = money+100
    #money+=100
    print(f"Money saved: {money}")
    print("Congratulation! You have reached the target")
