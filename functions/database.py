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

    

    