maths = int(input("maths: "))
eng = int(input("eng: "))
kis = int(input("kis: "))
chem = int(input("chem: "))
phy = int (input("phy: "))

average = (maths+eng+kis+chem+phy)/5
print(f"Average = {average}")

if average < 0:
    print("Invalid value")

if average > 100:4535
    print("Invalid value")

if average >= 71 and average < 100:
    print("A")

elif average>=61 and average < 71:
    print("B")

elif average>=51 and average < 61:
    print("C")

elif average>=41 and average < 51:
    print("D")

elif average>=0 and average < 41:
    print("E")

