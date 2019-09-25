import time
from squid import *
from button import *
from requests import get, RequestException


class Jokester(object):
    def __init__(self):
        self._b = Button(25)
        self._led = Squid(18, 23, 24)
        self._led.set_color(GREEN)
        
    def main_loop(self):
        while True:
            if self._b.is_pressed():
                self._led.set_color(PURPLE)
                time.sleep(5)
                self._led.set_color(GREEN)
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

