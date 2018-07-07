import threading
import logging
import time

logging.basicConfig(
	level = logging.DEBUG,
	format = "%(asctime)s | %(levelname)s | %(message)s",
)

def deep_process(task="sun tan", space=3, type="+sync"):
	# simulate a long running process
	logging.info(f"({type}) {task}: started. t-{space}")
	time.sleep(space)
	logging.info(f"({type}) {task}: finished")

tasks = ["games", "codes", "sleep"]
spaces = [6, 6, 4]

# synchronous (-sync)
for task in tasks:
	space = spaces[tasks.index(task)]
	deep_process(task, space, "-sync")


# asynchronous (+sync)
for task in tasks:
	space = spaces[tasks.index(task)]
	thread = threading.Thread(target=deep_process, args=([task, space, "+sync"]))
	thread.start()

# move the synchronous test behind the asynchronous test
# and see what happens

# right now, the -sync tests run each to completion
# before giving space to the next call
# unlike that of the +sync tests