
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

                 ):
        self.Name = Name
        self.Picture = Picture
        self.Color = Color
        self.Longitude = Longitude
        self.Latitude = Latitude
        self.Location = Location
        self.Category = Category

    def get_name(self):
        return self.Name

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

class healthy(MapPlace):
    __tablename__ = 'MapPlace'

    def __init__(self, Name, Picture, Color , Longitude, Latitude,location):
        super().__init__(Name, Picture, Color , Longitude, Latitude,location )
        self.Category = ''

    def get_category(self):
        return self.Category


