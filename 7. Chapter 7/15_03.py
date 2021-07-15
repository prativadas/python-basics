
# larger to smaller - left aligned-not inverted

# for i in range(3):               # i indicates rows. i=0,1,2
#     for j in range(3-i):        
#         print('*', end='')
#     print()

# #efficient method.leftaligned pyramid.

# for i in range(3):       
#         print((i+1)*'*')  # for i=0, * printed =1; i=1,* printed =2. here no concept of space.



#efficient method.right-aligned pyramid. 
   
# for i in range(3):                     # i indicates rows. i=0,1,2
#         print(' '*(i)+(3-i)*('*'))



# inverted reverse right angle triangle pyramid
#Downward half - Pyramid
#larger to smaller - right aligned #Downward half - Pyramid

# for i in range(3):
#     print(' '*i+'*'*(3-i))  #when i=0,empty space=0 following by *. i=1, space=1
#                             #for row=1, space =0, row=2, space=1 so on

#reverse right angle triangle. right aligned

for i in range(3):
    print(' '*(2-i)+'*'*(i+1))   #here row=1,space=2;row=2,space=1;row=3,space=0. so space is decreasing with increase in row.

