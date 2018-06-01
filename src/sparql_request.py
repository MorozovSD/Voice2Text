from SPARQLWrapper import SPARQLWrapper, JSON


def get_ids(search_filter):
    print('START sparql_request')
    prefix = """prefix dbr: <http://dbpedia.org/resource/>
prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
prefix dbpedia-owl: <http://dbpedia.org/ontology/>
prefix movie: <http://data.linkedmdb.org/resource/movie/>
"""
    core_select = """select distinct * where  {
    { ?film a movie:film       } union 
    { ?film a dbpedia-owl:Film }

    ?film ?prop ?object.
    FILTER (CONTAINS(STR(?prop), "imdbId"))

    ?film rdfs:label ?label.
    FILTER (langMatches(lang(?label), "en"))
"""

    sparql_genre = ''
    try:
        if search_filter.genre is not None:
            sparql_genre = """
        ?film <http://dbpedia.org/ontology/genre> ?genre.
        ?genre rdfs:label ?genrelabel.
        FILTER (langMatches(lang(?genrelabel), "en"))
        FILTER regex(str(?genrelabel), "({})", "i")
    """.format(search_filter.genre.replace(' ', '.'))

        sparql_year = ''
        if search_filter.year is not None:
            sparql_year = """?film <http://dbpedia.org/ontology/releaseDate> ?releaseDate.
        FILTER (year(xsd:datetime(?releaseDate)) = {})""".format(int(search_filter.year))

        sparql_country = ''
        if search_filter.country is not None:
            sparql_country = """
        ?film dbpedia-owl:country ?country
        FILTER regex(str(?country), "({})", "i")
        """.format(search_filter.country.replace(' ', '.'))

        sparql_producer = ''
        if search_filter.producer is not None:
            sparql_producer = """?film dbpedia-owl:producer ?producer
        FILTER regex(str(?producer), "({})", "i")""".format(search_filter.producer.replace(' ', '.'))

        sparql_name = ''
        if search_filter.name is not None:
            sparql_name = 'FILTER regex(str(?label), "({})", "i")\n'.format(search_filter.name.replace(' ', '.'))

        request_end = '}'
        query = prefix + \
                core_select + \
                sparql_genre + sparql_year + sparql_country + sparql_producer + sparql_name \
                + request_end
        # print(query)
        sparql = SPARQLWrapper("http://dbpedia.org/sparql")
        sparql.setQuery(query)

        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()
        _return = []
        for result in results["results"]["bindings"]:
            _return.append(result['object']['value'])
        return _return, search_filter.rate, results
    except Exception:
        return None, None, None

