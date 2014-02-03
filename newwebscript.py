import os
import tornado.ioloop
import tornado.web
import pager
import pymongo
from pymongo import MongoClient
from pymongo import ASCENDING, DESCENDING

client  = MongoClient("localhost",27017)
db = client.facebookdatabase

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
            
        posts = db.facebookdatabase.find().sort("created_time", DESCENDING).skip(pages).limit(50)
        people = []
        for i in posts:
            
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


            person= Post(i[u"from"][u"name"],i[u"message"],idz,i[u"picture"],i[u"created_time"])
            people.append(person)
        #print "am done"
            
        self.render("2col_temp.html", title="Home", items = people, section="MainPage" )

class NextHandler(tornado.web.RequestHandler):
    def get(self):
        posts = db.facebookdatabase.find().sort("created_time", DESCENDING).skip(50).limit(50)
        people = []
        for i in posts:
            
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


            person= Post(i[u"from"][u"name"],i[u"message"],idz,i[u"picture"],i[u"created_time"])
            people.append(person)
            
        self.render("newindex.html", title="Home", items = people, )

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
        self.render("2col_temp.html", title = "Employment", items=people, section="Employment")

class AccountingHandler(tornado.web.RequestHandler):
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
        self.render("electronics.html", title = "Automobiles", items=haha)

class SecretarialHandler(tornado.web.RequestHandler):
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
        self.render("electronics.html", title = "Automobiles", items=haha)

class ITHandler(tornado.web.RequestHandler):
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
        self.render("electronics.html", title = "Automobiles", items=haha)

class MarketingHandler(tornado.web.RequestHandler):
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
        self.render("electronics.html", title = "Automobiles", items=haha) 

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
        self.render("electronics.html", title = "Electronics", items=haha)

class CarHandler(tornado.web.RequestHandler):
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
        self.render("electronics.html", title = "Automobiles", items=haha)

class ElectronicsHandler(tornado.web.RequestHandler):
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
        self.render("electronics.html", title = "Automobiles", items=haha)

class LaptopHandler(tornado.web.RequestHandler):
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
        self.render("electronics.html", title = "Automobiles", items=haha)
        
class PhoneHandler(tornado.web.RequestHandler):
    def get(self):
        her  = db.facebookdatabase.find({"category":"electronics"}).sort("created_time", DESCENDING).limit(50)
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
        self.render("electronics.html", title = "Electronics", items=haha)  

class PersonalHandler(tornado.web.RequestHandler):
    def get(self):
        her  = db.facebookdatabase.find({"category":"electronics"}).sort("created_time", DESCENDING).limit(50)
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
        self.render("electronics.html", title = "Electronics", items=haha)  

class ClothingHandler(tornado.web.RequestHandler):
    def get(self):
        her  = db.facebookdatabase.find({"category":"personalcare"}).sort("created_time", DESCENDING).limit(50)
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
        self.render("clothing.html", title = "Clothing", items=haha) 
        
 class PerfumeHandler(tornado.web.RequestHandler):
    def get(self):
        her  = db.facebookdatabase.find({"category":"personalcare"}).sort("created_time", DESCENDING).limit(50)
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
        self.render("clothing.html", title = "Clothing", items=haha)  
        
 class ClothingHandler(tornado.web.RequestHandler):
    def get(self):
        her  = db.facebookdatabase.find({"category":"personalcare"}).sort("created_time", DESCENDING).limit(50)
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
        self.render("clothing.html", title = "Clothing", items=haha)
 
 class MotorHandler(tornado.web.RequestHandler):
    def get(self):
        her  = db.facebookdatabase.find({"category":"personalcare"}).sort("created_time", DESCENDING).limit(50)
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
        self.render("clothing.html", title = "Clothing", items=haha)                                        

class PerfumeHandler(tornado.web.RequestHandler):
    def get(self):
        her  = db.facebookdatabase.find({"category":"personalcare"}).sort("created_time", DESCENDING).limit(50)
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
        self.render("clothing.html", title = "Clothing", items=haha)
        
class MopedHandler(tornado.web.RequestHandler):
    def get(self):
        her  = db.facebookdatabase.find({"category":"personalcare"}).sort("created_time", DESCENDING).limit(50)
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
        self.render("clothing.html", title = "Clothing", items=haha)

class PartsHandler(tornado.web.RequestHandler):
    def get(self):
        her  = db.facebookdatabase.find({"category":"personalcare"}).sort("created_time", DESCENDING).limit(50)
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
        self.render("clothing.html", title = "Clothing", items=haha)


Pager = Pager()
settings = {"ui_modules":pager,}

if __name__ == "__main__":
    __file__ = r"c:\\python27\\Groupp"
    static_path = os.path.join(os.path.dirname(__file__), "Groupp\\static")
    template_path = os.path.join(os.path.dirname(__file__), "Groupp\\template")
    app = tornado.web.Application([
    (r"/", MainHandler),(r"/employment", EmploymentHandler),(r"/clothing", ClothingHandler),\
    (r"/housing", HousingHandler),(r"/cars", CarHandler),(r"/electronics", PhoneHandler),\
    (r"/accounting", LaptopHandler),(r"/electronics", ElectronicsHandler),(r"/electronics", MarketingHandler),
    (r"/electronics", SecretarialHandler),(r"/electronics", ITHandler),(r"/electronics", AccountingHandler)
    ,(r"/next", NextHandler),],debug=True,static_path=static_path,template_path=template_path)

    app.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
