import pymongo
from pymongo import MongoClient

client  = MongoClient("mongodb://macdavel:fbdb@ds061158.mongolab.com:61158/fbdb")
db = client.fbdb


import facebook
import json,urllib2

token = facebook.get_app_access_token("672341669466315","a636a46c97773a0c48d2f77f4dbb2120")
graph = facebook.GraphAPI(token)


while True:
    for group in ["105841229530931","291608204298420",]:
        print "########################################################"
        posts = graph.get_connections(group,"feed")
        sum1 = 0
        unformatted_posts = posts[u"data"]
        while sum1 <2:
            #if string[u"created_time"] == i[u"created_time"]:
                #print "am stopping"
                
            for i in unformatted_posts:
                evaluation = db.facebookdatabase.find_one({"created_time": i[u"created_time"]})
                if evaluation == None:
                    print evaluation
                    try:
                        i[u"message"]
                    except:
                        i[u"message"] = "Failed to collect Message"
                    mess2 = i[u"message"]

                                         
                    if u"clothing" in mess2 or u"cloth" in mess2:
                        print "found category"
                        i["category"] = "clothing"
                    else:
                        pass
                    if u"perfumes" in mess2 or u"100ml" in mess2:
                        print "found category"
                        i["category"] = "perfumes"
                    else:
                        pass
                    
                    for me in [u"samsung",u"nokia",u"blackberry",u"iphone",u"bb",u"BB",u"8520",u"Iphone",u"htc",u"tablet",u"android",u"Android"]:
                        if me in mess2:
                            print "found category"
                            i["category"] = "phones"
                        else:
                            pass
                    for me in [u"Laptop",u"laptop",u"toshiba",u"500gb",u"500GB",]:
                        if me in mess2:
                            print "found category"
                            i["category"] = "laptops"
                        else:
                            pass

                    for me in [u"toyota",u"Toyota",u"unregistered",u"registered",u"million"]:
                        if me in mess2:
                            print "Found category"
                            i["category"] = "cars"
                        else:
                            pass
                        
                    for her in [u"house",u"housing","rent"]:
                        if her in mess2:
                            print "found category"
                            i["category"] = "housing"
                        else:
                            pass
                    for me in [u"accounting",u"account",u"acca",u"ACCA"]:
                        if me in mess2:
                            print "found category"
                            i["category"] = "accounting"
                        else:
                            pass
                    for me in [u"secretary",u"driver",]:
                        if me in mess2:
                            print "found category"
                            i["category"] = "secretarial"
                        else:
                            pass

                    for me in [u"marketing",u"Marketing",u"business administration",u"ABE"]:
                        if me in mess2:
                            i["category"] = "marketing"
                        else:
                            pass
                        

                        
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
            new = nextpost.replace("limit=25","limit=1000")
            link = urllib2.urlopen(new)
                
            new_unformatted_posts = json.loads(link.read())
            posts = new_unformatted_posts
            unformatted_posts = new_unformatted_posts[u"data"]
            sum1 += 1
