import os
import shutil
import time

class Organizer:
    def __init__(self, pathway):
        self.pathway = os.path.expanduser(pathway)

        if not os.path.isdir(self.pathway):
            raise NotADirectoryError(f"Invalid path: {self.pathway}")

        if not self.file_names():
            raise FileNotFoundError("No files found in the specified directory.")

    def list_all(self):
        return [name for name in os.listdir(self.pathway)]

    def list_dir(self):
        return [name for name in os.listdir(self.pathway)
                if os.path.isfile(os.path.join(self.pathway, name))]

    def list_dir_folders(self):
        return [name for name in os.listdir(self.pathway)
                if os.path.isdir(os.path.join(self.pathway, name))]

    def folder_names(self):
        extensions = set()
        for name in self.file_names():
            ext = os.path.splitext(name)[1].lstrip('.')
            if ext:
                extensions.add(ext)
        return list(extensions)

    def file_names(self):
        return self.list_dir()

    def folder_creation(self):
        for ext in self.folder_names():
            folder_path = os.path.join(self.pathway, ext)
            if not os.path.exists(folder_path):
                os.mkdir(folder_path)

    def files_move(self):
        ext_to_folder = {
            ext: os.path.join(self.pathway, ext)
            for ext in self.folder_names()
        }
        for name in self.file_names():
            ext = os.path.splitext(name)[1].lstrip('.')
            if ext in ext_to_folder:
                src = os.path.join(self.pathway, name)
                dst = os.path.join(ext_to_folder[ext], name)
                shutil.move(src, dst)

    def detect_and_move(self, ext):
        ext = ext.lstrip('.')
        target_folder = os.path.join(self.pathway, ext)
        os.makedirs(target_folder, exist_ok=True)
        for name in self.file_names():
            if os.path.splitext(name)[1].lstrip('.') == ext:
                src = os.path.join(self.pathway, name)
                dst = os.path.join(target_folder, name)
                shutil.move(src, dst)

    def find_large(self, size_mb):
        large_files = []
        for name in self.file_names():
            full_path = os.path.join(self.pathway, name)
            size = os.stat(full_path).st_size / (1024 * 1024)
            if size > size_mb:
                large_files.append((name, round(size, 2)))
        return large_files

    def sort_by_size(self):
        return sorted(
            self.file_names(),
            key=lambda x: os.path.getsize(os.path.join(self.pathway, x)),
            reverse=True
        )

    def get_file_info(self, name):
        full_path = os.path.join(self.pathway, name)
        stat = os.stat(full_path)
        return {
            "name": name,
            "size_mb": round(stat.st_size / (1024 * 1024), 2),
            "modified": time.ctime(stat.st_mtime),
            "created": time.ctime(stat.st_ctime),
            "permissions": oct(stat.st_mode)[-3:]
        }

    def modified_after(self, days):
        cutoff_time = time.time() - (days * 86400)
        recent_files = []
        for name in self.list_dir():
            full_path = os.path.join(self.pathway, name)
            mod_time = os.stat(full_path).st_mtime
            if mod_time >= cutoff_time:
                recent_files.append((
                    name,
                    time.ctime(mod_time),
                    round(os.stat(full_path).st_size / (1024 * 1024), 2)
                ))
        return recent_files
