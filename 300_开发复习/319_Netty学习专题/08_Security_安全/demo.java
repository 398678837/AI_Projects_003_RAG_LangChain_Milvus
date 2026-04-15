package com.example.netty.security;

import io.netty.bootstrap.ServerBootstrap;
import io.netty.channel.*;
import io.netty.channel.nio.NioEventLoopGroup;
import io.netty.channel.socket.nio.NioServerSocketChannel;
import io.netty.handler.ssl.*;

import javax.net.ssl.KeyManagerFactory;
import javax.net.ssl.TrustManagerFactory;
import java.io.FileInputStream;
import java.security.KeyStore;

public class SecurityDemo {

    public static void main(String[] args) {
        System.out.println("=== Netty安全示例 ===");

        try {
            sslTlsDemo();
            sslHandlerDemo();
            certificateDemo();
            bestPracticesDemo();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void sslTlsDemo() {
        System.out.println("\n--- 1. SSL/TLS ---");
        System.out.println("SSL/TLS作用:");
        System.out.println("  - 数据加密");
        System.out.println("  - 身份认证");
        System.out.println("  - 完整性保护");
        System.out.println();
        System.out.println("TLS版本:");
        System.out.println("  - TLS 1.2（推荐）");
        System.out.println("  - TLS 1.3（最新）");
    }

    private static void sslHandlerDemo() {
        System.out.println("\n--- 2. SslHandler ---");
        System.out.println("服务端SSL配置:");
        System.out.println("SslContext sslCtx = SslContextBuilder.forServer(");
        System.out.println("    new File(\"server.crt\"),");
        System.out.println("    new File(\"server.key\")");
        System.out.println(").build();");
        System.out.println();
        System.out.println("客户端SSL配置:");
        System.out.println("SslContext sslCtx = SslContextBuilder.forClient()");
        System.out.println("    .trustManager(new File(\"ca.crt\"))");
        System.out.println("    .build();");
        System.out.println();
        System.out.println("添加到Pipeline:");
        System.out.println("ch.pipeline().addLast(sslCtx.newHandler(ch.alloc()));");
    }

    private static void certificateDemo() {
        System.out.println("\n--- 3. 证书管理 ---");
        System.out.println("生成自签名证书:");
        System.out.println("  openssl req -x509 -newkey rsa:4096 -keyout server.key -out server.crt -days 365");
        System.out.println();
        System.out.println("KeyStore和TrustStore:");
        System.out.println("  KeyStore: 存储自己的私钥和证书");
        System.out.println("  TrustStore: 存储信任的CA证书");
    }

    private static void bestPracticesDemo() {
        System.out.println("\n--- 4. 安全最佳实践 ---");
        System.out.println("1. 使用最新TLS版本");
        System.out.println("2. 使用强加密套件");
        System.out.println("3. 验证证书");
        System.out.println("4. 定期更新证书");
        System.out.println("5. 禁用旧协议");
    }
}
