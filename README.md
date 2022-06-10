# Step 4 : Simple Flask
## 再來我們想要先簡單建立一個Flask網頁

1. 我們先簡單寫一個網頁，造訪網頁時會顯示```Hello World in static file```
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h2> Hello World in static file</h2>
</body>
</html>
```
2. 再來我們將使用Flask來顯示網頁
```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('index.html')

if __name__ == '__main__':
   app.run("127.0.0.1",5050,debug=True)
```

3. 成果
	<img src="https://raw.githubusercontent.com/michael54856/AIOT_hw5/Step3-Web-Using-Database/Image/step3_1.png">












