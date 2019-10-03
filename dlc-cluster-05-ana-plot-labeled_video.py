import deeplabcut
import glob
import sys
print(">>>>>>>")
print("1-2 attention to the 'config_path' please ")
print("2-2 attention to the 'glob.glob()' please ")
print("<<<<<<<")
import concurrent.futures
#videolists = glob.glob("/gpfsdata/home/sqiu/data/video/novel_context/20180704/asf/*asf")
#videolists = glob.glob("/gpfsdata/home/sqiu/data/video/novel_context/20180706_chs/asf/*asf")
videolists = glob.glob("/gpfsdata/home/sqiu/data/video/stage_1_training/*/*.mp4")
if len(videolists) ==0:
	print("there is no video selected")
	sys.exit()
else:
	print(videolists)

config_path = r'/gpfsdata/home/sqiu/job/dlc/linear_track_40cm-QS-2019-09-06/config.yaml'

def task(gpuNo):
    deeplabcut.analyze_videos(config_path,videolists,shuffle=1,save_as_csv=True,videotype=".mp4",gputouse=gpuNo)


with concurrent.futures.ProcessPoolExecutor() as executor:
    for i,_ in enumerate(executor.map(task,[0,1,2]),1):
        print (i,len(videolists))
#deeplabcut.analyze_videos(config_path,videolists,shuffle=1,save_as_csv=True,videotype=".mp4",gputouse=0)
deeplabcut.plot_trajectories(config_path,videolists)
deeplabcut.create_labeled_video(config_path,videolists)
