import deeplabcut


print(">>>>>>>")
print("1-1 move config.yaml from cluster to local ")
print("<<<<<<<")

config_path = r'/gpfsdata/home/sqiu/job/dlc/ephy_bi_asf-Qs-2019-05-08/config.yaml'
videolists = glob.glob("/gpfsdata/home/sqiu/data/video/#M028/20181102/*asf")
deeplabcut.extrat_outlier_frames(config_path,videolists,videotype='.asf',outlieralgorithm='fitting',automatic=True)
#deeplabcut.extrat_outlier_frames(config_path,videolists,videotype='.asf',outlieralgorithm='jump',automatic=True)
#deeplabcut.extrat_outlier_frames(config_path,videolists,videotype='.asf',outlieralgorithm='uncertain',automatic=True)
#deeplabcut.refine_labels(config_path)
#deeplabcut.merge_datasets(config_path)


print("the next step is create_training_dataset again")




