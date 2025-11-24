s= None
tong=0
dem=0
while s!='done':
    s=input('Enter a number:')
    try:
        s=int(s)
        tong=tong+s
        dem=dem+1
    except:
        if s!='done':
            print('Invalid input')
print(tong, dem, tong/dem)