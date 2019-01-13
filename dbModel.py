
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


class healthy(MapPlace):
    __tablename__ = 'MapPlace'

    def __init__(self, Name, Picture, Color , Longitude, Latitude,Location,Category ,Postal_Code):
        super().__init__(Name, Picture, Color , Longitude, Latitude,Location, Category ,Postal_Code )
        self.Category = 'Healthy'

    def get_category(self):
        return self.Category
