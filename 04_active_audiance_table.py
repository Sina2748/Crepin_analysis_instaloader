print('Instaloader Started!')
import instaloader
import sqlite3
import time
import pickle

L = instaloader.Instaloader()

### Our bot 
USER = "anis2423f"

### Target profile
PROFILE = 'adighodsi'
# PROFILE = 'tohidi.hossein'

### instaloader starts
# Load session previously saved with `instaloader -l USERNAME`:
L.load_session_from_file(USER)

profile = instaloader.Profile.from_username(L.context, PROFILE)

### databais starts
try:
    conn = sqlite3.connect('sqlite_{}.db'.format(PROFILE))
    cursor = conn.cursor()
except:
    print("db conn error!")




### create a list of likers who like more than threshhold
threshhold = 10

# create table of active audiance 
try:       
    cursor.execute('''CREATE TABLE active_audiance_threshhold_{}
                (username text,
                number_of_likes int,
                is_private text,                
                follower_number int,
                followee_number int,
                followee_list bolb
                )'''.format(threshhold))
    
except:
        print("db create table error!")

cursor.execute("SELECT * FROM cumulative_likers_table WHERE number_of_likes > {} AND is_crawled = 'no' ".format(threshhold))
rows = cursor.fetchall()
number_username = len(rows)
print(rows)
j = 0
for row in rows:
    
    j += 1
    username = row[0]
    number_of_likes = row[1]
    is_crawled = row[2]

    print("user {} had liked {} posts!".format(username, number_of_likes))
    print(".............. starting to crawl person {}  of  {} ".format(j, number_username))

    if is_crawled == "no":
        #is pivate?
        PROFILE2 = username
        profile2 = instaloader.Profile.from_username(L.context, PROFILE2) 
        is_private = "no"

        if profile2.is_private == True:
            is_private = "yes"
            print(">>>> {} is private".format(username))
        # number of 
        follower_number = profile2.followers
        followee_number = profile2.followees

        # followee list
        if is_private == "yes":
            followees_list = []

        elif is_private == "no":
            followees = profile2.get_followees()
            followees_list = []
            i = 0
            for followee in followees:
                i = i + 1
                print(">>> {} of {}. {} was added!".format(i, followee_number, followee.username))
                followees_list = followees_list + [followee.username]
                time.sleep(0.9)

        #adding info to table
        query = '''INSERT INTO active_audiance_threshhold_{}(
                username,
                number_of_likes,
                is_private,                
                follower_number,
                followee_number,
                followee_list            
                ) VALUES 
                (?,?,?,?,?,?)'''.format(threshhold)
                
        my_pickled_object = pickle.dumps(followees_list)
        # print(my_pickled_object)
        
        data = (username, number_of_likes, is_private, follower_number, followee_number, my_pickled_object)            
        cursor.execute(query, data)
        #adding crwled marke 
        print("progress was made to databais! {} of {}".format(j,number_username))    
        conn.commit()

        #changing the crwal status
   
        query = """UPDATE Cumulative_likers_table SET is_crawled = ? WHERE liker_username = ? """
        ss = "yes" 
        data = (ss,username) 
        print("{}, {}".format(query, data))          
        cursor.execute(query, data)

        print("progress was made to databais!") 
        print(".............. {}  of  {} people have been crawled!!".format(j, number_username)) 
        conn.commit()


    else:
        pass
     
conn.close()
print('Instaloader Finished!')



