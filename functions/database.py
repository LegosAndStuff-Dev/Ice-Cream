from Disecon import start
import sqlite3


def database(name: str):
    if name.lower() == "ice cream advertise":
        conn = sqlite3.connect("iceCream.db")
        c = conn.cursor()

        try:
            c.execute("""CREATE TABLE advertise (
                user_ID int,
                advertise int
            
            )""")

            print("advertise table made")
            
        except:
            pass

    elif name.lower() == "ice cream location":
        conn = sqlite3.connect("iceCream.db")
        c = conn.cursor()

        try:
            c.execute("""CREATE TABLE location (
                user_ID int,
                locations int
            
            )""")

            print("location table made")
            
        except:
            pass

    elif name.lower() == "economy":
        start()

        #conn = sqlite3.connect("economy.db")
        #c = conn.cursor()
    
        #try:
        #    c.execute("""CREATE TABLE economy (
        #        user_ID text,
        #        wallet int,
        #        bank int,
        #        net int
        #    
        #    )""")

        #    print("Economy table made")
            
        #except:
        #    pass
        
        #conn.commit()
        #conn.close()

    
def addAdvertise(userID: int):
    conn = sqlite3.connect("iceCream.db")
    c = conn.cursor()

    c.execute(f"SELECT * FROM advertise WHERE user_ID = {userID}")
    items = c.fetchall()

    none = str(items)

    if none == "[]":
        c.execute(f"INSERT INTO advertise VALUES ({userID}, 1)")

        conn.commit()
        conn.close()

    else:
        for item in items:
            amount = int(item[1])

        amount += 1

        c.execute(f"""UPDATE advertise SET advertise = {amount}
                    WHERE user_ID = {userID}  
                """)

        conn.commit()
        conn.close()

def removeAdvertise(userID: int):
    conn = sqlite3.connect("iceCream.db")
    c = conn.cursor()

    c.execute(f"SELECT * FROM advertise WHERE user_ID = {userID}")
    items = c.fetchall()

    none = str(items)

    if none == "[]":
        return "No Row"

    else:
        for item in items:
            amount = int(item[1])

        if amount == 0:
            return "No Row"

        else:
            amount -= 1

            c.execute(f"""UPDATE advertise SET advertise = {amount}
                        WHERE user_ID = {userID}  
                    """)

            conn.commit()
            conn.close()

def getLocationNum(userID: int):
    conn = sqlite3.connect("iceCream.db")
    c = conn.cursor()

    c.execute(f"SELECT * FROM location WHERE user_ID={userID}")

    items = c.fetchall()
    none = str(items)

    if none == "[]":
        locationNum = 0

    else:
        for item in items:
            locationNum = int(item[1])

        
    return locationNum


        
    