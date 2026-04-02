# Java IO/NIO

## 1. IO概述

### 1.1 IO的分类
- **按数据流方向**：输入流、输出流
- **按数据单位**：字节流、字符流
- **按流的角色**：节点流、处理流

### 1.2 IO流体系
```
InputStream
├─ FileInputStream
├─ ByteArrayInputStream
├─ ObjectInputStream
└─ ...

OutputStream
├─ FileOutputStream
├─ ByteArrayOutputStream
├─ ObjectOutputStream
└─ ...

Reader
├─ FileReader
├─ BufferedReader
├─ InputStreamReader
└─ ...

Writer
├─ FileWriter
├─ BufferedWriter
├─ OutputStreamWriter
└─ ...
```

## 2. 字节流

### 2.1 FileInputStream
```java
FileInputStream fis = null;
try {
    fis = new FileInputStream("input.txt");
    int data;
    while ((data = fis.read()) != -1) {
        System.out.print((char) data);
    }
} catch (IOException e) {
    e.printStackTrace();
} finally {
    if (fis != null) {
        fis.close();
    }
}
```

### 2.2 FileOutputStream
```java
FileOutputStream fos = null;
try {
    fos = new FileOutputStream("output.txt");
    String content = "Hello World";
    fos.write(content.getBytes());
} catch (IOException e) {
    e.printStackTrace();
} finally {
    if (fos != null) {
        fos.close();
    }
}
```

## 3. 字符流

### 3.1 FileReader
```java
FileReader fr = null;
try {
    fr = new FileReader("input.txt");
    int data;
    while ((data = fr.read()) != -1) {
        System.out.print((char) data);
    }
} catch (IOException e) {
    e.printStackTrace();
} finally {
    if (fr != null) {
        fr.close();
    }
}
```

### 3.2 FileWriter
```java
FileWriter fw = null;
try {
    fw = new FileWriter("output.txt");
    String content = "Hello World";
    fw.write(content);
} catch (IOException e) {
    e.printStackTrace();
} finally {
    if (fw != null) {
        fw.close();
    }
}
```

## 4. 缓冲流

### 4.1 BufferedReader
```java
BufferedReader br = null;
try {
    br = new BufferedReader(new FileReader("input.txt"));
    String line;
    while ((line = br.readLine()) != null) {
        System.out.println(line);
    }
} catch (IOException e) {
    e.printStackTrace();
} finally {
    if (br != null) {
        br.close();
    }
}
```

### 4.2 BufferedWriter
```java
BufferedWriter bw = null;
try {
    bw = new BufferedWriter(new FileWriter("output.txt"));
    bw.write("Hello World");
    bw.newLine();
    bw.write("Java IO");
} catch (IOException e) {
    e.printStackTrace();
} finally {
    if (bw != null) {
        bw.close();
    }
}
```

## 5. 转换流

### 5.1 InputStreamReader
```java
InputStreamReader isr = null;
try {
    isr = new InputStreamReader(new FileInputStream("input.txt"), "UTF-8");
    int data;
    while ((data = isr.read()) != -1) {
        System.out.print((char) data);
    }
} catch (IOException e) {
    e.printStackTrace();
} finally {
    if (isr != null) {
        isr.close();
    }
}
```

### 5.2 OutputStreamWriter
```java
OutputStreamWriter osw = null;
try {
    osw = new OutputStreamWriter(new FileOutputStream("output.txt"), "UTF-8");
    osw.write("Hello World");
} catch (IOException e) {
    e.printStackTrace();
} finally {
    if (osw != null) {
        osw.close();
    }
}
```

## 6. 对象流

### 6.1 ObjectOutputStream
```java
ObjectOutputStream oos = null;
try {
    oos = new ObjectOutputStream(new FileOutputStream("object.dat"));
    Person person = new Person("张三", 25);
    oos.writeObject(person);
} catch (IOException e) {
    e.printStackTrace();
} finally {
    if (oos != null) {
        oos.close();
    }
}
```

### 6.2 ObjectInputStream
```java
ObjectInputStream ois = null;
try {
    ois = new ObjectInputStream(new FileInputStream("object.dat"));
    Person person = (Person) ois.readObject();
    System.out.println(person.getName() + ": " + person.getAge());
} catch (IOException | ClassNotFoundException e) {
    e.printStackTrace();
} finally {
    if (ois != null) {
        ois.close();
    }
}
```

