import deeplabcut
import glob

print(">>>>>>>")
print("1-2 attention to the 'config_path' please ")
print("2-2 attention to the 'glob.glob()' please ")
print("<<<<<<<")

videolists = glob.glob("/gpfsdata/home/sqiu/data/video/#M028/20181102/*asf")

config_path = r'/gpfsdata/home/sqiu/job/dlc/ephy_bi_asf-Qs-2019-05-08/config.yaml'


deeplabcut.analyze_videos(config_path,videolists,shuffle=1,save_as_csv=True,videotype=".AVI")
deeplabcut.plot_trajectories(config_path,videolists)
deeplabcut.create_labeled_video(config_path,videolists)