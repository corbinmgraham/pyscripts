import os
import sys

def change_ext(match='.test123', ext=".test123"):
    changed = 0
    unchanged = 0
    for i,file in enumerate(os.listdir()):
        name, prev_ext = os.path.splitext(file)
        if prev_ext == match:
            new = name + ext
            os.rename(file,new)
            print(f"Moved file '{file}' to '{new}'")
            changed += 1
        else:
            print("Didn't move:", file)
            unchanged += 1
    print(f"{changed} files moved, {unchanged} didn't move.")

def help():
    print('USE: extension.py [-h] [EXTENSION_MATCH EXTENSION_CHANGE]')
    print('EXAMPLE: extension.py .jpg .png')

if __name__ == '__main__':
    args = sys.argv
    if args[1] == '-h':
        help()
    else:
        try:
            change_ext(match=args[1], ext=args[2])
        except:
            print('Fields incorrect.')
            help()
    exit()