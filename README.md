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

      
  
