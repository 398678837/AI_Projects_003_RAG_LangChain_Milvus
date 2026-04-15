package com.example.netty.bestpractices;

import io.netty.bootstrap.Bootstrap;
import io.netty.bootstrap.ServerBootstrap;
import io.netty.channel.*;
import io.netty.channel.nio.NioEventLoopGroup;
import io.netty.util.ReferenceCountUtil;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class BestPracticesDemo {

    private static final Logger logger = LoggerFactory.getLogger(BestPracticesDemo.class);

    public static void main(String[] args) {
        System.out.println("=== Netty最佳实践示例 ===");

        try {
            codingStandardsDemo();
            exceptionHandlingDemo();
            resourceManagementDemo();
            loggingDemo();
            testingDemo();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void codingStandardsDemo() {
        System.out.println("\n--- 1. 编码规范 ---");
        System.out.println("命名规范:");
        System.out.println("  - Handler: XxxHandler");
        System.out.println("  - Codec: XxxEncoder/XxxDecoder");
        System.out.println("  - Pipeline: 从编解码开始，然后业务");
        System.out.println();
        System.out.println("Pipeline顺序:");
        System.out.println("  1. IdleStateHandler");
        System.out.println("  2. 解码器");
        System.out.println("  3. 编码器");
        System.out.println("  4. 业务Handler");
    }

    private static void exceptionHandlingDemo() {
        System.out.println("\n--- 2. 异常处理 ---");
        System.out.println("public class MyHandler extends ChannelInboundHandlerAdapter {");
        System.out.println("    private static final Logger logger = LoggerFactory.getLogger(MyHandler.class);");
        System.out.println("    @Override");
        System.out.println("    public void exceptionCaught(ChannelHandlerContext ctx, Throwable cause) {");
        System.out.println("        logger.error(\"Channel异常\", cause);");
        System.out.println("        ctx.close();");
        System.out.println("    }");
        System.out.println("}");
    }

    private static void resourceManagementDemo() {
        System.out.println("\n--- 3. 资源管理 ---");
        System.out.println("优雅关闭:");
        System.out.println("EventLoopGroup bossGroup = new NioEventLoopGroup();");
        System.out.println("EventLoopGroup workerGroup = new NioEventLoopGroup();");
        System.out.println("try {");
        System.out.println("    // 业务逻辑");
        System.out.println("} finally {");
        System.out.println("    bossGroup.shutdownGracefully();");
        System.out.println("    workerGroup.shutdownGracefully();");
        System.out.println("}");
        System.out.println();
        System.out.println("ByteBuf释放:");
        System.out.println("ReferenceCountUtil.release(msg);");
        System.out.println("// 或使用SimpleChannelInboundHandler自动释放");
    }

    private static void loggingDemo() {
        System.out.println("\n--- 4. 日志 ---");
        System.out.println("日志级别:");
        System.out.println("  - ERROR: 错误");
        System.out.println("  - WARN: 警告");
        System.out.println("  - INFO: 重要信息");
        System.out.println("  - DEBUG: 调试信息");
        System.out.println("  - TRACE: 详细跟踪");
        System.out.println();
        System.out.println("建议:");
        System.out.println("  - 连接建立/断开: INFO");
        System.out.println("  - 异常: ERROR");
        System.out.println("  - 消息收发: DEBUG");
        System.out.println("  - 详细流程: TRACE");
    }

    private static void testingDemo() {
        System.out.println("\n--- 5. 测试 ---");
        System.out.println("使用EmbeddedChannel测试:");
        System.out.println("EmbeddedChannel channel = new EmbeddedChannel(new MyHandler());");
        System.out.println("channel.writeInbound(\"test\");");
        System.out.println("String result = channel.readOutbound();");
        System.out.println("// 断言验证");
    }
}
