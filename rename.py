#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : voiceforge
@File    : rename.py
@Author  : ying.liu
@Time    : 2026/3/13 14:45
@Desc    : 
"""

import os

folder = input("请输入需要重命名的文件夹路径: ").strip()

if not os.path.isdir(folder):
    print("路径无效")
    exit()

# 只获取 mp3 文件
files = [f for f in os.listdir(folder)
         if os.path.isfile(os.path.join(folder, f))
         and f.lower().endswith('.mp3')]

if not files:
    print("该文件夹下没有找到 mp3 文件")
    exit()

files.sort()

log = []
print("\n开始重命名：")
print("-" * 40)

for i, filename in enumerate(files, start=1):
    old_path = os.path.join(folder, filename)
    new_name = f"{i}.mp3"
    new_path = os.path.join(folder, new_name)

    # 避免重名冲突
    if old_path == new_path:
        continue

    os.rename(old_path, new_path)
    record = f"{filename}  ->  {new_name}"
    log.append(record)
    print(record)

# 输出映射表
print("-" * 40)
print(f"\n共重命名 {len(log)} 个文件")

# 保存映射表
log_file = os.path.join(folder, "rename_log.txt")
with open(log_file, "w", encoding="utf-8") as f:
    f.write("原文件名  ->  新文件名\n")
    f.write("-" * 40 + "\n")
    for line in log:
        f.write(line + "\n")

print(f"映射表已保存到：{log_file}")
