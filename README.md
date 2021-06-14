# Final_Project￼

The Bad News Bears present…
“A Wine recommendation Single Page Application for the Consumer” 

Authored by: Collins Tweneboah, John Gore, & Ricky Kong

We are building a Single Page Application to recommend the optimal Wine Varietal to the consumer. Consumer inputs wine preferences  based on questionnaire that covers the base characteristics of wine tasting. Information compiled for the model will consist of 2 separate Datasets. The concept is focused around using objective data with a subjective preference to get a result. The consumer not only will leave with a result and recommendations, but also, a better understanding of wine tasting (under the hood). 



Varietal	Style	Body	Alchohol	Acidity	Dryness	Tannins	Aroma/Flavor Chatracteristics
							
Pinot Noir	Red	light,medium	high	medium,high	medium, dry	low, medium	Strawberry, berries, cherry
Merlot	Red	medium,full	high	medium	medium, dry	medium	Blackberry, plum, currant, chocolate, vanilla
Zinfandel	Red	full	very high	low,medium	medium, dry	low, medium	Berries, jammy, cherry, earthy
Cabernet Sauvignon	Red	medium,,full	medium, high	medium,high	medium,dry, verydry	medium, high	Blueberries, black currant, cassis, raspberries, oaky
Syrah(Shiraz)	Red	full	medium, high	medium	medium	medium, high	peppery, spice, blackberry, cinnamon
Petite Sirah	Red	full	medium, high	medium	medium, dry	medium	Blackberry, pepper, jammy
Sangiovese	Red	light. Medium	medium, high	medium,high	dry, verydry	medium, high	Cherry, fruity, spice
Cabernet Franc	Red	full	high,veryhigh	medium,high	dry, verydry	low, medium	Raspberry, cassis, herbaceous
Barbera	Red	medium,,full	medium	medium,high	medium, dry	medium	Berries, red fruit
Tempranillo 	Red	medium	medium, high	low,medium	medium	me	cherry, strawberry, plum
Malbec	Red	medium,,full	medium, high	medium	medium	medium	Cherry, strawberry, plum
Sauvignon Blanc	White	Light,Medium	high	high	dry, verydry	low	Apple, pear, yeast
Chardonnay	White	Medium, full	medium, high	medium,high	dry, verydry	low, medium	Herbaceous, grassy, hay, citrus, grapefruity
Viognier	White	Medium	high	medium	medium	low	Pear, apple, oak, buttery, creamy
Pinot Gris	White	Light	low, medium	medium,high	verydry	low	Floral, peach, apricot, pear, fruity
Pinot Blanc	White	Medium	medium	low,medium	medium, dry	low	Crisp, pear, peach, apricot
Pinot Grigio	White	Light	low, medium	medium,high	verydry	low	Pear, apple, floral
Chenin Blanc	White	Medium	low, medium	high	medium, dry	low	Peaches, fruity
Gewurztraminer	White	Light	low	low,	medium, offsweet	low	Lychee nut, spices, rose petals
Riesling	White	light,medium	low	high	medium, offsweet	low	Apple, lemon, floral, apricot, fruity
Moscato	White	medium,full	low	low,medium	offsweet	low	peach, apricot, and orange citrus,
							
			(12-15%)				
			low=12-12.5%				
			medium=13.5-14.5%				
			high= 14.5-15%				
			veryhigh=15%-17%				


		Dataset 1: plays the role of the master key to calculate the input from the consumer. The model will calculate Wines to recommend by their Varietals, or style of grapes. The criteria of the various wine varietals will cover areas such style (red or white), body, alcohol, acidity, dryness, tannins, and aroma/flavor Characteristics from 11 Red Varietals and 10 White Varietals.  The Consumer will have a footnoted reference of the criteria explained in the simplest possible context.  The idea…educate the learner. This dataset was compiled manually and design to be as simple and fluid as possible to train and test our model.

So…. Why did we formulate in this manner???

Domestically, wines are classified by their varietals. In Europe, wines are classified by the region of harvest (where the grapes are grown). In an example such as France, specific varietals are only grown in specific areas of the country. Cabernet Sauvignon and Merlot are grown in Bordeaux where as Pinot Noir and Chardonnay hale from Burgundy. The governing of French wine come with very strict rules based on region/appellation(or subregion) growth. Therefore, by having a base understanding of the core wine varietals, you can take this new knowledge on vacation to find these styles of Wine overseas. 


		Dataset 2: a large composition of wine bottle recommendations from each of the varietals in calculation.  The results from the model will then pull a list of bottle recommendations based on the output of the consumer calculated varietal. The data was compiled via use of web scraping from a wine specific website which utilizes a wine rating system to calculate bottle recommendations. Media sources such as Wine Spectator and Wine Enthusiast have created systems that rates every bottle of wine that gets produced globally. 

So….. Why not calculate the consumer recommendations using this dataset primarily?

Criteria that goes into a rating for Wine Spectator rated wine does not offer information to learn from, in regards to tasting feedback. Areas such as rating score, cases production, soil/climate and price …do not provide the consumer with education applicable to the tasting process. Another reason is the vintage year.(Does anyone know what the year printed on a wine label means???? <that’s what I thought>) In the 
Industry, wines change every year…simply stated. In attempts to recommend to the consumer a wine, it would be quite different of a result. Harvest year to year does not produce identical grape structure annually. The winemaker evaluates the harvest and blends the grapes to create the these flavor structures (so…. No, they do not add cherries, berries, and leather to the wine when they make it). It is key in the process to keep the data level with the areas that effect the consumer.


The Stack Development Process

The data sets are computed by Flask and MongoDB on the backend. On the frontend, we set up an Single Page Application with HTML, CSS, & Javascript with the use of the React.js library and use of NODE.js modules. This, to run an User Interactive interface, where the user runs their the questionnaire and the data computes their optimal time wine and then outputs a set of 10  bottle recommendations off the second data set.







FIN

￼
