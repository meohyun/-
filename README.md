# scikit_learn_example

scikit_learn 라이브러리를 활용한 머신러닝을 연습해 보았습니다.

위의 데이터셋은 유방암 진단을 위한 데이터셋이고 이를 모델에 학습시켜 그 정확도를 환산하는 프로그램입니다.


먼저 필요한 라이브러리를 import 해줍니다.

      from sklearn.datasets import load_breast_cancer #1
      import pandas as pd #2
      from sklearn.model_selection import train_test_split #3
      from sklearn.linear_model import LogisticRegression #3
      
 1. scikit_learn의 유방암 데이터셋을 불러옵니다. 
 2. pandas 형식으로 데이터를 불러옵니다.
 3. train_test_split 함수로 데이터셋을 학습데이터와 테스트데이터로 나눕니다.
 4. scikit_learn 모델중 로지스틱 회귀모델을 사용합니다.




        breast__cancer_data = load_breast_cancer()

        # 데이터 정보 보기
        # WDBC-Malignant -> 악성, WDBC-Benign -> 양성 두가지로 분류
        print(breast__cancer_data.DESCR)
            

 load_breast_cancer 함수로 유방암 진단 데이터셋을 가져오고
 breast_cancer_data 변수에 저장합니다.
 DESCR을 이용하여 데이터셋의 정보를 볼 수 있습니다. 이 데이터셋은 유방암을 악성,양성 둘중 하나로 분류하는 데이터셋입니다.
 따라서 분류를 해야 하므로 로지스틱 회귀 모델이 적절하다고 볼 수 있습니다.



      # 입력변수 정의
      X = pd.DataFrame(breast__cancer_data.data,columns= breast__cancer_data.feature_names)

      # 목표변수 정의
      y = pd.DataFrame(breast__cancer_data.target,columns=['class'])
 
 pandas의 DataFrame 함수를 사용하여 데이터셋을 pandas 형식으로 저장합니다.
 입력변수는 X에 저장해주고
 목표변수는 악성과 양성을 나타내는 'class' column을 y에 저장합니다.
 


      # 데이터셋 나누기
      x_train,x_test,y_train,y_test = train_test_split(X,y,test_size=0.2 ,random_state=5)
      
      
 학습데이터와 테스트데이터를 나눠줍니다. 
 test_size는 전체데이터의 몇퍼센트 만큼을 테스트 데이터로 사용할건지를 나타내는 파라미터 입니다.
 0.2 이면 20퍼센트를 사용하겠다는 의미입니다.
 
 random_state 파라미터는 머신러닝을 진행할때마다 랜덤으로 테스트데이터와 학습데이터를 나누기 때문에 두 데이터가 계속 바뀌게 됩니다.
 이를 막기위해 임의의 숫자를 적어놓으면 매번 동일한 테스트데이터와 학습데이터를 사용할 수 있습니다.
      

      # 모델 만들기
      model = LogisticRegression(solver='saga',max_iter= 2000)
      model.fit(x_train,y_train)
      y_train = y_train.values.ravel()
      
 
 로지스틱 회귀를 이용한 머신러닝 모델을 만들어 줍니다.
 solver 파라미터는 해당 모델의 알고리즘 방식을 정의합니다. 'saga'방식을 사용해보겠습니다.
 max_iter 파라미터는 최적의 세타값을 찾기위해 몇번의 경사하강을 진행할 것인지 정합니다.
 
 모델에 입력변수와 목표변수의 학습데이터를 적용합니다.
 
 ※ y_train = y_train.values.ravel()은 경고문구를 막기위해 작성한 코드입니다.※


      # 모델의 정확도 
      score = model.score(x_test,y_test)
      print("정확도: {}%".format(round(score * 100,2)))
      
 
 모델의 정확도를 score 함수를 사용하여 측정할 수 있습니다.
 로지스틱 회귀는 항상 0과 1사이의 값이 나오므로 100을 곱해준후 소수점 둘째자리에서 반올림을 하여 퍼센트를 나타냈습니다.
 
 

  
