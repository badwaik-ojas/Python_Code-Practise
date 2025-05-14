import sys

def main():
    list = sys.argv
    if len(list) > 1:
         print(list[1:])

if __name__ == "__main__": 
    main()