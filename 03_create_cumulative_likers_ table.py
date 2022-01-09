print('SQLite Started!')
# import instaloader
import sqlite3
# import time

### Target profile
PROFILE = 'adighodsi'

### databais starts
try:
    conn = sqlite3.connect('sqlite_{}.db'.format(PROFILE))
    cursor = conn.cursor()
except:
    print("db connection error!")

### read databais to extract likers of all posts, List_all
cursor.execute("SELECT * FROM posts")
rows = cursor.fetchall()
number_of_post_tables = len(rows)


# makeing the list of table names
list_all = []
for i in range(1,number_of_post_tables+1):
    table_names = "likers_of_post_" + str(i)
    # print("resiving likers of table {}".format(table_names))   
    cursor.execute("SELECT * FROM {}".format(table_names)) 
    rows = cursor.fetchall()
    for row in rows:        
        list_all = list_all + list(row)
    
print("list of all likers is creeated!!!")
# print(list_all)

### dellete duplicates of the list, list_one
list_one = list(set(list_all))
print("list of individual likets is crested!!!")
# print(list_one)

### make a loop to count list_on items in list_all
like_numbler_list = []
for person_one in list_one:
    like_numbler = 0
    
    for person_all in list_all:
        if person_one == person_all:
            like_numbler = like_numbler + 1
    print("> {} liked {} times.".format(person_one, like_numbler))

    #makeing a list of like counts
    like_numbler_str = str(like_numbler)
    like_numbler_list = like_numbler_list + [like_numbler_str]
# print(like_numbler_list)

### add list_one and counts to a new table
try: 
    cursor.execute('''CREATE TABLE Cumulative_likers_table
                (liker_username text,
                number_of_likes int
                )''')
    print("Table of post Cumulative_likers_table is created!")
except:
    print("===> OperationalError!!")
    pass

# adding data to db
for i in range(1, len(list_one)):
    query = '''INSERT INTO Cumulative_likers_table(
                liker_username,
                number_of_likes
                ) VALUES 
                (?, ?)'''
            
    data = (list_one[i],like_numbler_list[i])   
    # print("{}, {}".format(query, data))         
    cursor.execute(query, data)           
    
conn.commit()
# finishing up
print("likers username and number of their likes was added to databais!!")
conn.close()