# --expdir (-p)			实验保存地址
# --mode (-m) 			运行模式 train/evaluate/inference
# --downstream (-d) 	下游任务recipe名称 详见s3prl/downstream
# --upstream (-u)		上游预训练模型 详见s3prl/upstream

# --config (-c)			配置文件(.yaml) 默认为downstream/your_downstream_recipe/config.yaml
# --past_exp (-e) 		从断点开始训练 path/to/your/experiment/directory 或 path/to/your/checkpoint.ckpt
# --init_ckpt (-i)		从断点开始评估 path/to/your/checkpoint.ckpt
# --hub 				model hub torch/huggingface
# --expname (-n)		实验名称
# --auto_resume (-a)	是否总是从实验目录自动恢复断点
# --cache_dir			下载文件缓存地址
# --verbose				是否打印模型信息
# --upstream_trainable  预训练模型是否参与参数联调
# --upstream_layer_selection 预训练模型中参与加权求和计算特征向量的层 默认所有层都是用

prepare: # 生成IEMOCAP_full_release/meta_data/
	python prepare.py
	python IEMOCAP_preprocess.py /home/zzf/dataset/IEMOCAP_full_release

ser_wavlm:
	cd ../.. && CUDA_VISIBLE_DEVICES=0 python run_downstream.py \
		--expdir /home/zzf/experiment-s3prl/ser_wavlm_dev \
		--cache_dir /home/zzf/pretrained/s3prl/wavlm \
		--mode train \
		--upstream wavlm \
		--downstream emotion \
		--config ./downstream/emotion/config.yaml

ser_wavlm-eval:
	cd ../.. && CUDA_VISIBLE_DEVICES=0 python run_downstream.py \
		--expdir /home/zzf/experiment-s3prl/ic_wavlm_dev \
		--cache_dir /home/zzf/pretrained/s3prl/wavlm \
		--mode evaluate \
		--upstream wavlm \
		--downstream fluent_commands \
		--config ./downstream/fluent_commands/config.yaml \
		--past_exp /home/zzf/experiment-s3prl/ic_wavlm_dev/dev-best.ckpt