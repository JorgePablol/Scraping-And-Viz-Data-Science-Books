# [Web Scraping And Data Analysis Amazon's Data Science Library](#Table-Of-Contents)
On this project I scraped the Amazon Data Science Library given by searching 'Data Science' on the search bar, the website scraped was amazon.com.mx which is amazon version for Mexico, nevertheless most of books scraped are in english, don't forget that all the prices will be in mexican pesos. Also I couldn't scrape all the prices at all. 
Anyway this is an interesting project to take the better decision on what book to read, hopefully another data related person will take a look to my project and select the best book for him or her.

You can see the results below or go directly to the [table of contents](#Table-Of-Contents)

# [Results](#Table-Of-Contents)
I will put some screenshots of the visualization in tableau, I think in this case it's better to explore the entire [visualization](https://public.tableau.com/views/DataScienceLibraryViz/Story1?:language=es&:display_count=y&publish=yes&:origin=viz_share_link)
If the results seduce you, go to the complete viz on that link.

## [The Best Books](#Table-Of-Contents)

![best](https://user-images.githubusercontent.com/58957744/116431835-c189b200-a80d-11eb-8d52-e9a4e8d09998.png)

## [Good Books](#Table-Of-Contents) 

![good](https://user-images.githubusercontent.com/58957744/116431839-c2224880-a80d-11eb-904c-50cf7cef916b.png)

## [Possible Surprises](#Table-Of-Contents)

![sur](https://user-images.githubusercontent.com/58957744/116431845-c2badf00-a80d-11eb-804e-050e8285031a.png)

## [The Worst Books](#Table-Of-Contents)

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
* [Tools And Libraries](#Tools-And-Libraries)
* [Scraping](#Scraping)
* [Cleaning](#Cleaning)
* [Visualization](#Visualization)

# [Tools And Libraries](#Table-Of-Contents)
* Python 3.7
* Scrapy 
* Tableau
* Pandas
* Matplotlib
* Numpy
* Jupyter Notebook


# [Scraping](#Table-Of-Contents)
Scrapy for Python 3.7 was the key framework to scrape all the data, you can find the spider [here](Web-Scraping-and-Data-Analysis-with-Tableau/scraper/scraper/spiders/books.py)

I will add some photos of the scraping but for deeper thoughts go to the file.

![scraping](https://user-images.githubusercontent.com/58957744/116435952-86897d80-a811-11eb-8236-521fd646cd00.png)

# [Cleaning](#Table-Of-Contents)
The data was cleaned on a jupyter notebook that can be found [here](link) 

As you can read on the next image the process is described and modularized the key library here was pandas.

![cleaning](https://user-images.githubusercontent.com/58957744/116435956-87221400-a811-11eb-94b0-e5a3af5e13e6.png)

# [Analysis](#Table-Of-Contents)
This kind of data is more descriptive in terms of showing the different books by querying the data more than applying statistical techniques to describe the data, so the analysis file is filled with queries. You can go to the entire file [here]()

![analysis](https://user-images.githubusercontent.com/58957744/116435954-87221400-a811-11eb-9ae8-33478fb8817a.png)

