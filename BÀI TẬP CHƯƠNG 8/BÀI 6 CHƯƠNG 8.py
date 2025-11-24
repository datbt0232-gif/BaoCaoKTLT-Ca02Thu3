numbers = []

while True:
    s = input("Enter a number: ")
    if s == "done":
        break
    try:
        num = float(s)
        numbers.append(num)
    except:
        print("Invalid input")

print("Maximum:", max(numbers))
print("Minimum:", min(numbers))