import os

def recurse_dir(cur_path):
    # 遍历目录下所有"文件(包括子目录)"
    for file in os.listdir(cur_path):
        file_path = os.path.join(cur_path, file)
        if file_path.split('/')[-1][0] == '.': # 文件匹配 => 操作
	        # 操作
            cmd = f'rm {file_path}'
            print(cmd)
            os.system(cmd)
        elif os.path.isdir(file_path): # 目录 => 递归
            recurse_dir(file_path)


recurse_dir('/home/zzf/dataset/IEMOCAP_full_release')
