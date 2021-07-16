# QBot  ![build](https://github.com/linyuan0213/qbot/actions/workflows/docker-image.yml/badge.svg)   [![Codacy Badge](https://api.codacy.com/project/badge/Grade/9d770ff883e94d5190f3ff57c7f29c8e)](https://app.codacy.com/gh/linyuan0213/qbot?utm_source=github.com&utm_medium=referral&utm_content=linyuan0213/qbot&utm_campaign=Badge_Grade_Settings)

<div align=center><img src="https://minio.xcreal.site:443/blog//2021/7/15/logo_transparent.png" alt="logo_transparent" width="300" height="300" alien /></div>

使用 QBot 可以通过 Telegram Bot 轻松下载和管理 Qbittorrent，通过发送文件或者链接即可下载对应资源

### 安装

为了使用 Qbot 需要安装相关依赖，并且启用 QBittorrent web UI，只支持python3

```sh
pip install -r requirements.txt
```

### 配置

编辑 config.yaml，配置 QBittorrent 的用户名、密码和Telegram Bot token，最后需要通过设置环境变量来获取配置文件路径：

```sh
export QB_CONF=/path/to/config.yaml
```

### 启动

```sh
python app.py
```

### 通过 docker 安装

```sh
docker run -e "QB_CONF=/etc/qbot/config.yaml" -v /path/to/config.yaml:/etc/qbot/config.yaml --name qbot linyuan0213/qbot:latest
```

### 通过 docker-compose 安装

编辑 **docker-compose.yaml** 文件，然后再执行 **docker-compose up -d** 
