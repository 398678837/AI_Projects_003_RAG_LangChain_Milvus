package com.example.springai.finetuning;

import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Map;

/**
 * Spring AI 模型微调示例
 */
@RestController
@RequestMapping("/finetune")
public class FineTuningDemo {
    
    private final FineTuningService fineTuningService;
    
    public FineTuningDemo(FineTuningService fineTuningService) {
        this.fineTuningService = fineTuningService;
    }
    
    /**
     * 创建微调任务
     */
    @PostMapping("/create")
    public FineTuningJob createFineTuningJob(@RequestBody FineTuningRequest request) {
        return fineTuningService.createJob(
            request.getTaskType(),
            request.getTrainingData(),
            request.getValidationData(),
            request.getConfig()
        );
    }
    
    /**
     * 获取微调任务状态
     */
    @GetMapping("/status/{jobId}")
    public FineTuningJob getJobStatus(@PathVariable String jobId) {
        return fineTuningService.getJob(jobId);
    }
    
    /**
     * 列出所有微调任务
     */
    @GetMapping("/jobs")
    public List<FineTuningJob> listJobs() {
        return fineTuningService.listJobs();
    }
    
    /**
     * 取消微调任务
     */
    @PostMapping("/cancel/{jobId}")
    public String cancelJob(@PathVariable String jobId) {
        fineTuningService.cancelJob(jobId);
        return "微调任务已取消";
    }
    
    /**
     * 评估微调后的模型
     */
    @PostMapping("/evaluate/{modelId}")
    public EvaluationResult evaluateModel(@PathVariable String modelId, 
                                        @RequestBody List<Example> testData) {
        return fineTuningService.evaluate(modelId, testData);
    }
    
    /**
     * 使用微调后的模型
     */
    @PostMapping("/use/{modelId}")
    public String useModel(@PathVariable String modelId, 
                          @RequestBody String prompt) {
        return fineTuningService.useModel(modelId, prompt);
    }
}

/**
 * 微调服务接口
 */
interface FineTuningService {
    FineTuningJob createJob(String taskType, 
                          List<Example> trainingData, 
                          List<Example> validationData, 
                          FineTuningConfig config);
    
    FineTuningJob getJob(String jobId);
    
    List<FineTuningJob> listJobs();
    
    void cancelJob(String jobId);
    
    EvaluationResult evaluate(String modelId, List<Example> testData);
    
    String useModel(String modelId, String prompt);
}

/**
 * 微调请求类
 */
class FineTuningRequest {
    private String taskType;
    private List<Example> trainingData;
    private List<Example> validationData;
    private FineTuningConfig config;
    
    public String getTaskType() {
        return taskType;
    }
    
    public void setTaskType(String taskType) {
        this.taskType = taskType;
    }
    
    public List<Example> getTrainingData() {
        return trainingData;
    }
    
    public void setTrainingData(List<Example> trainingData) {
        this.trainingData = trainingData;
    }
    
    public List<Example> getValidationData() {
        return validationData;
    }
    
    public void setValidationData(List<Example> validationData) {
        this.validationData = validationData;
    }
    
    public FineTuningConfig getConfig() {
        return config;
    }
    
    public void setConfig(FineTuningConfig config) {
        this.config = config;
    }
}

/**
 * 微调任务类
 */
class FineTuningJob {
    private String id;
    private String status;
    private double progress;
    private String modelId;
    private long createdAt;
    private long updatedAt;
    
    public String getId() {
        return id;
    }
    
    public void setId(String id) {
        this.id = id;
    }
    
    public String getStatus() {
        return status;
    }
    
    public void setStatus(String status) {
        this.status = status;
    }
    
    public double getProgress() {
        return progress;
    }
    
    public void setProgress(double progress) {
        this.progress = progress;
    }
    
    public String getModelId() {
        return modelId;
    }
    
    public void setModelId(String modelId) {
        this.modelId = modelId;
    }
    
    public long getCreatedAt() {
        return createdAt;
    }
    
    public void setCreatedAt(long createdAt) {
        this.createdAt = createdAt;
    }
    
    public long getUpdatedAt() {
        return updatedAt;
    }
    
    public void setUpdatedAt(long updatedAt) {
        this.updatedAt = updatedAt;
    }
    
