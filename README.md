# Web Scraping And Data Analysis Amazon's Data Science Library
On this project I scraped the Amazon Data Science Library given by searching 'Data Science' on the search bar, the website scraped was amazon.com.mx which is amazon version for Mexico, nevertheless most of books scraped are in english, don't forget that all the prices will be in mexican pesos. Also I couldn't scrape all the prices at all. 
Anyway this is an interesting project to take the better decision on what book to read, hopefully another data related person will take a look to my project and select the best book for him or her.

You can see the results below or go directly to the [table of contents](#Table-Of-Contents)

# Results
I will put some screenshots of the visualization in tableau, I think in this case it's better to explore the entire [visualization](https://public.tableau.com/views/DataScienceLibraryViz/Story1?:language=es&:display_count=y&publish=yes&:origin=viz_share_link)
If the results seduce you, go to the complete viz on that link.

## The best books
![Sin título](https://user-images.githubusercontent.com/58957744/116408795-d60f7f80-a7f8-11eb-8aa8-90e803d59031.png)

## Good books not very popular (less than 50 reviews)

![2](https://user-images.githubusercontent.com/58957744/116408790-d4de5280-a7f8-11eb-99b4-9147644336e5.png)

## The worst books (by stars and reviews)

![worst](https://user-images.githubusercontent.com/58957744/116409149-2e468180-a7f9-11eb-9854-a44f9d968c75.png)

## Stars distribution

![6](https://user-images.githubusercontent.com/58957744/116408793-d60f7f80-a7f8-11eb-98e7-d91e30e8e33d.png)

This project was so interesting and I love it that's why is part of my portfolio, I did entirely from the scraper with scrapy to the visualizations with tableau, hope you have found an interesting book.

#Table Of Contents
* [Results](#Results)
* [Scraping](#Scraping)
* [Cleaning](#Cleaning)
* [Visualization](#Visualization)

# Scraping
The scraping was done entirely with scrapy framework for python 3.7, the spider which is the document that scrapes the information can be found **Web-Scraping-and-Data-Analysis-with-Tableau/scraper/scraper/spiders/books.py** The spider is books.py. There you will see the way I scraped the library.

# Cleaning
The data was cleaned on a jupyter notebook that can be found [here](link) 
