#!/usr/bin/env python3
"""
Jokester class definition.

"""
from squid import *
from button import *
from threading import Thread
from requests import get, RequestException


class Jokester(object):

    def __init__(self):
        self._b = Button(25)
        self._led = Squid(18, 23, 24)
        self._led.set_color(GREEN)
        Thread(target=self._listen_for_press).start()
        self._category_requests = {
            "Trump Jokes": ("GET", "https://api.tronalddump.io/random/quote",
                            {"accept": "application/json"}, 'value'),
            "Dad Jokes": ("GET", "https://icanhazdadjoke.com/",
                          {"accept": 'application/json'}, 'joke'),
            "Chuck Norris Jokes": ("GET", "https://api.chucknorris.io/jokes/random",
                                   {"accept": 'application/json'}, 'value'),
        }

    def _listen_for_press(self):
        while True:
            if self._b.is_pressed():
                print("button pressed heard from thread!!")

    def main_loop(self):
        while True:
            if self._b.is_pressed():
                self.get_rand_joke()

    def get_rand_joke(self):
        try:
            rec = get('https://icanhazdadjoke.com/',
                      headers={'Accept': 'application/json'})

            if rec.status_code != 200:
                print("Error: request status code is [ {} ]"
                      .format(rec.status_code))
            else:
                print(rec.json()['joke'])

        except RequestException as e:
            print(e)

    def test_all_apis(self):
        for category, rec in self._category_requests.items():
            print("Category  [  {}  ]".format(category))
            print("Making request to URL:  [  {}  ]".format(rec[1]))
            try:
                get_rec = get(rec[1], headers=rec[2])
                if get_rec.status_code != 200:
                    print("Error: status code for request [{}]  =  {}".format(rec[1], rec[2]))
                    continue
                print("{}".format(get_rec.json()[rec[3]]))
            except RequestException as e:
                print(e)

