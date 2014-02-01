import os
import tornado.httpserver
import tornado.options
import tornado.ioloop
import tornado.web
import pymongo
from pymongo import MongoClient
from pymongo import ASCENDING, DESCENDING

from tornado.options import define, options
define("port", default=5000, help="run on the given port", type=int)

client  = MongoClient("mongodb://macdavel:fbdb@ds061158.mongolab.com:61158/fbdb")
db = client.fbdb



#client  = MongoClient("localhost",27017)
#db = client.facebookdatabase

#First we created a class pager for the recent posts
#We only did pagination for recent posts because
#it had a large number of posts
#Our sorting algorithm did not yield many results and
#it is a point of improvement for our project


###
#We use pager to keep track of what page we are on
#could have done it with a variable aswell

class Pager(object):
    def __init__(self):
        self.page = 0 


#####
#Once we get the posts from the database,we make them instances
#Instead of passing the posts to the html template
#We pass the instances because it is easier to access the info

        
class Post(object):
    def __init__(self,name, message,id_, picture,time):
        self.name = name
        self.message = message
        self.id = id_
        self.picture = picture
        self.time = time



#The main Handles the home page
#It is just static images here so nothing complicated required
class MainHandler(tornado.web.RequestHandler):
    def get(self):           
        self.render("HOME.html", title="Home", )








class RecentHandler(tornado.web.RequestHandler):
    
    def get(self):

        #################
#This is where the fun begins
#First we start by checking for arguments for pagination
#Our template creates two columns from the results hence
#we have to iterate over two lists
#This makes it difficult for pagination
#Because you do not want the 50 results that were in column 2
#to be in the first column of the next page
#essentially you want to skip 2 pages
#we decided to use a fancy algorithm for this
#that is the pagination code
        page = self.get_arguments("page",None)
        if len(page) == 0:
            pages = Pager.page
        else:
            if page[0] == "next":
                Pager.page += 1
                pages = Pager.page
            else:
                if Pager.page >= 1:
                    Pager.page  = Pager.page - 1
                    pages = Pager.page
                else:
                    pages = Pager.page
        if pages <= 1:
            first_pagination = pages
        elif pages%2 == 0:
            first_pagination = pages+1
        else:
            first_pagination = pages+2
        second_pagination = first_pagination+1

        ############################################

        ####
        #we then go on to get a cursor from the database and use it
        #to iterate over the posts and while iterating we create instances
        #which are then passed into the template
                    
        raw_posts  = db.facebookdatabase.find().sort("created_time", DESCENDING).skip(first_pagination*50).limit(5)
        post_instances = []
        for i in raw_posts:
            
            name = i[u"from"][u"name"]
            try:
                i[u"message"]
            except:
                i[u"message"] = "Failed to collect message"

            try:
                i[u"picture"]
            except:
                i[u"picture"] = "http://crockpotladies.com/wp-content/uploads/2011/10/610x300xNo-Image-Available-610x300.jpg.pagespeed.ic.BuZqmFMIyd.jpg"
            idz =  "http://www.facebook.com/"+i[u"from"][u"id"]


            name = Post(i[u"from"][u"name"],i[u"message"],idz,i[u"picture"],i[u"created_time"])
            post_instances.append(name)

        ####
        #We create two lists of instances
        #Because our template displays the info in two column format
        raw_postsere  = db.facebookdatabase.find().sort("created_time", DESCENDING).skip(second_pagination*50).limit(5)
        post_instances_2 = []
        for me in raw_postsere:
            
            you = me[u"from"][u"name"]
            try:
                me[u"message"]
            except:
                me[u"message"] = "Failed to collect message"

            try:
                me[u"picture"]
            except:
                me[u"picture"] = "http://crockpotladies.com/wp-content/uploads/2011/10/610x300xNo-Image-Available-610x300.jpg.pagespeed.ic.BuZqmFMIyd.jpg"
            idz =  "http://www.facebook.com/"+me[u"from"][u"id"]


            you = Post(me[u"from"][u"name"],me[u"message"],idz,me[u"picture"],me[u"created_time"])
            post_instances_2.append(you)
        self.render("2col_temp.html", title = "Automobiles", items=post_instances, seconditems=post_instances_2, section="Recent Postings")





        
#################################################
#This Process is repeated for all the pages on the website
#########################################################



