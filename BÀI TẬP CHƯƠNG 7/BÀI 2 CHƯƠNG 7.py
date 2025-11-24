
fname = input("Enter the file name: ")
fhand = open(fname)
count = 0
total = 0.0

for line in fhand:
    line = line.strip()
    if line.startswith("X-DSPAM-Confidence:"):
        value = float(line.split(":")[1])
        total += value
        count += 1
avg = total / count
print("Average spam confidence:", avg)