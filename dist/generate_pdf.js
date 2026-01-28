// 生成PDF用户手册的脚本
// 使用html2pdf.js库将HTML转换为PDF

const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

console.log('开始生成PDF用户手册...');

try {
    // 读取HTML文件内容
    const htmlPath = path.join(__dirname, 'user_manual.html');
    let htmlContent = fs.readFileSync(htmlPath, 'utf8');
    
    // 添加html2pdf.js库的引用
    const html2pdfScript = `
    <script src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js"></script>
    <script>
        window.onload = function() {
            const element = document.body;
            const opt = {
                margin: 10,
                filename: 'hagimi_user_manual.pdf',
                image: { type: 'jpeg', quality: 0.98 },
                html2canvas: { scale: 2 },
                jsPDF: { unit: 'mm', format: 'a4', orientation: 'portrait' }
            };
            
            html2pdf().set(opt).from(element).save();
            console.log('PDF生成成功');
        };
    </script>`;
    
    // 将脚本添加到HTML文件末尾
    htmlContent = htmlContent.replace('</body>', html2pdfScript + '</body>');
    
    // 保存修改后的HTML文件
    const tempHtmlPath = path.join(__dirname, 'user_manual_pdf.html');
    fs.writeFileSync(tempHtmlPath, htmlContent);
    
    console.log('已准备好转换HTML到PDF的临时文件');
    console.log('请在浏览器中打开以下文件并等待PDF自动下载：');
    console.log(tempHtmlPath);
    
    // 创建一个简单的HTML启动器，自动打开临时文件并执行转换
    const launcherHtml = `
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <meta charset="UTF-8">
        <title>生成PDF中...</title>
        <style>
            body {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                font-family: Arial, sans-serif;
                background-color: #f0f0f0;
            }
            .container {
                text-align: center;
                padding: 40px;
                background: white;
                border-radius: 10px;
                box-shadow: 0 0 20px rgba(0,0,0,0.1);
            }
            button {
                padding: 10px 20px;
                font-size: 16px;
                background-color: #4ecdc4;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                margin-top: 20px;
            }
            button:hover {
                background-color: #3dbdb6;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h2>正在准备生成PDF用户手册</h2>
            <p>请点击下方按钮在浏览器中打开转换页面</p>
            <p>PDF文件将自动开始下载</p>
            <button onclick="window.open('user_manual_pdf.html')">打开转换页面</button>
            <button onclick="window.close()" style="background-color: #ff6b6b; margin-left: 10px;">关闭</button>
        </div>
    </body>
    </html>`;
    
    const launcherPath = path.join(__dirname, 'pdf_launcher.html');
    fs.writeFileSync(launcherPath, launcherHtml);
    
    console.log('也可以打开以下启动器页面获取更友好的体验：');
    console.log(launcherPath);
    
    console.log('\n注意：由于浏览器安全限制，自动PDF生成需要在浏览器环境中运行。');
    console.log('请在浏览器中打开上述文件之一，PDF将自动下载到您的默认下载文件夹。');
    
} catch (error) {
    console.error('生成PDF过程中发生错误：', error);
    console.log('\n备选方案：');
    console.log('1. 直接在浏览器中打开 user_manual.html');
    console.log('2. 使用浏览器的打印功能 (Ctrl+P 或 Cmd+P)');
    console.log('3. 在打印对话框中选择 "保存为PDF" 选项');
    console.log('4. 选择保存位置并确认');
}