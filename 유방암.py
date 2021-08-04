from sklearn.datasets import load_breast_cancer
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

breast__cancer_data = load_breast_cancer()

# 데이터 정보 보기
# WDBC-Malignant -> 악성, WDBC-Benign -> 양성 두가지로 분류
print(breast__cancer_data.DESCR)

# 입력변수 정의
X = pd.DataFrame(breast__cancer_data.data,columns= breast__cancer_data.feature_names)

# 목표변수 정의
y = pd.DataFrame(breast__cancer_data.target,columns=['class'])
print(y)

# 데이터셋 나누기
x_train,x_test,y_train,y_test = train_test_split(X,y,test_size=0.2 ,random_state=5)

# 모델 만들기
model = LogisticRegression(solver='saga',max_iter= 2000)
model.fit(x_train,y_train)

# 로지스틱 회귀할때 추가하기!
y_train = y_train.values.ravel()

# 모델의 정확도 
score = model.score(x_test,y_test)
print("정확도: {}%".format(round(score * 100,2)))
# print(model.coef_) # 세타0 의 값
# print(model.intercept_) # 세타1의 값
