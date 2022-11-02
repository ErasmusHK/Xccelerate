# Week4 Test
# This is a simple real estate price prediction problem
# Source URL: https://www.kaggle.com/quantbruce/real-estate-price-prediction
# Data Set Characteristic
# Target: Column 11 is a quantitative measure of house price of unit area
# Attribute Information:
# 1   No
# 2   X1 transaction date
# 3   X2 house age
# 4   X3 distance to the nearest MRT station
# 5   X4 number of convenience stores
# 6   X5 latitude
# 7   X6 longitude

# feel free to plot any graph for data visualization but it will not be graded



# import the library
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
import math
import pandas as pd


#Question1
def load():
	'''
	load the dataset
	return df
	'''
	#SOLUTION START( ~ 1 line of code)
	df = pd.read_csv(".\\data\\realestate.csv")

	#SOLUTION END
	return df

df = load()
print(df.head())


# Since there is no need of 'No' column and 'transcation date',
# so we will drop them
df.drop(['No'],axis='columns', inplace=True)
df.drop(['X1 transaction date'], axis='columns' ,inplace=True)


#Question2
def getShape():
	'''
	return the shape of dataframe
	'''
	#SOLUTION START( ~ 1 line of code)
	df.drop(columns=["No","X1 transaction date"], inplace=True)
	return df.shape
	#SOLUTION END

print(getShape())

#Question3
def getInfo():
	'''
	return the information of information about a DataFrame
	including the index dtype and columns, non-null values and memory usage.
	'''
	#SOLUTION START( ~ 1 line of code)
	return df.info()

	#SOLUTION END

print(getInfo())

# Question4
def checkNull():
	'''
	this function check if any null value
	expected output:
	No                                        0
	X1 transaction date                       0
	X2 house age                              0
	X3 distance to the nearest MRT station    0
	X4 number of convenience stores           0
	X5 latitude                               0
	X6 longitude                              0
	Y house price of unit area                0
	dtype: int64
	'''

	#SOLUTION START( ~ 1 line of code)
	return df.isnull().sum()

	#SOLUTION END


print(checkNull())

#Question5
def getStatistic():
	'''
	return the statistic of Dataframe such as count, mean, std, min, max, etc
	'''

	#SOLUTION START( ~ 1 line of code)
	return df.describe()
	#SOLUTION END

print(getStatistic())


#Now, we will extract the target variable which is 'Y house price of unit area' from the dataframe for training

df_y = df[['Y house price of unit area']]
df_X = df.drop(['Y house price of unit area'],axis='columns')

print(df_y.head())
print(df_X.head())


#Question 6
# Split the data into 80%training/20%testing sets
# IMPORTANT:for grading purpose,  please set the same seed random_state = 42

def split():
	'''
	IMPORTANT: this function will return four values X_train, X_test, y_train, y_test
	'''
	#SOLUTION START( ~ 1-2 line of code)
	df_y = df["Y house price of unit area"]
	df_x = df.drop("Y house price of unit area", axis = 1)
	return train_test_split(df_x, df_y, test_size=0.2, random_state=42)
	#SOLUTION END

X_train, X_test, y_train, y_test = split()


#Question 7
def makeModel():
	'''
	this function will create linear regression object,train the model using the training sets,
	make predictions using the testing set
	this function returns coefficients, intercept, mse, rmse, variance
	'''

	# Create linear regression object
	#SOLUTION START(~ 1 line of code)
	lr = linear_model.LinearRegression()
	#SOLUTION END

	# Train the model using the training sets
	#SOLUTION START(~ 1 line of code)
	lr.fit(X_train, y_train)

	#SOLUTION END

	# Make predictions using the testing set
	#SOLUTION START(~ 1 line of code)
	y_pred = lr.predict(X_test)
	#SOLUTION END

	#fill in the blanks, how to get the value of coefficients, intercept, mse, rmse, r2score
	#SOLUTION START
	#The coefficients i.e. the slope
	coefficients = lr.coef_#YOUR ANSWER
	intercept = lr.intercept_#YOUR ANSWER
	mse = mean_squared_error(y_test, y_pred)#YOUR ANSWER
	rmse = mean_squared_error(y_test, y_pred, squared=False)#YOUR ANSWER
	r2score = r2_score(y_test, y_pred)#YOUR ANSWER
	#SOLUTION END


	return (coefficients, intercept, mse, rmse, r2score)

print(makeModel())
