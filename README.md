# Viewpoint
首届社交群体智能算法大赛赛题二

以下指南将帮助你在本地机器上安装和运行该项目，进行开发和测试。

# 安装要求
python 3.9

cuda 11.7

cuDNN 8.9

torch 2.0.1+cu117

tensorflow 2.10.0


# 安装步骤
导入项目，安装依赖包，requirements.txt在根目录下

# 测试
1、进入 applications/tasks/text_classification目录下 

2、使用命令 python run_trainer.py --param_path ./examples/cls_ernie_fc_ch.json 进行训练模型 配置文件地址applications/tasks/text_classificatio/examples/cls_ernie_fc_ch.json

3、使用命令 python ./run_infer.py  --param_path ./examples/cls_ernie_fc_ch_infer.json 进行预测 配置文件地址在applications/tasks/text_classificatio/examples/cls_ernie_fc_ch_infer.json

预测结果： applications/tasks/text_classification/output/predict_result.txt 

4、运行applications/tasks/text_classification目录下的utils.py，得到output目录下的predict_result_label.json即为test_label.json文件
