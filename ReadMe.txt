Windows系统环境部署：
1.下载安装python3.7和pycharm编辑器
  登录https://www.python.org/downloads/windows/ 下载python包，正常下载安装，安装完成后打开cmd，输入python，进入python编辑界面，则安装成功，如不成功，一般是未配置环境变量，配置环境变量即可。
  登录https://www.jetbrains.com/pycharm/download/#section=windows 下载Community版，正常安装
  登录http://npm.taobao.org/mirrors/chromedriver/ 下载对应chrome版本的chromedriver，替换掉tools下的chromedriver
2.导入第三方库
  打开cmd，使用pip install -r requirements.txt,导入所有使用的第三方库
3.执行case
  执行python run_all_test.py

Linux系统环境部署：
