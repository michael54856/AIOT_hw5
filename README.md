# Step 3 : Web Using Database
## 再來我們想要將資料庫的內容繪製在網頁上

### 首先我們要先撰寫```GetData.php```

1. 一開始要先跟資料庫進行連線，與localHost連接,使用者為superUser,密碼為123,存取aiotdb這個資料庫
```php
$mysqli = new mysqli("localhost","superUser","123","aiotdb"); 
```
2. 檢查連線狀況
```php
if ($mysqli -> connect_errno) 
{
  echo "Failed to connect to MySQL: " . $mysqli -> connect_error;
  exit();
}
```
3. 執行Query
```php
$sqlcmd2 = "select * from sensors";
$result = $mysqli -> query($sqlcmd2); //$result is a pointer
```
4. 將結果到放Array中
```php
$data; //array
$i=0;
while ($row=mysqli_fetch_array($result,MYSQLI_NUM))
{
	$data[$i]=$row;
	$i ++;
}
```
5. 將資料編碼成json格式返回
```php
echo json_encode($data);
```

6. 關閉連線
```php
$mysqli -> close();
```

<img src="https://raw.githubusercontent.com/michael54856/AIOT_hw5/Step2-Import-Database/Image/step2_1.png">












