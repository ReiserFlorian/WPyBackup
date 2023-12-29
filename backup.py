#!/usr/bin/python
import etc

class Backup(etc.WPyBackupBase):
    pass

if __name__ == '__main__':
    backup = Backup()
    backup.checkCursors()
    if backup.checkMode():
        exit(0)