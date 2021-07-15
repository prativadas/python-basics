marksobtained = int(input('enter your marks: '))

if(marksobtained>=90 and marksobtained<= 100):
    print('Ex grade')

elif(marksobtained>= 80 and marksobtained<= 90):
    print('A grade')

elif(marksobtained>=70 and marksobtained<= 80):
    print('B grade')

elif(marksobtained>=60 and marksobtained<=70):
    print('C grade')

elif(marksobtained>=50 and marksobtained<= 60):
    print('D grade')

else:
    print('F grade')
