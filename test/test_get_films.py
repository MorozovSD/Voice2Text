from unittest import TestCase

from src.imdb_requests import get_films
from src.sparql_request import get_ids

class StubSearchFilter:
    def __init__(self,
                 year=None,
                 genre=None,
                 country=None,
                 rate=None,
                 name=None,
                 producer=None):
        self.year = year
        self.genre = genre
        self.country = country
        self.rate = rate
        self.name = name
        self.producer = producer

class TestGet_films(TestCase):
    def test_get_films(self):
        genreFilter = StubSearchFilter(genre='Comedy', rate=7)
        _return, rate, results = get_ids(genreFilter)
        films = get_films(_return, limit=2, rating=genreFilter.rate)
        self.assertLessEqual(len(films), 2, 'Найдено не больше чем, запрошено')
        for film in films:
            print(film)
            self.assertGreaterEqual(float(film['rating']), float(genreFilter.rate), 'Рейтинг фильмов, удовлетворяет фильтру')
