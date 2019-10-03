import deeplabcut
import glob

import concurrent.futures

print(">>>>>>>")
print("1-2 attention to the 'config_path' please ")
print("2-2 attention to the 'glob.glob()' please ")
print("<<<<<<<")

config_path = r'/gpfsdata/home/sqiu/job/dlc/Novel-Qs-2019-04-29/config.yaml'
videolists = glob.glob("/gpfsdata/home/sqiu/data/video/novel_context/20180514/asf/*asf")[2:4]
print(videolists)
deeplabcut.extract_outlier_frames(config_path,videolists,automatic=True)


#def task(videolist):
#    return deeplabcut.extract_outlier_frames(config_path,videolist,automatic=True)


#with concurrent.futures.ProcessPoolExecutor() as executor:
#    for i,_ in enumerate(executor.map(task,videolists[0:6]),1):
#        print (f'{i}/{len(videolists)} is done')

print("added video path also added to config.yaml")




