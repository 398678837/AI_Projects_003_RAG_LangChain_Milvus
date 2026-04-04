import java.io.*;
import java.nio.ByteBuffer;
import java.nio.channels.FileChannel;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

public class IODemo {
    public static void main(String[] args) {
        // 1. 字节流
        System.out.println("=== 字节流演示 ===");
        try (FileInputStream fis = new FileInputStream("input.txt")) {
            int data;
            while ((data = fis.read()) != -1) {
                System.out.print((char) data);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        
        // 2. 字符流
        System.out.println("\n=== 字符流演示 ===");
        try (FileReader fr = new FileReader("input.txt")) {
            int data;
            while ((data = fr.read()) != -1) {
                System.out.print((char) data);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        
        // 3. 缓冲流
        System.out.println("\n=== 缓冲流演示 ===");
        try (BufferedReader br = new BufferedReader(new FileReader("input.txt"))) {
            String line;
            while ((line = br.readLine()) != null) {
                System.out.println(line);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        
        // 4. 对象流
        System.out.println("\n=== 对象流演示 ===");
        try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream("object.dat"))) {
            Person person = new Person("张三", 25);
            oos.writeObject(person);
            System.out.println("对象写入成功");
        } catch (IOException e) {
            e.printStackTrace();
        }
        
        try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream("object.dat"))) {
            Person person = (Person) ois.readObject();
            System.out.println("读取到对象：" + person.getName() + ", " + person.getAge());
        } catch (IOException | ClassNotFoundException e) {
            e.printStackTrace();
        }
        
        // 5. NIO Buffer
        System.out.println("\n=== NIO Buffer演示 ===");
        ByteBuffer buffer = ByteBuffer.allocate(1024);
        buffer.put("Hello NIO".getBytes());
        buffer.flip();
        byte[] bytes = new byte[buffer.remaining()];
        buffer.get(bytes);
        System.out.println(new String(bytes));
        
        // 6. NIO Channel
        System.out.println("\n=== NIO Channel演示 ===");
        try (RandomAccessFile file = new RandomAccessFile("input.txt", "rw")) {
            FileChannel channel = file.getChannel();
            ByteBuffer channelBuffer = ByteBuffer.allocate(1024);
            int bytesRead = channel.read(channelBuffer);
            while (bytesRead != -1) {
                channelBuffer.flip();
                while (channelBuffer.hasRemaining()) {
                    System.out.print((char) channelBuffer.get());
                }
                channelBuffer.clear();
                bytesRead = channel.read(channelBuffer);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        
        // 7. Path与Files类
        System.out.println("\n=== Path与Files类演示 ===");
        try {
            List<String> lines = Files.readAllLines(Paths.get("input.txt"));
            System.out.println("文件内容：" + lines);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

// 可序列化的Person类
class Person implements Serializable {
    private static final long serialVersionUID = 1L;
    private String name;
    private int age;
    
    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }
    
    public String getName() {
        return name;
    }
    
    public int getAge() {
        return age;
    }
}