class EmploymentHandler(tornado.web.RequestHandler):
    def get(self):
        raw_posts  = db.facebookdatabase.find({"category":"accounting"}).sort("created_time", DESCENDING).limit(5)
        people = []
        for i in raw_posts:
            
            person = i[u"from"][u"name"]
            try:
                i[u"message"]
            except:
                i[u"message"] = "Failed to collect message"

            try:
                i[u"picture"]
            except:
                i[u"picture"] = "http://crockpotladies.com/wp-content/uploads/2011/10/610x300xNo-Image-Available-610x300.jpg.pagespeed.ic.BuZqmFMIyd.jpg"
            idz =  "http://www.facebook.com/"+i[u"from"][u"id"]

            person = Post(i[u"from"][u"name"],i[u"message"],idz,i[u"picture"],i[u"created_time"])
            people.append(person)
        self.render("2col_temp.html", title = "Employment", items=people,seconditems=people, section="Employment")


        
class PersonalcareHandler(tornado.web.RequestHandler):
    def get(self):
        raw_posts  = db.facebookdatabase.find({"category":"clothing"}).sort("created_time", DESCENDING).limit(5)
        post_instances = []
        for i in raw_posts:
            
            name = i[u"from"][u"name"]
            try:
                i[u"message"]
            except:
                i[u"message"] = "Failed to collect message"

            try:
                i[u"picture"]
            except:
                i[u"picture"] = "http://crockpotladies.com/wp-content/uploads/2011/10/610x300xNo-Image-Available-610x300.jpg.pagespeed.ic.BuZqmFMIyd.jpg"
            idz =  "http://www.facebook.com/"+i[u"from"][u"id"]


            name = Post(i[u"from"][u"name"],i[u"message"],idz,i[u"picture"],i[u"created_time"])
            post_instances.append(name)
        self.render("2col_temp.html", title = "Clothing", items=post_instances,seconditems=post_instances,section="Personal Care")
        
class ElectronicsHandler(tornado.web.RequestHandler):
    def get(self):
        raw_posts  = db.facebookdatabase.find({u"category":"phones"}).sort("created_time", DESCENDING).limit(5)
        post_instances = []
        for i in raw_posts:
            
            name = i[u"from"][u"name"]
            try:
                i[u"message"]
            except:
                i[u"message"] = "Failed to collect message"

            try:
                i[u"picture"]
            except:
                i[u"picture"] = "http://crockpotladies.com/wp-content/uploads/2011/10/610x300xNo-Image-Available-610x300.jpg.pagespeed.ic.BuZqmFMIyd.jpg"
            idz =  "http://www.facebook.com/"+i[u"from"][u"id"]


            name = Post(i[u"from"][u"name"],i[u"message"],idz,i[u"picture"],i[u"created_time"])
            post_instances.append(name)
        self.render("2col_temp.html", title = "Electronics", items=post_instances,seconditems=post_instances, section="Electronics")

class HousingHandler(tornado.web.RequestHandler):
    def get(self):
        raw_posts  = db.facebookdatabase.find({"category":"housing"}).sort("created_time", DESCENDING).limit(5)
        post_instances = []
        for i in raw_posts:
            
            name = i[u"from"][u"name"]
            try:
                i[u"message"]
            except:
                i[u"message"] = "Failed to collect message"

            try:
                i[u"picture"]
            except:
                i[u"picture"] = "http://crockpotladies.com/wp-content/uploads/2011/10/610x300xNo-Image-Available-610x300.jpg.pagespeed.ic.BuZqmFMIyd.jpg"
            idz =  "http://www.facebook.com/"+i[u"from"][u"id"]


            name = Post(i[u"from"][u"name"],i[u"message"],idz,i[u"picture"],i[u"created_time"])
            post_instances.append(name)
        self.render("2col_temp.html", title = "Electronics", items=post_instances,seconditems=post_instances, section="Housing")

class MotorHandler(tornado.web.RequestHandler):
    def get(self):
        raw_posts  = db.facebookdatabase.find({"category":"cars"}).sort("created_time", DESCENDING).limit(5)
        post_instances = []
        for i in raw_posts:
            
            name = i[u"from"][u"name"]
            try:
                i[u"message"]
            except:
                i[u"message"] = "Failed to collect message"

            try:
                i[u"picture"]
            except:
                i[u"picture"] = "http://crockpotladies.com/wp-content/uploads/2011/10/610x300xNo-Image-Available-610x300.jpg.pagespeed.ic.BuZqmFMIyd.jpg"
            idz =  "http://www.facebook.com/"+i[u"from"][u"id"]


            name = Post(i[u"from"][u"name"],i[u"message"],idz,i[u"picture"],i[u"created_time"])
            post_instances.append(name)
        self.render("2col_temp.html", title = "Automobiles", items=post_instances, seconditems=post_instances, section="Motors")

