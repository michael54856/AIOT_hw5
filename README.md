# Step 3 : Web Using Database
## 再來我們想要將資料庫的內容繪製在網頁上

1. 首先我們要先撰寫```GetData.php```，一開始要先跟資料庫進行連線
```php
//1. 與localHost連接,使用者為superUser,密碼為123,存取aiotdb這個資料庫
$mysqli = new mysqli("localhost","superUser","123","aiotdb"); 
```
2. 檢查連線狀況
```php
//2. 檢查連線狀況
if ($mysqli -> connect_errno) 
{
  echo "Failed to connect to MySQL: " . $mysqli -> connect_error;
  exit();
}
```
3. 執行Query
```php
//3. 執行query
$sqlcmd2 = "select * from sensors";
$result = $mysqli -> query($sqlcmd2); //$result is a pointer
```



<img src="https://raw.githubusercontent.com/michael54856/AIOT_hw5/Step2-Import-Database/Image/step2_1.png">












