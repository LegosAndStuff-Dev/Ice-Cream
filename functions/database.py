from Disecon import start
import sqlite3


def database(name: str):
    if name.lower() == "shop items":
        conn = sqlite3.connect("shop_items.db")
        c = conn.cursor()
        
        try:
            c.execute("""CREATE TABLE shop_items (
                name text,
                price int,
                option text,
                use text,
                visible text
                
            )""")
            
        except:
            print("Shop Items was not mad")
            pass
        
        conn.commit()
        conn.close()

    elif name.lower() == "items own":
        conn = sqlite3.connect("shop.db")
        c = conn.cursor()
        
        try:
            c.execute("""CREATE TABLE items_own (
                user_id text,
                item_name text,
                amount text 
            
            )""")
            
            print("Items Own table made")
            
        except:
            print("items owner table not made")
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

    

    