class AccountingHandler(tornado.web.RequestHandler):
    def get(self):
        raw_posts  = db.facebookdatabase.find({"category":"accounting"}).sort("created_time", DESCENDING).limit(5)
        post_instances = []
        for i in raw_posts:
            
            name = i[u"from"][u"name"]
            try:
                i[u"message"]
            except:
                i[u"message"] = "Failed to collect message"

            try:
                i[u"picture"]
            except:
                i[u"picture"] = "http://crockpotladies.com/wp-content/uploads/2011/10/610x300xNo-Image-Available-610x300.jpg.pagespeed.ic.BuZqmFMIyd.jpg"
            idz =  "http://www.facebook.com/"+i[u"from"][u"id"]


            name = Post(i[u"from"][u"name"],i[u"message"],idz,i[u"picture"],i[u"created_time"])
            post_instances.append(name)
        self.render("2col_temp.html", title = "Automobiles", items=post_instances, seconditems=post_instances,section="Accounting Jobs")

class SecretarialHandler(tornado.web.RequestHandler):
    def get(self):
        raw_posts  = db.facebookdatabase.find({"category":"secretary"}).sort("created_time", DESCENDING).limit(5)
        post_instances = []
        for i in raw_posts:
            
            name = i[u"from"][u"name"]
            try:
                i[u"message"]
            except:
                i[u"message"] = "Failed to collect message"

            try:
                i[u"picture"]
            except:
                i[u"picture"] = "http://crockpotladies.com/wp-content/uploads/2011/10/610x300xNo-Image-Available-610x300.jpg.pagespeed.ic.BuZqmFMIyd.jpg"
            idz =  "http://www.facebook.com/"+i[u"from"][u"id"]


            name = Post(i[u"from"][u"name"],i[u"message"],idz,i[u"picture"],i[u"created_time"])
            post_instances.append(name)
        self.render("2col_temp.html", title = "Automobiles", items=post_instances,seconditems=post_instances, section="Secretarial Jobs")

class ITHandler(tornado.web.RequestHandler):
    def get(self):
        raw_posts  = db.facebookdatabase.find({"category":"technology"}).sort("created_time", DESCENDING).limit(5)
        post_instances = []
        for i in raw_posts:
            
            name = i[u"from"][u"name"]
            try:
                i[u"message"]
            except:
                i[u"message"] = "Failed to collect message"

            try:
                i[u"picture"]
            except:
                i[u"picture"] = "http://crockpotladies.com/wp-content/uploads/2011/10/610x300xNo-Image-Available-610x300.jpg.pagespeed.ic.BuZqmFMIyd.jpg"
            idz =  "http://www.facebook.com/"+i[u"from"][u"id"]


            name = Post(i[u"from"][u"name"],i[u"message"],idz,i[u"picture"],i[u"created_time"])
            post_instances.append(name)
        self.render("2col_temp.html", title = "Automobiles", items=post_instances,seconditems=post_instances, section = "IT Jobs")

class MarketingHandler(tornado.web.RequestHandler):
    def get(self):
        raw_posts  = db.facebookdatabase.find({"category":"marketing"}).sort("created_time", DESCENDING).limit(5)
        post_instances = []
        for i in raw_posts:
            
            name = i[u"from"][u"name"]
            try:
                i[u"message"]
            except:
                i[u"message"] = "Failed to collect message"

            try:
                i[u"picture"]
            except:
                i[u"picture"] = "http://crockpotladies.com/wp-content/uploads/2011/10/610x300xNo-Image-Available-610x300.jpg.pagespeed.ic.BuZqmFMIyd.jpg"
            idz =  "http://www.facebook.com/"+i[u"from"][u"id"]


            name = Post(i[u"from"][u"name"],i[u"message"],idz,i[u"picture"],i[u"created_time"])
            post_instances.append(name)
        self.render("2col_temp.html", title = "Automobiles", items=post_instances,seconditems=post_instances, section = "Marketing Jobs")

class MobileHandler(tornado.web.RequestHandler):
    def get(self):
        raw_posts  = db.facebookdatabase.find({"category":u"phones"}).sort("created_time", DESCENDING).limit(5)
        post_instances = []
        for i in raw_posts:
            
            name = i[u"from"][u"name"]
            try:
                i[u"message"]
            except:
                i[u"message"] = "Failed to collect message"

            try:
                i[u"picture"]
            except:
                i[u"picture"] = "http://crockpotladies.com/wp-content/uploads/2011/10/610x300xNo-Image-Available-610x300.jpg.pagespeed.ic.BuZqmFMIyd.jpg"
            idz =  "http://www.facebook.com/"+i[u"from"][u"id"]


            name = Post(i[u"from"][u"name"],i[u"message"],idz,i[u"picture"],i[u"created_time"])
            post_instances.append(name)
        self.render("2col_temp.html", title = "Automobiles", items=post_instances,seconditems=post_instances ,section = "Mobile Phones")

