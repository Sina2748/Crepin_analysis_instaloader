print('Instaloader Started!')
import instaloader
import sqlite3
import time


L = instaloader.Instaloader()

# Our bot 
USER = "anis2423j"

# Target profile
# PROFILE = 'adighodsi_creation'
PROFILE = 'adighodsi'

### databais starts
try:
    conn = sqlite3.connect('sqlite_{}.db'.format(PROFILE))
    cursor = conn.cursor()
except:
        print("db conn error!")

try:       
    cursor.execute('''CREATE TABLE likers
                (user text            
                )''')
except:
        print("db create table error!")
        




# Load session previously saved with `instaloader -l USERNAME`:
L.load_session_from_file(USER)

profile = instaloader.Profile.from_username(L.context, PROFILE)

### ----- ###
# print a list of all the users who liked a post
i = 0
print("Fetching likes of all posts of profile {}.".format(profile.username))
for post in profile.get_posts():
    print(post)
    for like in post.get_likes():
        a = like.username  
        print(a)
        
        i = i + 1
        print(i)
        
        query = '''INSERT INTO likers(
        user) VALUES 
        (?)'''
        data = (a,)
        
        cursor.execute(query, data)
        conn.commit()
        time.sleep(1)
        

    # one_liker = post.get_likes()
    # print(one_liker['username'])
    # likes = likes + post.get_likes()






# with open("likers of a post.txt", 'w') as f:
#     for user in likes:
#         print(user, file=f)

# print("Fetching followers of profile {}.".format(profile.username))
# followers = set(profile.get_followers())

# ghosts = followers - likes

# print("Storing ghosts into file.")


conn.close()
print('Instaloader Finished!')