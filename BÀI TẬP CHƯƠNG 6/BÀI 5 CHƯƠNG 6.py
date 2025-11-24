str = 'X-DSPAM-Confidence:0.8475'
a=str.find(':')+1
b=len(str)
c=str[a:b]
float(c)
print(c)