# 04_Codec_编解码器

## 学习目标
- 理解编解码器的作用
- 掌握ByteToMessageDecoder
- 掌握MessageToByteEncoder
- 理解内置编解码器
- 学会自定义编解码器

## 关键要点
### 1. 编解码器概述
- 编码和解码
- ChannelInboundHandler
- ChannelOutboundHandler
- 组合使用

### 2. 解码器
- ByteToMessageDecoder
- decode()方法
- decodeLast()方法
- Cumulator

### 3. 编码器
- MessageToByteEncoder
- encode()方法
- 类型参数
- 自动释放

### 4. 内置编解码器
- StringDecoder/StringEncoder
- LineBasedFrameDecoder
- DelimiterBasedFrameDecoder
- FixedLengthFrameDecoder
- LengthFieldBasedFrameDecoder
- LengthFieldPrepender
- ProtobufDecoder/ProtobufEncoder

### 5. 自定义编解码器
- 继承ByteToMessageDecoder
- 实现decode()
- 处理半包
- 处理粘包

### 6. 编解码器组合
- CombinedChannelDuplexHandler
- Codec
- 多个编解码器顺序

## 实践任务
1. 使用内置编解码器
2. 实现自定义编解码器
3. 解决粘包拆包问题
4. 使用编解码器组合

## 参考资料
- Netty Codec
