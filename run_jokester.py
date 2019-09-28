#!/usr/bin/env python3
"""
Driver program to run the Jokester.

"""
def main():
    jokes = Jokester()
    # jokes = Jokester(test=True)
    jokes.main_loop()
    # jokes.test_all_apis()
    del jokes


if __name__ == '__main__':
    main()

