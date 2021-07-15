# QBot   <img src="https://img.shields.io/docker/automated/linyuan0213/qbot?style=plastic" alt="https://img.shields.io/docker/automated/linyuan0213/qbot?style=plastic"  />
<img src="https://minio.xcreal.site:443/blog//2021/7/15/logo_transparent.png" alt="logo_transparent" style="zoom:15%;" align=center />

使用 QBot 可以通过 Telegram Bot 轻松下载和管理 Qbittorrent，通过发送文件或者链接即可下载对应资源

手动安装

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

