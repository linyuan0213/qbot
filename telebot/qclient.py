from config.config import conf
from qb.qb import QClient

host = conf.get_conf()['qbittorrent']['host']
username = conf.get_conf()['qbittorrent']['username']
passwd = conf.get_conf()['qbittorrent']['passwd']

qclient = QClient(host=host, username=username, passwd=passwd)