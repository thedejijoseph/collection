# file manager script
# liase with the file system for changes
# in a directory

import os
import time
import uuid
import hashlib

class Listener:
    def __init__(self, dirpath):
        self.dirpath = dirpath

    def listen(self):
        t0 = os.path.getmtime(self.dirpath)

        while True:
            t1 = os.path.getmtime(self.dirpath)
            if t1 > t0:
                # notify for modification
                print("modified")
                t0 = t1
    
    def notify(self, message):
        pass

class Watcher:
    def __init__(self, path_to_dir):
        # provide a path to dir to be watched
        
        self.path = os.path.abspath(path_to_dir)
        if not os.path.isdir(self.path):
            # throw an error
            print(f"dir does not exist: {self.path}")
            return
        
        self.dir = os.path.dirname(self.path)
        self.filepaths = self._filepaths()
        self.files = self._filenames()
        self.tree = {}
        self.logfile = os.path.join(self.path, "watch.log")
    
    def _filepaths(self):
        filepaths = []
        sptd_exts = [".py", ".mp4"]
        
        os.chdir(self.path)
        for dirpt, _, files in os.walk("."):
            for file in files:
                filepath = os.path.join(dirpt, file)
                filepaths.append(filepath)

        sptd_files = []
        for filepath in filepaths:
            ext = os.path.splitext(filepath)[1]
            if ext in sptd_exts:
                sptd_files.append(filepath)

        return sptd_files
    
    def _filenames(self):
        filepaths = self.filepaths
        filenames = [os.path.basename(path) for path in filepaths]
        return filenames
    
    def build_tree(self):
        for filepath in self.filepaths:
            filename = os.path.basename(filepath)
            filepath = filepath
            uid = str(uuid.uuid4())[:8]
            content = hashlib.sha1(open(filepath).read().encode()).hexdigest()
            ctime = os.path.getctime(filepath)
            mtime = os.path.getmtime(filepath)
            
            with open(self.logfile, "w") as f:
                entry = f"{uid}, {filename}, {filepath}, {content}, {ctime}, {mtime}"
                f.write(entry + "\n")

def levenshteinDistance(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    distances = range(len(s1) + 1)
    for i2, c2 in enumerate(s2):
        distances_ = [i2+1]
        for i1, c1 in enumerate(s1):
            if c1 == c2:
                distances_.append(distances[i1])
            else:
                distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
        distances = distances_
    return distances[-1]

def lvdiff(s1, s2):
	return levenshteinDistance(s1, s2)

def diff(s1, s2):
	edit = lvdiff(s1, s2)
	rt = edit / len(s1)
	return "{0:.3f}".format(rt)

def sim(s1, s2):
	diff_ = diff(s1, s2)
	if diff_ > 1.0:
		diff_ = 1.0
	sim = 1.0 - diff_
	return "{0:.2f}".format(sim)


def watch(path_to_dir):
	return Watcher(path_to_dir)
