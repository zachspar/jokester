#!/usr/bin/env python3
"""
Testing script to make sure all APIs work as expected.

"""
from requests import get, RequestException


REQUESTS = {
    "Trump Jokes": ("GET", "https://api.tronalddump.io/random/quote",
                    {"accept": "application/json"}, 'value'),
    "Dad Jokes": ("GET", "https://icanhazdadjoke.com/",
                  {"accept": 'application/json'}, 'joke'),
    "Chuck Norris Jokes": ("GET", "https://api.chucknorris.io/jokes/random",
                           {"accept": 'application/json'}, 'value'),
}


def test_all_apis():
    for category, rec in REQUESTS.items():
        print("Category  [  {}  ]".format(category))
        print("Making request to URL:  [  {}  ]".format(rec[1]))
        try:
            get_rec = get(rec[1], headers=rec[2])
            if get_rec.status_code != 200:
                print("Error: status code for request [{}]  =  {}".format(rec[1], rec[2]))
                continue
            print("{}\n\n".format(get_rec.json()[rec[3]]))
        except RequestException as e:
            print(e)


if __name__ == '__main__':
    test_all_apis()