## 7. NIO概述

### 7.1 NIO与IO的区别
| 特性       | IO                  | NIO                 |
|------------|---------------------|---------------------|
| 模型       | 阻塞IO              | 非阻塞IO            |
| 操作单位   | 字节流/字符流       | 缓冲区（Buffer）    |
| 方式       | 流（Stream）        | 通道（Channel）     |
| 选择器     | 无                  | 选择器（Selector）  |

### 7.2 NIO核心组件
- **Buffer**：缓冲区，用于存储数据
- **Channel**：通道，用于读写数据
- **Selector**：选择器，用于监听多个通道的事件

## 8. NIO Buffer

### 8.1 Buffer的使用
```java
ByteBuffer buffer = ByteBuffer.allocate(1024);

// 写入数据
buffer.put("Hello World".getBytes());

// 切换为读模式
buffer.flip();

// 读取数据
byte[] bytes = new byte[buffer.remaining()];
buffer.get(bytes);
System.out.println(new String(bytes));

// 清空缓冲区
buffer.clear();
```

### 8.2 Buffer的类型
- ByteBuffer
- CharBuffer
- ShortBuffer
- IntBuffer
- LongBuffer
- FloatBuffer
- DoubleBuffer

## 9. NIO Channel

### 9.1 FileChannel
```java
RandomAccessFile file = new RandomAccessFile("input.txt", "rw");
FileChannel channel = file.getChannel();

ByteBuffer buffer = ByteBuffer.allocate(1024);
int bytesRead = channel.read(buffer);
while (bytesRead != -1) {
    buffer.flip();
    while (buffer.hasRemaining()) {
        System.out.print((char) buffer.get());
    }
    buffer.clear();
    bytesRead = channel.read(buffer);
}
file.close();
```

### 9.2 SocketChannel
```java
SocketChannel channel = SocketChannel.open();
channel.connect(new InetSocketAddress("www.example.com", 80));

ByteBuffer buffer = ByteBuffer.allocate(1024);
channel.read(buffer);
buffer.flip();
while (buffer.hasRemaining()) {
    System.out.print((char) buffer.get());
}
channel.close();
```

## 10. NIO Selector

### 10.1 Selector的使用
```java
Selector selector = Selector.open();

ServerSocketChannel serverSocket = ServerSocketChannel.open();
serverSocket.bind(new InetSocketAddress(8080));
serverSocket.configureBlocking(false);
serverSocket.register(selector, SelectionKey.OP_ACCEPT);

while (true) {
    int readyChannels = selector.select();
    if (readyChannels == 0) continue;
    
    Set<SelectionKey> selectedKeys = selector.selectedKeys();
    Iterator<SelectionKey> keyIterator = selectedKeys.iterator();
    
    while (keyIterator.hasNext()) {
        SelectionKey key = keyIterator.next();
        
        if (key.isAcceptable()) {
            // 处理连接
        } else if (key.isReadable()) {
            // 处理读操作
        } else if (key.isWritable()) {
            // 处理写操作
        }
        
        keyIterator.remove();
    }
}
```

## 11. Path与Files类

### 11.1 Path类
```java
Path path = Paths.get("input.txt");
System.out.println("文件名：" + path.getFileName());
System.out.println("父路径：" + path.getParent());
System.out.println("根路径：" + path.getRoot());
```

### 11.2 Files类
```java
// 读取文件
List<String> lines = Files.readAllLines(Paths.get("input.txt"));

// 写入文件
Files.write(Paths.get("output.txt"), "Hello World".getBytes());

// 复制文件
Files.copy(Paths.get("input.txt"), Paths.get("output.txt"));

// 删除文件
Files.delete(Paths.get("input.txt"));
```

## 12. IO性能优化

### 12.1 选择合适的IO模型
- 简单文件操作：使用传统IO
- 高并发网络操作：使用NIO

### 12.2 缓冲的使用
- 尽量使用缓冲流（BufferedReader、BufferedWriter等）
- 合理设置缓冲区大小

### 12.3 字符编码
- 明确指定字符编码，避免默认编码导致的问题
- 优先使用UTF-8编码

### 12.4 资源管理
- 使用try-with-resources自动关闭资源
- 确保所有IO资源都被正确关闭