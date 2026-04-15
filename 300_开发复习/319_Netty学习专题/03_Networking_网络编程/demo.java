package com.example.netty.networking;

import io.netty.bootstrap.Bootstrap;
import io.netty.bootstrap.ServerBootstrap;
import io.netty.buffer.ByteBuf;
import io.netty.buffer.Unpooled;
import io.netty.channel.*;
import io.netty.channel.nio.NioEventLoopGroup;
import io.netty.channel.socket.SocketChannel;
import io.netty.channel.socket.nio.NioServerSocketChannel;
import io.netty.channel.socket.nio.NioSocketChannel;
import io.netty.handler.codec.*;
import io.netty.handler.timeout.IdleState;
import io.netty.handler.timeout.IdleStateEvent;
import io.netty.handler.timeout.IdleStateHandler;
import io.netty.util.CharsetUtil;

import java.net.InetSocketAddress;
import java.nio.charset.StandardCharsets;
import java.util.concurrent.TimeUnit;

public class NetworkingDemo {

    public static void main(String[] args) {
        System.out.println("=== Netty网络编程示例 ===");

        try {
            tcpServerDemo();
            tcpClientDemo();
            codecDemo();
            heartbeatDemo();
            reconnectionDemo();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void tcpServerDemo() {
        System.out.println("\n--- 1. TCP服务端 ---");

        System.out.println("TCP服务端示例代码:");
        System.out.println("EventLoopGroup bossGroup = new NioEventLoopGroup(1);");
        System.out.println("EventLoopGroup workerGroup = new NioEventLoopGroup();");
        System.out.println("try {");
        System.out.println("    ServerBootstrap bootstrap = new ServerBootstrap();");
        System.out.println("    bootstrap.group(bossGroup, workerGroup)");
        System.out.println("             .channel(NioServerSocketChannel.class)");
        System.out.println("             .option(ChannelOption.SO_BACKLOG, 1024)");
        System.out.println("             .childOption(ChannelOption.SO_KEEPALIVE, true)");
        System.out.println("             .childHandler(new ChannelInitializer<SocketChannel>() {");
        System.out.println("                 @Override");
        System.out.println("                 protected void initChannel(SocketChannel ch) {");
        System.out.println("                     ch.pipeline().addLast(new StringDecoder(StandardCharsets.UTF_8));");
        System.out.println("                     ch.pipeline().addLast(new StringEncoder(StandardCharsets.UTF_8));");
        System.out.println("                     ch.pipeline().addLast(new SimpleChannelInboundHandler<String>() {");
        System.out.println("                         @Override");
        System.out.println("                         protected void channelRead0(ChannelHandlerContext ctx, String msg) {");
        System.out.println("                             System.out.println(\"收到客户端消息: \" + msg);");
        System.out.println("                             ctx.writeAndFlush(\"服务端收到: \" + msg);");
        System.out.println("                         }");
        System.out.println("                         @Override");
        System.out.println("                         public void channelActive(ChannelHandlerContext ctx) {");
        System.out.println("                             System.out.println(\"客户端连接: \" + ctx.channel().remoteAddress());");
        System.out.println("                         }");
        System.out.println("                         @Override");
        System.out.println("                         public void channelInactive(ChannelHandlerContext ctx) {");
        System.out.println("                             System.out.println(\"客户端断开: \" + ctx.channel().remoteAddress());");
        System.out.println("                         }");
        System.out.println("                         @Override");
        System.out.println("                         public void exceptionCaught(ChannelHandlerContext ctx, Throwable cause) {");
        System.out.println("                             cause.printStackTrace();");
        System.out.println("                             ctx.close();");
        System.out.println("                         }");
        System.out.println("                     });");
        System.out.println("                 }");
        System.out.println("             });");
        System.out.println("    ChannelFuture future = bootstrap.bind(8080).sync();");
        System.out.println("    System.out.println(\"服务端启动成功，监听端口: 8080\");");
        System.out.println("    future.channel().closeFuture().sync();");
        System.out.println("} finally {");
        System.out.println("    bossGroup.shutdownGracefully();");
        System.out.println("    workerGroup.shutdownGracefully();");
        System.out.println("}");

        System.out.println("\n服务端关键方法:");
        System.out.println("  - bind(): 绑定端口");
        System.out.println("  - channelActive(): 连接建立");
        System.out.println("  - channelRead(): 读取数据");
        System.out.println("  - channelInactive(): 连接断开");
        System.out.println("  - exceptionCaught(): 异常处理");
    }

    private static void tcpClientDemo() {
        System.out.println("\n--- 2. TCP客户端 ---");

        System.out.println("TCP客户端示例代码:");
        System.out.println("EventLoopGroup group = new NioEventLoopGroup();");
        System.out.println("try {");
        System.out.println("    Bootstrap bootstrap = new Bootstrap();");
        System.out.println("    bootstrap.group(group)");
        System.out.println("             .channel(NioSocketChannel.class)");
        System.out.println("             .option(ChannelOption.CONNECT_TIMEOUT_MILLIS, 5000)");
        System.out.println("             .handler(new ChannelInitializer<SocketChannel>() {");
        System.out.println("                 @Override");
        System.out.println("                 protected void initChannel(SocketChannel ch) {");
        System.out.println("                     ch.pipeline().addLast(new StringDecoder(StandardCharsets.UTF_8));");
        System.out.println("                     ch.pipeline().addLast(new StringEncoder(StandardCharsets.UTF_8));");
        System.out.println("                     ch.pipeline().addLast(new SimpleChannelInboundHandler<String>() {");
        System.out.println("                         @Override");
        System.out.println("                         protected void channelRead0(ChannelHandlerContext ctx, String msg) {");
        System.out.println("                             System.out.println(\"收到服务端消息: \" + msg);");
        System.out.println("                         }");
        System.out.println("                         @Override");
        System.out.println("                         public void channelActive(ChannelHandlerContext ctx) {");
        System.out.println("                             System.out.println(\"连接服务端成功\");");
        System.out.println("                             ctx.writeAndFlush(\"Hello Server!\");");
        System.out.println("                         }");
        System.out.println("                         @Override");
        System.out.println("                         public void exceptionCaught(ChannelHandlerContext ctx, Throwable cause) {");
        System.out.println("                             cause.printStackTrace();");
        System.out.println("                             ctx.close();");
        System.out.println("                         }");
        System.out.println("                     });");
        System.out.println("                 }");
        System.out.println("             });");
        System.out.println("    ChannelFuture future = bootstrap.connect(\"localhost\", 8080).sync();");
        System.out.println("    future.channel().closeFuture().sync();");
        System.out.println("} finally {");
        System.out.println("    group.shutdownGracefully();");
        System.out.println("}");

        System.out.println("\n客户端关键方法:");
        System.out.println("  - connect(): 连接服务端");
        System.out.println("  - channelActive(): 连接建立");
        System.out.println("  - channelRead(): 读取数据");
        System.out.println("  - writeAndFlush(): 发送数据");
    }

    private static void codecDemo() {
        System.out.println("\n--- 3. 编解码器 ---");

        System.out.println("常用编解码器:");
        System.out.println("  - StringDecoder/StringEncoder: 字符串编解码");
        System.out.println("  - LineBasedFrameDecoder: 按行分割");
        System.out.println("  - DelimiterBasedFrameDecoder: 按分隔符分割");
        System.out.println("  - FixedLengthFrameDecoder: 固定长度");
        System.out.println("  - LengthFieldBasedFrameDecoder: 基于长度字段");
        System.out.println("  - ProtobufDecoder/ProtobufEncoder: Protobuf编解码");

        System.out.println("\nLineBasedFrameDecoder示例:");
        System.out.println("ch.pipeline().addLast(new LineBasedFrameDecoder(1024));");
        System.out.println("ch.pipeline().addLast(new StringDecoder(StandardCharsets.UTF_8));");
        System.out.println("// 消息格式: Hello\\nWorld\\n");

        System.out.println("\nDelimiterBasedFrameDecoder示例:");
        System.out.println("ByteBuf delimiter = Unpooled.copiedBuffer(\"$\", StandardCharsets.UTF_8);");
        System.out.println("ch.pipeline().addLast(new DelimiterBasedFrameDecoder(1024, delimiter));");
        System.out.println("ch.pipeline().addLast(new StringDecoder(StandardCharsets.UTF_8));");
        System.out.println("// 消息格式: Hello$World$");

        System.out.println("\nFixedLengthFrameDecoder示例:");
        System.out.println("ch.pipeline().addLast(new FixedLengthFrameDecoder(10));");
        System.out.println("ch.pipeline().addLast(new StringDecoder(StandardCharsets.UTF_8));");
        System.out.println("// 每个消息固定10字节");

        System.out.println("\nLengthFieldBasedFrameDecoder示例:");
        System.out.println("ch.pipeline().addLast(new LengthFieldBasedFrameDecoder(");
        System.out.println("    1024 * 1024,  // 最大帧长度");
        System.out.println("    0,               // 长度字段偏移");
        System.out.println("    4,               // 长度字段长度");
        System.out.println("    0,               // 长度调整");
        System.out.println("    4                // 跳过的字节数");
        System.out.println("));");
        System.out.println("// 消息格式: [4字节长度][消息内容]");

        System.out.println("\n粘包拆包解决方案:");
        System.out.println("  1. 固定长度: FixedLengthFrameDecoder");
        System.out.println("  2. 分隔符: DelimiterBasedFrameDecoder");
        System.out.println("  3. 长度字段: LengthFieldBasedFrameDecoder（推荐）");
    }

    private static void heartbeatDemo() {
        System.out.println("\n--- 4. 心跳机制 ---");

        System.out.println("IdleStateHandler使用:");
        System.out.println("ch.pipeline().addLast(new IdleStateHandler(");
        System.out.println("    30,  // 读空闲时间（秒）");
        System.out.println("    60,  // 写空闲时间（秒）");
        System.out.println("    90   // 读写空闲时间（秒）");
        System.out.println("));");
        System.out.println("ch.pipeline().addLast(new HeartbeatHandler());");

        System.out.println("\n心跳处理器示例:");
        System.out.println("public class HeartbeatHandler extends ChannelInboundHandlerAdapter {");
        System.out.println("    private static final ByteBuf HEARTBEAT = Unpooled.unreleasableBuffer(");
        System.out.println("        Unpooled.copiedBuffer(\"HEARTBEAT\", StandardCharsets.UTF_8));");
        System.out.println("    @Override");
        System.out.println("    public void userEventTriggered(ChannelHandlerContext ctx, Object evt) {");
        System.out.println("        if (evt instanceof IdleStateEvent) {");
        System.out.println("            IdleStateEvent event = (IdleStateEvent) evt;");
        System.out.println("            if (event.state() == IdleState.READER_IDLE) {");
        System.out.println("                System.out.println(\"读空闲，发送心跳\");");
        System.out.println("                ctx.writeAndFlush(HEARTBEAT.duplicate());");
        System.out.println("            } else if (event.state() == IdleState.WRITER_IDLE) {");
        System.out.println("                System.out.println(\"写空闲\");");
        System.out.println("            } else if (event.state() == IdleState.ALL_IDLE) {");
        System.out.println("                System.out.println(\"读写空闲，关闭连接\");");
        System.out.println("                ctx.close();");
        System.out.println("            }");
        System.out.println("        }");
        System.out.println("    }");
        System.out.println("    @Override");
        System.out.println("    public void channelRead(ChannelHandlerContext ctx, Object msg) {");
        System.out.println("        ByteBuf buf = (ByteBuf) msg;");
        System.out.println("        if (buf.equals(HEARTBEAT)) {");
        System.out.println("            System.out.println(\"收到心跳包\");");
        System.out.println("        } else {");
        System.out.println("            ctx.fireChannelRead(msg);");
        System.out.println("        }");
        System.out.println("    }");
        System.out.println("}");

        System.out.println("\n心跳机制作用:");
        System.out.println("  - 检测连接是否存活");
        System.out.println("  - 防止连接被防火墙切断");
        System.out.println("  - 及时发现断线");
        System.out.println("  - 节省资源");
    }

    private static void reconnectionDemo() {
        System.out.println("\n--- 5. 断线重连 ---");

        System.out.println("断线重连示例:");
        System.out.println("public class ReconnectClient {");
        System.out.println("    private Bootstrap bootstrap;");
        System.out.println("    private EventLoopGroup group;");
        System.out.println("    private String host;");
        System.out.println("    private int port;");
        System.out.println("    private int retryCount = 0;");
        System.out.println("    private static final int MAX_RETRY = 10;");
        System.out.println();
        System.out.println("    public ReconnectClient(String host, int port) {");
        System.out.println("        this.host = host;");
        System.out.println("        this.port = port;");
        System.out.println("        this.group = new NioEventLoopGroup();");
        System.out.println("        this.bootstrap = new Bootstrap();");
        System.out.println("        bootstrap.group(group)");
        System.out.println("                 .channel(NioSocketChannel.class)");
        System.out.println("                 .handler(new ChannelInitializer<SocketChannel>() {");
        System.out.println("                     @Override");
        System.out.println("                     protected void initChannel(SocketChannel ch) {");
        System.out.println("                         ch.pipeline().addLast(new ReconnectHandler());");
        System.out.println("                     }");
        System.out.println("                 });");
        System.out.println("    }");
        System.out.println();
        System.out.println("    public void connect() {");
        System.out.println("        bootstrap.connect(host, port).addListener(new ChannelFutureListener() {");
        System.out.println("            @Override");
        System.out.println("            public void operationComplete(ChannelFuture future) {");
        System.out.println("                if (future.isSuccess()) {");
        System.out.println("                    System.out.println(\"连接成功\");");
        System.out.println("                    retryCount = 0;");
        System.out.println("                } else {");
        System.out.println("                    retry();");
        System.out.println("                }");
        System.out.println("            }");
        System.out.println("        });");
        System.out.println("    }");
        System.out.println();
        System.out.println("    private void retry() {");
        System.out.println("        if (retryCount >= MAX_RETRY) {");
        System.out.println("            System.out.println(\"重连次数超过限制\");");
        System.out.println("            group.shutdownGracefully();");
        System.out.println("            return;");
        System.out.println("        }");
        System.out.println("        retryCount++;");
        System.out.println("        int delay = (int) (Math.pow(2, retryCount) * 1000);");
        System.out.println("        System.out.println(\"连接失败，\" + delay + \"ms后重连 (\" + retryCount + \"/\" + MAX_RETRY + \")\");");
        System.out.println("        group.schedule(() -> connect(), delay, TimeUnit.MILLISECONDS);");
        System.out.println("    }");
        System.out.println();
        System.out.println("    class ReconnectHandler extends ChannelInboundHandlerAdapter {");
        System.out.println("        @Override");
        System.out.println("        public void channelInactive(ChannelHandlerContext ctx) {");
        System.out.println("            System.out.println(\"连接断开，开始重连\");");
        System.out.println("            retry();");
        System.out.println("        }");
        System.out.println("    }");
        System.out.println("}");

        System.out.println("\n重连策略:");
        System.out.println("  - 指数退避: 1s, 2s, 4s, 8s...");
        System.out.println("  - 固定间隔: 每5秒重连一次");
        System.out.println("  - 最大重试次数: 防止无限重试");
    }
}
