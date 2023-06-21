

python BatchPreprocess_1.py

sleep 20

python BatchPreprocess_2.py

sleep 20

python BatchVoxelization.py

sleep 20

# 这条命令先不要运行,先直接运行下一个命令,看看是否可以运行起来,是否却文件.
# 我要确定一件事情,因为这个文件大多数都是为了可视化,但是没保存东西
python Match.py 

sleep 20 

python PoseEstimation.py 