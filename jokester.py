import time
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

