import deeplabcut

config_path = r'C:\gpfsdata\home\sqiu\job\dlc\ephy_bi_avi-Qs-2019-05-09\config.yaml'

if config_path:
    deeplabcut.extract_frames(config_path,'automatic','uniform')
else:
    print('config_path does not exist.')
    sys.exit()

deeplabcut.label_frames(config_path)

deeplabcut.check_labels(config_path)

#then transfer to cluster
print(">>>>>>>")
print("1-2 remember change the path way of 'config_path' of dlc-cluster-03-create_dataset-and-training.py in cluster")
print("2-2 remember to change the 'projection_path' in config.yaml of clucter")
print("<<<<<<<")
