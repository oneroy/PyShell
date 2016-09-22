# PyShell
## python 后门程序

基于python编写的后门程序，主要用于获取服务器shell以后，留后门或者执行cmd、python脚本使用。

### 使用方法:
```bash
[HELP]  PyShell.exe [-listen(-slave)] [ip] [port]         

[HELP]  python PyShell.py [-listen(-slave)] [ip] [port]    
```
### 功能参数:
```bash
connection：

[HELP]  exit    ----退出连接

[HELP]  kill    ----退出连接并自毁程序

[HELP]  playtask    ----创建计划任务

[HELP]  python -p file.py    ----在肉鸡上执行本地python脚本
```
### 优缺点：
* 程序对互相传输的数据进行了加密，以绕过防火墙。

* 当需要在肉鸡上执行python脚本时，不需要在肉鸡上上传相应的脚本文件，只需将本地脚本内容加密传输到肉鸡，并执行即可。

* 此程序在执行完命令以后，并不能时时回显结果，也就是说python脚本运行完以后才会返回输出，可以继续完善。

### 详细参照 [http://thief.one](http://thief.one/2016/09/05/PyShell-%E6%9C%A8%E9%A9%AC%E5%90%8E%E9%97%A8/)
