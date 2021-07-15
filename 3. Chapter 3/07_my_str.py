my_str = 'i am bahubali  ka  bachha  .'

find_doublespace = my_str.find("  ")  #find any character only once 

print(find_doublespace)

find_bahu = my_str.find('bahu')

print(find_bahu)   


my_str1 = 'i am bahubali ka bachha.'  # replace double space wth single space

find_doublespace = my_str1.find('  ')    # if element not found then returns -1

print(find_doublespace)