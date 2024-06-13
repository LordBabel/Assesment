'''
Brawl Stars database application by William Li Chen

'''
# imports
import sqlite3

# constants and variables
DATABASE = "assessment.db"


# functions


def print_all_brawlers():
    db = sqlite3.connect(DATABASE)
    conn = db.cursor()
    sql = "SELECT * FROM Brawlers ORDER BY ID"
    conn.execute(sql)
    result = conn.fetchall()    # loop through results, print it nicely
    print("ID   Wallbreak   Name           HP      Rarity ID   Year Released   Class ID")
    for brawler in result:
        print(f"{brawler[0]:<5}{brawler[1]:<12}{brawler[2]:<15}{brawler[3]:<8}{brawler[4]:<12}{brawler[5]:<16}{brawler[6]:<5}")
    db.close()


def print_wallbreak():
    db = sqlite3.connect(DATABASE)
    conn = db.cursor()
    sql = "SELECT * FROM Brawlers WHERE Wallbreak == 'Yes'"
    conn.execute(sql)
    result = conn.fetchall()    # loop through results, print it nicely
    print("ID   Wallbreak   Name           HP      Rarity ID   Year Released   Class ID")
    for brawler in result:
        print(f"{brawler[0]:<5}{brawler[1]:<12}{brawler[2]:<15}{brawler[3]:<8}{brawler[4]:<12}{brawler[5]:<16}{brawler[6]:<5}")
    db.close()


def print_new():
    db = sqlite3.connect(DATABASE)
    conn = db.cursor()
    sql = "SELECT * FROM Brawlers ORDER BY Year_Released desc"
    conn.execute(sql)
    result = conn.fetchall()    # loop through results, print it nicely
    print("ID   Wallbreak   Name           HP      Rarity ID   Year Released   Class ID")
    for brawler in result:
        print(f"{brawler[0]:<5}{brawler[1]:<12}{brawler[2]:<15}{brawler[3]:<8}{brawler[4]:<12}{brawler[5]:<16}{brawler[6]:<5}")
    db.close()


def print_og():
    db = sqlite3.connect(DATABASE)
    conn = db.cursor()
    sql = "SELECT * FROM Brawlers WHERE Year_Released == 2017"
    conn.execute(sql)
    result = conn.fetchall()    # loop through results, print it nicely
    print("ID   Wallbreak   Name           HP      Rarity ID   Year Released   Class ID")
    for brawler in result:
        print(f"{brawler[0]:<5}{brawler[1]:<12}{brawler[2]:<15}{brawler[3]:<8}{brawler[4]:<12}{brawler[5]:<16}{brawler[6]:<5}")
    db.close()


def print_high_HP():
    db = sqlite3.connect(DATABASE)
    conn = db.cursor()
    sql = "SELECT Name, HP FROM Brawlers ORDER BY HP desc;"
    conn.execute(sql)
    result = conn.fetchall()    # loop through results, print it nicely
    print("Brawler        HP")
    for brawler in result:
        print(f"{brawler[0]:<15}{brawler[1]:<5}")
    db.close()


def print_low_HP():
    db = sqlite3.connect(DATABASE)
    conn = db.cursor()
    sql = "SELECT Name, HP FROM Brawlers ORDER BY HP;"
    conn.execute(sql)
    result = conn.fetchall()    # loop through results, print it nicely
    print("Brawler        HP")
    for brawler in result:
        print(f"{brawler[0]:<15}{brawler[1]:<5}")
    db.close()


def print_under10000_HP():
    db = sqlite3.connect(DATABASE)
    conn = db.cursor()
    sql = "SELECT Name, HP FROM Brawlers WHERE HP < 10000 ORDER BY HP desc;"
    conn.execute(sql)
    result = conn.fetchall()    # loop through results, print it nicely
    print("Brawler        HP")
    for brawler in result:
        print(f"{brawler[0]:<15}{brawler[1]:<5}")
    db.close()


def print_no_wallbreak():
    db = sqlite3.connect(DATABASE)
    conn = db.cursor()
    sql = "SELECT * FROM Brawlers WHERE Wallbreak == 'No'"
    conn.execute(sql)
    result = conn.fetchall()    # loop through results, print it nicely
    print("ID   Wallbreak   Name           HP      Rarity ID   Year Released   Class ID")
    for brawler in result:
        print(f"{brawler[0]:<5}{brawler[1]:<12}{brawler[2]:<15}{brawler[3]:<8}{brawler[4]:<12}{brawler[5]:<16}{brawler[6]:<5}")
    db.close()


def print_kit():
    db = sqlite3.connect(DATABASE)
    conn = db.cursor()
    sql = "SELECT * FROM Brawlers WHERE Name == 'Kit'"
    conn.execute(sql)
    result = conn.fetchall()    # loop through results, print it nicely
    print("ID   Wallbreak   Name           HP      Rarity ID   Year Released   Class ID")
    for brawler in result:
        print(f"{brawler[0]:<5}{brawler[1]:<12}{brawler[2]:<15}{brawler[3]:<8}{brawler[4]:<12}{brawler[5]:<16}{brawler[6]:<5}")
    db.close()


def print_epic_wallbreak():
    db = sqlite3.connect(DATABASE)
    conn = db.cursor()
    sql = "SELECT * FROM Brawlers WHERE Wallbreak == 'Yes' AND Rarity_ID = 4"
    conn.execute(sql)
    result = conn.fetchall()    # loop through results, print it nicely
    print("ID   Wallbreak   Name           HP      Rarity ID   Year Released   Class ID")
    for brawler in result:
        print(f"{brawler[0]:<5}{brawler[1]:<12}{brawler[2]:<15}{brawler[3]:<8}{brawler[4]:<12}{brawler[5]:<16}{brawler[6]:<5}")
    db.close()


