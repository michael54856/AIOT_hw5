# Step 3 : Web Using Database
## 再來我們想要將資料庫的內容繪製在網頁上

1. 首先我們要先撰寫```GetData.php```，一開始要先跟資料庫進行連線
```php
$mysqli = new mysqli("localhost","superUser","123","aiotdb"); //與localHost連接,使用者為superUser,密碼為123,存取aiotdb這個資料庫
```
<img src="https://raw.githubusercontent.com/michael54856/AIOT_hw5/Step2-Import-Database/Image/step2_1.png">












