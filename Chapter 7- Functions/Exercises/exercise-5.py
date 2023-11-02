'''Write a function called describe_city() that accepts the name of a city and 
its country. The function should print a simple sentence, such as Reykjavik is 
in Iceland. Give the parameter for the country a default value. Call your 
function for three different cities, at least one of which is not in the 
default country.'''

# def is used to define the describe_city function, with city and country as parameters
def describe_city(city = "Tokyo", country = "Japan"): 
    # prints a message about the city and country
    print(f"{city} is in {country}.")

# prints message with default city and country
describe_city()
# prints message with different city and default country
describe_city(city = "Kyoto")
# prints message with different city and country
describe_city("Paris", "France")