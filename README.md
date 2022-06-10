# Step 5 : Flask Using Database And AI
## 接下來我們想要透過Flask來與資料庫取得資料，並透過訓練好的AI model對light這個資料進行預測並填入顏色
<br>

## 網頁修改

1. 由於我們需要```亂數產生light value```與```用AI預測light```，因此我們需要兩個網頁，分別是```indexAI.html```與```indexNoAI.html```
    * 當想要產生亂數資料時 -> 載入```indexNoAI.html```
    * 當想要使用AI預測顏色時 -> 載入```indexAI.html```

2. 由於我們只預測並只想顯示lights的資訊，因此我們要將Highcharts改成只顯示Light這個資訊，將series改成只顯示lights，```indexAI.html```與```indexNoAI.html```都要改
```html
series: [{
    name: 'Sensor-lights',
    data: lights
}],
```

3. ```indexAI.html```的ajax Function會連接```/getPredict```進行預測，而```indexNoAI.html```的ajax Function會連接```/setRandom```
```html
<!--indexAI.html-->
$(function () {
    $.ajax({									  
        url: '/getPredict',//連接的URL	  
        data: "{}",//夾帶的參數
        .
        .
```
```html
<!--indexNoAI.html-->
$(function () {
    $.ajax({									  
        url: '/setRandom',//連接的URL	  
        data: "{}",//夾帶的參數
        .
        .
```
## Flask app撰寫

4. 先import用到的library，並建立一個基礎的Flask App
```python
from flask import Flask, render_template, jsonify
import pandas as pd
from six.moves import urllib
import json
 
app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
```

5. 先定義基礎的路由，如果是一開始進去會回傳```indexAI.html```，如果進入```/noAI```會回傳```indexNoAI.html```
```python
@app.route("/")
def index():
    return render_template('indexAI.html')

@app.route("/noAI")
def noAI():
    return render_template('indexNoAI.html')    
```

6. 再來我們想定義```/setRandom```的Function()
    * 設定連接資料庫的資料，更改為superUser
    * 引入所需要的資料處理Library
    * 與資料庫進行連接
    * 執行MySQL指令，去更新light value的值
    * 執行MySQL指令，去讀取亂數後的light Value
    * 返回得到的sequence
```python
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
```


7. 再來我們想定義```/getPredict```的Function()
    * 設定連接資料庫的資料，更改為superUser
    * 引入所需要的資料處理Library
    * 使用pickle + gzip去開啟訓練好的Model
    * 與資料庫進行連接
    * 執行MySQL的指令，去sensors資料表讀取資料
    * 之後我們將資料進行reshape，之後餵進Model中進行預測，testY只會有0或1
    * 執行MySQL指令，讓status一開始全為0
    * 再來將status = 1的ID提取出來
    * 將提出來的ID依序將其資料庫中的sensor設為1
    * 將result編碼成json進行回傳
```python
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
    import pandas as pd                     
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
```


8. 最後是定義```/data.json```的Function()
```python
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
```

9. 問題: 由於我們按下```setRandom```的按鈕時，顏色並不會亂數產生，顏色依然照舊，可由下面兩張圖發現
    * Random前
    <img src="https://raw.githubusercontent.com/michael54856/AIOT_hw5/Step5-Flask-Using-Database-And-AI/Image/step5_1.png">
    * Random後
    <img src="https://raw.githubusercontent.com/michael54856/AIOT_hw5/Step5-Flask-Using-Database-And-AI/Image/step5_2.png">

10. 解決方法:
```python
在以下這個地方寫入:
@app.route("/setRandom")
def getData():
  c.execute("update sensors set status = RAND() where true")
目的是為了讓每次的Random也能一同改變顏色,而不是沿用上一次的
```

11. 修改後Random的效果，可發現顏色也一起改了
    * Random前
    <img src="https://raw.githubusercontent.com/michael54856/AIOT_hw5/Step5-Flask-Using-Database-And-AI/Image/step5_3.png">
    * Random後
    <img src="https://raw.githubusercontent.com/michael54856/AIOT_hw5/Step5-Flask-Using-Database-And-AI/Image/step5_4.png">

    