import configparser

from app.locale import LocaleManager

config = configparser.ConfigParser()
config.read('config.ini')

locale_manager = LocaleManager()

database_path = config['DATABASE']['DatabasePath']
sshfs_mount_folder = config['DATABASE']['SshfsMountPath']
system_terminal = config['SYSTEM']['Terminal']
