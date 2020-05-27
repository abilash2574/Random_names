import random
import sys

first_name = ("Paul", "Dick", "Chris", "Moe", "Dickie", "Faartz", "Kash", "Lord", "Hardick")
last_name = ("","","","","Kock","Raper","Black","Register","Brain","Head","Lester","Litoris","Twocock","Perv","Mussolini","Long")

while(True):
    temp1 = random.choice(first_name)
    temp2 = random.choice(last_name)
    print(temp1 + " " + temp2 , file=sys.stderr)
    print("Press Enter to find another name or (x) to exit")
    if input().lower() == 'x':
        exit()
