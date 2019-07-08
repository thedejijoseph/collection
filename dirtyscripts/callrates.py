# callrates.py
# i just wanna be able to be able to tell
# at what rate i was charged from the time i spent and
# the amount spent


def start():
    seconds = int(input("time spent in seconds: "))
    amount = input("amount charged in kobo: ")
    rate = rates(seconds, amount)
    print(f"you were charged at {rate} per second")


def rates(sec, amt):
    amt = float(amt)
    rate = (amt / sec)/100
    return "{0:.2f}".format(rate)

start()
