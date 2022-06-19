prepare:
	python scripts/LibriMix/data_prepare.py --part train-100 \
											 /home/zzf/dataset/librimix/Libri2Mix \
											 /home/zzf/dataset-s3prl/Libri2Mix
	python scripts/LibriMix/data_prepare.py --part dev \
											 /home/zzf/dataset/librimix/Libri2Mix \
											 /home/zzf/dataset-s3prl/Libri2Mix
	python scripts/LibriMix/data_prepare.py --part test \
											 /home/zzf/dataset/librimix/Libri2Mix \
											 /home/zzf/dataset-s3prl/Libri2Mix
	python scripts/LibriMix/subsample.py /home/zzf/dataset-s3prl/Libri2Mix/wav16k/min/dev \
										 /home/zzf/dataset-s3prl/Libri2Mix/wav16k/min/dev_1000

#ss-linear:

#ss-fbank:

#ss-spectrogram:

#ss-mel:

ss-wav2vec2:
	cd ../.. && CUDA_VISIBLE_DEVICES=2 python run_downstream.py \
		--expdir /home/zzf/experiment-s3prl/ss-wav2vec2 \
		--cache_dir /home/zzf/pretrained/s3prl/wav2vec2 \
		--mode train \
		--upstream wav2vec2 \
		--downstream separation_stft \
		--config ./downstream/separation_stft/configs/cfg.yaml