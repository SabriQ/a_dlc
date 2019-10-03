import deeplabcut
import glob

print(">>>>>>>")
print("1-2 attention to the 'config_path' please ")
print("2-2 attention to the 'glob.glob()' please ")
print("<<<<<<<")

config_path = r'/gpfsdata/home/sqiu/job/dlc/ephy_bi_asf-Qs-2019-05-08/config.yaml'
videolists = glob.glob("/gpfsdata/home/sqiu/data/video/#M028/20181102/*asf")
deeplabcut.extrat_outlier_frames(config_path,videolists)



