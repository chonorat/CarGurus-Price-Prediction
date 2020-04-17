# CarGurus-Price-Prediction

# Summary
The goal off this project was to analyze used car listing from the website CarGurus in order to better understand 
how certain factors influence a used cars price. A secondary goal was to use the developed model in order to predict
what a used car should be priced at or determine if a used car's price can be considered a 'Good Deal' or a 'Bad Deal'.
The full statistical analysis can be viewed in CarGurus Used Vehicle Report.pdf

# Tools
I used Python to scrape CarGurus and store the data in a local MySql data base.  I used R to visualise the data and 
conduct a statistical analysis.

# The Data
The data attributes I was able to gather from Cargurus include, Price, Miles, Transmission Type (Automatic or Manual),
Model, Make, Year, and Vehicle Class (Sedan, Mini-Van, Truck, etc.). I also included a field for whether or not the
manufacturer was a luxury brand or not.  I opted to only include cars from current manufacturers that have a relatively
large volume of posting on CarGurus.  Therefore manufactueres such as Mercury and Tesla were ommitted from the data.
Furthermore, I decided to ommitt cars over $80,000 dollars and cars under $2000 dollars.  Cars above $80,000 are luxury
vehicles that may include many trim and powertrain options which help maintain the resale value regardless of some of
the factors incorporated in the model.  Cars under $2000 were ommitted because, in my experieince, essentially any car
that can be driven off the lot can be sold for $1000 regardless of year, make, model etc. Lastly cars manufactured 
before 2006 were ommited because few cars older than this were posted on CarGurus. Lets now begin with some plots to 
visualise the data.



# Model Interpretation
Years Old: A one unit increase in years old predicts a 25.6% increase in vehicle price.
Miles: Every additional mile is associated with a .00042% decrease in vehicle price.
Model Average: A 1% increase in the average model price predicts a 1% increase vehicle price.
Years Old x Miles: For every year older a vehicle is, the effect miles has on price decreases by .00001%
Year Old X Model Average: For every year older a vehicle is, the effect model average has on price
decreases by 3%.
Coupe: Coupes are predicted to be 7.9% less expensive than convertibles.
Hatch: Hatches are predicted to be 13.5% less expensive than convertibles.
Minivans: Minivans are predicted to be 3.2% less expensive than convertibles.
Pick-Ups: Pick Ups are predicted to be 6.8% more expensive than convertibles.
Sedans: Sedans are predicted to be 10.3% less expensive than convertibles.
SUV: SUVs are predicted to be 6.2% less expensive than converibles.
Van: Vans are predicted to be 6.4% less expensive than convertibles.
Wagon: Wagons are predicted to be 8% less expensive than convertibles.


# Conclusion
Overall the model was able to explain almost 83% of the used car price on CarGurus listings. Since
the constant variance assumption of the error was satisfied, the P-Values for the coefficients are
accurate and the model can be used for inferential purposes. The average absolute prediction error
for the test data is $2,830. While this may seem high, it is important to remember data such as trim
package, condition, horsepower and vehicle accident history were not available from CarGurus.

$8,986 is the model’s prediciton for the listing price of my own personal car on CarGurus. I own a
2013 Ford Fusion with 100,000 miles and an automatic transmission. The model’s prediction appears
consistent with the search results on CarGurus for vehicles with the same specifications. It is
important to note the model does not attempt to predict the true market value for each vehicle,
rather the estimated price it would be listed for on CarGurus.

The model is able to predict used car listing prices with impressive accuracy despite lacking detailed
information about the vehicle. I feel the model has exhausted any possible variation that could
reasonably explained by the collected attributes. Collecting data for other fields such as trim,
horsepower, and accident history would likely greatly improve the model.
