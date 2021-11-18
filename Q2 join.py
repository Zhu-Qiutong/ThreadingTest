import time, random
import logging
import threading
import concurrent.futures


def call_vision(tote_id):
    print("call_vision", tote_id)
    time.sleep(3)
    pos = (random.random(), random.random())
    return pos


def move_to_pick(pos):
    print("move_to_pick", pos)
    time.sleep(1)


def move_to_scan():
    print("move_to_scan")
    time.sleep(1)


def move_to_place():
    print("move_to_place")
    time.sleep(1)


def move_to_home():
    print("move_to_home")
    time.sleep(1)


def tic():
    return time.time()


def toc(t):
    print("time elapsed", time.time() - t)


def get_vision(tote_id):
    pass


def trigger_vision(thread):
    thread.start()


class Database():
    def __init__(self):
        self.vision_data = 0


    def update(self, tote_id):
        self.vision_data = call_vision(tote_id)


    def init_thread(self):
        x = threading.Thread(target=self.update, args=(1,))
        return x

    def get_data(self, thread, tote_id):
        thread.join()
        return self.vision_data


database = Database()
vision = database.init_thread()

move_to_home()
trigger_vision(vision)


while True:
    # set time steamp
    time_start = tic()
    # home
    move_to_home()
    # get pos
    pos = database.get_data(vision, 1)
    # pick
    move_to_pick(pos)
    # scan
    move_to_scan()
    # process image
    vision = database.init_thread()
    trigger_vision(vision)
    # move to place
    move_to_place()
    toc(time_start)









