# Gabrielle Mehltretter, 16gplm, 20065730
# A program to go through given ufo sightings data and output asked information.
# The two states in the USA with the highest number of sightings.
# The two provinces in Canada with the highest number of sightings.
# The sightings count for every year in the dataset, listed by year.
# The number of sightings in each month for all years, listed by month.
# The number of sightings for each possible UFO shape.
# A list of the top five shapes, listed in decreasing order.

# Supplied
# Used by the readData function to parse an 8 digit date string into three
# integer date components.
def parseDate(dateString) :
    space = dateString.find(" ")
    if space == -1 :
        space = len(dateString)
    if space < 11 and space > 7 :
        date = dateString[0 : space]
        month, day, year = date.split("/")
        return int(year), int(month), int(day)
    else :
        return None, None, None

# Supplied
# Reads the given file, which consists of sighting data in comma-delimited text format,
# with one sighting per line.  A dictionary record is created for each sighting
# and a list of all these dictionaries is returned.  The form of the data is in:
# datetime,city,state,country,shape,duration (seconds),duration (hours/min),comments,date posted,latitude,longitude
# Dates are in the format: mm/dd/yyyy, but could also be m/d/yyyy.
def readData(filename) :
    data = []
    ufoFile = open(filename)
    for line in ufoFile :
        sighting = {}
        sighting["sightedYear"] = None      # Date sighting occurred
        sighting["sightedMonth"] = None
        sighting["sightedDay"] = None
        sighting["reportedYear"] = None     # Date sighting reported
        sighting["reportedMonth"] = None
        sighting["reportedDay"] = None
        sighting["country"] = None          # Location, mostly uses 2 letter abbreviations
        sighting["state"] = None
        sighting["city"] = None
        sighting["shape"] = None            # UFO shape
        sighting["duration"] = None         # Duration of sighting in seconds
        sighting["description"] = None      # Free-text description of sighting - not complete
        sighting["latitude"] = None         # Location of sighting
        sighting["longitude"] = None
        pieces = line.strip().split(',')
        if len(pieces) == 11 :
            sighting["sightedYear"], sighting["sightedMonth"], sighting["sightedDay"] = \
                                   parseDate(pieces[0].strip())
            sighting["city"] = pieces[1].strip()
            sighting["state"] = pieces[2].strip()
            sighting["country"] = pieces[3].strip()
            sighting["shape"] = pieces[4].strip()
            sighting["duration"] = pieces[5].strip()
            sighting["description"] = pieces[7].strip()
            sighting["reportedYear"], sighting["reportedMonth"], sighting["reportedDay"] = \
                                   parseDate(pieces[8].strip())
            try :
                sighting["latitude"] = float(pieces[9].strip())
                sighting["longitude"] = float(pieces[10].strip())
            except ValueError :
                sighting["latitude"] = None
                sighting["longitude"] = None
            data.append(sighting)
    ufoFile.close()
    return data

# Write your functions here
# This function goes through all the sightings and makes a dictionary of
# the number of sightings in each state. It then determines which two states have the highest
# number of sightings. It then prints the total number of sightings and the top two states.

def highestSightingsStates(data, countryIn):  # for USA
    sightingsDict = {} #(State : Sightings)

    for sighting in data:
        if sighting["country"] == countryIn:
            state = sighting["state"]
            if state in sightingsDict:
                sightingsDict[state] += 1
            else:
                sightingsDict[state] = 1

    totalSightings = sum(sightingsDict.values())
    print(str(totalSightings) + " sightings in " + countryIn)

    first = list(sightingsDict)[0]
    second = list(sightingsDict)[1]

    for sighting in sightingsDict:
        if sightingsDict[sighting] > sightingsDict[first]:
            second = first
            first = sighting
        elif sightingsDict[sighting] > sightingsDict[second]:
            second = sighting

    print("Highest state: " + first + " with " + str(sightingsDict[first]) + " sightings.")
    print("Second highest state: " + second + " with " + str(sightingsDict[second]) + " sightings.")

