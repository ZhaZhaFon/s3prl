install: # 去掉了setup.py中fairseq和lighthubert部分 若使用lighthubert另外安装即可
	cd .. && git clone git@github.com:facebookresearch/fairseq.git
	cd fairseq && pip install -e .
	cd ../s3prl && pip install -e ./
	pip install --force-reinstall pandas

	