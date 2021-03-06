# -*- coding: utf-8 -*-
'''
Created on 2017年3月26日

@author: houguangdong
'''

# Docker 安装 PHP
# 安装 PHP 镜像
# 方法一、通过 Dockerfile 构建
# 创建Dockerfile
# 首先，创建目录php-fpm,用于存放后面的相关东西。
# runoob@runoob:~$ mkdir -p ~/php-fpm/logs ~/php-fpm/conf
# logs目录将映射为php-fpm容器的日志目录
# conf目录里的配置文件将映射为php-fpm容器的配置文件
# 进入创建的php-fpm目录，创建Dockerfile
# FROM debian:jessie
# 
# # persistent / runtime deps
# ENV PHPIZE_DEPS \
#         autoconf \
#         file \
#         g++ \
#         gcc \
#         libc-dev \
#         make \
#         pkg-config \
#         re2c
# RUN apt-get update && apt-get install -y \
#         $PHPIZE_DEPS \
#         ca-certificates \
#         curl \
#         libedit2 \
#         libsqlite3-0 \
#         libxml2 \
#     --no-install-recommends && rm -r /var/lib/apt/lists/*
# 
# ENV PHP_INI_DIR /usr/local/etc/php
# RUN mkdir -p $PHP_INI_DIR/conf.d
# 
# ##<autogenerated>##
# ENV PHP_EXTRA_CONFIGURE_ARGS --enable-fpm --with-fpm-user=www-data --with-fpm-group=www-data
# ##</autogenerated>##
# 
# ENV GPG_KEYS 0BD78B5F97500D450838F95DFE857D9A90D90EC1 6E4F6AB321FDC07F2C332E3AC2BF0BC433CFC8B3
# 
# ENV PHP_VERSION 5.6.22
# ENV PHP_FILENAME php-5.6.22.tar.xz
# ENV PHP_SHA256 c96980d7de1d66c821a4ee5809df0076f925b2fe0b8c362d234d92f2f0a178e2
# 
# RUN set -xe \
#     && buildDeps=" \
#         $PHP_EXTRA_BUILD_DEPS \
#         libcurl4-openssl-dev \
#         libedit-dev \
#         libsqlite3-dev \
#         libssl-dev \
#         libxml2-dev \
#         xz-utils \
#     " \
#     && apt-get update && apt-get install -y $buildDeps --no-install-recommends && rm -rf /var/lib/apt/lists/* \
#     && curl -fSL "http://php.net/get/$PHP_FILENAME/from/this/mirror" -o "$PHP_FILENAME" \
#     && echo "$PHP_SHA256 *$PHP_FILENAME" | sha256sum -c - \
#     && curl -fSL "http://php.net/get/$PHP_FILENAME.asc/from/this/mirror" -o "$PHP_FILENAME.asc" \
#     && export GNUPGHOME="$(mktemp -d)" \
#     && for key in $GPG_KEYS; do \
#         gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \
#     done \
#     && gpg --batch --verify "$PHP_FILENAME.asc" "$PHP_FILENAME" \
#     && rm -r "$GNUPGHOME" "$PHP_FILENAME.asc" \
#     && mkdir -p /usr/src/php \
#     && tar -xf "$PHP_FILENAME" -C /usr/src/php --strip-components=1 \
#     && rm "$PHP_FILENAME" \
#     && cd /usr/src/php \
#     && ./configure \
#         --with-config-file-path="$PHP_INI_DIR" \
#         --with-config-file-scan-dir="$PHP_INI_DIR/conf.d" \
#         $PHP_EXTRA_CONFIGURE_ARGS \
#         --disable-cgi \
# # --enable-mysqlnd is included here because it's harder to compile after the fact than extensions are (since it's a plugin for several extensions, not an extension in itself)
#         --enable-mysqlnd \
# # --enable-mbstring is included here because otherwise there's no way to get pecl to use it properly (see https://github.com/docker-library/php/issues/195)
#         --enable-mbstring \
#         --with-curl \
#         --with-libedit \
#         --with-openssl \
#         --with-zlib \
#     && make -j"$(nproc)" \
#     && make install \
#     && { find /usr/local/bin /usr/local/sbin -type f -executable -exec strip --strip-all '{}' + || true; } \
#     && make clean \
#     && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false -o APT::AutoRemove::SuggestsImportant=false $buildDeps
# 
# COPY docker-php-ext-* /usr/local/bin/
# 
# ##<autogenerated>##
# WORKDIR /var/www/html
# 
# RUN set -ex \
#     && cd /usr/local/etc \
#     && if [ -d php-fpm.d ]; then \
#         # for some reason, upstream's php-fpm.conf.default has "include=NONE/etc/php-fpm.d/*.conf"
#         sed 's!=NONE/!=!g' php-fpm.conf.default | tee php-fpm.conf > /dev/null; \
#         cp php-fpm.d/www.conf.default php-fpm.d/www.conf; \
#     else \
#         # PHP 5.x don't use "include=" by default, so we'll create our own simple config that mimics PHP 7+ for consistency
#         mkdir php-fpm.d; \
#         cp php-fpm.conf.default php-fpm.d/www.conf; \
#         { \
#             echo '[global]'; \
#             echo 'include=etc/php-fpm.d/*.conf'; \
#         } | tee php-fpm.conf; \
#     fi \
#     && { \
#         echo '[global]'; \
#         echo 'error_log = /proc/self/fd/2'; \
#         echo; \
#         echo '[www]'; \
#         echo '; if we send this to /proc/self/fd/1, it never appears'; \
#         echo 'access.log = /proc/self/fd/2'; \
#         echo; \
#         echo 'clear_env = no'; \
#         echo; \
#         echo '; Ensure worker stdout and stderr are sent to the main error log.'; \
#         echo 'catch_workers_output = yes'; \
#     } | tee php-fpm.d/docker.conf \
#     && { \
#         echo '[global]'; \
#         echo 'daemonize = no'; \
#         echo; \
#         echo '[www]'; \
#         echo 'listen = [::]:9000'; \
#     } | tee php-fpm.d/zz-docker.conf
# 
# EXPOSE 9000
# CMD ["php-fpm"]
# 通过Dockerfile创建一个镜像，替换成你自己的名字
# runoob@runoob:~/php-fpm$ docker build -t php:5.6-fpm .
# 创建完成后，我们可以在本地的镜像列表里查找到刚刚创建的镜像
# runoob@runoob:~/php-fpm$ docker images
# REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
# php                 5.6-fpm             025041cd3aa5        6 days ago          456.3 MB
# 方法二、docker pull php
# 查找Docker Hub上的php镜像
# runoob@runoob:~/php-fpm$ docker search php
# NAME                      DESCRIPTION                                     STARS     OFFICIAL   AUTOMATED
# php                       While designed for web development, the PH...   1232      [OK]       
# richarvey/nginx-php-fpm   Container running Nginx + PHP-FPM capable ...   207                  [OK]
# phpmyadmin/phpmyadmin     A web interface for MySQL and MariaDB.          123                  [OK]
# eboraas/apache-php        PHP5 on Apache (with SSL support), built o...   69                   [OK]
# php-zendserver            Zend Server - the integrated PHP applicati...   69        [OK]       
# million12/nginx-php       Nginx + PHP-FPM 5.5, 5.6, 7.0 (NG), CentOS...   67                   [OK]
# webdevops/php-nginx       Nginx with PHP-FPM                              39                   [OK]
# webdevops/php-apache      Apache with PHP-FPM (based on webdevops/php)    14                   [OK]
# phpunit/phpunit           PHPUnit is a programmer-oriented testing f...   14                   [OK]
# tetraweb/php              PHP 5.3, 5.4, 5.5, 5.6, 7.0 for CI and run...   12                   [OK]
# webdevops/php             PHP (FPM and CLI) service container             10                   [OK]
# ...
# 这里我们拉取官方的镜像,标签为5.6-fpm
# runoob@runoob:~/php-fpm$ docker pull php:5.6-fpm
# 等待下载完成后，我们就可以在本地镜像列表里查到REPOSITORY为php,标签为5.6-fpm的镜像。
# 使用php-fpm镜像
# 运行容器
# runoob@runoob:~/php-fpm$ docker run -p 9000:9000 --name  myphp-fpm -v ~/nginx/www:/www -v $PWD/conf:/usr/local/etc/php -v $PWD/logs:/phplogs   -d php:5.6-fpm
# 00c5aa4c2f93ec3486936f45b5f2b450187a9d09acb18f5ac9aa7a5f405dbedf
# runoob@runoob:~/php-fpm$ 
# 命令说明:
# -p 9000:9000 :将容器的9000端口映射到主机的9000端口
# --name myphp-fpm :将容器命名为myphp-fpm
# -v ~/nginx/www:/www :将主机中项目的目录www挂载到容器的/www
# -v $PWD/conf:/usr/local/etc/php ：将主机中当前目录下的conf目录挂载到容器的/usr/local/etc/php
# -v $PWD/logs:/phplogs ：将主机中当前目录下的logs目录挂载到容器的/phplogs
# 查看容器启动情况
# runoob@runoob:~/php-fpm$ docker ps
# CONTAINER ID    IMAGE         COMMAND      ...    PORTS                    NAMES
# 00c5aa4c2f93    php:5.6-fpm   "php-fpm"    ...    0.0.0.0:9000->9000/tcp   myphp-fpm 通过浏览器访问phpinfo()
# 
# PS:此处是通过nginx+php实现web服务，nginx配置文件的fastcgi_pass应该配置为myphp-fpm容器的IP。
# fastcgi_pass  172.17.0.4:9000;
# 容器IP的查方法
# docker inspect 容器ID或容器名 |grep '"IPAddress"'