#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
PDF用户手册生成脚本
使用pdfkit库将HTML转换为PDF
"""

import os
import sys
import subprocess

def check_dependencies():
    """检查依赖项是否安装"""
    try:
        # 尝试导入pdfkit
        import pdfkit
        print("✓ pdfkit库已安装")
        return True
    except ImportError:
        print("✗ pdfkit库未安装，正在尝试安装...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "pdfkit"])
            print("✓ pdfkit库安装成功")
            return True
        except Exception as e:
            print(f"✗ 安装pdfkit失败: {e}")
            return False

def check_wkhtmltopdf():
    """检查wkhtmltopdf是否安装"""
    try:
        # 尝试获取wkhtmltopdf版本
        result = subprocess.run(["wkhtmltopdf", "--version"], capture_output=True, text=True)
        if result.returncode == 0:
            print("✓ wkhtmltopdf已安装")
            return True
        else:
            return False
    except FileNotFoundError:
        print("✗ wkhtmltopdf未找到，请先安装wkhtmltopdf")
        print("下载地址: https://wkhtmltopdf.org/downloads.html")
        return False

def generate_pdf():
    """生成PDF文件"""
    try:
        # 导入pdfkit
        import pdfkit
        
        # HTML文件路径
        html_file = "user_manual.html"
        
        # 检查HTML文件是否存在
        if not os.path.exists(html_file):
            print(f"✗ 错误: {html_file} 文件不存在")
            return False
        
        # PDF输出文件路径
        pdf_file = "哈基米番茄钟与闹钟用户手册.pdf"
        
        # 转换选项
        options = {
            'page-size': 'A4',
            'margin-top': '15mm',
            'margin-right': '15mm',
            'margin-bottom': '15mm',
            'margin-left': '15mm',
            'encoding': "UTF-8",
            'no-outline': None,
            'quiet': '',
            'title': '哈基米番茄钟与闹钟用户手册'
        }
        
        print(f"正在从 {html_file} 生成 {pdf_file}...")
        
        # 执行转换
        pdfkit.from_file(html_file, pdf_file, options=options)
        
        print(f"✓ PDF生成成功: {os.path.abspath(pdf_file)}")
        return True
        
    except Exception as e:
        print(f"✗ PDF生成失败: {e}")
        return False

def alternative_method():
    """提供备选方案"""
    print("\n===== 备选PDF生成方法 =====")
    print("方法1: 使用浏览器打印功能")
    print("  1. 在浏览器中打开 user_manual.html")
    print("  2. 按下 Ctrl+P (Windows/Linux) 或 Cmd+P (Mac)")
    print("  3. 在打印对话框中选择 '保存为PDF'")
    print("  4. 选择保存位置并点击 '保存'")
    print()
    print("方法2: 使用在线HTML到PDF转换工具")
    print("  可以使用以下网站进行转换:")
    print("  - https://html2pdf.com/")
    print("  - https://www.sejda.com/html-to-pdf")
    print("  - https://pdfforge.org/pdfcreator-online")

if __name__ == "__main__":
    print("======== 哈基米番茄钟与闹钟用户手册生成器 ========")
    print()
    
    # 首先尝试Python方法
    if check_dependencies() and check_wkhtmltopdf():
        success = generate_pdf()
        if not success:
            alternative_method()
    else:
        alternative_method()
    
    print()
    print("================= 操作完成 =================")