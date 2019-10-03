import deeplabcut
import glob


wd = r'C:\gpfsdata\home\sqiu\job\dlc'
videolists = glob.glob(r'C:\gpfsdata\home\sqiu\job\dlc\0725\*.avi')

config_path = deeplabcut.create_new_project('innate','wdy',videolists,wd,copy_videos=False,videotype='.avi')
print(">>>>>>>>>>")

print("remember change the marker name and dotsize")

print(">>>>>>>>>>")
