print('Instaloader Started!')
import instaloader

L = instaloader.Instaloader()

# Our bot 
USER = "anis2423h"

# Target profile
PROFILE = 'adighodsi'

# Load session previously saved with `instaloader -l USERNAME`:
L.load_session_from_file(USER)

profile = instaloader.Profile.from_username(L.context, PROFILE)

### ----- ###
# print a list of all the users who liked a post
likes = []
print("Fetching likes of all posts of profile {}.".format(profile.username))
for post in profile.get_posts():
    print(post)
    for like in post.get_likes():
        print(like.username)
        likes = likes + [like.username]

    # one_liker = post.get_likes()
    # print(one_liker['username'])
    # likes = likes + post.get_likes()

print(likes)

with open("likers of a post.txt", 'w') as f:
    for user in likes:
        print(user, file=f)

# print("Fetching followers of profile {}.".format(profile.username))
# followers = set(profile.get_followers())

# ghosts = followers - likes

# print("Storing ghosts into file.")

print('Instaloader Finished!')