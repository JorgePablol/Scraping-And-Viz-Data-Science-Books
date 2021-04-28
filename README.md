# [Web Scraping And Data Analysis Amazon's Data Science Library](#Table-Of-Contents)
On this project I scraped the Amazon Data Science Library given by searching 'Data Science' on the search bar, the website scraped was amazon.com.mx which is amazon version for Mexico, nevertheless most of books scraped are in english, don't forget that all the prices will be in mexican pesos. Also I couldn't scrape all the prices at all. 
Anyway this is an interesting project to take the better decision on what book to read, hopefully another data related person will take a look to my project and select the best book for him or her.

You can see the results below or go directly to the [table of contents](#Table-Of-Contents)

# [Results](#Table-Of-Contents)
I will put some screenshots of the visualization in tableau, I think in this case it's better to explore the entire [visualization](https://public.tableau.com/views/DataScienceLibraryViz/Story1?:language=es&:display_count=y&publish=yes&:origin=viz_share_link)
If the results seduce you, go to the complete viz on that link.

## [The Best Books](#Table-Of-Contents)

![best](https://user-images.githubusercontent.com/58957744/116431835-c189b200-a80d-11eb-8d52-e9a4e8d09998.png)

## [Good Books](#Table-Of-Contents) (less than 50 reviews)

![good](https://user-images.githubusercontent.com/58957744/116431839-c2224880-a80d-11eb-904c-50cf7cef916b.png)

## [Possible Surprises](#Table-Of-Contents) (not so popular neither the highest rated books)

![sur](https://user-images.githubusercontent.com/58957744/116431845-c2badf00-a80d-11eb-804e-050e8285031a.png)

## [The Worst Books](#Table-Of-Contents) (by stars and reviews)

![worst](https://user-images.githubusercontent.com/58957744/116431849-c3537580-a80d-11eb-9d7b-3bcc4fb6ac74.png)

## [Stars Distribution](#Table-Of-Contents)

![stardist](https://user-images.githubusercontent.com/58957744/116432025-ebdb6f80-a80d-11eb-94a2-b03260e1be19.png)

This project was so interesting and I love it that's why is part of my portfolio, I did entirely from the scraper with scrapy to the visualizations with tableau, hope you have found an interesting book.

# Table Of Contents
* [Results](#Results)
    * [The Best Books](#The-Best-Books)
    * [Good Books](#Good-Books)
    * [Possible Surprises](#Possible-Surprises)
    * [The Worst Books](#The-Worst-Books)
    * [Stars Distribution](#Stars-Distribution)
* [Scraping](#Scraping)
* [Cleaning](#Cleaning)
* [Visualization](#Visualization)

# [Scraping](#Table-Of-Contents)
The scraping was done entirely with scrapy framework for python 3.7, the spider which is the document that scrapes the information can be found **Web-Scraping-and-Data-Analysis-with-Tableau/scraper/scraper/spiders/books.py** The spider is books.py. There you will see the way I scraped the library.

# [Cleaning](#Table-Of-Contents)
The data was cleaned on a jupyter notebook that can be found [here](link) 
