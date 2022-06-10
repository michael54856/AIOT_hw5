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
### 再來是網頁的主體```index.html```

7. highcharsinit()會設定HighChart的一些資訊
```html
function highcharsinit(){
	$('#container').highcharts({
		title: {
			text: 'Sensor data from MySQL to Highcharts',
			x: -20 
		},
		/*subtitle: {
			text: 'Light Value',
			x: -20
		},*/
		xAxis: {
			title: {
			text: 'Time'
			},
			categories: time,
			labels:{ //隱藏X軸的標籤
				enabled: false,
			}
		},
		yAxis: {
			title: {
			text: 'value',
			}
		},
		//圖表的資料
		
		series: [{
			name: 'Sensor-humids',
			data: humis
		},{
			name: 'Sensor-temps',
			data: temps
		},{
			name: 'Sensor-lights',
			data: lights
		}]
	});
}

```

8. 再來我們需要一個ajax Function來取得GetData.php回傳的資料，並根據status來更改顏色
```html
$(function () {
	$.ajax({									  
		url: 'GetData.php',//連接的URL	  
		data: "{}",//夾帶的參數
		dataType: 'json', //資料格式 
		success: function(data)	//傳送成功的function
			{	
				lights = [];
				humis=[];
				temps = [];
				time = [];
				
				for (var i =  0; i < data.length; i++)
				{
					if(parseInt(data[i][5])==0) //如果status是1,全部都設為紅色
					{
						lights.push({y:parseInt(data[i][2]), color: '#FF0000' }); 
						humis.push({y:parseInt(data[i][4]), color: '#FF0000' });
						temps.push({y:parseInt(data[i][3]), color: '#FF0000' });
					}
					else//如果status是0,lights設為綠色,humis設為藍色,temps設為黑色
					{
						lights.push({y:parseInt(data[i][2]), color: '#00FF00' });
						humis.push({y:parseInt(data[i][4]), color: '#000000' });
						temps.push({y:parseInt(data[i][3]), color: '#0000FF' });
					}
					time.push(data[i][1]);
				}
				highcharsinit();
				} //success end

		}); //ajax end

	}); //function end
```



<img src="https://raw.githubusercontent.com/michael54856/AIOT_hw5/Step2-Import-Database/Image/step2_1.png">












