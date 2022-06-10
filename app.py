from flask import Flask, render_template, jsonify
import pandas as pd
from six.moves import urllib
import json
 
app = Flask(__name__)
 
@app.route("/data.json")
def data():
    timeInterval = 1000
    data = pd.DataFrame()
    featureList = ['market-price', 
                   'trade-volume']
    for feature in featureList:
        url = "https://api.blockchain.info/charts/"+feature+"?timespan="+str(timeInterval)+"days&format=json"
        data['time'] = pd.DataFrame(json.loads(urllib.request.urlopen(url).read().decode('utf-8'))['values'])['x']*1000
        data[feature] = pd.DataFrame(json.loads(urllib.request.urlopen(url).read().decode('utf-8'))['values'])['y']
    result = data.to_dict(orient='records')
    seq = [[item['time'], item['market-price'], item['trade-volume']] for item in result]
    return jsonify(seq)
 


@app.route("/")
def index():
    return render_template('indexAI.html')

@app.route("/noAI")
def noAI():
    return render_template('indexNoAI.html')    

@app.route("/setRandom")
def getData():
    #設定連接資料庫的資料，更改為superUser
    myserver ="localhost" 
    myuser="superUser"
    mypassword="123"
    mydb="aiotdb"
    
    #引入所需要的資料處理Library
    debug =0
    from  pandas import DataFrame as df
    import pandas as pd                   
    import numpy as np
    import pymysql.cursors

    #與資料庫進行連接
    conn = pymysql.connect(host=myserver,user=myuser, passwd=mypassword, db=mydb)
    c = conn.cursor()
 

    #執行MySQL指令，去更新light value的值
    c.execute("update sensors set value = RAND()*1000 where true")
    conn.commit()
    
    #執行MySQL指令，去讀取亂數後的light Value
    c.execute("SELECT * FROM sensors")
    results = c.fetchall()
    print(type(results))
    print(results[:10])
    if debug:
        input("pause ....select ok..........")

    test_df = df(list(results),columns=['id','time','value','temp','humi','status'])

    #返回得到的sequence
    print(test_df.head(10))
    result = test_df.to_dict(orient='records')
    seq = [[item['id'], item['time'], item['value'], item['temp'], item['humi'], item['status']] for item in result]
    return jsonify(seq)



@app.route("/getPredict")
def getPredict():
    #設定連接資料庫的資料，更改為superUser
    myserver ="localhost"
    myuser="superUser"
    mypassword="123"
    mydb="aiotdb"
    
    #引入所需要的資料處理Library
    debug =0
    from  pandas import DataFrame as df
    import pandas as pd                     # 引用套件並縮寫為 pd
    import numpy as np

    #使用pickle + gzip去開啟訓練好的Model
    import pickle
    import gzip
    with gzip.open('./model/myModel.pgz', 'r') as f:
        model = pickle.load(f)

    #與資料庫進行連接      
    import pymysql.cursors
    conn = pymysql.connect(host=myserver,user=myuser, passwd=mypassword, db=mydb)
    c = conn.cursor()
    if debug:
        input("pause.. conn.cursor() ok.......")
    
    #執行MySQL的指令，去sensors資料表讀取資料
    c.execute("SELECT * FROM sensors")
    results = c.fetchall()
    print(type(results))
    print(results[:10])
    if debug:
        input("pause ....select ok..........")
    

    #之後我們將資料進行reshape，之後餵進Model中進行預測，testY只會有0或1
    test_df = df(list(results),columns=['id','time','value','temp','humi','status'])
    print(test_df.head(10))
    testX=test_df['value'].values.reshape(-1,1)
    testY=model.predict(testX)
    print(model.score(testX,testY))
    
    test_df['status']=testY
    print(test_df.head(10))
    
    if debug:
        input("pause.. now show correct one above.......")
    
    #執行MySQL指令，讓status一開始全為0
    c.execute('update sensors set status=0 where value>0')
    
    #再來將status = 1的ID提取出來
    id_list=list(test_df[test_df['status']==1].id)
    print(id_list)

    #將提出來的ID依序將其資料庫中的sensor設為1
    for _id in id_list:
        c.execute('update sensors set status=1 where id='+str(_id))
    
    conn.commit()
    
    #將result編碼成json進行回傳
    result = test_df.to_dict(orient='records')
    seq = [[item['id'], item['time'], item['value'], item['temp'], item['humi'], item['status']] for item in result]
    return jsonify(seq)



if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

