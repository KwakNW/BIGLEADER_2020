# Predicting the crowded level of visitors to national parks using AI deep learning technology
데이터 사이언스 및 AI 융합 기반의 빅리더 양성 아카데미 중 팀 프로젝트 수행

<h5>사용 언어 및 Tool</h5>

- Python
- JAVA
- Android Studio
- QGIS

<h5> 분석과정 </h5>

![image](https://user-images.githubusercontent.com/68180545/139637404-e37fbbb6-58bc-4e1d-b322-911b6b4c7339.png)
![image](https://user-images.githubusercontent.com/68180545/139637534-bf031aa6-2c14-4136-b678-75f6f1be9bdf.png)
![image](https://user-images.githubusercontent.com/68180545/139637629-99e513db-bcd1-4472-baac-41d75a893a36.png)
![image](https://user-images.githubusercontent.com/68180545/139637662-34f43de5-d638-4547-a3ae-b290fc298b39.png)
![image](https://user-images.githubusercontent.com/68180545/139637687-5e7dc759-5f33-4c39-8ac4-9bf58091812e.png)
![image](https://user-images.githubusercontent.com/68180545/139637736-a786d666-f37c-4bfa-bb25-68f65560e3fc.png)

<h5> 모델 성능 비교 </h5>

![image](https://user-images.githubusercontent.com/68180545/139637803-558661d4-21ec-4385-8389-8f8cbac5fd03.png)
![image](https://user-images.githubusercontent.com/68180545/139637826-9d3542c0-f783-44ee-954b-fbebcc546f89.png)

정확도 및 Confusion Matrix 수행 결과 5단계보다 3단계의 효용성이 더 높아 3단계 DNN 모델로 구현

<h5> 결과 </h5>

![image](https://user-images.githubusercontent.com/68180545/139637955-45b9e80e-1e78-4385-af49-0382d0de7dac.png)

----------------------------------------------------------------------------------------------------------------------------

<h4> [서버] </h4>

200826_get.py -> 어플에서 서버로 정보 받아오는 파일
200826_serve.py -> 서버를 통해 어플로 정보 넘겨주는 파일

둘다 StreamServer라서 172.30.1.36 부분을 해당 컴퓨터에 맞는 ip주소로 변환필요 (핸드폰이랑 같은 ip사용)
Android Studio 즉 어플에서도 변경 필요..

<h4> [데이터]</h4>

200901_계수기 => 2007~2019년 계수기 데이터 csv화 한 것(LSTM에 사용)
couse.pkl => 코스별 포인터번호로 연결해놓은 파일

<h4> [APP의 현재 문제점.] </h4>

1. Database(DB)를 생성하는 과정에서 컴퓨터 Directory에 있는 DB를 Application(App)에서 사용할 수 있게 코드를 변경하다보니 APP자체에서 DB를 생성하는 동작이 불가능.
2. 즐겨찾기를 눌렀을 때 현재 즐겨찾기에 추가된 상태인지 아닌지 판단할 수 있는 부분이 없어 APP 실행 시 무조건 비어있는 별이 표시가 됨. 추가적으로 즐겨찾기 Activity에서 즐겨찾기 해제 시 오류 발생.
3. 전체적인 주석의 부족 및 사용하지 않는 코드가 다수 존재.

android studio 코드는 용량상 문제로 업로드 불가
