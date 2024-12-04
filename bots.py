import threading
import time
import json

with open('inventory.dat', 'r') as f:
    inventory = json.load(f)

def bot_fetcher(fetcher_list, cart, lock):
    for item in fetcher_list:
        time.sleep(inventory[item][1])
        with lock:
            cart.append([item, inventory[item][0]])

def bot_clerk(items):
    cart = []
    lock = threading.Lock()
    fetcher_lists = [[], [], []]

    for i, item in enumerate(items):
        fetcher_lists[i % 3].append(item)

    threads = []
    for fetcher_list in fetcher_lists:
        thread = threading.Thread(target=bot_fetcher, args=(fetcher_list, cart, lock))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return cart
