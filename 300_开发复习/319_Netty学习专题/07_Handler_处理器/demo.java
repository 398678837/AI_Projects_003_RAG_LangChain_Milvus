package com.example.netty.handler;

import io.netty.channel.*;

public class HandlerDemo {

    public static void main(String[] args) {
        System.out.println("=== Netty Handler示例 ===");

        try {
            channelInboundHandlerDemo();
            channelOutboundHandlerDemo();
            simpleChannelInboundHandlerDemo();
            channelPipelineDemo();
            channelHandlerContextDemo();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void channelInboundHandlerDemo() {
        System.out.println("\n--- 1. ChannelInboundHandler ---");
        System.out.println("入站处理器示例:");
        System.out.println("public class MyInboundHandler extends ChannelInboundHandlerAdapter {");
        System.out.println("    @Override");
        System.out.println("    public void channelActive(ChannelHandlerContext ctx) {");
        System.out.println("        System.out.println(\"连接建立\");");
        System.out.println("    }");
        System.out.println("    @Override");
        System.out.println("    public void channelRead(ChannelHandlerContext ctx, Object msg) {");
        System.out.println("        System.out.println(\"收到消息: \" + msg);");
        System.out.println("        ctx.fireChannelRead(msg);");
        System.out.println("    }");
        System.out.println("    @Override");
        System.out.println("    public void channelReadComplete(ChannelHandlerContext ctx) {");
        System.out.println("        ctx.flush();");
        System.out.println("    }");
        System.out.println("    @Override");
        System.out.println("    public void exceptionCaught(ChannelHandlerContext ctx, Throwable cause) {");
        System.out.println("        cause.printStackTrace();");
        System.out.println("        ctx.close();");
        System.out.println("    }");
        System.out.println("}");
    }

    private static void channelOutboundHandlerDemo() {
        System.out.println("\n--- 2. ChannelOutboundHandler ---");
        System.out.println("出站处理器示例:");
        System.out.println("public class MyOutboundHandler extends ChannelOutboundHandlerAdapter {");
        System.out.println("    @Override");
        System.out.println("    public void write(ChannelHandlerContext ctx, Object msg, ChannelPromise promise) {");
        System.out.println("        System.out.println(\"发送消息: \" + msg);");
        System.out.println("        ctx.write(msg, promise);");
        System.out.println("    }");
        System.out.println("}");
    }

    private static void simpleChannelInboundHandlerDemo() {
        System.out.println("\n--- 3. SimpleChannelInboundHandler ---");
        System.out.println("简化入站处理器:");
        System.out.println("public class MySimpleHandler extends SimpleChannelInboundHandler<String> {");
        System.out.println("    @Override");
        System.out.println("    protected void channelRead0(ChannelHandlerContext ctx, String msg) {");
        System.out.println("        System.out.println(\"收到: \" + msg);");
        System.out.println("    }");
        System.out.println("}");
    }

    private static void channelPipelineDemo() {
        System.out.println("\n--- 4. ChannelPipeline ---");
        System.out.println("Pipeline添加Handler:");
        System.out.println("ch.pipeline().addLast(\"decoder\", new StringDecoder());");
        System.out.println("ch.pipeline().addLast(\"encoder\", new StringEncoder());");
        System.out.println("ch.pipeline().addLast(\"handler\", new MyHandler());");
        System.out.println();
        System.out.println("事件流动:");
        System.out.println("  入站: Handler1 -> Handler2 -> Handler3");
        System.out.println("  出站: Handler3 -> Handler2 -> Handler1");
    }

    private static void channelHandlerContextDemo() {
        System.out.println("\n--- 5. ChannelHandlerContext ---");
        System.out.println("Context常用方法:");
        System.out.println("  ctx.channel();");
        System.out.println("  ctx.pipeline();");
        System.out.println("  ctx.writeAndFlush(msg);");
        System.out.println("  ctx.fireChannelRead(msg);");
        System.out.println("  ctx.close();");
    }
}
