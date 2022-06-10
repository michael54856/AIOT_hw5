# Step 2 : Import Database

1. 開啟**XAMPP**並點選```Admin```開啟控制介面
    <img src="https://raw.githubusercontent.com/michael54856/AIOT_hw5/Step2-Import-Database/Image/step2_1.png">
2. 點選使用者帳號
    <img src="https://raw.githubusercontent.com/michael54856/AIOT_hw5/Step2-Import-Database/Image/step2_2.png">
3. 點選新增使用者帳號
    <img src="https://raw.githubusercontent.com/michael54856/AIOT_hw5/Step2-Import-Database/Image/step2_3.png">
3. 使用者名稱打上```superUser```,密碼打上```123```
    <img src="https://raw.githubusercontent.com/michael54856/AIOT_hw5/Step2-Import-Database/Image/step2_4.png">


2. 下載 [Visual Studio Code](https://code.visualstudio.com/) , [XAMPP](https://www.apachefriends.org/zh_tw/download.html) , [Git](https://git-scm.com/)
3. 在[Github](https://github.com/)中建立一個新的repository (**AIOT_hw5**)
4. 到**Visual Studio Code** clone這個新建立的專案
    按下```Ctrl+Shift+P```並打入```Git Clone```
    <img src="https://raw.githubusercontent.com/michael54856/AIOT_hw5/Step1-Development-Environment-Setup/Image/step1_1.png">
    <br>
    貼上我們剛剛建立的repository網址```https://github.com/michael54856/AIOT_hw5.git```
    <img src="https://raw.githubusercontent.com/michael54856/AIOT_hw5/Step1-Development-Environment-Setup/Image/step1_2.png">
5. 用 Ctrl + ` 叫出Terminal並安裝所需要的套件
```python
pip install Flask 
pip install Jinja2 
pip install sklearn 
pip install pandas  
pip install numpy 
pip install six
pip install PyMySQL
```
6. 為了要能夠Upload File到Github,要先設定一些識別資料
    * C:> git config --global user.name "Michael Wang"
    * C:> git config --global user.email michael548562@gmail.com

7. 建立其他Branches 
    按下```Ctrl+Shift+P```並打入```Git Checkout to```
    <img src="https://raw.githubusercontent.com/michael54856/AIOT_hw5/Step1-Development-Environment-Setup/Image/step1_3.png">
    <br>
    選擇**Create new branch**
    <img src="https://raw.githubusercontent.com/michael54856/AIOT_hw5/Step1-Development-Environment-Setup/Image/step1_4.png">
    <br>
    輸入新的branch名稱
    <img src="https://raw.githubusercontent.com/michael54856/AIOT_hw5/Step1-Development-Environment-Setup/Image/step1_5.png">
    <br>
    按下**Publish Branch**
    <br>
    <img src="https://raw.githubusercontent.com/michael54856/AIOT_hw5/Step1-Development-Environment-Setup/Image/step1_6.png">






