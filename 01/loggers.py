import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug("script initialization")

handle = input("your twitter handle: ")

logging.debug("we have his twitter handle")

print("we can now stalk you easily, %s" %(handle))

logging.debug("we're done here")