from dbModel import *
import random

name = ["派派", "阿肥", "咪咪", "妞妞", "胖胖"
    , "大頭", "阿寶", "皮皮", "嘟嘟", "妮妮"
    ]

picture = ["http://imgur.com/yI00Ehb.jpg",
           "http://i.imgur.com/TtmYVK2.jpg",
           "http://i.imgur.com/EFN7FTv.jpg",
           "http://i.imgur.com/RpD34tu.jpg",
           "http://i.imgur.com/ryCH0b5.jpg",
           "http://i.imgur.com/kzi5kKy.jpg",
           "http://i.imgur.com/bOfNUzK.jpg",
           "http://i.imgur.com/vtb1WCH.jpg",
           "http://i.imgur.com/xrfHjtK.jpg",
           "http://i.imgur.com/z7JCSX8.jpg",
           ]

color = ["#E44040", "#EC21C7", "#8C4C80", "#A41FEC", "#B99ADA"
    , "#4E15E9", "#154EE9", "#4B9CF8", "#65BCD8", "#13EFE4"
   ]

location = ["AMK","AMK","AMK","AMK","AMK",
    "AMK","AMK","AMK","AMK","AMK",

                                                         ]

category = [

                                                        ]

if __name__ == '__main__':
    print('Start Generator Data......')
    for colors in color:
        if colors == "#8C4C80":
            index_category = "Healthy"
            category.append(index_category)
        else:
            index_category = None
            category.append(index_category)

    for index in range(len(name and picture and color and location and category)):
        index_name = name[index]
        index_picture = picture[index]
        index_color = color[index]
        index_location = location[index]
        index_category = category[index]
        insert_data = MapPlace(
            Name=index_name ,
            Picture=index_picture,
            Color=index_color,
            Longitude=random.uniform(120.47, 121.4),
            Latitude=random.uniform(22.5, 25),
            Location=index_location,
            Category=index_category,
        )
        db.session.add(insert_data)
    db.session.commit()
    print('Generator Data Done')
