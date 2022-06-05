# 创新实验大作业

各附件功能及使用方式

#### exploit.c

缓冲区溢出漏洞的代码，编译后部署与zombie主机上，attacker通过缓冲区溢出攻击来获取zombie主机的权限

**使用方式**

```
gcc -o exploit exploit.c -fno-stack-protector
```

#### exp.py

attacker用于进行缓冲区溢出攻击的脚本文件

**使用方式**

```
python3 exp.py
```

注：需下载pwntools包

```
pip3 install pwntools
```

#### SQLi.sql

server的数据库生成脚本，包含管理员账号和密码的sha1信息

**使用方式**：

```
sudo mysql -u root
mysql> use elgg;
mysql> source SQLi.sql;
mysql> exit
```

#### front

server上部署的前端代码

**使用方式**

```
sudo cp -r front /var/www/
sudo chmod -R 5555 front
```

此外还需要修改apache2和其他虚拟机的/etc/hosts文件