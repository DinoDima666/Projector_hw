# Write a program that generates 26 text files named A.txt, B.txt, and so on up to Z.txt. 
# To each file append a random number between 1 and 100. 
# Create a summary file (summary.txt) that contains the name of the file and the number in that file: 
# A.txt: 67 B.txt: 12...Z.txt: 98

import random


def txt_generator():
    for char in range(65, 91):
        with open(f"{chr(char)}.txt", "w") as gen_txt, open("summary.txt", "a") as summary:
            rand_int = random.randint(1,100)
            gen_txt.write(f"{rand_int}")
            summary.write(f"{chr(char)}.txt:{rand_int}, ")

txt_generator()

