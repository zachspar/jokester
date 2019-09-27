#!/usr/bin/env python3
"""
Run the Jokester main program.

"""
from jokester import Jokester


def main():
    jokes = Jokester()
    # jokes.main_loop()
    jokes.test_all_apis()


if __name__ == '__main__':
    main()

