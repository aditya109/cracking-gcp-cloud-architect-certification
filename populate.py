import os
import re


def main():
    l = os.getcwd()
    a = os.listdir(l)
    for dir in a:
        if not re.search("git", dir) and dir != "." and not re.search("vscode", dir):
            # with open(os.path.join(l,os.path.join(dir, "README.txt")), 'w') as fp :
            #     pass           
            pass

main()
