# Python 爬取实时变化的 WebSocket 数据

[源地址](https://juejin.im/post/5c80b768f265da2dae514d4f)

### aiowebsocket 做了什么

代码不长，使用的时候只需要将目标网站 WebSocket 地址填入，然后按照流程发送数据即可，那么 aiowebsocket 在这个过程中做了什么呢？

- 首先，aiowebsocket 根据 WebSocket 地址，向指定的服务端发送握手请求，并校验握手结果。
- 然后，在确认握手成功后，将数据发送给服务端。
- 整个过程中为了保持连接不断开，aiowebsocket 会自动与服务端响应 ping pong。
- 最后，aiowebsocket 读取服务端推送的消息



![image-20191216112426409](https://klause-blog-pictures.oss-cn-shanghai.aliyuncs.com/ipic/2019-12-16-032426.png)

![image-20191216112512020](https://klause-blog-pictures.oss-cn-shanghai.aliyuncs.com/ipic/2019-12-16-032512.png)