# Step 3 : Web Using Database
## 再來我們想要將資料庫的內容繪製在網頁上

1. 首先我們要設定每個data代表的顏色
```html
for (var i =  0; i < data.length; i++)
{
    if(parseInt(data[i][5])==0){
        lights.push({y:parseInt(data[i][2]), color: '#FF0000' });
        humis.push({y:parseInt(data[i][4]), color: '#FF0000' });
        temps.push({y:parseInt(data[i][3]), color: '#FF0000' });
    }else{
        lights.push({y:parseInt(data[i][2]), color: '#0000FF' });
        humis.push({y:parseInt(data[i][4]), color: '#000000' });
        temps.push({y:parseInt(data[i][3]), color: '#00FF00' });
    }
    time.push(data[i][1]);
}
```
<img src="https://raw.githubusercontent.com/michael54856/AIOT_hw5/Step2-Import-Database/Image/step2_1.png">












