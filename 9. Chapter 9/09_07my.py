#store factorial values from 2 to 4 in separate files. how to do it like multiplication table????

for i in range(2, 5):
    with open(f"factorial/fact_of_{i}.txt", 'w') as f:
        for j in range(i):
            f.write(f'{i}*{j-1}')

        
     
        
# def factorial_iter(n):
# #     product = 1
# #     for i in range(n):
# #         product = product * (i+1)
# #     return product