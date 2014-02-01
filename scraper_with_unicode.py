import pymongo
from pymongo import MongoClient


#####
#start by making connection to server

client  = MongoClient("mongodb://macdavel:fbdb@ds061158.mongolab.com:61158/fbdb")
db = client.fbdb

#mport facebook
import facebook
import json,urllib2

#get the token
#This is achieved using an app ID and App secret
#gotten from the facebook developer site
#These codes uniquely identify our app with facebook
#after that, we access the graph
token = facebook.get_app_access_token("672341669466315","a636a46c97773a0c48d2f77f4dbb2120")
graph = facebook.GraphAPI(token)

########
#to collect posts we use the infinite loop
while True:
    #we the two numbers in the list below are the groups
    #we get our information from
    for group in ["105841229530931","291608204298420",]:
        #we use the print statement to show us that we have switched groups
        print "########################################################"


        ###
        #once you are in the group you get the posts
        
        posts = graph.get_connections(group,"feed")

        ##
        #sum1 is used to control how many pages of results we analyse
        #so after each page we analyse,we add 1 to sum1
        
        sum1 = 0
        unformatted_posts = posts[u"data"]
        while sum1 <10:
                
            for i in unformatted_posts:


                #once we get the rwa posts, we have to check if they are in the
                #database
                evaluation = db.facebookdatabase.find_one({"created_time": i[u"created_time"]})
                if evaluation == None:
                    #if they are not in the database we process
                    #the posts and add them to the db
                    try:
                        i[u"message"]
                    except:
                        i[u"message"] = "Failed to collect Message"
                    message_str = i[u"message"]

                     #####################################
                    #Below is our sorting algorithm
                    #we look for key words in the post
                    #if we have a match, we put them in the category
                    
                    if u"clothing" in message_str or u"cloth" in message_str:
                        print "found category"
                        i["category"] = "clothing"
                    else:
                        pass
                    if u"perfumes" in message_str or u"100ml" in message_str:
                        print "found category"
                        i["category"] = "perfumes"
                    else:
                        pass
                    
                    for word in [u"samsung",u"nokia",u"blackberry",u"iphone",u"bb",u"BB",u"8520",u"Iphone",u"htc",u"tablet",u"android",u"Android"]:
                        if word in message_str:
                            print "found category"
                            i["category"] = "phones"
                        else:
                            pass
                    for word in [u"Laptop",u"laptop",u"toshiba",u"500gb",u"500GB",]:
                        if word in message_str:
                            print "found category"
                            i["category"] = "laptops"
                        else:
                            pass

                    for word in [u"toyota",u"Toyota",u"unregistered",u"registered",u"million"]:
                        if word in message_str:
                            print "Found category"
                            i["category"] = "cars"
                        else:
                            pass
                        
                    for word in [u"house",u"housing","rent"]:
                        if word in message_str:
                            print "found category"
                            i["category"] = "housing"
                        else:
                            pass
                    for word in [u"accounting",u"account",u"acca",u"ACCA"]:
                        if word in message_str:
                            print "found category"
                            i["category"] = "accounting"
                        else:
                            pass
                    for word in [u"secretary",u"driver",]:
                        if word in message_str:
                            print "found category"
                            i["category"] = "secretarial"
                        else:
                            pass

                    for word in [u"marketing",u"Marketing",u"business administration",u"ABE"]:
                        if word in message_str:
                            i["category"] = "marketing"
                        else:
                            pass
                        
#finally we insert the posts in the database and we are done
                        
                    db.facebookdatabase.insert(i)
                    try:
                        i["category"]
                    except:
                        i["category"] = "general"
                    print i["category"]
                        

                else:
                    print "finally found it"
                    pass
               #use loop to dump into data base
            nextpost = posts[u"paging"][u"next"]
            new = nextpost.replace("limit=25","limit=100")
            link = urllib2.urlopen(new)
                
            new_unformatted_posts = json.loads(link.read())
            posts = new_unformatted_posts
            unformatted_posts = new_unformatted_posts[u"data"]
            sum1 += 1
