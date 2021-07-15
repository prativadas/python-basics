 #generate table from 2 to 20, save them in different files


for i in range(2, 21):                 #using 2 for loops as we know which tables we want 2 to 20. 
    with open(f"tables/Multiplication_table_of_{i}.txt", 'w') as f:          #we 1st open the file then write in it 
        for j in range(1, 11):              
            f.write(f"{i}X{j}={i*j}\n")
            # if j!=10:        #if want to remove space after 10th iteration
            #     f.write('\n')
