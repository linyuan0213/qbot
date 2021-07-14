import logging

from qbittorrentapi import Client
from qbittorrentapi import LoginFailed


logger = logging.getLogger(__name__)

class QClient:

    def __init__(self, host, username, passwd):

        self.qb = Client(host=host, username=username, password=passwd)

        try:    
            self.qb.auth_log_in()
        except LoginFailed as e:
            logger.debug('Login failed!')



    def get_all_torrents(self):
        torrents = self.qb.torrents_info()
        return torrents

    def get_downloading_torrents(self):
        torrents = self.get_all_torrents()
        torrent_list = list()
        for torrent in torrents:
            if torrent.state_enum.is_downloading:
                torrent_list.add(torrent)

    def get_downloading_torrents(self):
        torrents = self.get_all_torrents()
        torrent_list = list()
        for torrent in torrents:
            if torrent.state_enum.is_complete:
                torrent_list.add(torrent)
        return torrent_list

    def get_paused_torrents(self):
        torrents = self.get_all_torrents()
        torrent_list = list()
        for torrent in torrents:
            if torrent.state_enum.is_complete:
                torrent_list.add(torrent)
        return torrent_list

    def add_link(self, link, save_path = None, category = None, is_paused=True):
        return self.qb.torrents_add(urls=link, save_path=save_path, category=category, is_paused=is_paused, use_auto_torrent_management=False) 

    def add_torrent(self, file_name, save_path = None, category = None, is_paused=True):

        try:
            with open(file=file_name, mode='rb') as torrent_file:
               return self.qb.torrents_add(torrent_files=torrent_file, save_path=save_path, category=category, is_paused=is_paused,  use_auto_torrent_management=False) 
        except FileNotFoundError:
            logger.debug('Torrent file not found')
            return


    def pause_all(self):
        self.qb.torrents_pause(torrent_hashes='all')

    def resume_all(self):
        self.qb.torrents_resume(torrent_hashes='all')




# magnet_link = 'magnet:?xt=urn:btih:5CCSABJXEQ3CJJ4IOV347DT6FSCQTSRV&dn=&tr=http%3A%2F%2F104.238.198.186%3A8000%2Fannounce&tr=udp%3A%2F%2F104.238.198.186%3A8000%2Fannounce&tr=http%3A%2F%2Ftracker.openbittorrent.com%3A80%2Fannounce&tr=udp%3A%2F%2Ftracker3.itzmx.com%3A6961%2Fannounce&tr=http%3A%2F%2Ftracker4.itzmx.com%3A2710%2Fannounce&tr=http%3A%2F%2Ftracker.publicbt.com%3A80%2Fannounce&tr=http%3A%2F%2Ftracker.prq.to%2Fannounce&tr=http%3A%2F%2Fopen.acgtracker.com%3A1096%2Fannounce&tr=https%3A%2F%2Ft-115.rhcloud.com%2Fonly_for_ylbud&tr=http%3A%2F%2Ftracker1.itzmx.com%3A8080%2Fannounce&tr=http%3A%2F%2Ftracker2.itzmx.com%3A6961%2Fannounce&tr=udp%3A%2F%2Ftracker1.itzmx.com%3A8080%2Fannounce&tr=udp%3A%2F%2Ftracker2.itzmx.com%3A6961%2Fannounce&tr=udp%3A%2F%2Ftracker3.itzmx.com%3A6961%2Fannounce&tr=udp%3A%2F%2Ftracker4.itzmx.com%3A2710%2Fannounce&tr=http%3A%2F%2Ftr.bangumi.moe%3A6969%2Fannounce'
# add_magnet(magnet_link=magnet_link)

# file_name = '777409a229b7277b6b6c2dba2fce8427b206499b.torrent'
# add_torrent(file_name=file_name)

# torrnets = get_downloading_torrents()
# for torrent in torrnets:
#     print(torrent['name'])