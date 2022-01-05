
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



PROFILE2 = 'anis2423j'
profile2 = instaloader.Profile.from_username(L.context, PROFILE2)




for post in profile2.get_posts():
    post = post.from_shortcode(L.context, SHORTCODE) 
    print(post)
post = post.from_shortcode(L.context, SHORTCODE)
print("this is it")
print(post)
    ### i is number of loops 
i = 0
for liker in post.get_likes():
    aa = liker
    print(aa)    
            
    query = '''INSERT INTO {}(
    liker_username) VALUES 
    (?)'''.format(post_shortcode)
    data = (aa,)
    
    time.sleep(0.5)
print("{} table is completed. i= {}".format(post_shortcode, i))