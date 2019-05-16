'''
	(Splitting Data)
        => 머신 러닝 기법 중에서도 지도 학습(Supervised Learning)
'''
import numpy as np
from sklearn.model_selection import train_test_split

x = np.arange(10).reshape((5,2))
y = range(5)


x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.4,random_state=1234)

print(x_train)
print(y_train,'\n')

print(x_test)
print(y_test,'\n')

