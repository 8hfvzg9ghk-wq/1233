const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

// 创建dist目录
const distDir = path.join(__dirname, 'dist');
if (!fs.existsSync(distDir)) {
  fs.mkdirSync(distDir, { recursive: true });
  console.log('创建dist目录成功');
}

// 复制HTML文件
const htmlFiles = fs.readdirSync(__dirname).filter(file => file.endsWith('.html'));
htmlFiles.forEach(file => {
  const source = path.join(__dirname, file);
  const destination = path.join(distDir, file);
  fs.copyFileSync(source, destination);
  console.log(`复制 ${file} 到 dist`);
});

// 复制JS文件
const jsFiles = fs.readdirSync(__dirname).filter(file => file.endsWith('.js'));
jsFiles.forEach(file => {
  const source = path.join(__dirname, file);
  const destination = path.join(distDir, file);
  fs.copyFileSync(source, destination);
  console.log(`复制 ${file} 到 dist`);
});

// 复制CSS文件（如果有）
const cssFiles = fs.readdirSync(__dirname).filter(file => file.endsWith('.css'));
cssFiles.forEach(file => {
  const source = path.join(__dirname, file);
  const destination = path.join(distDir, file);
  fs.copyFileSync(source, destination);
  console.log(`复制 ${file} 到 dist`);
});

// 复制resources目录
const resourcesDir = path.join(__dirname, 'resources');
const distResourcesDir = path.join(distDir, 'resources');
if (fs.existsSync(resourcesDir)) {
  copyDirectory(resourcesDir, distResourcesDir);
  console.log('复制resources目录到dist');
}

console.log('构建完成！');

// 递归复制目录函数
function copyDirectory(source, destination) {
  if (!fs.existsSync(destination)) {
    fs.mkdirSync(destination, { recursive: true });
  }
  
  const files = fs.readdirSync(source);
  files.forEach(file => {
    const sourcePath = path.join(source, file);
    const destinationPath = path.join(destination, file);
    
    if (fs.lstatSync(sourcePath).isDirectory()) {
      copyDirectory(sourcePath, destinationPath);
    } else {
      fs.copyFileSync(sourcePath, destinationPath);
    }
  });
}