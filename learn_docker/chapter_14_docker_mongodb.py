# -*- coding: utf-8 -*-
'''
Created on 2017年3月26日

@author: houguangdong
'''
# Docker 安装 MongoDB
# 方法一、通过 Dockerfile 构建
# 创建Dockerfile
# 首先，创建目录mongo,用于存放后面的相关东西。
# runoob@runoob:~$ mkdir -p ~/mongo  ~/mongo/db
# db目录将映射为mongo容器配置的/data/db目录,作为mongo数据的存储目录
# 进入创建的mongo目录，创建Dockerfile
# FROM debian:wheezy
# 
# # add our user and group first to make sure their IDs get assigned consistently, regardless of whatever dependencies get added
# RUN groupadd -r mongodb && useradd -r -g mongodb mongodb
# 
# RUN apt-get update \
#     && apt-get install -y --no-install-recommends \
#         numactl \
#     && rm -rf /var/lib/apt/lists/*
# 
# # grab gosu for easy step-down from root
# ENV GOSU_VERSION 1.7
# RUN set -x \
#     && apt-get update && apt-get install -y --no-install-recommends ca-certificates wget && rm -rf /var/lib/apt/lists/* \
#     && wget -O /usr/local/bin/gosu "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg --print-architecture)" \
#     && wget -O /usr/local/bin/gosu.asc "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg --print-architecture).asc" \
#     && export GNUPGHOME="$(mktemp -d)" \
#     && gpg --keyserver ha.pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4 \
#     && gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \
#     && rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \
#     && chmod +x /usr/local/bin/gosu \
#     && gosu nobody true \
#     && apt-get purge -y --auto-remove ca-certificates wget
# 
# # gpg: key 7F0CEB10: public key "Richard Kreuter <richard@10gen.com>" imported
# RUN apt-key adv --keyserver ha.pool.sks-keyservers.net --recv-keys 492EAFE8CD016A07919F1D2B9ECBEC467F0CEB10
# 
# ENV MONGO_MAJOR 3.0
# ENV MONGO_VERSION 3.0.12
# 
# RUN echo "deb http://repo.mongodb.org/apt/debian wheezy/mongodb-org/$MONGO_MAJOR main" > /etc/apt/sources.list.d/mongodb-org.list
# 
# RUN set -x \
#     && apt-get update \
#     && apt-get install -y \
#         mongodb-org=$MONGO_VERSION \
#         mongodb-org-server=$MONGO_VERSION \
#         mongodb-org-shell=$MONGO_VERSION \
#         mongodb-org-mongos=$MONGO_VERSION \
#         mongodb-org-tools=$MONGO_VERSION \
#     && rm -rf /var/lib/apt/lists/* \
#     && rm -rf /var/lib/mongodb \
#     && mv /etc/mongod.conf /etc/mongod.conf.orig
# 
# RUN mkdir -p /data/db /data/configdb \
#     && chown -R mongodb:mongodb /data/db /data/configdb
# VOLUME /data/db /data/configdb
# 
# COPY docker-entrypoint.sh /entrypoint.sh
# ENTRYPOINT ["/entrypoint.sh"]
# 
# EXPOSE 27017
# CMD ["mongod"]
# 通过Dockerfile创建一个镜像，替换成你自己的名字
# runoob@runoob:~/mongo$ docker build -t mongo:3.2 .
# 创建完成后，我们可以在本地的镜像列表里查找到刚刚创建的镜像
# runoob@runoob:~/mongo$ docker images  mongo:3.2
# REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
# mongo               3.2                 282fd552add6        9 days ago          336.1 MB
# 方法二、docker pull mongo:3.2
# 查找Docker Hub上的mongo镜像
# runoob@runoob:~/mongo$ docker search mongo
# NAME                              DESCRIPTION                      STARS     OFFICIAL   AUTOMATED
# mongo                             MongoDB document databases ...   1989      [OK]       
# mongo-express                     Web-based MongoDB admin int...   22        [OK]       
# mvertes/alpine-mongo              light MongoDB container          19                   [OK]
# mongooseim/mongooseim-docker      MongooseIM server the lates...   9                    [OK]
# torusware/speedus-mongo           Always updated official Mon...   9                    [OK]
# jacksoncage/mongo                 Instant MongoDB sharded cluster  6                    [OK]
# mongoclient/mongoclient           Official docker image for M...   4                    [OK]
# jadsonlourenco/mongo-rocks        Percona Mongodb with Rocksd...   4                    [OK]
# asteris/apache-php-mongo          Apache2.4 + PHP + Mongo + m...   2                    [OK]
# 19hz/mongo-container              Mongodb replicaset for coreos    1                    [OK]
# nitra/mongo                       Mongo3 centos7                   1                    [OK]
# ackee/mongo                       MongoDB with fixed Bluemix p...  1                    [OK]
# kobotoolbox/mongo                 https://github.com/kobotoolb...  1                    [OK]
# valtlfelipe/mongo                 Docker Image based on the la...  1                    [OK]
# 这里我们拉取官方的镜像,标签为3.2
# runoob@runoob:~/mongo$ docker pull mongo:3.2
# 等待下载完成后，我们就可以在本地镜像列表里查到REPOSITORY为mongo,标签为3.2的镜像。
# 使用mongo镜像
# 运行容器
# runoob@runoob:~/mongo$ docker run -p 27017:27017 -v $PWD/db:/data/db -d mongo:3.2
# cda8830cad5fe35e9c4aed037bbd5434b69b19bf2075c8626911e6ebb08cad51
# runoob@runoob:~/mongo$
# 命令说明：
# -p 27017:27017 :将容器的27017 端口映射到主机的27017 端口
# -v $PWD/db:/data/db :将主机中当前目录下的db挂载到容器的/data/db，作为mongo数据存储目录
# 查看容器启动情况
# runoob@runoob:~/mongo$ docker ps 
# CONTAINER ID   IMAGE        COMMAND                   ...    PORTS                      NAMES
# cda8830cad5f   mongo:3.2    "/entrypoint.sh mongo"    ...    0.0.0.0:27017->27017/tcp   suspicious_goodall
# 使用mongo镜像执行mongo 命令连接到刚启动的容器,主机IP为172.17.0.1
# runoob@runoob:~/mongo$ docker run -it mongo:3.2 mongo --host 172.17.0.1
# MongoDB shell version: 3.2.7
# connecting to: 172.17.0.1:27017/test
# Welcome to the MongoDB shell.
# For interactive help, type "help".
# For more comprehensive documentation, see
#   http://docs.mongodb.org/
# Questions? Try the support group
#   http://groups.google.com/group/mongodb-user
# >