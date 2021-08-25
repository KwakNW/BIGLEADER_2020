
from gevent.server import StreamServer
import PredictModel_Num
import time
import pandas as pd

def handler(cs, ca):
    print('데이터 전송 시작')
    
    file = open("model_data.csv", "wb")
    msg = cs.recv(1024)
    data = msg
    
    while msg:
        msg = cs.recv(1024)
        data += msg
        
    file.write(data)
    file.close()
    
#     file = 'model_data.csv'
    
    prediction = PredictModel_Num.Predict('model_data.csv')
    result = prediction.fit()
    print('결과는 : ', result)

    file = open("result.txt", "w", encoding = 'utf-8')
    file.write(str(result))
    file.close()

server = StreamServer(('172.30.1.36', 5118), handler)
print("서버시작")
server.serve_forever()
print("서버시작")

