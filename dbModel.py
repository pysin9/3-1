
from Entity import *


class MapPlace(db.Model):
    __tablename__ = 'MapPlace'

    def __init__(self
                 , Name
                 , Picture
                 , Color
                 , Longitude
                 , Latitude
                 , Location
                 , Category
                 , Postal_Code

                 ):
        self.Name = Name
        self.Picture = Picture
        self.Color = Color
        self.Longitude = Longitude
        self.Latitude = Latitude
        self.Location = Location
        self.Category = Category
        self.Postal_Code = Postal_Code


    def check(self):
        for colors in self.Color:
            if colors == "#de2d26":
                self.Category = "Spicy"
                self.Category = self.Category
            elif colors == "#000000":
                self.Category = "Halal"
                self.Category = self.Category
            elif colors == "#377eb8":
                self.Category = "Vegertarian"
                self.Category = self.Category
            elif colors == "#4daf4a":
                self.Category = "Healthy"
                self.Category = self.Category
            elif colors == "#984ea3":
                self.Category = "Elder friendly"
                self.Category = self.Category
            elif colors == "#fc8d59":
                self.Category = "Desert"
                self.Category = self.Category
            elif colors == "#A0522D":
                self.Category = "Hawker"
                self.Category = self.Category
            elif colors == "#E4D03B":
                self.Category = "Cafes"
                self.Category = self.Category
            else :
                self.Category = None
    def get_name(self):
        return self.Name

    # app.jinja_env.globals.update(get_name=get_name)

    def get_picture(self):
        return self.Picture

    def get_color(self):
        return self.Color

    def get_longitude(self):
        return self.Longitude

    def get_latitude(self):
        return self.Latitude

    def get_location(self):
        return self.Location

    def get_category(self):
        return self.Category

    def get_postal_code(self):
        return self.Postal_Code


