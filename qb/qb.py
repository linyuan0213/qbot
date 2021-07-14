import logging

from qbittorrentapi import Client
from qbittorrentapi import LoginFailed


logger = logging.getLogger(__name__)


class QClient:

    def __init__(self, host, username, passwd):

        self.qb = Client(host=host, username=username, password=passwd)

        try:
            self.qb.auth_log_in()
        except LoginFailed:
            logger.debug('Login failed!')

    def get_all_torrents(self):
        torrents = self.qb.torrents_info()
        return torrents

    def get_downloading_torrents(self):
        torrents = self.get_all_torrents()
        torrent_list = list()
        for torrent in torrents:
            if torrent.state_enum.is_downloading:
                torrent_list.append(torrent)

    def get_completed_torrents(self):
        torrents = self.get_all_torrents()
        torrent_list = list()
        for torrent in torrents:
            if torrent.state_enum.is_complete:
                torrent_list.append(torrent)
        return torrent_list

    def get_paused_torrents(self):
        torrents = self.get_all_torrents()
        torrent_list = list()
        for torrent in torrents:
            if torrent.state_enum.is_paused:
                torrent_list.append(torrent)
        return torrent_list

    def add_link(self, link, save_path=None, category=None, is_paused=True):
        return self.qb.torrents_add(urls=link,
                                    save_path=save_path,
                                    category=category,
                                    is_paused=is_paused,
                                    use_auto_torrent_management=False
                                    )

    def add_torrent(self, file_name, save_path=None,
                    category=None, is_paused=True):

        try:
            with open(file=file_name, mode='rb') as torrent_file:
                return self.qb.torrents_add(torrent_files=torrent_file,
                                            save_path=save_path,
                                            category=category,
                                            is_paused=is_paused,
                                            use_auto_torrent_management=False) 
        except FileNotFoundError:
            logger.debug('Torrent file not found')
            return

    def pause_all(self):
        self.qb.torrents_pause(torrent_hashes='all')

    def resume_all(self):
        self.qb.torrents_resume(torrent_hashes='all')
