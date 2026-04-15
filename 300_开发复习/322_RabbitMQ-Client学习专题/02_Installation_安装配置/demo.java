package com.example.rabbitmq.installation;

import java.util.*;

public class InstallationDemo {

    public static void main(String[] args) {
        System.out.println("=== RabbitMQ安装配置示例 ===");

        try {
            installationMethodsDemo();
            configFileDemo();
            startStopDemo();
            managementPluginDemo();
            basicConfigDemo();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void installationMethodsDemo() {
        System.out.println("\n--- 1. 安装方式 ---");

        System.out.println("Erlang/OTP安装:");
        System.out.println("  - RabbitMQ依赖Erlang");
        System.out.println("  - 需要先安装Erlang");
        System.out.println("  - 版本兼容性需要注意");

        System.out.println("\nWindows安装:");
        System.out.println("  - 下载Erlang安装包");
        System.out.println("  - 下载RabbitMQ安装包");
        System.out.println("  - 按顺序安装");
        System.out.println("  - 使用Chocolatey: choco install rabbitmq");

        System.out.println("\nLinux安装:");
        System.out.println("  - Ubuntu/Debian:");
        System.out.println("    sudo apt-get install rabbitmq-server");
        System.out.println();
        System.out.println("  - CentOS/RHEL:");
        System.out.println("    sudo yum install rabbitmq-server");

        System.out.println("\nMac安装:");
        System.out.println("  - 使用Homebrew:");
        System.out.println("    brew install rabbitmq");

        System.out.println("\nDocker安装:");
        System.out.println("  docker run -d --name rabbitmq \\");
        System.out.println("    -p 5672:5672 \\");
        System.out.println("    -p 15672:15672 \\");
        System.out.println("    rabbitmq:3-management");
    }

    private static void configFileDemo() {
        System.out.println("\n--- 2. 配置文件 ---");

        System.out.println("配置文件位置:");
        System.out.println("  - Linux: /etc/rabbitmq/");
        System.out.println("  - Windows: C:\\Program Files\\RabbitMQ Server\\rabbitmq_server-xxx\\etc\\");
        System.out.println("  - Mac: /usr/local/etc/rabbitmq/");

        System.out.println("\nrabbitmq.conf (新格式):");
        String rabbitmqConf = "listeners.tcp.default = 5672\n" +
                "management.listener.port = 15672\n" +
                "default_user = guest\n" +
                "default_pass = guest\n" +
                "default_vhost = /\n" +
                "log.file.level = info\n" +
                "vm_memory_high_watermark.relative = 0.4\n" +
                "disk_free_limit.absolute = 2GB";
        System.out.println(rabbitmqConf);

        System.out.println("\nenvironment variables:");
        String envVars = "RABBITMQ_NODE_PORT=5672\n" +
                "RABBITMQ_NODENAME=rabbit@localhost\n" +
                "RABBITMQ_LOG_BASE=/var/log/rabbitmq\n" +
                "RABBITMQ_MNESIA_BASE=/var/lib/rabbitmq/mnesia";
        System.out.println(envVars);
    }

    private static void startStopDemo() {
        System.out.println("\n--- 3. 启动停止 ---");

        System.out.println("Linux/Mac:");
        System.out.println("  # 启动");
        System.out.println("  sudo systemctl start rabbitmq-server");
        System.out.println("  # 或");
        System.out.println("  sudo service rabbitmq-server start");
        System.out.println();
        System.out.println("  # 停止");
        System.out.println("  sudo systemctl stop rabbitmq-server");
        System.out.println();
        System.out.println("  # 重启");
        System.out.println("  sudo systemctl restart rabbitmq-server");
        System.out.println();
        System.out.println("  # 状态");
        System.out.println("  sudo systemctl status rabbitmq-server");
        System.out.println("  # 或");
        System.out.println("  sudo rabbitmqctl status");

        System.out.println("\nWindows:");
        System.out.println("  # 启动服务");
        System.out.println("  rabbitmq-service.bat install");
        System.out.println("  rabbitmq-service.bat start");
        System.out.println();
        System.out.println("  # 停止服务");
        System.out.println("  rabbitmq-service.bat stop");

        System.out.println("\n使用rabbitmqctl:");
        System.out.println("  # 查看状态");
        System.out.println("  rabbitmqctl status");
        System.out.println();
        System.out.println("  # 停止应用");
        System.out.println("  rabbitmqctl stop_app");
        System.out.println();
        System.out.println("  # 启动应用");
        System.out.println("  rabbitmqctl start_app");
        System.out.println();
        System.out.println("  # 重置");
        System.out.println("  rabbitmqctl reset");
    }

    private static void managementPluginDemo() {
        System.out.println("\n--- 4. 管理插件 ---");

        System.out.println("启用管理插件:");
        System.out.println("  rabbitmq-plugins enable rabbitmq_management");

        System.out.println("\n访问管理界面:");
        System.out.println("  URL: http://localhost:15672");
        System.out.println("  默认用户: guest");
        System.out.println("  默认密码: guest");
        System.out.println("  注意: guest只能从localhost访问");

        System.out.println("\n管理界面功能:");
        System.out.println("  - Connections: 连接管理");
        System.out.println("  - Channels: 通道管理");
        System.out.println("  - Exchanges: 交换机管理");
        System.out.println("  - Queues: 队列管理");
        System.out.println("  - Admin: 用户和权限管理");

        System.out.println("\n其他有用的插件:");
        System.out.println("  - rabbitmq_shovel: 消息转发");
        System.out.println("  - rabbitmq_federation: 联邦");
        System.out.println("  - rabbitmq_tracing: 消息跟踪");
        System.out.println("  - rabbitmq_stomp: STOMP协议");
        System.out.println("  - rabbitmq_mqtt: MQTT协议");
    }

    private static void basicConfigDemo() {
        System.out.println("\n--- 5. 基本配置 ---");

        System.out.println("端口配置:");
        System.out.println("  - 5672: AMQP");
        System.out.println("  - 15672: HTTP管理");
        System.out.println("  - 25672: 节点间通信");
        System.out.println("  - 1883: MQTT");
        System.out.println("  - 61613: STOMP");

        System.out.println("\n内存配置:");
        System.out.println("  vm_memory_high_watermark.relative = 0.4");
        System.out.println("  # 使用40%的内存");

        System.out.println("\n磁盘配置:");
        System.out.println("  disk_free_limit.absolute = 2GB");
        System.out.println("  # 至少保留2GB磁盘空间");

        System.out.println("\n创建用户:");
        System.out.println("  rabbitmqctl add_user myuser mypassword");
        System.out.println("  rabbitmqctl set_user_tags myuser administrator");
        System.out.println("  rabbitmqctl set_permissions -p / myuser \".*\" \".*\" \".*\"");

        System.out.println("\n创建虚拟主机:");
        System.out.println("  rabbitmqctl add_vhost myvhost");
        System.out.println("  rabbitmqctl set_permissions -p myvhost myuser \".*\" \".*\" \".*\"");
    }
}
