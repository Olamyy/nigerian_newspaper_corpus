# Nigerian NewsPaper Corpus
> A growing corpus of digital Nigerian news sites.

[![Build Status][travis-image]][travis-url]


This collection of newspapers in digital form is a rich source of information for NLP researchers and engineers with interest in exploring Nigeria. It's of great use to enthusiasts in humanities, social sciences and diachronic studies, including history, media, communications and lexicography.

This dataset contains (or is to contain) category based crawling articles from 30 news sites. The sites:

1. [The Punch](https://punchng.com/)
2. [Vanguard](https://www.vanguardngr.com/)
3. [PM News](http://www.pmnewsnigeria.com/)
4. [Daily Trust](https://www.dailytrust.com.ng/)
5. [The Guardian](http://guardian.ng/)
6. [Leadership](https://leadership.ng/)
8. [New Telegraph](https://newtelegraphonline.com/)
8. [Business Day](http://www.businessdayonline.com/NG/)
8. [The Sun](http://sunnewsonline.com/category/national/)
8. [Daily Times of Nigeria](https://dailytimes.ng/)
8. [Media Trust](https://www.dailytrust.com.ng/)
8. [The Nation](http://thenationonlineng.net/)
8. [This Day](https://punchng.com/)
8. [National Mirror](https://www.nationalmirroronline.net/)
8. [The Daily Independent](https://independent.ng/)
8. [The Daily Post](http://dailypost.ng/)
8. [Osun Defender](http://www.osundefender.com/)
8. [Peoples Daily](http://www.peoplesdailyng.com/)
8. [Nigerian Observer](http://nigerianobservernews.com/)
8. [National Network](https://www.nationalnetworkonline.com/en/s)
8. [Stears Business](https://www.stearsng.com/)
8. [Blueprint Newspaper](https://www.blueprint.ng/)
8. [The News Journal](http://newsjournal.com.ng/)
8. [Tell Magazine](https://tell.ng/)
8. [The Tide](http://www.thetidenewsonline.com/)
8. [Business Hallmark](http://hallmarknews.com/)
8. [Urhobo Vanguard](http://urhobotoday.com/)
8. [Complete Sport](https://www.completesportsnigeria.com/)
8. [Daylight Nigeria](http://daylight.ng/)


P.S : In the list above, only __The Punch__ has been crawled.


## Folder Structure
The repository contains two main folders. `corpus` and `scripts`.
The `scripts` folder contains the crawler python script named according to the site it was written for.
The `corpus` folder contains the crawled data.

Each folder in the corpus corresponds to a news site and each file in the folder corresponds to a category on the site.

The features available for each file is described below:

```
{
    "titles" : "Article Title",
    "published_date": "Date artcile was published",
    "visits": "The number of visits on the article page",
    "crawled_date": "The date the artcile was crawled",
    "text" : "Article Content",
    "author" : "Article Author"
}

```

## Tool set
While there's no specific set of tools for doing this, some of the tools I used while doing this include:
1. [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/doc)
2. [Requests](http://docs.python-requests.org/en/master/)

## Possible Usages
There are quite a lot of possible usage of the corpus made available here.
Some possible research topics that can be explored around this includes:

Natural Language Generation
1. Auto-generation of news reports
2. Visual Question Generation

Natural Language Understanding
1. [Topic Modelling](http://www.cs.nyu.edu/~petrov/lecture2.pdf)
4. [Text Summarization](http://www.cs.nyu.edu/~petrov/lecture12.pdf)
6. Questions Answering NLP Systems
5. [Word Alignments](http://www.cs.nyu.edu/~petrov/lecture9.pdf)
3. NLP Adversarial Attack Research
2. [Syntatic Parsing](http://www.cs.nyu.edu/~petrov/lecture7.pdf)

## Release History

* 0.1
    * ADDED: News category for punch
    * ADDED: Editorial category for punch

## Meta

Olamilekan Wahab – [@__olamilekan__](https://twitter.com/__olamilekan__) – olamyy53@gmail.com

Distributed under the MIT license. See ``LICENSE`` for more information.

## Contributing

1. Fork it (<https://github.com/Olamyy/nigerian_newspaper_corpus/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

<!-- Markdown link & img dfn's -->
[npm-image]: https://img.shields.io/npm/v/datadog-metrics.svg?style=flat-square
[npm-url]: https://npmjs.org/package/datadog-metrics
[npm-downloads]: https://img.shields.io/npm/dm/datadog-metrics.svg?style=flat-square
[travis-image]: https://img.shields.io/travis/dbader/node-datadog-metrics/master.svg?style=flat-square
[travis-url]: https://travis-ci.org/dbader/node-datadog-metrics
[wiki]: https://github.com/yourname/yourproject/wiki