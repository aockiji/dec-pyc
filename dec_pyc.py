import os
import subprocess

def decompile_pyc_files(source_dir, dest_dir):
    if not os.path.isdir(source_dir):
        print(f"Source directory '{source_dir}' does not exist.")
        return
    os.makedirs(dest_dir, exist_ok = True)
    for root, _, files in os.walk(source_dir):
        print(" ")
        print(f"Processing directory: {root}")
        rel_path = os.path.relpath(root, source_dir) 
        curr_dir = dest_dir
        if rel_path != ".":
            curr_dir = os.path.join(dest_dir, rel_path)
            os.makedirs(curr_dir, exist_ok = True)
        for file in files:
            if file.endswith('.pyc'):
                src_file = os.path.join(root, file)
                subprocess.run(['uncompyle6', '-o', curr_dir, src_file])
                print(f"Decompiled {src_file} to {curr_dir}")