from SPARQLWrapper import SPARQLWrapper, JSON


def sparql_request(search_filter):
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
    if search_filter.genre:
        sparql_genre = """
    ?film <http://dbpedia.org/ontology/genre> ?genre.
    ?genre rdfs:label ?genrelabel.
    FILTER (langMatches(lang(?genrelabel), "en"))
    FILTER regex(str(?genrelabel), "({})", "i")
""".format(search_filter.genre.replace(' ', '.'))

    sparql_year = ''
    if search_filter.year:
        sparql_year = """?film <http://dbpedia.org/ontology/releaseDate> ?releaseDate.
    FILTER (year(xsd:datetime(?releaseDate)) = {})""".format(int(search_filter.year))

    sparql_country = ''
    if search_filter.country:
        sparql_country = """
    ?film dbpedia-owl:country ?country
    FILTER regex(str(?country), "({})", "i")
    """.format(search_filter.country.replace(' ', '.'))

    sparql_producer = ''
    if search_filter.producer:
        sparql_producer = """?film dbpedia-owl:producer ?producer
    FILTER regex(str(?producer), "({})", "i")""".format(search_filter.producer.replace(' ', '.'))

    sparql_name = ''
    if search_filter.name:
        sparql_name = 'FILTER regex(str(?label), "({})", "i")\n'.format(search_filter.name.replace(' ', '.'))

    request_end = '}'
    qeuery = prefix + \
             core_select + \
             sparql_genre + sparql_year + sparql_country + sparql_producer + sparql_name \
             + request_end
    #print(qeuery)
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setQuery(qeuery)

    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    _return = []
    for result in results["results"]["bindings"]:
        _return.append(result['object']['value'])
    return _return, search_filter.rate, results
