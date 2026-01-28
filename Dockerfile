# 使用官方Nginx镜像作为基础
FROM nginx:alpine

# 维护者信息
LABEL maintainer="Hakimi Pomodoro App"

# 复制项目文件到Nginx的默认静态文件目录
COPY . /usr/share/nginx/html

# 复制自定义Nginx配置文件（可选）
COPY nginx.conf /etc/nginx/conf.d/default.conf

# 暴露80端口
EXPOSE 80

# 启动Nginx服务
CMD ["nginx", "-g", "daemon off;"]