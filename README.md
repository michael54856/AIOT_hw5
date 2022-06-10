# Step 5 : Flask Using Database And AI
## 接下來我們想要透過Flask來與資料庫取得資料，並透過訓練好的AI model對light這個資料進行預測並填入顏色
<br>

## 網頁修改

1. 由於我們需要```亂數產生light value```與```用AI預測light```，因此我們需要兩個網頁，分別是```indexAI.html```與```indexNoAI.html```
    * 當想要產生亂數資料時 -> 載入```indexNoAI.html```
    * 當想要使用AI預測顏色時 -> 載入```indexAI.html```
