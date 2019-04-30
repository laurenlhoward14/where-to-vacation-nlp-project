import pickle
import random
from project4data import cities, countries

with open('ranked_df.pickle','rb') as read_file:
    ranked_df = pickle.load(read_file)


def recommendation(inputs, original_df=ranked_df, iteration=1):
        ''' Function will return up to three cities to recommend
        Inputs:
        inputs = User ranking of each topic
        original_df = Dataframe of each city ranking
        Iteration = Default of 1 - starts a counter of how many times the function runs'''

        # Match the user rank and topic rank for each city
        topic = str(list(inputs.keys())[list(inputs.values()).index(iteration)])
        new_df = original_df.loc[original_df[topic] == inputs[topic]]

        # Check Number of cities returned
        if iteration == 6 and len(new_df) >0:
            if len(new_df) >= 3:
                city = random.sample(list(new_df.index), k=3)
            else:
                city = (list(new_df.index)[:3])
        elif iteration == 6 or len(new_df) == 0:
            if len(original_df) >= 3:
                city = random.sample(list(original_df.index), k=3)
            else:
                city = (list(original_df.index)[:3])
        else:
            iteration +=1
            return recommendation(inputs, original_df=new_df, iteration=iteration) #input new

        return city

indexes = []
correct_countries = []
def return_countries(city):
    """Function takes in a list of cities and returns the corresponding country"""
    indexes = []
    correct_countries = []
    # Locate indexes of city name in full city list
    for idx, c in enumerate(city):
        indexes.append(cities.index(city[idx]))

    # Locate each country in full list of countries for particular city
    for c in indexes:
        correct_countries.append(countries[c])

    return correct_countries
