import re
import base64
import os

# 定义要提取的图片类型和对应的文件名
image_map = {
    'serviceTitle': '服务类型图标.png',
    'passTitle': '通行证类型图标.png',
    'numberTitle': '编号图标.png',
    'clockTitle': '时间图标.png',
    'progress li:not(:last-child)': '箭头图标.png'
}

# 读取HTML文件内容
html_path = os.path.join('f:', '999', '进出校通行证2.html')
try:
    with open(html_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
    print(f'成功读取HTML文件: {html_path}')
except Exception as e:
    print(f'读取HTML文件失败: {e}')
    exit(1)

# 提取每个图片的base64编码并保存
for selector, filename in image_map.items():
    # 构建正则表达式以匹配特定选择器的background属性
    if selector == 'progress li:not(:last-child)':
        pattern = r'progress li:not\(:last-child\)\s*\{[^}]*background:\s*url\(data:image/png;base64,([^\)]+)\)'
    else:
        pattern = r'\.' + selector + r'\s*\{[^}]*background:\s*url\(data:image/png;base64,([^\)]+)\)'
    
    # 搜索匹配项
    match = re.search(pattern, html_content)
    if match:
        base64_data = match.group(1)
        # 解码base64数据
        try:
            image_data = base64.b64decode(base64_data)
            # 保存图片
            image_path = os.path.join('f:', '999', filename)
            with open(image_path, 'wb') as img_file:
                img_file.write(image_data)
            print(f'已保存图片: {filename}')
        except Exception as e:
            print(f'保存图片 {filename} 失败: {e}')
    else:
        print(f'未找到 {selector} 对应的图片')

print('图片提取完成!')