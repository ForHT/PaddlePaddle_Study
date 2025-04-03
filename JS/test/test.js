// 导入net模块
const net = require('net');

// 创建TCP服务器
const server = net.createServer((socket) => {
    console.log('客户端已连接');

    // 监听数据事件
    socket.on('data', (data) => {
        console.log(`接收到数据: ${data.toString()}`);
        
        // 发送响应给客户端
        socket.write('Hello, Client!');
    });

    // 监听客户端关闭事件
    socket.on('end', () => {
        console.log('客户端已断开连接');
    });

    // 监听错误事件
    socket.on('error', (err) => {
        console.error(`发生错误: ${err.message}`);
    });
});

// 服务器监听指定端口
const PORT = 12345;
server.listen(PORT, () => {
    console.log(`TCP服务器正在监听端口 ${PORT}...`);
});
