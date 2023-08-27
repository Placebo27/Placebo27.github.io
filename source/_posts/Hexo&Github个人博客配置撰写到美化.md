---
title: Hexo&Github个人博客配置撰写到美化
tags: 
- Hexo
- Github
categories: 
- Blog
typora-root-url: ../
date: 2023-06-02 23:29:35
---

# Hexo&Github个人博客配置撰写到美化

## 配置博客

- `hexo cl` 是 `hexo clean`的简写。意思是清除本地的缓存，实际上就是把博客文件夹下的`public`文件夹删除掉了。这个`public`是基于本地的文件生成的、用于上传到仓库或者其他网站服务器上的文件夹，可以理解为本地文件上网的中转站、交通工具，删掉了也不影响本地的内容。
- `hexo g` 是`hexo generate`的简写，意思是生成public文件夹。
- `hexo d`是`hexo deploy`的简写，意思是将生成的public文件夹部署到网上，我们这里是部署到github上面。为了顺利部署，我们前面也提到过，要在站点文件夹下`_config.yml`文件中修改一些内容，如下：

### 博客文件夹

我们打开自己的博客根目录，了解一下里面的这些文件（夹）都是干什么的：

![1680958520314](/images/配置博客/1680958520314.png)

- `_config.yml`：俗称**站点配置文件**，很多与博客网站的格式、内容相关的设置都需要在里面改。
- `node_modules`:存储Hexo插件的文件，可以实现各种扩展功能。一般不需要管。
- `package.json`：别问我，我也不知道干嘛的。
- `scaffolds`：模板文件夹，里面的`post.md`文件可以设置每一篇博客的模板。具体用起来就知道能干嘛了。
- `source`：非常重要。所有的个人文件都在里面！
- `themes`：主题文件夹，可以从[Hexo主题官网](https://hexo.io/themes/)或者网上大神的Github主页下载各种各样美观的主题，让自己的网站变得逼格高端的关键！

接下来重点介绍`source`文件夹。新建的博客中，`source`文件夹下默认只有一个子文件夹——`_posts`。我们写的博客都放在这个子文件夹里面。我们还可以在`source`里面新建各种子文件夹满足自己的个性化需求，对初学者而言，我们先把精力放在主线任务上，然后再来搞这些细节。

![1680958715749](/images/配置博客/1680958715749.png)

### 新建博客文件

博客文件格式为`.md`（Markdown格式文件，建议使用[Typora软件](https://www.typora.io/)进行编辑）。**注意**：不要新建`.md`文件，一定要用代码建立新的博客 ：

```
hexo new "新建文件名"
或者hexo n "文件名"
```

写好内容后，在命令行进行hexo三部曲：

> 'hexo cl'命令用于清除缓存文件（db.json）和已生成的静态文件（public）。例如：在更换主题后，如果发现站点更改不生效，可以运行该命令。

```cobol
hexo cl
```

```
hexo g
```

```cobol
hexo s
```

然后随便打开一个浏览器，在网址栏输入`localhost:4000/`，就能发现自己的网站更新了！不过这只是在本地进行了更新，要想部署到网上（Github上），输入如下代码：

```
hexo d
```

然后在浏览器地址栏输入`https://yourname.github.io`，或者`yourname.github.io`就能在网上浏览自己的博客了！

> 注意：本地调试其实并不用每次都要hexo三部曲，只需要`hexo s`，就可以用`localhost:4000`来查看修改效果，可以节省大量时间 

以上，我们的博客网站1.0版本就搭建完成了，如果没有更多的需求，做到这里基本上就可以了。如果有更多的要求，还需要进一步的精耕细作！

### 修改博客信息

首先打开`_config.yml`**站点配置文件**，找到**Site**注释的地方，这里是博客的基本信息。

![1680963693171](/images/配置博客/1680963693171.png)

这些都按照个人需要修改，下面是所有配置的释义：

title: # 标题
subtitle: # 副标题
description: # 站点描述（可以写简介或格言）
keywords: # 搜索关键词
author: # 作者
language: zh-CN # 语言（这里按你的主题themes中languages文件夹下的文件名填写）
timezone: Asia/Shanghai # 时区（中国时区）

### 更改主题

这个388主题，说实话太难看了，因此要去找一个好看的主题，Hexo官方专门提供了一个主题库，可以找到非常多的Hexo主题，并下载更换。

个人觉得**NexT**主题挺好看的，主要是简约，所以我就拿NexT主题为例更换吧。

首先，打开[主题库](https://hexo.io/themes/),搜索NexT， 点击主题的名字，就可以跳转到主题的下载页面 

![1680964031232](/images/配置博客/1680964031232.png)

 往下滑找到**安装**标签，这包含了主题的下载安装方法。 

![1680965510560](/images/配置博客/1680965510560.png)

 这里我们选择较快的npm下载。首先，切换到博客的根目录，也就是Blog文件夹中，输入`npm install hexo-theme-next`就可以安装NexT主题了，npm安装的NexT主题的目录在**node_modules**文件夹下的**hexo-theme-next**文件夹中，里面包含了NexT的配置文件。 

![1680964267170](/images/配置博客/1680964267170.png)

![1680964767983](/images/配置博客/1680964767983.png)

也可以使用git，通过git命令进行下载（克隆）

```
git clone https://github.com/next-theme/hexo-theme-next themes/next
```

![1680965881830](/images/配置博客/1680965881830.png)

如果不会使用git命令，就在github上进行下载

![1680964436969](/images/配置博客/1680964436969.png)

 把这个文件下载到本地之后，修改配置文件。首先找到自己博客文件夹的地址，将下载的文件夹放到 

`.\Blog\themes`目录下，然后返回上级目录。

最后，要记得修改`_config.yml`配置文件 中的theme主题

![1680964912309](/images/配置博客/1680964912309.png)

## NEXT主题优化

对于next的主题优化可以说是耗时耗力的，建议以个人需求为主，无需将所有内容添加进个人博客，这部分建议结合个人需求适当挑选其中内容进行配置。

### 更改NEXT主题

next主题有四种：Muse、Mist、Pisces、Gemini，如下图所示

Muse：![1683950862678](/images/配置博客/1683950862678.png)

Mist：![1683951027038](/images/配置博客/1683951027038.png)

Pisces：![1683951112541](/images/配置博客/1683951112541.png)

Gemini：![1683951226689](/images/配置博客/1683951226689.png)

- Muse - 默认 Scheme，这是 NexT 最初的版本，黑白主调，大量留白
- Mist - Muse 的紧凑版本，整洁有序的单栏外观
- Pisces - 双栏 Scheme，小家碧玉似的清新
- Gemini - 左侧网站信息及目录，块+片段结构布局

打开博客目录Blog/themes/next/下的_config.yml（**主题配置文件**），只要将你所选主题前的注释`#`剪切到当前主题就行了：

```text
# Schemes
scheme: Muse	    #这是默认主题
#scheme: Mist
#scheme: Pisces
#scheme: Gemini
```

接下来同更新博客操作，打开git bash在命令行一键三连：

```
hexo cl && hexo g && hexo s
```

然后打开浏览器，在网址栏输入`localhost:4000/`，就能发现自己的网站更新了！![1680965379223](/images/配置博客/1680965379223.png)

若要部署到Github上：

```bash
hexo d
```

### 设置博客icon

图标素材：[iconfont-阿里巴巴矢量图标库](https://www.iconfont.cn/) 

选择合适的icon，分别下载16，32，180大小png格式及400大小svg格式的图标，放置在 `/themes/next/source/imges/` 文件夹中。

修改**主题配置文件**中 `favicon` 中的内容，依次替换`small`，`medium`，`apple_touch_icon`，`safari_pinned_tab`字段的图片名；如果是直接替换原来的图标文件则不需要修改。

### 设置导航菜单

#### 导航菜单展示

第一种方法比较麻烦，打开**主题配置文件**，修改 `menu` 中的内容，编辑想要展示的内容，可参考下方示例：

```yaml
menu:
  home: / || fa fa-home                      #首页
  tags: /tags/ || fa fa-tags                 #标签
  categories: /categories/ || fa fa-th       #分类
  archives: /archives/ || fa fa-archive      #归档
  #schedule: /schedule/ || fa fa-calendar    #日历
  #sitemap: /sitemap.xml || fa fa-sitemap    #站点地图，供搜索引擎爬取
  #commonweal: /404/ || fa fa-heartbeat      #腾讯公益404
  # List||fas fa-list:
  #   Music: /music/ || fas fa-music
  #   Movie: /movies/ || fas fa-video
  link: /link/ || fas fa-link                #友情链接
  about: /about/ || fa fa-user			    #关于

# Enable / Disable menu icons / item badges.    
menu_settings:
  icons: true       # 是否显示各个页面的图标
  badges: true      # 是否显示分类/标签/归档页的内容量
```

“||”前面的是目标链接，后面的是图标名称，next使用的图标全是[图标库 - Font Awesome 中文网](https://link.zhihu.com/?target=http%3A//www.fontawesome.com.cn/faicons/%23web-application)这一网站的，有想用的图标直接在该网站上面找图标的名称就行。

新添加的菜单需要翻译对应的中文，打开`theme/next/languages/zh-CN.yml`，在`menu`下设置：

```yml
menu:
  home: 首页
  archives: 归档
  categories: 分类
  tags: 标签
  about: 关于我
  search: 搜索
  schedule: 日程表
  sitemap: 站点地图
  commonweal: 公益 404
  link: 友人帐
```

第二种方法可以直接在第一步中的**主题配置文件**一步到位（但是以后更改language时菜单内容依然会是如下中文）：

```yml
menu:
  首页: / || fa fa-home
  标签: /tags/ || fa fa-tags
  分类: /categories/ || fa fa-th
  归档: /archives/ || fa fa-archive
  #schedule: /schedule/ || fa fa-calendar
  #sitemap: /sitemap.xml || fa fa-sitemap
  #commonweal: /404/ || fa fa-heartbeat
  # List||fas fa-list:
  #   Music: /music/ || fas fa-music
  #   Movie: /movies/ || fas fa-video
  友人帐: /link/ || fas fa-link
  关于我: /about/ || fa fa-user
  
# Enable / Disable menu icons / item badges.    
menu_settings:
  icons: true       # 是否显示各个页面的图标
  badges: true      # 是否显示分类/标签/归档页的内容量
```

#### 生成菜单栏关键页面

进入 Hexo 博客的根目录，右键`Bash`：

##### 标签页

```bash
hexo new page tags
```

打开 `source/tags/index.md` 文件，修改如下：

```markdown
---
title: 标签
date: 2023-05-13 21:03:07
type: "tags"
---
```

**给文章添加"tags"属性**

打开需要添加标签的文章，为其添加`tags`属性。下方的`tags: - Hexo - Github`
就是这篇文章的多个标签。

```
---
title: Hexo&Github搭建个人博客
date: 2023-05-12 20:46:38
tags: 
- Hexo
- Github
---
```

至此，成功给文章添加标签，点击首页的“标签”可以看到该标签下的所有文章。当然，只有添加了`tags: xxx`的文章才会被收录到首页的“标签”中。

##### 分类页

```bash
hexo new page categories
```

打开 `source/categories/index.md 文件`，修改如下： 

```
---
title: 分类
date: 2023-05-13 21:03:22
type: "categories"
---
```

**给文章添加分类"categories"属性**

打开需要添加分类的文章，为其添加`categories`属性。下方的`categories: - Blog`表示添加这篇文章到“Blog”这个分类。注意：hexo一篇文章只能属于一个分类，也就是说如果在“- Blog”下方添加了“- xxx”，hexo不会产生两个分类，而是把分类嵌套（即该文章属于 “- Blog”下的 “- xxx”分类）。

```
---
title: Hexo&Github搭建个人博客
date: 2023-05-12 20:46:38
tags: 
- Hexo
- Github
categories: 
- Blog
---
```

至此，成功给文章添加分类，点击首页的“分类”可以看到该分类下的所有文章。当然，只有添加了`categories: xxx`的文章才会被收录到首页的“分类”中。

打开博客目录下的`scaffolds/post.md`文件，在`tages:`下面加入`categories:`，保存，以后执行`hexo new "文章名"`命令生成的文件页面里就有`categories:`项了。

scaffolds目录下，是新建页面的模板，执行新建命令时，是根据这里的模板页来完成的，所以可以在这里根据你自己的需求添加一些默认值。

##### 友情链接

```
hexo new page link
```

打开 `source/link/index.md` 文件，修改如下： 

```
---
title: 友情链接
date: 2023-05-13 21:03:32
type: "link"
---
```

**添加友情链接**

在上述`index.md`文件内容下方，根据个人喜好填写其中内容：

```yml
 # 友人帐

- ## [Plucky](https://plucky923.github.io/)

![Plucky](images/index/R-C.jpg)

- ### 简介：饥饿艺术家

-----------------------------------------------------------------------------------------------------------------------------

- ## [Solar1s](https://solar1s.t0nkov.site/)

![Solar1s](images/index/android-chrome-384x384.png)

- ### 简介：A postgraduate student of School of Cyber Science and Engineering, SouthEast University in Nanjing.
```

##### 关于我

```
hexo new page about
```

打开 `source/about-me/index.md` 文件，修改如下：

```
---
title: 关于我
date: 2023-05-13 21:03:41
type: "about"
---
# 下方填写一些个人公开信息
```

>  注意：如果有启用评论，默认页面带有评论。需要关闭的话，添加字段`comments`并将值设置为false。 

### 设置阅读原文按钮

NexT主题下的首页默认是显示每一篇文章的全文的，如果文章很长就要往下拉很远才能看到下一篇文章，而我们要设置成每一篇文章只预览前5行，然后底部显示一个阅读原文的按钮，点击可以进入阅读全文。

首先安装插件，打开站点根目录，右键Bash：

```
npm install hexo-excerpt --save
```

打开**站点配置文件**`_config.yml`添加：

```
excerpt:			# 一定要顶格写，注意格式
  depth: 5			# 他的大小就是全文阅读预览长度设置
  excerpt_excludes: []
  more_excludes: []
  hideWholePostExcerpts: true
```

打开NexT主题的**主题配置文件**，即站点根目录`\themes\next\_config.yml`，搜索`excerpt_description`，然后改为true：

```
# Use `description` in front-matter to specify post excerpt.
excerpt_description: true
```

### 设置已读进度条

修改**主题配置文件**，将`reading_progress` 的`enable`设置为`true`即可，位置颜色和高度都可以自行调整。

### 边角的 GitHub banner

在**主题配置文件**中修改 `github_banner` 字段：

```
github_banner:
  enable: true
  permalink: https://github.com/你的用户名
```

### 设置头像

编辑**主题配置文件**，修改字段`avatar`，头像图片放在 `/themes/source/images/` 中，其中可以设置头像的地址 ，头像的形状，以及旋转动画：

```
avatar:
  url: #/images/avatar.jpeg   #图片的位置，也可以是http://xxx.com/avatar.png
  rounded: true               #头像框为圆形
  rotated: true				 #头像随光标旋转
```



## github备份本地文件

### 本地博客站点备份

因为站点实际上是部署在本地的，现在在 GitHub 上只有一些静态文件，一旦本地文件丢失或者损坏，就要重新搭建网站，甚至文章也会丢失，为了在这种情况发生的情况下能够快速恢复本地站点，可以在 GitHub 上新建分支，用于备份本地站点文件。

> **注：**该部分根据个人需要自行选择。除用作备份，还可解决多个PC设备间站点同步问题，如实现办公和个人电脑间站点的同步。

之前我们的本地站点文件夹为 `Blog` ，在其他合适的位置新建文件夹 `Hexo`，将GitHub远程仓库复制到本地，右键启用`Git Bash Here`：

```bash
git clone 你的仓库地址 Hexo 
```

删除除了版本控制 `.git` 之外的所有文件

```bash
cd Hexo && rm -r *
```

将 `Blog` 文件夹下的所有文件复制到 `Hexo` 文件夹

如果使用的主题是从Github克隆的，那么手动或者使用命令删除它的Git文件（以next主题为例），否则无法将主题文件`push`

```bash
rm -r themes/next/.git
```

### github配置

创建新分支 `hexo`

```bash
git checkout -b hexo
```

推送到`hexo`分支

```bash
git add . # 保存到暂存区
git commit -m "Hexo branch" # 提交信息为hexo分支
git push --set-upstream origin hexo # 设置为上游分支
```

那么到此原来的 `Blog` 文件夹就可以删除了，当然也可以作为本地备份。

### 博客站点及备份更新

#### 博客站点更新

更新到 `master/main` 分支

```bash
hexo g -d # 生成并部署失败则反复hexo d即可
```

#### 博客备份更新

备份到 `hexo` 分支，更新远程仓库的本地备份

```bash
git add . 
git commit -m "提交信息" 
git push
```

