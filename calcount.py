class Calories:
    def __init__(self, calone  , caltwo , calthree  ):
        self.calone = calone
        self.caltwo = caltwo
        self.calthree = calthree

    def get_calone(self):
        return self.calone

    def get_caltwo(self):
        return self.caltwo

    def get_calthree(self):
        return self.calthree

    def set_calone(self,calone):
        self.calone = calone

    def set_caltwo(self,caltwo):
        self.caltwo = caltwo

    def set_calthree(self,calthree):
        self.calthree = calthree

    def __str__(self):
        s = '{} calories'.format(int(self.get_calone())+int(self.get_caltwo())+int(self.get_calthree()))
        return s
