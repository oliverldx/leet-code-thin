import os
import re
import sys

def filter_code_blocks(input_dir_path, output_dir_path, languages_to_remove):
    # 正则表达式匹配代码块
    code_block_pattern = re.compile(r'^```[^`]*\n(.*?)```', re.DOTALL | re.MULTILINE)
    
    # 构建正则表达式来匹配要删除的代码块
    languages_pattern = '|'.join(languages_to_remove.split(','))
    languages_code_block_pattern = re.compile(rf'^```(?P<lang>{languages_pattern})\n(.*?)```', re.DOTALL | re.MULTILINE | re.IGNORECASE)

    # 确保输出目录存在
    if not os.path.exists(output_dir_path):
        os.makedirs(output_dir_path)

    # 遍历输入目录下的所有文件
    for filename in os.listdir(input_dir_path):
        if filename.endswith('.md'):
            input_file_path = os.path.join(input_dir_path, filename)
            output_file_path = os.path.join(output_dir_path, filename.replace('.md', '.md'))

            with open(input_file_path, 'r', encoding='utf-8') as file:
                markdown_content = file.read()

            # 删除指定的代码块
            new_content = languages_code_block_pattern.sub('', markdown_content)

            # 写入新的Markdown文件
            with open(output_file_path, 'w', encoding='utf-8') as output_file:
                output_file.write(new_content)
                print(f'Processed {filename} and saved to {output_file_path}')

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python filter_code_blocks.py <input_directory> <output_directory> <languages_to_remove>")
        sys.exit(1)

    input_dir_path = sys.argv[1]
    output_dir_path = sys.argv[2]
    languages_to_remove = sys.argv[3]

    filter_code_blocks(input_dir_path, output_dir_path, languages_to_remove)
