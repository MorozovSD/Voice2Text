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


class TestGetIds(TestCase):
    def test_get_ids(self):
        print('***get_ids_test***')
        genreFilter = StubSearchFilter()
        results = get_ids(genreFilter)

        #print('----Correct return any----')
        self.assertTrue(results is not None)

    def test_get_ids_imdb(self):
        print('***test_get_ids_imdb***')
        genreFilter = StubSearchFilter()
        results, dont_care, dont_care2 = get_ids(genreFilter)

        #print('----Correct return imbd----')
        self.assertTrue(results is not None)

    def test_get_ids_rate(self):
        print('***test_get_ids_rate***')
        genreFilter = StubSearchFilter(rate=7)
        dont_care, results, dont_care2 = get_ids(genreFilter)

        #print('----Correct return rate----')
        self.assertTrue(results == 7)

    def test_get_ids_result(self):
        print('***test_get_ids_result***')
        genreFilter = StubSearchFilter()
        results = get_ids(genreFilter)

        #print('----Correct return sparcl result----')
        self.assertTrue(results is not None)

    def test_genre(self):
        print('***test_genre***')
        genreFilter = StubSearchFilter(genre='Comedy')
        _return, rate, results = get_ids(genreFilter)

        #print('----Correct imdb_id check----')
        #print('Films found {}'.format(len(_return)))
        self.assertTrue(len(_return) != 0)
        self.assertTrue(len(results["results"]["bindings"]) == len(_return))
        for ret in _return:
            self.assertTrue(len(ret) > 0)
        #print('----Correct genre check----')
        for result in results["results"]["bindings"]:
            self.assertTrue('genrelabel' in result)
            #print(result['label']['value'] + ' - ' + result['genrelabel']['value'])
            self.assertRegex(result['genrelabel']['value'].lower(), 'comedy', )

        #print('----Correct rate check----')
        #print('Rate filter is {}'.format(rate))
        self.assertTrue(rate is None)

    def test_year(self):
        print('***test_year***')
        yearFilter = StubSearchFilter(year='1990')
        _return, rate, results = get_ids(yearFilter)
        self.assertTrue(len(_return) != 0)
        self.assertTrue(len(results["results"]["bindings"]) == len(_return))
        for ret in _return:
            self.assertTrue(len(ret) > 0)
        self.assertTrue('releaseDate' in results["results"]["bindings"][0])

        #print('----Correct year check----')
        #for result in results["results"]["bindings"]:
            #print(result['label']['value'] + ' - ' +result['releaseDate']['value'])

        #print('----Correct imdb_id check----')
        #print('Films found {}'.format(len(_return)))

        #print('----Correct rate check----')
        #print('Rate filter is {}'.format(rate))
        self.assertTrue(rate is None)

    def test_coutry(self):
        print('***test_country***')
        yearFilter = StubSearchFilter(country='United States')
        _return, rate, results = get_ids(yearFilter)

        self.assertTrue(len(results["results"]["bindings"]) == len(_return))
        for ret in _return:
            self.assertTrue(len(ret) > 0)
        #print('----Correct country check----')
        for result in results["results"]["bindings"]:
            self.assertTrue('country' in result)
            #print(result['label']['value'] + ' - ' + result['country']['value'])
            self.assertRegex(result['country']['value'].lower(), 'united.states', )

        #print('----Correct imdb_id check----')
        #print('Films found {}'.format(len(_return)))
        self.assertTrue(len(_return) != '')

        #print('----Correct rate check----')
        #print('Rate filter is {}'.format(rate))
        self.assertTrue(rate is None)

    def test_name(self):
        print('***test_name***')
        testFilter = StubSearchFilter(name='love you')
        _return, rate, results = get_ids(testFilter)

        self.assertTrue(len(results["results"]["bindings"]) == len(_return))
        for ret in _return:
            self.assertTrue(len(ret) > 0)
        #print('----Correct name check----')
        for result in results["results"]["bindings"]:
            #print(result['label']['value'])
            self.assertTrue('label' in result)
            self.assertRegex(result['label']['value'].lower(), 'love you', )

        #print('----Correct imdb_id check----')
        #print('Films found {}'.format(len(_return)))
        self.assertTrue(len(_return) != 0)

        #print('----Correct rate check----')
        #print('Rate filter is {}'.format(rate))
        self.assertTrue(rate is None)

    def test_producer(self):
        print('***test_producer***')
        testFilter = StubSearchFilter(producer='Tarantino')
        _return, rate, results = get_ids(testFilter)

        self.assertTrue(len(results["results"]["bindings"]) == len(_return))
        for ret in _return:
            self.assertTrue(len(ret) > 0)
        #print('----Correct producer check----')
        for result in results["results"]["bindings"]:
            self.assertTrue('producer' in result)
            #print(result['label']['value'] + ' - ' + result['producer']['value'])
            self.assertRegex(result['producer']['value'].lower(), 'tarantino', )

        #print('----Correct imdb_id check----')
        #print('Films found {}'.format(len(_return)))
        self.assertTrue(len(_return) != 0)

        #print('----Correct rate check----')
        #print('Rate filter is {}'.format(rate))
        self.assertTrue(rate is None)


