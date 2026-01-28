# 哈基米AI聊天助手

这是一个具有哈基米风格UI的AI聊天应用，集成了智普LLM API。

## 功能特点

- 可爱的哈基米风格界面设计
- 流畅的动画和交互效果
- 集成智普LLM API进行智能对话
- 响应式设计，支持移动端
- 实时消息发送和接收
- 优雅的加载动画

## 如何使用

### 方法1：直接打开HTML文件

最简单的方法是直接在浏览器中打开`index.html`文件：

1. 找到`index.html`文件
2. 双击打开或右键选择使用浏览器打开

### 方法2：使用本地服务器

如果需要通过HTTP服务器访问（避免CORS问题），可以使用以下方法：

#### 使用Python

```bash
# Python 3
python -m http.server 8000

# 然后在浏览器中访问 http://localhost:8000
```

#### 使用Node.js

```bash
# 首先安装http-server
npm install -g http-server

# 然后运行
http-server -p 8000

# 然后在浏览器中访问 http://localhost:8000
```

## API说明

该应用使用智普LLM API进行对话生成。API密钥已内置在代码中：

- API密钥：75fddfa21a4e494bb489e6c91f43b8b2.txl11HJlz46p3oKz
- 模型：chatglm_lite_3

## 技术栈

- HTML5
- CSS3 (包含动画和渐变)
- JavaScript (原生，无需额外依赖)
- 智普LLM API

## 注意事项

1. 由于浏览器的跨域安全策略，直接打开HTML文件可能无法正常调用API。建议使用本地服务器方式访问。
2. API密钥为示例密钥，请根据实际情况替换为您自己的有效密钥。
3. 为了获得最佳体验，建议使用现代浏览器如Chrome、Firefox、Safari等。

## 自定义

您可以通过修改以下部分来自定义应用：

- 哈基米风格颜色：修改CSS中的渐变和颜色值
- 背景动画：调整CSS中的`@keyframes`动画
- API配置：在JavaScript部分修改API URL和参数
- 系统提示词：修改发送给API的system message

## 许可证

MIT