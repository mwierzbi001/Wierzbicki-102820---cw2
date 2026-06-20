import argparse

from application.calculator import add, sub

def main():
    argparser = argparse.ArgumentParser()

    argparser.add_argument("selection", choices=["add","sub"])
    argparser.add_argument("a", type=int)
    argparser.add_argument("b", type=int) #odczytanie argumentow

    arguments = argparser.parse_args() #obiekt

    if arguments.selection == "add":
        print(add(arguments.a, arguments.b))
    else:
        print(sub(arguments.a, arguments.b))


if __name__ == "__main__":
    main()