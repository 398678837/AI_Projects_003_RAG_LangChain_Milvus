import com.aliyun.oss.OSS;
import com.aliyun.oss.OSSClientBuilder;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.multipart.MultipartFile;

import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.URLEncoder;
import java.util.ArrayList;
import java.util.List;
import java.util.UUID;

// 主应用类
@SpringBootApplication
@EnableDiscoveryClient
public class OSSObjectStorageDemo {
    public static void main(String[] args) {
        SpringApplication.run(OSSObjectStorageDemo.class, args);
    }
}

// 文件控制器
@RestController
@RequestMapping("/api/files")
class FileController {
    private final OSS ossClient;
    private final String bucketName = "your-bucket-name";
    
    public FileController() {
        // 初始化 OSS 客户端
        String endpoint = "oss-cn-hangzhou.aliyuncs.com";
        String accessKeyId = "your-access-key-id";
        String accessKeySecret = "your-access-key-secret";
        this.ossClient = new OSSClientBuilder().build(endpoint, accessKeyId, accessKeySecret);
    }
    
    @PostMapping("/upload")
    public String upload(@RequestParam("file") MultipartFile file) throws IOException {
        // 生成文件名
        String originalFilename = file.getOriginalFilename();
        String extension = originalFilename.substring(originalFilename.lastIndexOf("."));
        String fileName = UUID.randomUUID().toString() + extension;
        
        // 上传文件
        try (InputStream inputStream = file.getInputStream()) {
            ossClient.putObject(bucketName, fileName, inputStream);
        }
        
        // 生成访问 URL
        return "https://" + bucketName + ".oss-cn-hangzhou.aliyuncs.com/" + fileName;
    }
    
    @GetMapping("/download/{fileName}")
    public void download(@PathVariable String fileName, HttpServletResponse response) throws IOException {
        // 获取文件
        com.aliyun.oss.OSSObject ossObject = ossClient.getObject(bucketName, fileName);
        
        // 设置响应头
        response.setContentType(ossObject.getObjectMetadata().getContentType());
        response.setHeader("Content-Disposition", "attachment; filename=" + URLEncoder.encode(fileName, "UTF-8"));
        
        // 输出文件
        try (InputStream inputStream = ossObject.getObjectContent();
             OutputStream outputStream = response.getOutputStream()) {
            byte[] buffer = new byte[1024];
            int len;
            while ((len = inputStream.read(buffer)) != -1) {
                outputStream.write(buffer, 0, len);
            }
        }
    }
    
    @DeleteMapping("/{fileName}")
    public String delete(@PathVariable String fileName) {
        // 删除文件
        ossClient.deleteObject(bucketName, fileName);
        return "File deleted: " + fileName;
    }
    
    @GetMapping
    public List<String> list() {
        List<String> files = new ArrayList<>();
        // 列举文件
        com.aliyun.oss.model.ObjectListing objectListing = ossClient.listObjects(bucketName);
        for (com.aliyun.oss.model.OSSObjectSummary objectSummary : objectListing.getObjectSummaries()) {
            files.add(objectSummary.getKey());
        }
        return files;
    }
}