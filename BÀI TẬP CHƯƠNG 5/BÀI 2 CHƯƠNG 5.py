s= None
max=0
min=0
dem=0
while s!='done':
    s=input('Enter a number:')
    try:
        s=int(s)
        if (s>max):
            max=s
        if (s<min or dem==0):
            min=s
        dem=dem+1
    except:
        if s!='done':
            print('Invalid input')
print(max, min)