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


class Pager(object):
    def __init__(self):
        self.page = 0 

class Post(object):
    def __init__(self,name, message,id_, picture,time):
        self.name = name
        self.message = message
        self.id = id_
        self.picture = picture
        self.time = time

class MainHandler(tornado.web.RequestHandler):
    def get(self):           
        self.render("HOME.html", title="Home", )

class RecentHandler(tornado.web.RequestHandler):
    
    def get(self):
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
                    
        her  = db.facebookdatabase.find().sort("created_time", DESCENDING).skip(first_pagination*50).limit(5)
        haha = []
        for i in her:
            
            hehe = i[u"from"][u"name"]
            try:
                i[u"message"]
            except:
                i[u"message"] = "Failed to collect message"

            try:
                i[u"picture"]
            except:
                i[u"picture"] = "http://crockpotladies.com/wp-content/uploads/2011/10/610x300xNo-Image-Available-610x300.jpg.pagespeed.ic.BuZqmFMIyd.jpg"
            idz =  "http://www.facebook.com/"+i[u"from"][u"id"]


            hehe = Post(i[u"from"][u"name"],i[u"message"],idz,i[u"picture"],i[u"created_time"])
            haha.append(hehe)
        herere  = db.facebookdatabase.find().sort("created_time", DESCENDING).skip(second_pagination*50).limit(5)
        hoho = []
        for me in herere:
            
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
            hoho.append(you)
        self.render("2col_temp.html", title = "Automobiles", items=haha, seconditems=hoho, section="Recent Postings")


class EmploymentHandler(tornado.web.RequestHandler):
    def get(self):
        her  = db.facebookdatabase.find({"category":"employment"}).sort("created_time", DESCENDING).limit(50)
        people = []
        for i in her:
            
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


            #Use for loop for pagination
            person = Post(i[u"from"][u"name"],i[u"message"],idz,i[u"picture"],i[u"created_time"])
            people.append(person)
        self.render("2col_temp.html", title = "Employment", items=people,seconditems=people, section="Employment")
class PersonalcareHandler(tornado.web.RequestHandler):
    def get(self):
        her  = db.facebookdatabase.find({"category":"clothing"}).sort("created_time", DESCENDING).limit(50)
        haha = []
        for i in her:
            
            hehe = i[u"from"][u"name"]
            try:
                i[u"message"]
            except:
                i[u"message"] = "Failed to collect message"

            try:
                i[u"picture"]
            except:
                i[u"picture"] = "http://crockpotladies.com/wp-content/uploads/2011/10/610x300xNo-Image-Available-610x300.jpg.pagespeed.ic.BuZqmFMIyd.jpg"
            idz =  "http://www.facebook.com/"+i[u"from"][u"id"]


            hehe = Post(i[u"from"][u"name"],i[u"message"],idz,i[u"picture"],i[u"created_time"])
            haha.append(hehe)
        self.render("2col_temp.html", title = "Clothing", items=haha,seconditems=haha,section="Personal Care")
        
class ElectronicsHandler(tornado.web.RequestHandler):
    def get(self):
        her  = db.facebookdatabase.find({u"category":"phones"}).sort("created_time", DESCENDING).limit(50)
        haha = []
        for i in her:
            
            hehe = i[u"from"][u"name"]
            try:
                i[u"message"]
            except:
                i[u"message"] = "Failed to collect message"

            try:
                i[u"picture"]
            except:
                i[u"picture"] = "http://crockpotladies.com/wp-content/uploads/2011/10/610x300xNo-Image-Available-610x300.jpg.pagespeed.ic.BuZqmFMIyd.jpg"
            idz =  "http://www.facebook.com/"+i[u"from"][u"id"]


            hehe = Post(i[u"from"][u"name"],i[u"message"],idz,i[u"picture"],i[u"created_time"])
            haha.append(hehe)
        self.render("2col_temp.html", title = "Electronics", items=haha,seconditems=haha, section="Electronics")

class HousingHandler(tornado.web.RequestHandler):
    def get(self):
        her  = db.facebookdatabase.find({"category":"housing"}).sort("created_time", DESCENDING).limit(50)
        haha = []
        for i in her:
            
            hehe = i[u"from"][u"name"]
            try:
                i[u"message"]
            except:
                i[u"message"] = "Failed to collect message"

            try:
                i[u"picture"]
            except:
                i[u"picture"] = "http://crockpotladies.com/wp-content/uploads/2011/10/610x300xNo-Image-Available-610x300.jpg.pagespeed.ic.BuZqmFMIyd.jpg"
            idz =  "http://www.facebook.com/"+i[u"from"][u"id"]


            hehe = Post(i[u"from"][u"name"],i[u"message"],idz,i[u"picture"],i[u"created_time"])
            haha.append(hehe)
        self.render("2col_temp.html", title = "Electronics", items=haha,seconditems=haha, section="Housing")

