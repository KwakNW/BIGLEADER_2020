#!/usr/bin/env python
# coding: utf-8

from gevent.server import StreamServer
import time

def handler(cs, ca):
    print("결과 전송 시작")
    file = open("result.txt", 'r', encoding = 'utf-8')
    result = file.read()
    file.close()
    cs.sendall(result.encode())
    cs.close()
    print("보내기 끝")
    
server = StreamServer(('172.30.1.36', 5117), handler)
print("서버시작")
server.serve_forever()





