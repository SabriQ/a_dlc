import deeplabcut

print(">>>>>>>")
print("0-1 if you want to training start from the breakpoint of last training ,please change 'init_weight' in pose_config.yaml in cluster dlc-model")
print("1-2 attention to the 'config_path' please ")
print("2-2 attention to the 'gputouse' please ")
print("<<<<<<<")


config_path = r'/gpfsdata/home/sqiu/job/dlc/miniscope_fear-CHS-2019-09-26/config.yaml'

deeplabcut.train_network(config_path,shuffle=1,trainingsetindex=0,gputouse=2,max_snapshots_to_keep=5,autotune=False,displayiters=100,saveiters=1000,maxiters=1000000)
deeplabcut.evaluate_network(config_path,plotting=True)