class MotorHandler(tornado.web.RequestHandler):
    def get(self):
        her  = db.facebookdatabase.find({"category":"cars"}).sort("created_time", DESCENDING).limit(50)
        haha = []
        for i in her:
            
            hehe = i[u"from"][u"name"]
            try:
                i[u"message"]
            except:
                i[u"message"] = "Failed to collect message"

            try:
                i[u"picture"]
            except:
                i[u"picture"] = "http://crockpotladies.com/wp-content/uploads/2011/10/610x300xNo-Image-Available-610x300.jpg.pagespeed.ic.BuZqmFMIyd.jpg"
            idz =  "http://www.facebook.com/"+i[u"from"][u"id"]


            hehe = Post(i[u"from"][u"name"],i[u"message"],idz,i[u"picture"],i[u"created_time"])
            haha.append(hehe)
        self.render("2col_temp.html", title = "Automobiles", items=haha, seconditems=haha, section="Motors")

class AccountingHandler(tornado.web.RequestHandler):
    def get(self):
        her  = db.facebookdatabase.find({"category":"accounting"}).sort("created_time", DESCENDING).limit(50)
        haha = []
        for i in her:
            
            hehe = i[u"from"][u"name"]
            try:
                i[u"message"]
            except:
                i[u"message"] = "Failed to collect message"

            try:
                i[u"picture"]
            except:
                i[u"picture"] = "http://crockpotladies.com/wp-content/uploads/2011/10/610x300xNo-Image-Available-610x300.jpg.pagespeed.ic.BuZqmFMIyd.jpg"
            idz =  "http://www.facebook.com/"+i[u"from"][u"id"]


            hehe = Post(i[u"from"][u"name"],i[u"message"],idz,i[u"picture"],i[u"created_time"])
            haha.append(hehe)
        self.render("2col_temp.html", title = "Automobiles", items=haha, seconditems=haha,section="Accounting Jobs")

class SecretarialHandler(tornado.web.RequestHandler):
    def get(self):
        her  = db.facebookdatabase.find({"category":"secretary"}).sort("created_time", DESCENDING).limit(50)
        haha = []
        for i in her:
            
            hehe = i[u"from"][u"name"]
            try:
                i[u"message"]
            except:
                i[u"message"] = "Failed to collect message"

            try:
                i[u"picture"]
            except:
                i[u"picture"] = "http://crockpotladies.com/wp-content/uploads/2011/10/610x300xNo-Image-Available-610x300.jpg.pagespeed.ic.BuZqmFMIyd.jpg"
            idz =  "http://www.facebook.com/"+i[u"from"][u"id"]


            hehe = Post(i[u"from"][u"name"],i[u"message"],idz,i[u"picture"],i[u"created_time"])
            haha.append(hehe)
        self.render("2col_temp.html", title = "Automobiles", items=haha,seconditems=haha, section="Secretarial Jobs")

class ITHandler(tornado.web.RequestHandler):
    def get(self):
        her  = db.facebookdatabase.find({"category":"technology"}).sort("created_time", DESCENDING).limit(50)
        haha = []
        for i in her:
            
            hehe = i[u"from"][u"name"]
            try:
                i[u"message"]
            except:
                i[u"message"] = "Failed to collect message"

            try:
                i[u"picture"]
            except:
                i[u"picture"] = "http://crockpotladies.com/wp-content/uploads/2011/10/610x300xNo-Image-Available-610x300.jpg.pagespeed.ic.BuZqmFMIyd.jpg"
            idz =  "http://www.facebook.com/"+i[u"from"][u"id"]


            hehe = Post(i[u"from"][u"name"],i[u"message"],idz,i[u"picture"],i[u"created_time"])
            haha.append(hehe)
        self.render("2col_temp.html", title = "Automobiles", items=haha,seconditems=haha, section = "IT Jobs")

