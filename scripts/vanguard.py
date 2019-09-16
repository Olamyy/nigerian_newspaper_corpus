from bs4 import BeautifulSoup
import requests
import datetime
import json

uri = "https://www.vanguardngr.com/{0}"

cat = {
      "News": "category/national-news", 
      "Sport": "category/sports", 
      "Metro Plus": "category/metro-plus", 
      "Politics": "category/politics", 
      "Business": "category/business", 
      "Finance": "category/finance", 
      "Tech": "category/technology", 
      "Motoring": "category/motoring", 
      "Entertainment": "category/entertainment", 
      "Editorial": "category/editorial", 
      "Opinion": "columnist/opinion", 
      "Columnist": "category/columnist", 
      "Relationship": "category/romance-an-relationships",
      "Viewpoint": "category/viewpoints"

      }

for cat_name, url in cat.items():

    filename = "corpus/vanguard/{}.json".format(cat_name.lower())

    print("Saving to {0}".format(filename))

    hold_out = uri.format(url)

    print(hold_out)

    request = requests.get(hold_out)

    soup = BeautifulSoup(request.content, "html.parser")

    paginate = soup.findAll("a", class_='page-numbers')[2]

    available_pages = int([paginate.text][0].replace(',', ''))

    print(available_pages)

    result_l = []

    print("Starting work on the {0} category".format(cat_name))
    print()

    for i in range(1, available_pages):
        print("Working on page {0} of {1}".format(i, cat_name))
        new_holdout = hold_out + "/page/{}".format(i)
        print("Building URL .....")
        print("URL built : {0}".format(new_holdout))
        print("{0} has {1} pages of articles".format(cat_name, available_pages))

        request = requests.get(new_holdout)
        soup = BeautifulSoup(request.content, "html.parser")


        articles = soup.findAll("article")

        for article in articles:
            links = article.findAll('a')
            for a in links:
                articles_on_page = [a['href']]
                print(articles)
                # for article in articles_on_page:
                #     print("Handling Articles on {0}".format(a['href']))
                #     print()
                #     request = requests.get(article)
                #     soup = BeautifulSoup(request.content, "html.parser")

    #                 try:
                        
    #                     authors = soup.find("p", style="text-align: justify;")
    #                     visits = soup.find("div", class_="tptn_counter")

    #                     result_map = {"titles": soup.find("h1", class_='post_title').text,
    #                                   "tags": soup.find('meta', attrs={'name':'news_keywords'}).get("content"),
    #                                   'published_date': soup.find("time", class_="entry-date published updated").text,
    #                                   'author': authors.text if authors else None,
    #                                    'visits': visits.text if visits else None,
    #                                   'text': soup.find("div", class_='entry-content').text,
    #                                   'category': cat_name,
    #                                   'crawled_on': repr(datetime.datetime.now())
    #                                   }
    #                     result_l.append(result_map)
    #                 except (AttributeError, ValueError) as error:
    #                     pass

    #         with open(filename, 'w') as fp:
    #             json.dump(result_l, fp)
    #         print('Done')
