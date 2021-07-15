def game():
    return 44677                # we enter this value here

score = game()                #returns default value of game()
with open("hiscore.txt") as f:          
    hiScoreStr = f.read()
    
if hiScoreStr=='':                  # if the var value is blank, can't be converted to int. 
    with open("hiscore.txt", "w") as f:  #condition ehrn file is blank. no previous score saved. then also overwrite
        f.write(str(score))                   # f.write() always takes str.

elif int(hiScoreStr)<score :
    with open("hiscore.txt", "w") as f:
        f.write(str(score))