class MarketingHandler(tornado.web.RequestHandler):
    def get(self):
        her  = db.facebookdatabase.find({"category":"marketing"}).sort("created_time", DESCENDING).limit(50)
        haha = []
        for i in her:
            
            hehe = i[u"from"][u"name"]
            try:
                i[u"message"]
            except:
                i[u"message"] = "Failed to collect message"

            try:
                i[u"picture"]
            except:
                i[u"picture"] = "http://crockpotladies.com/wp-content/uploads/2011/10/610x300xNo-Image-Available-610x300.jpg.pagespeed.ic.BuZqmFMIyd.jpg"
            idz =  "http://www.facebook.com/"+i[u"from"][u"id"]


            hehe = Post(i[u"from"][u"name"],i[u"message"],idz,i[u"picture"],i[u"created_time"])
            haha.append(hehe)
        self.render("2col_temp.html", title = "Automobiles", items=haha,seconditems=haha, section = "Marketing Jobs")

class MobileHandler(tornado.web.RequestHandler):
    def get(self):
        her  = db.facebookdatabase.find({"category":u"phones"}).sort("created_time", DESCENDING).limit(50)
        haha = []
        for i in her:
            
            hehe = i[u"from"][u"name"]
            try:
                i[u"message"]
            except:
                i[u"message"] = "Failed to collect message"

            try:
                i[u"picture"]
            except:
                i[u"picture"] = "http://crockpotladies.com/wp-content/uploads/2011/10/610x300xNo-Image-Available-610x300.jpg.pagespeed.ic.BuZqmFMIyd.jpg"
            idz =  "http://www.facebook.com/"+i[u"from"][u"id"]


            hehe = Post(i[u"from"][u"name"],i[u"message"],idz,i[u"picture"],i[u"created_time"])
            haha.append(hehe)
        self.render("2col_temp.html", title = "Automobiles", items=haha,seconditems=haha ,section = "Mobile Phones")

class LaptopHandler(tornado.web.RequestHandler):
    def get(self):
        her  = db.facebookdatabase.find({"category":"laptops"}).sort("created_time", DESCENDING).limit(50)
        haha = []
        for i in her:
            
            hehe = i[u"from"][u"name"]
            try:
                i[u"message"]
            except:
                i[u"message"] = "Failed to collect message"

            try:
                i[u"picture"]
            except:
                i[u"picture"] = "http://crockpotladies.com/wp-content/uploads/2011/10/610x300xNo-Image-Available-610x300.jpg.pagespeed.ic.BuZqmFMIyd.jpg"
            idz =  "http://www.facebook.com/"+i[u"from"][u"id"]


            hehe = Post(i[u"from"][u"name"],i[u"message"],idz,i[u"picture"],i[u"created_time"])
            haha.append(hehe)
        self.render("2col_temp.html", title = "Automobiles", items=haha,seconditems=haha ,section = "Computers")

class ClothingHandler(tornado.web.RequestHandler):
    def get(self):
        her  = db.facebookdatabase.find({"category":"clothing"}).sort("created_time", DESCENDING).limit(50)
        haha = []
        for i in her:
            
            hehe = i[u"from"][u"name"]
            try:
                i[u"message"]
            except:
                i[u"message"] = "Failed to collect message"

            try:
                i[u"picture"]
            except:
                i[u"picture"] = "http://crockpotladies.com/wp-content/uploads/2011/10/610x300xNo-Image-Available-610x300.jpg.pagespeed.ic.BuZqmFMIyd.jpg"
            idz =  "http://www.facebook.com/"+i[u"from"][u"id"]


            hehe = Post(i[u"from"][u"name"],i[u"message"],idz,i[u"picture"],i[u"created_time"])
            haha.append(hehe)
        self.render("2col_temp.html", title = "Automobiles", items=haha,seconditems=haha, section = "Clothing")
class PerfumeHandler(tornado.web.RequestHandler):
    def get(self):
        her  = db.facebookdatabase.find({"category":"perfumes"}).sort("created_time", DESCENDING).limit(50)
        haha = []
        for i in her:
            
            hehe = i[u"from"][u"name"]
            try:
                i[u"message"]
            except:
                i[u"message"] = "Failed to collect message"

            try:
                i[u"picture"]
            except:
                i[u"picture"] = "http://crockpotladies.com/wp-content/uploads/2011/10/610x300xNo-Image-Available-610x300.jpg.pagespeed.ic.BuZqmFMIyd.jpg"
            idz =  "http://www.facebook.com/"+i[u"from"][u"id"]


            hehe = Post(i[u"from"][u"name"],i[u"message"],idz,i[u"picture"],i[u"created_time"])
            haha.append(hehe)
        self.render("2col_temp.html", title = "Automobiles", items=haha, seconditems=haha ,section = "Perfumes")

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
    #http_server = tornado.httpserver.HTTPServer(app())
    #http_server.listen(os.environ.get("PORT", 5000))
    app.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

