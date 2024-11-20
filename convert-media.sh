#!/bin/bash

# 循环遍历当前目录及子目录下的所有Markdown文件
for file in **/*.md; do
    # 提取文件的目录和基本名称
    directory=$(dirname "$file")
    filename=$(basename "$file")
    output_file="$directory/$filename"

    # 执行pandoc命令，并将结果保存回原始文件
    pandoc --wrap=preserve -f markdown "$file" --extract-media="media" -t markdown-raw_attribute -o "$output_file"
done
