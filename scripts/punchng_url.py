from bs4 import BeautifulSoup
import requests
import logging

logging.basicConfig(
    format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

uri = "https://punchng.com/{0}"

cat = {"News": "topics/news", "Sport": "topics/sports", "Metro Plus": "topics/metro-plus", "Politics": "topics/politics", "Business": "topics/business", "Entertainment": "topics/entertainment",
       "Editorial": "topics/editorial", "Opinion": "columnist/opinion", "Columnist": "topics/columnist"}

for cat_name, url in cat.items():

    filename = "corpus/punchng_url.txt"

    logging.info("Saving to {0}".format(filename))

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

    logging.info("Starting work on the {0} category".format(cat_name))
    logging.info("{0} has {1} pages".format(cat_name, max_page + 1))

    for i in range(1088, int(max_page) + 1):
        logging.info("Working on page {0} of {1}".format(i, cat_name))
        new_holdout = hold_out + "/page/{}".format(i)
        logging.info("Building page {0}".format(new_holdout))
        current_page_article_count = int(max_page) + 1
        request = requests.get(new_holdout)
        soup = BeautifulSoup(request.content, "html.parser")

        paginate = soup.findAll("div", class_='items col-sm-12')

        for div in paginate:
            current_page_article_count -= 1
            links = div.findAll('a')
            for a in links:
                articles_on_page = [a['href']]
                with open(filename, 'a') as fp:
                    for article in articles_on_page:
                        fp.writelines(article + '\n')
            print('Done')
