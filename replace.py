import os
import glob
import re

dir_path = r'c:\Users\user\Documents\GitHub\HTC'
html_files = glob.glob(os.path.join(dir_path, '*.html'))

replacements = {
    '株式会社ネットメディアクリエーション': '株式会社HTコネクション',
    'Net Media Creation': 'HT Connection',
    'NET MEDIA CREATION': 'HT CONNECTION',
    'ネットメディアクリエーション': 'HTコネクション',
    '〒150-0031 東京都渋谷区桜丘町15-14 フジビル40-7F': '【本社】〒150-0031 東京都渋谷区桜丘町15-14 フジビル40 7階 2<br>【支社】〒150-0013 東京都渋谷区恵比寿1-5-9 SG恵比寿ビル 5F',
    'from-blue-600 to-cyan-400': 'from-slate-700 to-slate-400',
    'from-blue-600 to-cyan-500': 'from-slate-800 to-slate-500',
    'text-blue-600': 'text-slate-700',
    'bg-blue-600': 'bg-slate-700',
    'hover:text-blue-600': 'hover:text-slate-800',
    'hover:border-blue-300': 'hover:border-slate-300',
    'shadow-blue-200': 'shadow-slate-200',
    '!text-cyan-400': '!text-slate-500',
    'text-blue-400': 'text-slate-600',
    'text-blue-500': 'text-slate-500',
    'bg-blue-500/20': 'bg-slate-200',
    'bg-orange-500/20': 'bg-slate-200',
    'text-orange-400': 'text-slate-600',
    'bg-cyan-500/20': 'bg-slate-200',
    'text-cyan-400': 'text-slate-600',
    'bg-purple-500/20': 'bg-slate-200',
    'text-purple-400': 'text-slate-600',
    '#00d1ff 0%, #007bff 100%': '#f8fafc 0%, #cbd5e1 100%',
    '#1e293b, #007bff': '#1e293b, #64748b',
    '#007bff': '#475569'
}

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for old, new in replacements.items():
        content = content.replace(old, new)
        
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print('Replacements complete.')
