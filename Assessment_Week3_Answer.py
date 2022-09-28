import os
import pandas as pd

d1 = {'A':[1,0,0,1], 'B':[0,1,1,0], 'C':[0,1,1,0], 'D':[1,0,0,1]}

# the prints are for testing output

# Problem 1
def makeDataFrame(data):
	# YOUR SOLUTION STARTS HERE
	df = pd.DataFrame(data)
	return df
    # YOUR SOLUTION ENDS HERE

print(makeDataFrame(d1))

# Problem 2a
def load():
	#SOLUTION START( ~ 1 line of code)
	return pd.read_csv(f"{os.getcwd()}\\data\\openrice.csv")
	#SOLUTION END

df = load() # use df for the remaining problems

# Problem 2b
def makeCategory():
	#SOLUTION START( ~ 1-2 lines of code)
    df["price_category"] = df["price_range"]
    df.price_category.replace(["Below $50","$51-100","$101-200","$201-400"], ["Cheap","Not Cheap","Expensive","Very Expensive"], inplace = True)
    return df["price_category"]
	#SOLUTION END

print(makeCategory())

# Problem 2c
def totalDislike():
	#SOLUTION START( ~ 1-2 line of code)
    dfg = df.groupby(df.price_range).sum()
    return dfg["dislikes"]
	#SOLUTION END

print(totalDislike())


# Problem 2d
def totalBookmarks():
	#SOLUTION START( ~ 1-2 line of code)
    dfg = df.groupby(df.food_type).sum()
    return dfg.bookmarks["Hong Kong Style"]
	#SOLUTION END

print(totalBookmarks())


# Problem 2e
def extractReview():
	#SOLUTION START( ~ 1-2 line of code)
    l = list(df["number_of_reviews"])
    nl = []
    for i in range(len(l)) :
        nl.append(l[i].replace("(","").replace(" Reviews)",""))
    return pd.Series(nl,name="number_of_reviews")
	#SOLUTION END

print(extractReview())
