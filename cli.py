#!/usr/bin/env python3
import argparse
from greet import greet

def main():
    p = argparse.ArgumentParser()
    p.add_argument("name")
    args = p.parse_args()
    print(greet(args.name))

if __name__ == "__main__":
    main()
