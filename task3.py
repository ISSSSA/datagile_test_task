import os
import shutil
from pathlib import Path


class ZipCronFiles:
    source_dir = Path('etc')
    backup_dir = Path('etc/bkp')

    def __init__(self):
        print(self.source_dir)
        print(self.backup_dir)
        print(os.listdir(self.source_dir))
        self.dirs_to_archive = [d for d in os.listdir(self.source_dir) if
                                os.path.isdir(os.path.join(self.source_dir, d))
                                and d.startswith('cron.')]

    def zip(self) -> None:
        print(self.dirs_to_archive)
        for directory in self.dirs_to_archive:
            source_path = os.path.join(self.source_dir, directory)
            archive_name = f'{directory}'
            backup_path = os.path.join(self.backup_dir, archive_name)
            shutil.make_archive(backup_path, 'gztar', source_path)

            print(f'Директория {source_path} успешно архивирована в {backup_path}')


if __name__ == '__main__':
    zipApp = ZipCronFiles()
    zipApp.zip()
