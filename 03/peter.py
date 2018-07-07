# locker.py
# an insecure password locker

import sys
import sqlite3


# database
database = sqlite3.connect(".locker.db")
cursor = database.cursor()
try:
    locker = cursor.execute("select * from locker;").fetchall()
except sqlite3.OperationalError:
    cursor.execute("""
        create table locker
        (account text primary key,
        password text);
        """)
    database.commit
    locker = cursor.execute("select * from locker;").fetchall()


# support functions
def account_exists(account):
    acct = cursor.execute(f"""
    select account from locker
    where account="{account}";
    """).fetchone()

    if acct:
        return True
    else:
        return False


# locker actions
def newAccount(auth):
    try:
        account = auth[0]
        password = auth[1]
    except:
        if len(auth) != 2:
            print("couldn't parse arguments")
            print("""
usage:
    locker.py new [account] [password]

    create a new account to lock a password away

    requires two arguments
    [account]   the name of the account
    [password]  the password to lock away
""")
        sys.exit()

    if account_exists(account):
        print(f"an account named '{account}' already exists")
        sys.exit()

    cursor.execute(f"""
        insert into locker
        values("{account}", "{password}");
        """)
    database.commit()

    print(f"yay! a new account")


def fetchAccount(auth):
    try:
        account = auth[0]
    except:
        print("couldn't parse arguments")
        print("""
usage:
    locker.py fetch [account]

    copy the password at an account to clipboard
    (print to terminal if clipboard not available)

    requires one argument
    [account]  name of the account to fetch
""")
        sys.exit()

    if not account_exists(account):
        print("account does not exist")
        print("you can create a new one with:")
        print("    locker.py new [account] [password]")
        sys.exit()

    password = cursor.execute(f"""
     select password from locker
     where account="{account}";
     """).fetchone()[0]

    print("password retrieved")
    try:
        import pyperclip
        pyperclip.copy(password)
        print("password copied to clipboard")
    except:
        print("clipboard not available!!")
        hint = password.replace(password[3:], "*****")
        print(f"password hint: {hint}")


def editAccount(auth):
    try:
        account = auth[0]
        newpassword = auth[1]
    except:
        print("couldn't parse arguments")
        print("""
usage:
    locker.py edit [account] [newpassword]

    update the password locked away at an account

    requires two arguments
    [account]      the name of the account
    [newpassword]  the new password to lock away
""")
        sys.exit()

    if not account_exists(account):
        print("this account does not exist")
        print("you can create a new one with:")
        print("    locker.py new [account] [password]")
        sys.exit()

    cursor.execute("""
    update locker
    set password="{newpassword}"
    where account="{account}";
    """)
    database.commit()

    print("account's password updated")


def removeAccount(auth):
    try:
        account = auth[0]
    except:
        print("couldn't parse arguments")
        print("""
usage:
    locker.py remove [account]

    remove an account from the locker

    requires one argument
    [account]  name of the account to remove
""")
        sys.exit()

    if not account_exists(account):
        print("account does not exist")
        print("you can create a new one with:")
        print("    locker.py -new [account] [password]")
        sys.exit()

    password = cursor.execute(f"""
     delete from locker
     where account="{account}";
     """)
    database.commit()

    print("account removed unceremoniously")


def accountsPage():
    if locker != []:
        for acct in locker:
            account = acct[0]
            password = acct[1][:2] + "***"
            print(account.ljust(12), password.rjust(5))
    elif locker == []:
        print("there are no accounts in this locker")
        print("create a new one with:")
        print("    locker.py new [account] [password]")


# the app
app = "Locker is your insecure password safe"
usage = """
usage:
    locker.py new [account] [password]:
        create a new account

    locker.py fetch [account]:
        copy account's password to clipboard

    locker.py edit [account] [new-password]:
        edit password for an account
"""
hello = app + usage

try:
    script, action, *auth = sys.argv
except:
    action = "hello"

if action == "hello":
    print(hello)
elif action == "new":
    print("creating a new account...")
    print("")
    newAccount(auth)
elif action == "fetch":
    print("fetching account...")
    print("")
    fetchAccount(auth)
elif action == "edit":
    print("updating account...")
    print("")
    editAccount(auth)
elif action == "remove":
    print("removing account...")
    print("")
    removeAccount(auth)
elif action == "accounts":
    accountsPage()
else:
    print("couldn't parse arguments")
    print(usage)
