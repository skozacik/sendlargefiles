from librar import archive
import sys
import os
def makeArchive(archname,base,password,filename):
    a = archive.Archive(archname,base)
    a.add_file(os.path.abspath(filename))
    a.set_volume_size("25m")
    if password:
        a.set_password(password)
    a.set_exclude_base_dir(True)
    res = a.run(silent=False)
    return res

