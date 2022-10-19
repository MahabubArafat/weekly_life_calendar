import argparse
import sys
import os


def main():
    parser=argparse.ArgumentParser(description="hudai")

    parser.add_argument('-f','--filename',type=str,dest='filename',default="file er nam default")

    args=parser.parse_args()
    print(args)
    print(args.filename)
    print("---------------------------")
    print(parser)

if __name__=="__main__":
    main()