def computegrade(score):
    try:
        s = float(score)
    except:
        return "Bad score"
    if s < 0.0 or s > 1.0:
        return "Bad score"
    if s >= 0.9:
        grade = 'A'
    elif s >= 0.8:
        grade = 'B'
    elif s >= 0.7:
        grade = 'C'
    elif s >= 0.6:
        grade = 'D'
    else:
        grade = 'F'
    return grade
print(computegrade("0.95"))
print(computegrade("perfect"))
print(computegrade("10.0"))
print(computegrade("0.75"))
print(computegrade("0.5"))