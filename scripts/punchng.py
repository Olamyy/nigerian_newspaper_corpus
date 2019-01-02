from bs4 import BeautifulSoup
import requests
import datetime
import json

uri = "https://punchng.com/{0}"

cat = {"News": "topics/news", "Sport": "topics/sports", "Metro Plus": "topics/metro-plus", "Politics":
    "topics/politics", "Business": "topics/business", "Entertainment": "topics/entertainment", "Editorial":
           "topics/editorial", "Opinion": "columnist/opinion", "Columnist": "topics/columnist"}

for cat_name, url in cat.items():

    filename = "corpus/punchng/{}.json".format(cat_name.lower())

    print("Saving to {0}".format(filename))

    hold_out = uri.format(url)

    request = requests.get(hold_out)

    soup = BeautifulSoup(request.content, "html.parser")

    paginate = soup.find("div", class_='paginations')

    available_pages = [paginate.text]

    available_pages = available_pages[0].split('\n')
    available_pages = [i.replace(',', '') for i in available_pages if i.isdigit() or ',' in i]
    available_pages = [int(i) for i in available_pages]
    max_page = max(available_pages)
    result_l = []

    print("Starting work on the {0} category".format(cat_name))
    print()

    for i in range(1, int(max_page) + 1):
        print("Working on page {0} of {1}".format(i, cat_name))
        new_holdout = hold_out + "/page/{}".format(i)
        print("Building URL .....")
        print("URL built : {0}".format(new_holdout))
        print("{0} has {1} pages of articles".format(cat_name, int(max_page) + 1))
        request = requests.get(new_holdout)
        soup = BeautifulSoup(request.content, "html.parser")

        paginate = soup.findAll("div", class_='items col-sm-12')

        for div in paginate:
            links = div.findAll('a')
            for a in links:
                articles_on_page = [a['href']]
                for article in articles_on_page:
                    print("Handling Articles on {0}".format(a['href']))
                    print()
                    request = requests.get(article)
                    soup = BeautifulSoup(request.content, "html.parser")

                    try:
                        
                        authors = soup.find("p", style="text-align: justify;")
                        visits = soup.find("div", class_="tptn_counter")

                        result_map = {"titles": soup.find("h1", class_='post_title').text,
                                      "tags": soup.find('meta', attrs={'name':'news_keywords'}).get("content"),
                                      'published_date': soup.find("time", class_="entry-date published updated").text,
                                      'author': authors.text if authors else None,
                                      'visits': visits.text if visits else None,
                                      'text': soup.find("div", class_='entry-content').text,
                                      'category': cat_name,
                                      'crawled_on': repr(datetime.datetime.now())
                                      }
                        result_l.append(result_map)
                    except (AttributeError, ValueError) as error:
                        pass

            with open(filename, 'w') as fp:
                json.dump(result_l, fp)
            print('Done')
