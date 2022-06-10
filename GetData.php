
<?php
/*AddData.php*/
//1 . 與localHost連接,使用者為superUser,密碼為123,存取aiotdb這個資料庫
$mysqli = new mysqli("localhost","superUser","123","aiotdb");

//2. 檢查連線狀況
if ($mysqli -> connect_errno) {
  echo "Failed to connect to MySQL: " . $mysqli -> connect_error;
  exit();
}

//3. 執行query
$sqlcmd2 = "select * from sensors";
$result = $mysqli -> query($sqlcmd2); //$result is a pointer


//4. 將結果放到Array中
$data; //array
$i=0;
while ($row=mysqli_fetch_array($result,MYSQLI_NUM)){
	$data[$i]=$row;
	$i ++;
}

//5. 將資料編碼成json格式返回
 echo json_encode($data);

//6. 關閉連線
$mysqli -> close();
?>
