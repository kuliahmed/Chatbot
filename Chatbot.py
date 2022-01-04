import re
import random

sapaan = ["Hai Juga","Halo Juga","Apa Kabar"]

while True:
    x=input("User\t: ")
    if re.findall(r'halo|hai', x) :
        print("Bot\t: ", random.choice(sapaan))
    else:
        print("Bot\t: Aku Tidak Paham")