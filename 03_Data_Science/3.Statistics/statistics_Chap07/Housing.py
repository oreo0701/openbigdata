import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.formula.api import ols, glm

housing = pd.read_csv('Housing.csv', sep=',', header=0)
housing.columns = housing.columns.str.replace(' ', '_')

housing['housing_driveway'] = np.where(housing['driveway'] == 'yes', 1., 0.)
housing['housing_recroom'] = np.where(housing['recroom'] == 'yes', 1., 0.)
housing['housing_fullbase'] = np.where(housing['fullbase'] == 'yes', 1., 0.)
housing['housing_gashw'] = np.where(housing['gashw'] == 'yes', 1., 0.)
housing['housing_airco'] = np.where(housing['airco'] =='yes', 1., 0.)
housing['housing_prefarea'] = np.where(housing['prefarea'] == 'yes', 1., 0.)

#print(housing.head())
my_formula = 'price ~ lotsize + bedrooms + bathrms + stories + garagepl + housing_driveway+ housing_recroom + housing_fullbase + housing_gashw + housing_airco + housing_prefarea'
lm = ols(my_formula, data=housing).fit_regularized()

dependant_variable = housing['price']
independent_varaibles = housing[housing.columns.difference(['price', 'driveway', 'recroom', 'fullbase', 'gashw', 'airco',
                                                           'prefarea'])]
independent_variables_standardized = (independent_varaibles - independent_varaibles.mean()) /independent_varaibles.std()
housing_standardized = pd.concat([dependant_variable, independent_variables_standardized], axis=1)

lm_standardized = ols(my_formula, data=housing_standardized).fit_regularized()
print("\nCoefficients:\n%s" % lm_standardized.params)
new_observations = housing.ix[housing.index.isin(range(10)), independent_varaibles.columns]
y_predicted = lm.predict(new_observations)
y_predicted_rounded =[round(score,2) for score in y_predicted]
print(y_predicted_rounded)