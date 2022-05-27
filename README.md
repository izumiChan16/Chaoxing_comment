# 基于Python selenium的学习通自动评论

## 如何使用
1. 你需要git clone本项目，或者下载zip包
![](https://cos.izumichan16.cn/img/20220527112831.png)
2. 在pycharm或任意可以运行python代码的编辑器中打开本项目
3. 请确认你的python版本在3.x,本项目未做任何低于3.10版本的测试
4. 请导入`selenium`包
```shell
pip install selenium
```
4. 你需要下载[对应的selenium浏览器驱动](https://www.selenium.dev/zh-cn/documentation/webdriver/getting_started/install_drivers/)，将其放置到`driver`文件夹中  

![快速参考](https://cos.izumichan16.cn/img/20220527110545.png)  
浏览器的版本您可以在浏览器设置中查看
![版本查看](https://cos.izumichan16.cn/img/20220527111444.png)  
点击下载链接后，请选择对应的版本
![版本选择](https://cos.izumichan16.cn/img/20220527110618.png)  
选择合适的平台下载解压
![下载解压](https://cos.izumichan16.cn/img/20220527110629.png)  

将解压后的文件替换本项目`driver`文件夹中的`chromedriver`（如果您也是使用Linux上最新版的chrome则无需更换）

4. 请把`comment.py`文件中的`name_input`和`pwd_input`替换成你的用户名和密码

5. 如果你不是我班同学，请把`comment.py`文件中的url替换成你需要评论的主网页
![如图操作](https://cos.izumichan16.cn/img/20220527113245.png)

6. 最后您可以直接运行本程序
![](https://cos.izumichan16.cn/img/20220527113823.png)
![](https://cos.izumichan16.cn/img/20220527104941.png)

## 最后
有任何问题可以提交issue或微信联系我本人（仅限同学

欢迎star以及fork本项目