# This function goes through the data and depending on which key is wanted
# will make a list of all the types uder that key. For example if the key
# is month then the list will consist of the months January to December.

def uniqueValues(data, key):
    output = []
    for sighting in data:
        if sighting[key] not in output:
            output.append(sighting[key])

    return output

# This function counts the frequency for each of those types under the key.
# For example if the key is month it will return how many sightings there
# were for each month in the year.

def frequencyCount(data, key, allYears):
    frequencyDictionary = {}
    for year in allYears:
        frequencyDictionary[year] = 0
    for sighting in data:
        year = sighting[key]
        frequencyDictionary[year] += 1
    return frequencyDictionary

# This function puts the values in order. Printing the data in order. Again
# if the key were months it will print the data like 1 : number of sightings
# for each month.

def displayInOrder(dict):
    for keys, values in sorted(dict.items()):
        if not (keys == ""):
            print(str(keys) + " : " + str(values))

# This function finds the number of sightings with each shape ufo.

def highestFrequency(shapeFrequencies):
    max = list(shapeFrequencies)[0]
    for keys, value in shapeFrequencies.items():
        if value > shapeFrequencies[max]:
            max = keys
    return max

# This function searches the data for a certain date in history and pulls up sightings.

def search(data, year, month, day):
    output = []
    for sighting in data:
        if year == sighting["sightedYear"] and month == sighting["sightedMonth"] and day == sighting["sightedDay"]:
            output.append(d)
    return output

# Supplied
def main() :
    data = readData("ufo_sightings.csv")
    if len(data) == 0 :
        print("Ooooops. Exiting!")
        return
    print(len(data), "sightings read from file.")

    # Output from first call to highestSightingsStates, with ? for removed digits:
    # ????? sightings in USA
    # Highest state: ?? with ???? sightings.
    # Second highest state: ?? with ???? sightings.
    highestSightingsStates(data, "us")  # for USA
    highestSightingsStates(data, "ca")  # for Canada

    # Output of following three lines of code with some years skipped:
    # Frequencies in key order:
    # 1906 : 1
    # 1910 : 2
    # 1916 : 1
    # 1920 : 1
    # 1925 : 1
    # .... (other lines)
    # 2012 : 7357
    # 2013 : 7037
    # 2014 : 2260

    allYears = uniqueValues(data, "sightedYear")
    yearFrequencies = frequencyCount(data, "sightedYear", allYears)
    displayInOrder(yearFrequencies)

    # Output is month followed by the count for that month for all 12 months in a year.
    print("\nMonth sighting counts:")
    allMonths = uniqueValues(data, "sightedMonth")
    monthFrequencies = frequencyCount(data, "sightedMonth", allMonths)
    print(monthFrequencies)
    for month in range(1, 13):
        print(str(month) + ":" + str(monthFrequencies[month]))

    # Output of following three lines of code with some shapes skipped:
    # Frequencies in key order:
    # changed : 1
    # changing : 1962
    # chevron : 952
    # cigar : 2057
    # .... (other lines)
    # teardrop : 750
    # triangle : 7865
    # unknown : 5584
    allShapes = uniqueValues(data, "shape")
    shapeFrequencies = frequencyCount(data, "shape", allShapes)
    displayInOrder(shapeFrequencies)

    # Displays the top five shapes going by frequency count from highest to
    # lowest, giving the shape and the frequency count for that shape.
    print("\nTop five shapes:")
    for i in range(1, 6) :
        highest = highestFrequency(shapeFrequencies)
        print("No." + str(i) + " \"" + str(highest) + "\" with " + str(shapeFrequencies[highest]) + " sightings.")
        del shapeFrequencies[highest]

    # Displays the search results for a particular date.
    print("\nSupply a date for which you wish to list the available sightings:")
    year = input("Enter year (4 digits): ")
    month = input("Enter month (1 or 2 digits): ")
    day = input("Enter day (1 or 2 digits): ")
    searchResults = search(data, year, month, day)
    print(len(searchResults), "sightings made on this day:")
    for result in searchResults:
        for key in result:
            print(str(key) + " = " + str(result[key]))
        print()

main()
