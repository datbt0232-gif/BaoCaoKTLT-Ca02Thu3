try:
    hours = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))
except:
    print("Error, please enter numeric input")
    quit()

# Tính lương giống bài 1
if hours > 40:
    overtime = hours - 40
    pay = 40 * rate + overtime * rate * 1.5
else:
    pay = hours * rate

print("Pay:", pay)