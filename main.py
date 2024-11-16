a=float(input("enter the speed at first hour"))
b=float(input("enter the speed at second hour"))
c=float(input("enter the speed at third hour"))
avg=(a+b+c)/3
print(f"average is {avg}")
if avg > a and avg>b and avg>c:
    print(f"{avg} is is greater than {a}, {b} and {c}")
elif a>avg and a>b and a>c:
    print(f"{a} is is greater than {avg}, {b} and {c}")
elif b>avg and b>a and b>c:
    print(f"{b} is is greater than {avg}, {a} and {c}")
else:
    print(f"{c} is is greater than {avg}, {a} and {b}")