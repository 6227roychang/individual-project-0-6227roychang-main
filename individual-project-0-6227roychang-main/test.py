# Do not change this file.

import os

class bcolors:
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    WARNING = '\033[93m'

if __name__ == '__main__':
    os.system("rm -rf build; mkdir build && cd build; cmake ..; make;")
    # os.system("rm -r build && mkdir build && cd build && cmake -G \"MinGW Makefiles\" .. && make")

    pass_all = True
    for f in os.listdir('./input/'):
        os.system(f"cd build; ./arbitrary ../input/{f} ../output/{f}")
        inp = open('input/'+f,'r')
        a, b = map(int, inp.readlines()[0].split())
        try:
            with open('output/'+f,'r') as outp:
                lines = outp.readlines()

            for i in range(len(lines)):
                lines[i] = lines[i].replace('\n','')

            if f'1> {a}, {b}' in lines and \
                f'2> {a+b}, {a-b}' in lines and \
                f'3> {a%b}, {a*b}' in lines and \
                f'4> That\'s it!' in lines:
                print(f"{bcolors.OKGREEN}Test '{f.replace('.txt','')}'","PASSED")
            else:
                print(f"{bcolors.FAIL}Test '{f.replace('.txt','')}'","FAILED")
                pass_all = False
        except:
            print(f"{bcolors.WARNING}Test '{f.replace('.txt','')}' is not executed")
            pass_all = False
    
    if pass_all:
        exit(0)
    else:
        exit(1)
