# Web Scraping : Mission to Mars

## Step 1 - Scraping

### NASA Mars News
- Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text

### JPL Mars Space Images - Featured Image
- Visit the URL for the JPL Featured Space Image
- Use Splinter to navigate the site and find the image URL for the current Featured Mars Image and assign the URL string to a variable called featured_image_url
- Make sure to find the image URL to the full size .jpg image
- Make sure to save a complete URL string for this image

### Mars Facts
- Visit the Mars Facts webpage and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
- Use Pandas to convert the data to a HTML table string

![image](https://user-images.githubusercontent.com/69765842/103469145-0786ab80-4d2f-11eb-948c-d85a050009c5.png)

![image](https://user-images.githubusercontent.com/69765842/103469167-43ba0c00-4d2f-11eb-9418-ffa64f87b76b.png)

![image](https://user-images.githubusercontent.com/69765842/103469174-5e8c8080-4d2f-11eb-9bb7-131a5c8f80cc.png)

![image](https://user-images.githubusercontent.com/69765842/103469182-7b28b880-4d2f-11eb-85e8-84f3f219e646.png)

### Mars Hemispheres
- Visit the USGS Astrogeology site to obtain high resolution images for each of Mar's hemispheres
- Save both the image URL string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name.
- Use a Python dictionary to store the data using the keys img_url and title
- Append the dictionary with the image URL string and the hemisphere title to a list
- This list will contain one dictionary for each hemisphere

## Step 2 - MongoDB and Flask Application
- Convert Jupyter Notebook into a Python Script called scrape_mars.py with a function called scrape that will execute all of the scraping 
code from above and return one Python Dictionary containing all of the scraped data
- Create a route called /scrape that will import the scrape_mars.py script and call the scrape function
  - Store the return value in Mongo as a Python Dictionary
- Create a root route / that will query the Mongo database and pass the Mars Data into an HTML template to display the data
- Create a template HTML file called index.html that will take the Mars Data Dictionary and display all of the data in the appropriate HTML elements

![image](https://user-images.githubusercontent.com/69765842/103469231-19b51980-4d30-11eb-8d77-7576af36ecb0.png)


