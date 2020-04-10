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

# Conclusion
Overall the model was able to explain 83% of the used car price on CarGurus listings.  However, since the errors are
heteroskadestic, the beta p-values are no longer valid.  For this reason, interpreting the effects and signifigance of
the model will not lead to accurate conclusions.  The model however, can still be used to make predictions. The average
absolute error of predicted listing price on the test data set was $2850.  While this may seem high, it is important
to remember data such as trim package, condition, horsepower and vehicle accident history were not able to be collected
of CarGurus.

Despite not being very interpretable, the model is able to predict used car listing prices with impressive accuracy despite
lacking detailed information about the vehicle.  Further investigation and resolution of the heteroscedasticity would make
the model and effects of the individual predictors more interpretable.  One possible remedy is to implement weighted least
squares.
