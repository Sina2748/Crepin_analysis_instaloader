print('Instaloader Started!')
import instaloader
import sqlite3
import time


L = instaloader.Instaloader()

### Our bot 
USER = "anis2423j"

### Target profile
PROFILE = 'sina_samii'
# PROFILE = 'tohidi.hossein'

### databais starts
try:
    conn = sqlite3.connect('sqlite_{}.db'.format(PROFILE))
    cursor = conn.cursor()
except:
        print("db conn error!")
### Creating posts table
try:       
    cursor.execute('''CREATE TABLE posts
                (post_shortcode text,
                post_likes int,
                post_data text,
                post_is_video text,
                post_is_crawled_for_likes text                        
                )''')
except:
        print("db create table error!")
        

### instaloader starts
# Load session previously saved with `instaloader -l USERNAME`:
L.load_session_from_file(USER)

profile = instaloader.Profile.from_username(L.context, PROFILE)

### i is number of loops 
i = 0
### list of posts 
post_list = []
print("Fetching posts of profile {}.".format(profile.username))
for post in profile.get_posts():
    i = i + 1
    print("post {}".format(i))
    print("{} added to list".format(post))
    post_list = post_list + [post]    
    time.sleep(0.5)

### adding post list to db
print("adding posts to databais")
for post in post_list:
    a = post.shortcode  
    # print(a)    
    b = post.likes
    # print(b)
    c = post.date
    # print(c)
    d = ""
    if post.is_video == True:
        d = "True"
    elif post.is_video == False:
        d = "False"
    e = "No"

    query = '''INSERT INTO posts(
    post_shortcode,
    post_likes,
    post_data,
    post_is_video,
    post_is_crawled_for_likes) VALUES 
    (?,?,?,?,?)'''
    data = (a, b, c, d, e)
    
    cursor.execute(query, data)
    
conn.commit()
conn.close()
print('Instaloader Finished!')



        







# for like in post.get_likes():
#     a = like.username  
#     print(a)    
            
#     query = '''INSERT INTO likers(
#     user) VALUES 
#     (?)'''
#     data = (a,)
    
#     cursor.execute(query, data)
#     conn.commit()
#     time.sleep(0.5)
        

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

