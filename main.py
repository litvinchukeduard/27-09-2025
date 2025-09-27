from dataclasses import dataclass
from datetime import date
'''

VideoContent

Movie, Series Episode, YouTube video

1-5, episode number 1-5, views likes

Quality number: 
stars/5 * 100
stars/5 * 100
likes/views * 100
'''


@dataclass
class VideoContent:
    title: str
    release_date: date

    def calculateQualityNumber(self):
        raise NotImplementedError("Base class VideoContent does not have a way to calculate quality")


@dataclass
class Movie(VideoContent):
    stars: int
    director: str

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
    views: int
    likes: int

    @property
    def views(self):
        return self.views
    
    @views.setter
    def views(self, new_value):
        if new_value < 0:
            raise ValueError("Can not have value for views less than 0")
        
    @property
    def likes(self):
        return self.views
    
    @likes.setter
    def likes(self, new_value):
        if new_value < 0:
            raise ValueError("Can not have value for likes less than 0")

    def calculateQualityNumber(self):
        return (self.likes / self.views) * 100

if __name__ == '__main__':
    content = VideoContent("Test", date.today())
    # content.calculateQualityNumber()


    # movie = Movie("Pulp Fiction", date.today(), 3, 'Tarantino')
    # print(movie.calculateQualityNumber())
    video = YouTubeVideo("Test", date.today(), 1, -2)