import time, random
import logging
import threading
import concurrent.futures


def get_robot_pose():
    time.sleep(0.01)
    return random.random()

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


def wait_for_move_to_scan_then_trigger_vision():
    pose = get_robot_pose()
    while not 0.7 < pose < 0.8:
        pose = get_robot_pose()


class Database():
    def __init__(self):
        self.vision_data = 0


    def update(self, tote_id):
        self.vision_data = call_vision(tote_id)

    # vision
    def init_thread_1(self):
        x = threading.Thread(target=self.update, args=(1,))
        return x

    # wait for thread
    def init_thread_2(self):
        x = threading.Thread(target = wait_for_move_to_scan_then_trigger_vision, daemon=True)
        return x


    def get_data(self, thread):
        thread.join()
        return self.vision_data





database = Database()
move_to_home()
vision = database.init_thread_1()
trigger_vision(vision)
while True:
    # set time steamp
    time_start = tic()
    # home
    move_to_home()
    # get pos
    pos = database.get_data(vision)
    # pick
    move_to_pick(pos)
    # scan
    move_to_scan()
    # wait for trigger
    wait_for_trigger = database.init_thread_2()
    wait_for_trigger.start()
    # process image
    vision = database.init_thread_1()
    trigger_vision(vision)
    # move to place
    move_to_place()
    toc(time_start)
