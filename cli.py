#!/usr/bin/env python3
import argparse
from greet import greet


def main(argv=None):
    # Bygg parser varje gång main körs (inte på modulnivå)
    p = argparse.ArgumentParser()
    p.add_argument("name")
    p.add_argument("--upper", action="store_true")
    args = p.parse_args(argv)

    msg = greet(args.name)
    print(msg.upper() if args.upper else msg)


if __name__ == "__main__":
    main()
