import deeplabcut
import glob


wd = r'C:\gpfsdata\home\sqiu\job\dlc'
videolists = glob.glob(r'Y:\wujinni\MINIscope\RAW_DATA\CTX_CFC_6mice\M181078_DPCA1\20190404_shock\H1_M2_S14\*2.avi')

config_path = deeplabcut.create_new_project('miniscope','yqx',videolists,wd,copy_videos=False,videotype='.avi')
print(">>>>>>>>>>")

print("remember change the marker name and dotsize")

print(">>>>>>>>>>")
