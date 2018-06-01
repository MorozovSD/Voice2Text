import random
import requests
from bs4 import BeautifulSoup as bs

ids = ['0120669', '0094441', '0001878', '0228306', '0132988', '0103404', '0055672']
url = 'https://www.imdb.com/title/tt'

def get_text(block):
    return block.text.strip() if block else None

def get_films(ids, limit=5, rating=None):
    print('START imdb_request')
    films = []
    if not ids:
        return films
    if len(ids) > limit:
        random.shuffle(ids)

    for id in ids:
        res = requests.get(url+id)
        if res.status_code == 200:
            soup = bs(res.text, 'html.parser')

            rating_value = get_text(soup.find(itemprop='ratingValue'))
            if rating and not (rating_value and float(rating_value) >= rating):
                continue

            title = get_text(soup.find(itemprop='name'))

            description = None
            description_div = soup.find("div", {"class": "summary_text"})
            try:
                if not description_div.a:
                    description = get_text(description_div)
                elif get_text(description_div.a) != 'Add a Plot':
                    description_request = requests.get(url+id+'/plotsummary')
                    if description_request.status_code == 200:
                        description_soup = bs(description_request.text, 'html.parser')
                        description = get_text(description_soup.find(id='plot-summaries-content').find('p'))
            except:
                print('uuups with description')

            poster = soup.find("div", {"class": "poster"})
            poster = poster.img.get('src') if poster and poster.img else None

            films.append({
                'id': id,
                'title': title,
                'description': description,
                'poster': poster,
                'rating': rating_value,
                'url': url+id
            })

            limit -= 1
            if limit == 0:
                break

    return films

if __name__ == "__main__":
    films = get_films(ids, limit=5, rating=4)
    for film in films:
        print(film)