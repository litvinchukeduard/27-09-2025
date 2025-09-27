from dataclasses import dataclass, asdict
from datetime import date
from copy import deepcopy

import json
'''

VideoContent

Movie, Series Episode, YouTube video

1-5, episode number 1-5, views likes

Quality number: 
stars/5 * 100
stars/5 * 100
likes/views * 100
'''

def get_content_from_json(json_dict: dict):
    ...


# {"title": "Test", "release_date": "2025-09-27"}
@dataclass
class VideoContent:
    title: str
    price: int
    release_date: date

    @staticmethod
    def from_json(json_data):
        print(json_data)
        type = json_data['type']
        if type not in CLASS_REGISTRY:
            raise TypeError(f"Class deserialization is not possible for type '{type}'")
        
        cls = CLASS_REGISTRY[type] # Movie
        del json_data['type']
        return cls(**json_data)
        # if type == 'Movie':
        #     ...

    def as_json(self):
        # return {
        #     'title': self.title,
        #     'release_date': self.release_date.strftime('%d-%m-%Y'), #2025-09-27 27-09-2025
        #     'price': self.price
        # }
        dict = deepcopy(self.__dict__)
        dict['release_date'] = self.release_date.strftime('%d-%m-%Y')
        dict['type'] = self.__class__.__name__
        return dict

    def calculateQualityNumber(self):
        raise NotImplementedError("Base class VideoContent does not have a way to calculate quality")


# {"title": "Test", "release_date": "2025-09-27", "stars": 4, "director": "Test"}
@dataclass
class Movie(VideoContent):
    stars: int
    director: str

    def as_json(self):
        parent_dict = super().as_json()
        return parent_dict

    def __post_init__(self):
        if not (0 <= self.stars <= 5):
            raise ValueError("Stars can not be less than 0 or greater than 5")

    def calculateQualityNumber(self):
        return (self.stars / 5) * 100
    
    # def as_json(self):

    

# {"title": "Test", "release_date": "2025-09-27", "stars": 4, "director": "Test"}
@dataclass
class OldMovie(VideoContent):
    stars: int
    director: str

    def as_json(self):
        parent_dict = super().as_json()
        return parent_dict

    def __post_init__(self):
        if not (0 <= self.stars <= 5):
            raise ValueError("Stars can not be less than 0 or greater than 5")

    def calculateQualityNumber(self):
        return (self.stars / 5) * 100


@dataclass
class SeriesEpisode(Movie):
    series_name: str


@dataclass
class YouTubeVideo(VideoContent):
    _views: int
    _likes: int

    @staticmethod
    def from_json(json_data: dict):
        json_data['_views'] = json_data['views']
        json_data['_likes'] = json_data['likes']
        del json_data['likes']
        del json_data['views']
        return VideoContent.from_json(json_data)

    def as_json(self):
        parent_dict = super().as_json()
        del parent_dict['_views']
        del parent_dict['_likes']
        parent_dict['views'] = self.views
        parent_dict['likes'] = self.likes
        return parent_dict

    @property
    def views(self):
        return self._views
    
    @views.setter
    def views(self, new_value):
        if new_value < 0:
            raise ValueError("Can not have value for views less than 0")
        
    @property
    def likes(self):
        return self._likes
    
    @likes.setter
    def likes(self, new_value):
        if new_value < 0:
            raise ValueError("Can not have value for likes less than 0")

    def calculateQualityNumber(self):
        return (self.likes / self.views) * 100
    

CLASS_REGISTRY = {
    'Movie': Movie,
    'YouTubeVideo': YouTubeVideo,
    'OldMovie': OldMovie
}

if __name__ == '__main__':
    # content = VideoContent("Test", 100, date(1900, 1, 2))
    # print(dir(content))
    # print(content.__dict__)
    # content.calculateQualityNumber()

    m = Movie("Pulp Fiction", 100, date.today(), 3, 'Tarantino')
    print(m)

    # class_name = Movie
    # m_2 = class_name("Pulp Fiction", 100, date.today(), 3, 'Tarantino')
    # print(m_2)


    # movie = Movie("Pulp Fiction", 100, date.today(), 3, 'Tarantino')
    # # # print(movie.calculateQualityNumber())
    video = YouTubeVideo("Test", 100, date.today(), 1000, 200)
    # # print(dir(video))
    # # print(video.__class__.__name__)

    # # # print(video.__views)

    with open("video.json", "w") as file:
        json.dump(video.as_json(), file)
    # # print(video.calculateQualityNumber())
    print(YouTubeVideo.from_json({"title": "Test", "price": 100, "release_date": "27-09-2025", "type": "YouTubeVideo", "views": 1000, "likes": 200}))

    # list_one = [1, 2, 3]
    # list_two = list_one
    # list_two[1] = 5
    # print(list_one)
    # print(list_two)


