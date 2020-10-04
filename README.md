# 一、情况说明
本仓库是从`alexbers/mtprotoproxy fork`来的，本人不懂源码相关知识，也只是通过搜索和尝试，后面经过验证可行的，才放到这里，方便使用，所以本人做不到`源码方面`的更新。

我都做了哪些修改？
- 增加了从`nginx:stable`官方镜像里压缩`/etc/nginx/*`整个目录得到的配置文件
- 修改了`nginx.conf`主配置文件
- 修改了`docker-compose.yml`文件，增加了对`nginx:stable`的引用
- 修改了`config.py`，默认设置开启`proxy protocol`，默认设置伪装域名`www.cloudflare.com`

# 二、使用方法
## 2.1 安装docker和docker-compose
请确保你已经安装好了`docker`和`docker-compose`，这里不再展开说明
## 2.2 安装git
以debian10为例，以root用户执行下面命令：
    
    apt update && apt -y install git vim
    
## 2.3 克隆仓库
    
    git clone https://github.com/bishiping/mtprotoproxy.git
    
## 2.4 修改config.py配置文件
仔细观察作者写的`Dockerfile`后会发现：这个`config.py`文件会被拷贝到容器内部，且将来执行`mtprotoproxy.py`脚本时也会用到，所以，它是会影响你之后本地构建得到的镜像的内容，所以，在构建镜像前，我们可以修改此文件，构建完成后，就不要再去修改它了，如果实在想修改，你可以先把构建得到的镜像删除，再执行`docker-compose up -d`命令，它会基于此文件重新构建镜像，并以`docker-compose.yml`内规定的方式启动创建好的镜像为容器。
关于`config.py`要修改的内容：

- 端口号，建议不修改，因为在`docker-compose.yml`文件中，`mtproxy`程序被设置为仅本机（nginx）可访问
- 密码：这个建议修改，改几个字符就行，保证一共32位
- TLS_DOMAIN：伪装域名，建议使用开启了tls1.3的域名，如果你要修改，除了这个还要去修改`./nginx/nginx.conf`主配置文件，把里面的`www.cloudflare.com`也替换为你要修改的域名。

## 2.5 一键启动
回到`docker-compose.yml`文件所在的目录下，执行下面命令：
    
    docker-compose up -d //它会根据.yml文件先构建镜像，然后使用构建好的镜像启动，后面也会自动启动nginx
    
    docker-compose logs //查看链接，拷贝下来，注意把里面的端口号改成443
    
    docker-compose down //停止并移除此容器组
    
## 三、其它
关于此仓库，个人只做了配置文件方面的修改，方便使用， `http://ip:443` 和 `http://ip:80` 都会跳到nginx默认欢迎页，这个没有修改。
