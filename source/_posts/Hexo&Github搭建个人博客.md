---
title: Hexo&Github搭建个人博客
date: 2023-05-12 20:46:38
tags: Blog
---

# Hexo&Github搭建个人博客

## Nodejs

> 教程：[nodejs安装和环境配置-Windows_nodejs安装及环境配置](https://blog.csdn.net/weixin_52799373/article/details/123840137) 

## git

> 教程：[Windows系统Git安装教程（详解Git安装过程）](https://www.cnblogs.com/xueweisuoyong/p/11914045.html) 

## 本地部署

创建一个名为`Blog`的文件，作为博客根目录，在里面右键启用`Git Bash Here`

### Hexo安装

```
npm install hexo-cli -g
```

### 初始化Hexo博客

```
hexo init
```

如下图所示即为成功：![1680873666633](C:\Users\PLacebo\AppData\Roaming\Typora\typora-user-images\1680873666633.png)

### 生成本地Hexo页面

搭建本地博客完成后若想再次在本地访问博客则可直接从此步骤开始。

```
hexo server
或者hexo s
```

如下图所示即为成功：![1680873683510](C:\Users\PLacebo\AppData\Roaming\Typora\typora-user-images\1680873683510.png)

然后在浏览器中打开`http://localhost:4000/`，就能看到本地博客；按下`Ctrl+C`则关闭本地服务器。

## Github部署

### github注册

> 官方网址：[GitHub](https://github.com/) 

点击右上角`Sign up`完成注册。

### 新建仓库

在github个人首页，点击`Create repository`，如下图所示：![1680873809468](C:\Users\PLacebo\AppData\Roaming\Typora\typora-user-images\1680873809468.png)

命名为`username.github.io`（username 是你的用户名)，如下图：![1680873944366](C:\Users\PLacebo\AppData\Roaming\Typora\typora-user-images\1680873944366.png)

如果创建成功后页面为404，则尝试挂一下加速器，改host可能会有此问题，或者裸连。

创建成功后能在右上角Code选项下看见仓库的地址，这个仓库地址后面会用到。

### Git与github配置

此处为全局配置，所以可以在任意位置打开git bash, 设置用户名称和邮件地址（替换成自己的githubID和注册的邮箱）

```
git config --global user.name "Placebo27"
git config --global user.email "placeb0@qq.com"
```

#### 获取本地SSH公钥

**生成SSH公私钥对**

```
ssh-keygen -t rsa -C "你的邮箱地址"
```

一共四次回车，第二次回车前输入`y`

**复制SSH公钥**

在上一步SSH生成成功后的文件路径`C:/Users/用户名/.ssh`中找到`id_rsa.pub`文件，用文件编辑器打开并复制其内容；或者使用如下命令复制其内容（cmd或者Bash中皆可）：

```
clip < C:/Users/用户名/.ssh/id_rsa.pub
```

#### Github添加SSH key

打开 github 点击头像 -> Settings -> SSH and GPG keys -> New SSH key 新建 SSH key：![1680956656990](C:\Users\PLacebo\AppData\Roaming\Typora\typora-user-images\1680956656990.png)

![1680956631099](C:\Users\PLacebo\AppData\Roaming\Typora\typora-user-images\1680956631099.png)

![1680956679681](C:\Users\PLacebo\AppData\Roaming\Typora\typora-user-images\1680956679681.png)

Title可以随便起，将上述SSH公钥粘贴到Key文本框中：![1680957120218](C:\Users\PLacebo\AppData\Roaming\Typora\typora-user-images\1680957120218.png)

#### 测试SSH key是否配置成功

```
ssh -T git@github.com
```

第一次连接测试需要输入`yes`，若出现`successfully authenticated`则配置成功。

#### Git修改deploy配置项

打开`Blog/_config.yml`，修改底部deploy配置项：

```
deploy:
  type: git
  repository: 你的github仓库地址
  branch: main
```

### hexo-deployer-git自动部署发布工具安装

```
npm install hexo-deployer-git --save

```

![1680875583179](C:\Users\PLacebo\AppData\Roaming\Typora\typora-user-images\1680875583179.png)

### 生成public上传文件夹

进入到`Blog`博客根目录下，右键选择`Git Bash Here`：

如果不是首次上传则先清除本地的缓存（首次上传清不清除无所谓）：

```
hexo clean
或者hexo cl

```

```
hexo generate
或者hexo g

```

![1680876225334](C:\Users\PLacebo\AppData\Roaming\Typora\typora-user-images\1680876225334.png)

### 部署到github

将生成的public文件夹部署到github上，把本地hexo博客内容提交到github仓库：

```
hexo deploy
或者hexo d

```

如果发生如下报错：![1680876607176](C:\Users\PLacebo\AppData\Roaming\Typora\typora-user-images\1680876607176.png)

出现该问题不要惊慌，这个错误其实很简单，是因为同步文件缺失导致的，很明显我们push的hexo静态文件会缺失README.md这个文件，所以我们只需要把远端的README.md文件同步下来或者新建一个readme.md文档即可。

这里我选择新建README.md文档。（此操作后来发现，没什么用，但是也记录下来）

![1680877252167](C:\Users\PLacebo\AppData\Roaming\Typora\typora-user-images\1680877252167.png)

**实际解决方法：**

 1.在文件浏览器中勾选显示隐藏的项目 

 2.进入我们博客目录的`.deploy_git.git`子目录，找到config文件。 

 3.打开config文件，添加以下内容 ：

```
[user]
	email=你的邮箱
	name=GitHub用户名

```

若又出现以下错误，无法访问错误， 不要惊慌，多次尝试，或者更换网络再次尝试（加速器）：![1680877644122](C:\Users\PLacebo\AppData\Roaming\Typora\typora-user-images\1680877644122.png)

然后会弹出一个小窗口，登陆你的github账户进行连接，链接成功你会收到一封邮件。

![1680877867261](C:\Users\PLacebo\AppData\Roaming\Typora\typora-user-images\1680877867261.png)

这样就成功了，打开你的github个人仓库会看到你推送的文件。

![1680878108104](C:\Users\PLacebo\AppData\Roaming\Typora\typora-user-images\1680878108104.png)

然后通过你的仓库后面的链接`https://username.github.io`访问你的个人博客。

![1680878256004](C:\Users\PLacebo\AppData\Roaming\Typora\typora-user-images\1680878256004.png)

![1680878360529](C:\Users\PLacebo\AppData\Roaming\Typora\typora-user-images\1680878360529.png)

