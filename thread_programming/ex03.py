from threading import Thread
import requests
import time
def getHtml(url):
    resp = requests.get(url)
    with open('./image.png', 'wb') as f:
        f.write(resp.content)

url = 'https://post-phinf.pstatic.net/MjAyMTAxMDZfMTg4/MDAxNjA5ODk2NjA2MjQ1.t_NdFcv1AQb8k9rU3rr1NgAsX_-tEPErKlamo3hlk8Yg.K6iEcgbDugBg5KWv88IoP6MNnWBD6ATPYkX4Q4IC3pEg.JPEG/%EC%82%AC%EC%A7%84%EC%9E%90%EB%A3%8C_%EB%89%B4_%ED%8F%AC%EB%93%9C_%EC%9D%B5%EC%8A%A4%ED%94%8C%EB%A1%9C%EB%9F%AC_%ED%94%8C%EB%9E%98%ED%8B%B0%EB%84%98_2.jpg?type=w1200'
t1 = Thread(target=getHtml, args = (url,))
t1.start()

# 테스트 안해봄 