#%%
#Login Instagram
from InstagramAPI import InstagramAPI

api = InstagramAPI("username", "password")
if (api.login()):
    #api.getSelfUserFeed()  
    print("Login succes!")
else:
    print("Can't login!")
#%%
listNama = ['mohmahfudmd', 'airlanggahartarto','muhadjir_effendy'
,'luhut_binsar_pandjaitan','prabowo','retno_marsudi'
,'smindrawati','agusgumiwangk','syahrulyasinlimpo'
,'siti.nurbayabakar','edhy.prabowo','sofyan.djalil','erickthohir'
,'wishnutama','bambangbrodjonegoro']

listId = [9503537257,3010352830,3898729931,2883229423,2142213578,6157128675,
4142926332,7139255865,2090763378 ,6329551081,5469831536,
3668403949,259804442,6668780,5844048390]

#%%
import pandas as pd

def getInfo(username, user_id):
    api.getUsernameInfo(user_id)
    data = api.LastJson
    followers = data['user']['follower_count']
    post = data['user']['media_count']
    
    print('Username : ', username)
    print('Followers : ', followers)
    print('Posts : ', post)
    
    more_available = True
    max_id = ''
    result = 0
    comment = 0
    like = 0
    
    while more_available:
        api.getUserFeed(user_id, max_id)
        media = api.LastJson
        post2 = media['num_results']
    
        for i in range(int(post2)):
            check = 'comment_likes_enabled' in media['items'][i]
            #print(check)
            if  check==True:
                c = media['items'][i]['comment_count']
                comment += c
            else:
                c = 0
                comment += c
                
            l = media['items'][i]['like_count']
            like += l
            #print(media['items'][i]['comment_count'])
            #print(media['items'][i]['like_count'])
        result += api.LastJson['num_results']
        #print('result : ',result)
        more_available = api.LastJson['more_available']
        if more_available == False:
            print ('total post :', result)
            
        else:
            max_id = api.LastJson['next_max_id']
            #print(max_id)
    print('Total Comments : ', comment)
    print('Total Likes : ', like)
    d = [followers, post, comment, like]
    return d
#%%
for i in range(len(listNama)):
    output.append(getInfo(listNama[i],listId[i]))
    
df = pd.DataFrame(output)
df.columns = ['Total Followers','Total Post','Total Comments', 'Total Likes']