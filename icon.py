import win32api
import win32con
import codecs
import os
from PIL import Image

def transform_icon(file_path,out_path,size=(256,256)):
    jpg_image = Image.open(file_path)
    ico_image = jpg_image.resize(size)
    ico_image.save(out_path, format="ICO", quality=95, optimize=True)

def set_icon(folder_path,icon_path="icon.ico"):
    ini_str = f'''[.ShellClassInfo]\r\n
IconResource={icon_path},0\r\n
[ViewState]\r\n
Mode=\r\n
Vid=\r\n
FolderType=Pictures\r\n'''
    try:
        win32api.SetFileAttributes(os.path.join(folder_path, icon_path),
                                   win32con.FILE_ATTRIBUTE_HIDDEN + win32con.FILE_ATTRIBUTE_SYSTEM)
        desktop_ini = os.path.join(folder_path, "desktop.ini")
        if os.path.exists(desktop_ini):
            os.remove(desktop_ini)
        f = codecs.open(desktop_ini, 'w', 'utf-8')
        f.write(ini_str)
        f.close()
        win32api.SetFileAttributes(desktop_ini, win32con.FILE_ATTRIBUTE_HIDDEN + win32con.FILE_ATTRIBUTE_SYSTEM)
        win32api.SetFileAttributes(folder_path, win32con.FILE_ATTRIBUTE_READONLY)
        return True
    except:
        return False
    
