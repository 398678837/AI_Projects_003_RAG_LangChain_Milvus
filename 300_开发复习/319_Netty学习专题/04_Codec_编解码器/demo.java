package com.example.netty.codec;

import io.netty.buffer.ByteBuf;
import io.netty.channel.ChannelHandlerContext;
import io.netty.handler.codec.*;

import java.util.List;

public class CodecDemo {

    public static void main(String[] args) {
        System.out.println("=== Netty编解码器示例 ===");

        try {
            decoderDemo();
            encoderDemo();
            builtinCodecsDemo();
            customCodecDemo();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void decoderDemo() {
        System.out.println("\n--- 1. 解码器 ---");
        System.out.println("ByteToMessageDecoder示例:");
        System.out.println("public class MyDecoder extends ByteToMessageDecoder {");
        System.out.println("    @Override");
        System.out.println("    protected void decode(ChannelHandlerContext ctx, ByteBuf in, List<Object> out) {");
        System.out.println("        if (in.readableBytes() >= 4) {");
        System.out.println("            int length = in.readInt();");
        System.out.println("            if (in.readableBytes() >= length) {");
        System.out.println("                byte[] data = new byte[length];");
        System.out.println("                in.readBytes(data);");
        System.out.println("                out.add(new String(data));");
        System.out.println("            } else {");
        System.out.println("                in.resetReaderIndex();");
        System.out.println("            }");
        System.out.println("        }");
        System.out.println("    }");
        System.out.println("}");
    }

    private static void encoderDemo() {
        System.out.println("\n--- 2. 编码器 ---");
        System.out.println("MessageToByteEncoder示例:");
        System.out.println("public class MyEncoder extends MessageToByteEncoder<String> {");
        System.out.println("    @Override");
        System.out.println("    protected void encode(ChannelHandlerContext ctx, String msg, ByteBuf out) {");
        System.out.println("        byte[] data = msg.getBytes();");
        System.out.println("        out.writeInt(data.length);");
        System.out.println("        out.writeBytes(data);");
        System.out.println("    }");
        System.out.println("}");
    }

    private static void builtinCodecsDemo() {
        System.out.println("\n--- 3. 内置编解码器 ---");
        System.out.println("LineBasedFrameDecoder:");
        System.out.println("  new LineBasedFrameDecoder(1024)");
        System.out.println();
        System.out.println("DelimiterBasedFrameDecoder:");
        System.out.println("  ByteBuf delimiter = Unpooled.copiedBuffer(\"$\", CharsetUtil.UTF_8);");
        System.out.println("  new DelimiterBasedFrameDecoder(1024, delimiter)");
        System.out.println();
        System.out.println("FixedLengthFrameDecoder:");
        System.out.println("  new FixedLengthFrameDecoder(10)");
        System.out.println();
        System.out.println("LengthFieldBasedFrameDecoder:");
        System.out.println("  new LengthFieldBasedFrameDecoder(1024*1024, 0, 4, 0, 4)");
    }

    private static void customCodecDemo() {
        System.out.println("\n--- 4. 自定义编解码器 ---");
        System.out.println("自定义协议编解码器示例:");
        System.out.println("协议格式: [4字节长度][消息内容]");
    }
}