    public boolean isCompleted() {
        return "completed".equals(status) || "failed".equals(status) || "cancelled".equals(status);
    }
}

/**
 * 微调配置类
 */
class FineTuningConfig {
    private String modelName;
    private double learningRate;
    private int batchSize;
    private int epochs;
    private String fineTuningMethod;
    private Map<String, Object> additionalParams;
    
    public String getModelName() {
        return modelName;
    }
    
    public void setModelName(String modelName) {
        this.modelName = modelName;
    }
    
    public double getLearningRate() {
        return learningRate;
    }
    
    public void setLearningRate(double learningRate) {
        this.learningRate = learningRate;
    }
    
    public int getBatchSize() {
        return batchSize;
    }
    
    public void setBatchSize(int batchSize) {
        this.batchSize = batchSize;
    }
    
    public int getEpochs() {
        return epochs;
    }
    
    public void setEpochs(int epochs) {
        this.epochs = epochs;
    }
    
    public String getFineTuningMethod() {
        return fineTuningMethod;
    }
    
    public void setFineTuningMethod(String fineTuningMethod) {
        this.fineTuningMethod = fineTuningMethod;
    }
    
    public Map<String, Object> getAdditionalParams() {
        return additionalParams;
    }
    
    public void setAdditionalParams(Map<String, Object> additionalParams) {
        this.additionalParams = additionalParams;
    }
    
    public static Builder builder() {
        return new Builder();
    }
    
    public static class Builder {
        private String modelName;
        private double learningRate;
        private int batchSize;
        private int epochs;
        private String fineTuningMethod;
        private Map<String, Object> additionalParams;
        
        public Builder modelName(String modelName) {
            this.modelName = modelName;
            return this;
        }
        
        public Builder learningRate(double learningRate) {
            this.learningRate = learningRate;
            return this;
        }
        
        public Builder batchSize(int batchSize) {
            this.batchSize = batchSize;
            return this;
        }
        
        public Builder epochs(int epochs) {
            this.epochs = epochs;
            return this;
        }
        
        public Builder fineTuningMethod(String fineTuningMethod) {
            this.fineTuningMethod = fineTuningMethod;
            return this;
        }
        
        public Builder additionalParams(Map<String, Object> additionalParams) {
            this.additionalParams = additionalParams;
            return this;
        }
        
        public FineTuningConfig build() {
            FineTuningConfig config = new FineTuningConfig();
            config.setModelName(modelName);
            config.setLearningRate(learningRate);
            config.setBatchSize(batchSize);
            config.setEpochs(epochs);
            config.setFineTuningMethod(fineTuningMethod);
            config.setAdditionalParams(additionalParams);
            return config;
        }
    }
}

/**
 * 示例类
 */
class Example {
    private String input;
    private String output;
    private Map<String, Object> metadata;
    
    public String getInput() {
        return input;
    }
    
    public void setInput(String input) {
        this.input = input;
    }
    
    public String getOutput() {
        return output;
    }
    
    public void setOutput(String output) {
        this.output = output;
    }
    
    public Map<String, Object> getMetadata() {
        return metadata;
    }
    
    public void setMetadata(Map<String, Object> metadata) {
        this.metadata = metadata;
    }
}

/**
 * 评估结果类
 */
class EvaluationResult {
    private double accuracy;
    private double f1Score;
    private double precision;
    private double recall;
    private Map<String, Object> additionalMetrics;
    
    public double getAccuracy() {
        return accuracy;
    }
    
    public void setAccuracy(double accuracy) {
        this.accuracy = accuracy;
    }
    
    public double getF1Score() {
        return f1Score;
    }
    
    public void setF1Score(double f1Score) {
        this.f1Score = f1Score;
    }
    
    public double getPrecision() {
        return precision;
    }
    
    public void setPrecision(double precision) {
        this.precision = precision;
    }
    
    public double getRecall() {
        return recall;
    }
    
    public void setRecall(double recall) {
        this.recall = recall;
    }
    
    public Map<String, Object> getAdditionalMetrics() {
        return additionalMetrics;
    }
    
    public void setAdditionalMetrics(Map<String, Object> additionalMetrics) {
        this.additionalMetrics = additionalMetrics;
    }
}
