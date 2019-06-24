# selenium-
基于selenium的南京二手房数据自动化提出，并写入xml
### 1.创建虚拟环境并安装项目依赖
	首先要安装python的virtualenv虚拟环境，然后启动virtualenv虚拟环境，并在虚拟环境中使用pip 安装依赖的 库
	安装需要包 
	dicttoxml==1.7.4
	selenium==3.141.0
	urllib3==1.25
	(venv) $ pip install -r requirements.txt

### 2.项目步骤说明
  1）使用selenium.webdriver来连接谷歌浏览器，模拟点击筛选条件
  2）利用find_elements(By.XPATH)获取目标文本数据，并利用列表存储数据
  3）利用dicttoxml将数据写入到xml文件中
