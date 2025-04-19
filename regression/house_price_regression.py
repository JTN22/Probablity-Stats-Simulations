# Task: Build and evaluate a predictive model.

# Scenario: Predict house prices using features: 'Square_Feet', 'Bedrooms', and 'Age'.

# Instructions:
# 1. Create new features: Price per Square Foot, Age Group (categorical: 'New', 'Old', 'Very Old').
# 2. Fit a multiple linear regression model and report the coefficients and R^2 score.
# 3. Predict the price of a house with: Square_Feet = 2000, Bedrooms = 3, Age = 10 years.
# Libraries: pandas, statsmodels

import statsmodels.api as sm

# Sample data
data = pd.DataFrame({
    'Square_Feet': [1500, 2000, 2500, 3000, 3500],
    'Bedrooms': [3, 4, 3, 5, 4],
    'Age': [5, 10, 15, 20, 25],
    'Price': [300000, 400000, 450000, 600000, 500000]
})

# Feature engineering
data['Price_per_SqFt'] = data['Price'] / data['Square_Feet']
data['Age_Group'] = pd.cut(data['Age'], bins=[0, 10, 20, 30], labels=['New', 'Old', 'Very Old'])

# Regression model
X = data[['Square_Feet', 'Bedrooms', 'Age']]
X = sm.add_constant(X)
y = data['Price']

model = sm.OLS(y, X).fit()
print(model.summary())

# Predict price
prediction = model.predict([1, 2000, 3, 10])
print(f"Predicted Price: {prediction[0]}")
