print('Instaloader Started!')
import instaloader
import sqlite3
import time

L = instaloader.Instaloader()

### Our bot 
USER = "anis2423j"

### Target profile
PROFILE = 'adighodsi_creation'
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
    print("db connection error!")

### loading the list of posts
cursor.execute("SELECT post_shortcode FROM posts")

rows = cursor.fetchall()
post_shortcode_list = []
for row in rows:
    a = list(row)
    post_shortcode_list = post_shortcode_list + a

number_of_posts = len(post_shortcode_list)

print("> There are {} entries! Let's explore likes.".format(number_of_posts))


### deifneing Post
PROFILE2 = 'anis2423j'
profile2 = instaloader.Profile.from_username(L.context, PROFILE2)    
for post in profile2.get_posts():
    ae = "rg"
   

### i is number of loops 
i = 0

### starting and ending(not inclouded) post
start = 0
end = 400

length = end - start 
### exploring likes of every post 
for post_shortcode in post_shortcode_list[start :end]:
    i = i + 1
    table_name = "likers_of_post_" + str(i)            

    ### Creating a table for every post_shortcode  
    try: 
        cursor.execute('''CREATE TABLE {}
                    (liker_username text                            
                    )'''.format(table_name))
        print( "Table of post {}, named {}, is created!".format(i,post_shortcode))
    except:
        print("===> OperationalError!!")
        pass

    ### check if post is crawled befor    
    #reading datavais    
    query = """SELECT post_is_crawled_for_likes FROM posts WHERE post_shortcode = ? """
    data = (post_shortcode, )
    cursor.execute(query, data)
    #finding crawell status
    rows = cursor.fetchall()
    for row in rows:
        crawell_check = row[0]
    
    if crawell_check == "Yes":
        print(">>>>>>>>>>>>>>>>>>> {} likes has been crawled before!!!!!".format(post_shortcode))

    elif crawell_check == "No":
        print("we are good to go, post is NOT crawled befor !!")                

        ### adding likers of the post_shortcode to table
        post = post.from_shortcode(L.context, post_shortcode)
        print("fetching likers of the post {}, named {}:".format(i, post))    


        for liker in post.get_likes():
            aa = liker.username  
            print(">>> {}".format(aa))                
                   
            query = '''INSERT INTO {}(
            liker_username) VALUES 
            (?)'''.format(table_name)
            
            data = (aa,)            
            cursor.execute(query, data)
            
            #show how much is left
            print("post {} of {}".format(i, length))
            
            conn.commit()
            time.sleep(0.5)
        print("--- Table {}, named {}, is completed!!!".format(i, post_shortcode))

        ### changging the crawl satatus
        query = """UPDATE posts SET post_is_crawled_for_likes = ? WHERE post_shortcode = ? """
        data = ("Yes", post_shortcode)
        cursor.execute(query, data)
        conn.commit()

conn.close()
print('Instaloader Finished!')








# ### list of posts 
# post_list = []
# print("Fetching posts of profile {}.".format(profile.username))
# for post in profile.get_posts():
#     i = i + 1
#     print("post {}".format(i))
#     print("{} added to list".format(post))
#     post_list = post_list + [post]    
#     time.sleep(0.5)

# ### adding post list to db
# print("adding posts to databais")
# for post in post_list:
#     a = post.shortcode  
#     # print(a)    
#     b = post.likes
#     # print(b)
#     c = post.date
#     # print(c)
#     d = ""
#     if post.is_video == True:
#         d = "True"
#     elif post.is_video == False:
#         d = "False"
#     # print(d)

#     query = '''INSERT INTO posts(
#     post_shortcode,
#     post_likes,
#     post_data,
#     post_is_video) VALUES 
#     (?,?,?,?)'''
#     data = (a, b, c, d)
    
#     cursor.execute(query, data)
    
# conn.commit()
# conn.close()
# print('Instaloader Finished!')
        







# 






# with open("likers of a post.txt", 'w') as f:
#     for user in likes:
#         print(user, file=f)

# print("Fetching followers of profile {}.".format(profile.username))
# followers = set(profile.get_followers())

# ghosts = followers - likes

# print("Storing ghosts into file.")

