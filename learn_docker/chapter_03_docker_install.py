# -*- coding: utf-8 -*-
'''
Created on 2017年3月25日

@author: houguangdong
'''
# Ubuntu Docker 安装
# Docker 支持以下的 Ubuntu 版本：
# Ubuntu Precise 12.04 (LTS)
# Ubuntu Trusty 14.04 (LTS)
# Ubuntu Wily 15.10
# 其他更新的版本……
# 前提条件
# Docker 要求 Ubuntu 系统的内核版本高于 3.10 ，查看本页面的前提条件来验证你的 Ubuntu 版本是否支持 Docker。
# 通过 uname -r 命令查看你当前的内核版本
# runoob@runoob:~$ uname -r
# 
# 使用脚本安装 Docker
# 1、获取最新版本的 Docker 安装包
# runoob@runoob:~$ wget -qO- https://get.docker.com/ | sh
# 
# 输入当前用户的密码后，就会下载脚本并且安装Docker及依赖包。
# 
# 安装完成后有个提示：
#     If you would like to use Docker as a non-root user, you should now consider
#     adding your user to the "docker" group with something like:
# 
#     sudo usermod -aG docker runoob
#    Remember that you will have to log out and back in for this to take effect!  
# 当要以非root用户可以直接运行docker时，需要执行 sudo usermod -aG docker runoob 命令，然后重新登陆，否则会有如下报错
# 
# 2、启动docker 后台服务
# runoob@runoob:~$ sudo service docker start
# 
# 3、测试运行hello-world
# runoob@runoob:~$ docker run hello-world
# 
# 
# 
# 
# CentOS Docker 安装
# Docker支持以下的CentOS版本：
# CentOS 7 (64-bit)
# CentOS 6.5 (64-bit) 或更高的版本
# 前提条件
# 目前，CentOS 仅发行版本中的内核支持 Docker。
# Docker 运行在 CentOS 7 上，要求系统为64位、系统内核版本为 3.10 以上。
# Docker 运行在 CentOS-6.5 或更高的版本的 CentOS 上，要求系统为64位、系统内核版本为 2.6.32-431 或者更高版本。
# 使用 yum 安装（CentOS 7下）
# Docker 要求 CentOS 系统的内核版本高于 3.10 ，查看本页面的前提条件来验证你的CentOS 版本是否支持 Docker 。
# 通过 uname -r 命令查看你当前的内核版本
# [root@runoob ~]# uname -r 3.10.0-327.el7.x86_64
# 
# 安装 Docker
# Docker 软件包和依赖包已经包含在默认的 CentOS-Extras 软件源里，安装命令如下：
# [root@runoob ~]# yum -y install docker
# 
# 安装完成。
# 
# 启动 Docker 后台服务
# [root@runoob ~]# service docker start
# 
# 测试运行 hello-world
# [root@runoob ~]#docker run hello-world
# 
# 由于本地没有hello-world这个镜像，所以会下载一个hello-world的镜像，并在容器内运行。
# 使用脚本安装 Docker
# 1、使用 sudo 或 root 权限登录 Centos。
# 2、确保 yum 包更新到最新。
# $ sudo yum update
# 3、执行 Docker 安装脚本。
# $ curl -fsSL https://get.docker.com/ | sh
# 执行这个脚本会添加 docker.repo 源并安装 Docker。
# 4、启动 Docker 进程。
# $ sudo service docker start
# 5、验证 docker 是否安装成功并在容器中执行一个测试的镜像。
# $ sudo docker run hello-world
# 到此，docker 在 CentOS 系统的安装完成。
# 
# 
# Windows Docker 安装
# Docker 引擎使用的是 Linux 内核特性，所以我们需要在 Windows 上使用一个轻量级的虚拟机 (VM) 来运行 Docker。
# 我们通过 Boot2Docker 来安装虚拟机和运行 Docker
# 安装
# 1、安装Boot2Docker 
# 最新版 Boot2Docker 下载地址： https://github.com/boot2docker/windows-installer/releases/latest
# 目前最新版为v1.8.0, 下载地址为： https://github.com/boot2docker/windows-installer/releases/download/v1.8.0/docker-install.exe
# 2、运行安装文件
# 运行安装文件，它将会安装 virtualbox、MSYS-git boot2docker Linux 镜像和 Boot2Docker 的管理工具。
# 
# 接着连续点击"Next"，进到如下界面
# 
# 点击"Install"开始安装。
# 
# 安装完成。
# 
# 从桌面上或者 Program Files 中运行 Boot2Docker Start。
# Boot2Docker Start 将启动一个 Unix shell 来配置和管理运行在虚拟主机中的 Docker，我们可以通过运行 docker version 来查看它是否正常工作。
# 
# 运行 Docker
# 使用boot2docker.exe ssh 连接到虚拟主机上，然后执行docker run hello-world
# 
# 
# 到此，docker在Windows系统的安装完成。