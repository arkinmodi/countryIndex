# Updated on August 27, 2018

import json

def jsonDecoder():
    # Takes the JSON files and parses them into dictionaries
    with open('data/continents.json') as data_file:    
        continents = json.load(data_file)

    with open('data/countries.json') as data_file:    
        countries = json.load(data_file)

    with open('data/languages.json') as data_file:    
        languages = json.load(data_file)

    return continents, countries, languages

def continentIndex(continent):
    continentIndex = jsonDecoder()[0]
    contCode = continentIndex[continent.capitalize()]   # Continent Code
    countryIndex = jsonDecoder()[1]
    validCountries = []

    # Checks every country and add the ones with the matching country code
    for key, value in countryIndex.items():
        if value["continent"] == contCode:
            validCountries.append(value["name"])
    
    return validCountries

def countryIndex(country):
    continentIndex = jsonDecoder()[0]
    countryIndex = jsonDecoder()[1]
    languageIndex = jsonDecoder()[2]
    langList = []

    # Finds the information of the specified country
    for key, value in countryIndex.items():
        if value["name"] == country.title():
           countryInfo = value
    
    for key, value in countryInfo.items():

        # Replaces the continent entry with its full name (i.e. NA will be changed to North America)
        if key == "continent":
            for continentKey, continentValue in continentIndex.items():
                if continentValue == value:
                    del(countryInfo["continent"])
                    countryInfo["continent"] = continentKey
                
        # Replaces the language entry with its full name and native name (i.e. hi will be changed to Hindi, हिन्दी)
        elif key == "languages":
            for languageKey, languageValue in languageIndex.items():
                if value[0] == languageKey or value[1] == languageKey:
                    langList.append(languageValue)
                    del(countryInfo["languages"])
                    countryInfo["languages"] = langList

    return countryInfo


def main():
    mode = input("Which lookup mode? Country or Continent: ")

    # Prints out all the countries in the continent
    if mode.lower() == "continent":
        continent = input("Which continent?: ").lower()
        result = continentIndex(continent)

        print("Countries in " + continent.capitalize() + ":")
        for country in result:
            print(country)

    # Prints out the counties information
    elif mode.lower() == "country":
        country = input("Which country?: ").lower()
        result = countryIndex(country)
        
        for key, value in result.items():
            print(key + ": " + str(value))

    else:
        print("Invalid")

main()