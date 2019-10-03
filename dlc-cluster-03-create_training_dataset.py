print("remember 'export DLClight=True'")
import deeplabcut

print(">>>>>>>")
print("0-2 remember change the path way of 'config_path' of dlc-cluster-03-create_dataset-and-training.py in cluster")
print("0-2 remember to change the 'projection_path' in config.yaml of clucter")
print("<<<<<<<")

config_path = r'/gpfsdata/home/sqiu/job/dlc/miniscope_fear-CHS-2019-09-26/config.yaml'

#deeplabcut.create_training_dataset(config_path,num_shuffles=1,windows2linux=False) 

deeplabcut.create_training_dataset(config_path,num_shuffles=1) 


print(">>>>>>>")
print("1-1 if you want to training start from the breakpoint of last training ,please change 'init_weight' in pose_config.yaml in cluster dlc-model")
print("<<<<<<<")

