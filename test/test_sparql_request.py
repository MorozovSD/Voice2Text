from unittest import TestCase

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


class Testget_ids(TestCase):
    def test_get_ids(self):
        print('\n\n\n***get_ids_test***')
        genreFilter = StubSearchFilter()
        results = get_ids(genreFilter)

        print('----Correct return any----')
        self.assertTrue(results is not None)

    def test_get_ids_imdb(self):
        print('\n\n\n***test_get_ids_imdb***')
        genreFilter = StubSearchFilter()
        results, dont_care, dont_care2 = get_ids(genreFilter)

        print('----Correct return imbd----')
        self.assertTrue(results is not None)

    def test_get_ids_rate(self):
        print('\n\n\n***test_get_ids_rate***')
        genreFilter = StubSearchFilter(rate=7)
        dont_care, results, dont_care2 = get_ids(genreFilter)

        print('----Correct return rate----')
        self.assertTrue(results == 7)

    def test_get_ids_result(self):
        print('\n\n\n***test_get_ids_result***')
        genreFilter = StubSearchFilter()
        results = get_ids(genreFilter)

        print('----Correct return sparcl result----')
        self.assertTrue(results is not None)

    def test_genre(self):
        print('\n\n\n***test_genre***')
        genreFilter = StubSearchFilter(genre='Comedy')
        _return, rate, results = get_ids(genreFilter)

        print('----Correct genre check----')
        for result in results["results"]["bindings"]:
            print(result['label']['value'] + ' - ' + result['genrelabel']['value'])
            self.assertRegex(result['genrelabel']['value'].lower(), 'comedy', )

        print('----Correct imdb_id check----')
        print('Films found {}'.format(len(_return)))
        self.assertTrue(len(_return) != 0)

        print('----Correct rate check----')
        print('Rate filter is {}'.format(rate))
        self.assertTrue(rate is None)

    def test_year(self):
        print('\n\n\n***test_year***')
        yearFilter = StubSearchFilter(year='1990')
        _return, rate, results = get_ids(yearFilter)

        print('----Correct year check----')
        for result in results["results"]["bindings"]:
            print(result['label']['value'] + ' - ' +result['releaseDate']['value'])

        print('----Correct imdb_id check----')
        print('Films found {}'.format(len(_return)))
        self.assertTrue(len(_return) != 0)

        print('----Correct rate check----')
        print('Rate filter is {}'.format(rate))
        self.assertTrue(rate is None)

    def test_coutry(self):
        print('\n\n\n***test_country***')
        yearFilter = StubSearchFilter(country='United States')
        _return, rate, results = get_ids(yearFilter)

        print('----Correct country check----')
        for result in results["results"]["bindings"]:
            print(result['label']['value'] + ' - ' + result['country']['value'])
            self.assertRegex(result['country']['value'].lower(), 'united.states', )

        print('----Correct imdb_id check----')
        print('Films found {}'.format(len(_return)))
        self.assertTrue(len(_return) != 0)

        print('----Correct rate check----')
        print('Rate filter is {}'.format(rate))
        self.assertTrue(rate is None)

    def test_name(self):
        print('\n\n\n***test_name***')
        testFilter = StubSearchFilter(name='love you')
        _return, rate, results = get_ids(testFilter)

        print('----Correct name check----')
        for result in results["results"]["bindings"]:
            print(result['label']['value'])
            self.assertRegex(result['label']['value'].lower(), 'love you', )

        print('----Correct imdb_id check----')
        print('Films found {}'.format(len(_return)))
        self.assertTrue(len(_return) != 0)

        print('----Correct rate check----')
        print('Rate filter is {}'.format(rate))
        self.assertTrue(rate is None)

    def test_producer(self):
        print('\n\n\n***test_producer***')
        testFilter = StubSearchFilter(producer='Tarantino')
        _return, rate, results = get_ids(testFilter)

        print('----Correct producer check----')
        for result in results["results"]["bindings"]:
            print(result['label']['value'] + ' - ' + result['producer']['value'])
            self.assertRegex(result['producer']['value'].lower(), 'tarantino', )

        print('----Correct imdb_id check----')
        print('Films found {}'.format(len(_return)))
        self.assertTrue(len(_return) != 0)

        print('----Correct rate check----')
        print('Rate filter is {}'.format(rate))
        self.assertTrue(rate is None)