def print_legendary_assassin():
    db = sqlite3.connect(DATABASE)
    conn = db.cursor()
    sql = "SELECT * FROM Brawlers WHERE Rarity_ID == 6 AND Class_ID = 2"
    conn.execute(sql)
    result = conn.fetchall()    # loop through results, print it nicely
    print("ID   Wallbreak   Name           HP      Rarity ID   Year Released   Class ID")
    for brawler in result:
        print(f"{brawler[0]:<5}{brawler[1]:<12}{brawler[2]:<15}{brawler[3]:<8}{brawler[4]:<12}{brawler[5]:<16}{brawler[6]:<5}")
    db.close()

# important variables, needed for stardle
wallbreak = ""
hp = 0
hplow = 0
year = 0
yearlow = 0
rarity = 0

def brawl_stardle():
    # important variables
    
    checker = 0
    db = sqlite3.connect(DATABASE)
    conn = db.cursor()
    print("Please make a first guess, for info.")
    print("What info did you gain, out of these 4 options?")
    print('''
    1. Wallbreak
    2. HP
    3. Year Released
    4. Rarity
          ''')
    while checker == 0:  # loop until valid answer
        inputs = input("Please select an option, 1 for Wallbreak, 2 for HP, 3 for Year Released and 4 for Rarity. ")
        # checking what option was selected
        # running different code based on each option, that stores user inputted data
        if inputs == "1":
            checker = 1
            print('''
                  1. Wallbreak
                  2. No Wallbreak
                  ''')
            inputwall = input("Please enter an option: ")
            if inputwall == "1":
                wallbreak = "Yes"
            elif inputwall == "2":
                wallbreak = "No"
            else:
                print("Please enter a valid option.")
                checker = 0
        elif inputs == "2":
            checker = 1
            print('''
                  1. Above
                  2. Below
                  3. Equal
                  ''')
            inputHP = input("Please enter an option, if the HP was Above, Below, or Equal to your guess: ")
            if inputHP == "1":
                hplow = 1
            if inputHP == "2":
                hplow = 2
            if inputHP == "3":
                hplow = 3
            inputHPValue = input("Please enter the HP value: ")
            try:
                inputHPValueINT = int(inputHPValue)
                hp = inputHPValueINT
            except:
                print("Please enter a valid number next time.")
                
        elif inputs == "3":
            checker = 1
            print('''
                  1. Above
                  2. Below
                  3. Equal
                  ''')
            inputYear = input("Please enter an option, if the Year was Above, Below, or Equal to your guess: ")
            if inputYear == "1":
                yearlow = 1
            if inputYear == "2":
                yearlow = 2
            if inputYear == "3":
                yearlow = 3
            print('''
                  1. 2017
                  2. 2018
                  3. 2019
                  4. 2020
                  5. 2021
                  6. 2022
                  7. 2023
                  8. 2024
                  ''')
        elif inputs == "4":
            checker = 1
        else:
            print(" Invalid Input.")
        extrainfo = input("Do you have more info to input? 1 for Yes, 2 for No: ")
        if extrainfo == "1":
            checker = 0
        elif extrainfo == "2":
            pass
        else:
            print("Please enter a valid option next time.")

    print(hp)
    print(wallbreak)
    sql = "SELECT * FROM Brawlers WHERE Rarity_ID == 6 AND Class_ID = 2"
    conn.execute(sql)
    result = conn.fetchall()    # loop through results, print it nicely
    print("ID   Wallbreak   Name           HP      Rarity ID   Year Released   Class ID")
    for brawler in result:
        print(f"{brawler[0]:<5}{brawler[1]:<12}{brawler[2]:<15}{brawler[3]:<8}{brawler[4]:<12}{brawler[5]:<16}{brawler[6]:<5}")
    db.close()


def custom_sql():
    user = input("Please enter a Username: ")  # username and password system
    if user == "Babel":
        password = input("Please enter your Password: ")
        if password == "password123":
            pass
            print("Here are the columns in the database:")
            print("ID  Wallbreak  Name  HP  Rarity ID  Year Released  Class ID")
            print("Please enter a SQL statement: ")
            db = sqlite3.connect(DATABASE)
            try:  # try to do a custom sql statement
                conn = db.cursor()
                sql = input("")
                conn.execute(sql)
                result = conn.fetchall()   
                for brawler in result:
                    print(brawler)
                db.close()
            except:
                print("Please retry with a valid SQL statement.")  # except to catch errors




        else:
            print("Please enter a valid Password next time.")
    else:
        print("Please enter a valid Username next time.")


while True:
    checker = 0
    # main
    print("What would you like to do with this Brawl Stars Database?")
    # menu
    print("Please input an option.")
    print('''
    1. Search through data
    2. Modify, Remove or Add data
    3. Brawl Stardle helper
    4. Custom SQL query 
    ''')
    while checker == 0:  # loop until valid answer
        inputs = input("Please type one of the numbers above. ")
        # checking what option was selected
        if inputs == "1":
            checker = 1
        elif inputs == "2":
            checker = 1
        elif inputs == "3":
            checker = 1
            brawl_stardle()
        elif inputs == "4":
            checker = 1
            custom_sql()
        else:
            print("Invalid Input.")
