import numpy as np
import pandas as pd
import statsmodels.api as sm
import random

iris = pd.read_csv('iris.csv', sep=',', header=0)
iris.columns = [heading.lower() for heading in \
                iris.columns.str.replace(".","_")]
iris['iris01'] = np. where(iris['variety'] == 'Setosa', 1., 0.)
# iris['iris01'] = np.where(iris['variety'] == 'Versicolor', 1., 0.)

dependent_variable = iris['iris01']
independent_variables = iris[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
independent_variables_with_constant = sm.add_constant(independent_variables, prepend=True)

logit_model = sm.Logit(dependent_variable, independent_variables_with_constant).fit_regularized()

sample_data_index_list = [48, 49, 50, 51, 52, 53]
new_observations = iris.ix[iris.index.isin(sample_data_index_list), independent_variables.columns]
new_observations_with_constant = sm.add_constant(new_observations, prepend=True)

print("\n샘플링 데이터 예측 테스트")
print("10개 샘플링 데이터 리스트")
print(new_observations_with_constant.head(10))
y_predicted = logit_model.predict(new_observations_with_constant)
y_predicted_rounded = [round(score, 2) for score in y_predicted]

index =1
for predicted_value in y_predicted_rounded:
    if predicted_value > 0.5:
        print("%d번째 샘플링 데이터 예측 결과 %f : Setosa 확실" %(index, predicted_value))
    else:
        print("%d번째 샘플링 데이터 예측 결과 %f : Setosa 아닌 다른 품종" %(index, predicted_value))
    index +=1
