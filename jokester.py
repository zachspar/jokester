#!/usr/bin/env python3
"""
Jokester class definition.

"""
import time
from squid import *
from button import *
from threading import Thread
from requests import get, RequestException


class Jokester(object):

    def __init__(self, test=False):
        self._category_idx = 0
        self._keep_running = True
        self._emit_joke_button = Button(25)
        self._change_category_button = Button(21)
        self._led = Squid(18, 23, 24)
        if not test:
            Thread(target=self._listen_for_press, daemon=True).start()
        self._category_requests = {
            "Trump Jokes": ("GET", "https://api.tronalddump.io/random/quote",
                            {"accept": "application/json"}, 'value'),
            "Dad Jokes": ("GET", "https://icanhazdadjoke.com/",
                          {"accept": 'application/json'}, 'joke'),
            "Chuck Norris Jokes": ("GET", "https://api.chucknorris.io/jokes/random",
                                   {"accept": 'application/json'}, 'value'),
        }
        self._req_objs = list(self._category_requests.items())

    def __del__(self):
        self._led.set_color(OFF)

    def _listen_for_press(self):
        while True:
            if self._change_category_button.is_pressed():
                if self._category_idx == len(self._category_requests) - 1:
                    self._category_idx = 0
                else:
                    self._category_idx += 1
                print("Changed category to  ::  [ {} ] !\n\n"\
                        .format(self._req_objs[self._category_idx][0]))

    def main_loop(self):
        while True:
            if self._emit_joke_button.is_pressed():
                self.get_rand_joke()

    def get_rand_joke(self):
        self._led.set_color(GREEN)
        try:
            req = self._req_objs[self._category_idx]
            rec = get(req[1][1], headers=req[1][2])
            if rec.status_code != 200:
                self._led.set_color(RED)
                print("Error: request status code is [ {} ]"
                      .format(rec.status_code))
                time.sleep(5)
            else:
                print("Category :: [ {} ]\n\t{}\n"\
                        .format(req[0], rec.json()[req[1][3]]))
        except RequestException as e:
            print(e)
        self._led.set_color(OFF)

    def test_all_apis(self):
        for category, rec in self._category_requests.items():
            print("Category  [  {}  ]".format(category))
            print("Making request to URL:  [  {}  ]".format(rec[1]))
            try:
                get_rec = get(rec[1], headers=rec[2])
                if get_rec.status_code != 200:
                    self._led.set_color(RED)
                    print("Error: status code for request [{}]  =  {}"\
                            .format(rec[1], rec[2]))
                    time.sleep(5)
                    self._led.set_color(OFF)
                    continue
                print("{}\n\n".format(get_rec.json()[rec[3]]))
            except RequestException as e:
                print(e)

