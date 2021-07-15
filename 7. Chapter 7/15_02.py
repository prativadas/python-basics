#pyramid
#reverse right angle triangle. left alinged

# for i in range(3):                        # i indicates rows. i=0,1,2
#     print(' '*(2-i)+'*'*(i+1))            # for i=0,1,1 leftspace=2,1,0;  

#reverse right angle pyramid efficient method. from above method complete the pyramid by adding another right alinged pyramid

for i in range(3):                       # i = 0,1,2
    print(' '*(2-i)+'*'*(i+1)+'*'*(i))   # for row=1,leftspace=2,rightspace=2
                                         # as rows increasing space increases in both left and right