class LaptopHandler(tornado.web.RequestHandler):
    def get(self):
        raw_posts  = db.facebookdatabase.find({"category":"laptops"}).sort("created_time", DESCENDING).limit(5)
        post_instances = []
        for i in raw_posts:
            
            name = i[u"from"][u"name"]
            try:
                i[u"message"]
            except:
                i[u"message"] = "Failed to collect message"

            try:
                i[u"picture"]
            except:
                i[u"picture"] = "http://crockpotladies.com/wp-content/uploads/2011/10/610x300xNo-Image-Available-610x300.jpg.pagespeed.ic.BuZqmFMIyd.jpg"
            idz =  "http://www.facebook.com/"+i[u"from"][u"id"]


            name = Post(i[u"from"][u"name"],i[u"message"],idz,i[u"picture"],i[u"created_time"])
            post_instances.append(name)
        self.render("2col_temp.html", title = "Automobiles", items=post_instances,seconditems=post_instances ,section = "Computers")

class ClothingHandler(tornado.web.RequestHandler):
    def get(self):
        raw_posts  = db.facebookdatabase.find({"category":"clothing"}).sort("created_time", DESCENDING).limit(5)
        post_instances = []
        for i in raw_posts:
            
            name = i[u"from"][u"name"]
            try:
                i[u"message"]
            except:
                i[u"message"] = "Failed to collect message"

            try:
                i[u"picture"]
            except:
                i[u"picture"] = "http://crockpotladies.com/wp-content/uploads/2011/10/610x300xNo-Image-Available-610x300.jpg.pagespeed.ic.BuZqmFMIyd.jpg"
            idz =  "http://www.facebook.com/"+i[u"from"][u"id"]


            name = Post(i[u"from"][u"name"],i[u"message"],idz,i[u"picture"],i[u"created_time"])
            post_instances.append(name)
        self.render("2col_temp.html", title = "Automobiles", items=post_instances,seconditems=post_instances, section = "Clothing")
class PerfumeHandler(tornado.web.RequestHandler):
    def get(self):
        raw_posts  = db.facebookdatabase.find({"category":"perfumes"}).sort("created_time", DESCENDING).limit(5)
        post_instances = []
        for i in raw_posts:
            
            name = i[u"from"][u"name"]
            try:
                i[u"message"]
            except:
                i[u"message"] = "Failed to collect message"

            try:
                i[u"picture"]
            except:
                i[u"picture"] = "http://crockpotladies.com/wp-content/uploads/2011/10/610x300xNo-Image-Available-610x300.jpg.pagespeed.ic.BuZqmFMIyd.jpg"
            idz =  "http://www.facebook.com/"+i[u"from"][u"id"]


            name = Post(i[u"from"][u"name"],i[u"message"],idz,i[u"picture"],i[u"created_time"])
            post_instances.append(name)
        self.render("2col_temp.html", title = "Automobiles", items=post_instances, seconditems=post_instances ,section = "Perfumes")

Pager = Pager()

if __name__ == "__main__":
    path = os.getcwd()
    static_path = os.path.join(path, "static")
    template_path = os.path.join(path, "template")
    app = tornado.web.Application([
    (r"/", MainHandler),(r"/recent", RecentHandler),(r"/employment", EmploymentHandler),(r"/personalcare", PersonalcareHandler),\
    (r"/housing", HousingHandler),(r"/cars", MotorHandler),(r"/electronics", ElectronicsHandler),\
    (r"/laptops", LaptopHandler),(r"/phones", MobileHandler),(r"/marketing", MarketingHandler),
    (r"/secretary", SecretarialHandler),(r"/it", ITHandler),(r"/accounting", AccountingHandler),
    (r"/clothing", ClothingHandler),(r"/perfumes", PerfumeHandler)
    ,],debug=True,static_path=static_path,template_path=template_path)
    
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(os.environ.get("PORT", 5000))
    app.listen(tornado.options.options.port) #These two commented out because of deployment to heroku
    #app.listen(8888)                           #uncomment for running on local machine
    #tornado.ioloop.IOLoop.instance().start()

