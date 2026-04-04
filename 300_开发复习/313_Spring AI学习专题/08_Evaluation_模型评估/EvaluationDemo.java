package com.example.springai.evaluation;

import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Map;

/**
 * Spring AI 模型评估示例
 */
@RestController
@RequestMapping("/evaluate")
public class EvaluationDemo {
    
    private final EvaluationService evaluationService;
    
    public EvaluationDemo(EvaluationService evaluationService) {
        this.evaluationService = evaluationService;
    }
    
    /**
     * 评估分类模型
     */
    @PostMapping("/classification")
    public EvaluationResult evaluateClassification(@RequestBody ClassificationEvaluationRequest request) {
        return evaluationService.evaluateClassification(
            request.getModelId(),
            request.getTestData()
        );
    }
    
    /**
     * 评估生成模型
     */
    @PostMapping("/generation")
    public EvaluationResult evaluateGeneration(@RequestBody GenerationEvaluationRequest request) {
        return evaluationService.evaluateGeneration(
            request.getModelId(),
            request.getTestData()
        );
    }
    
    /**
     * 评估问答模型
     */
    @PostMapping("/qa")
    public EvaluationResult evaluateQA(@RequestBody QAEvaluationRequest request) {
        return evaluationService.evaluateQA(
            request.getModelId(),
            request.getTestData()
        );
    }
    
    /**
     * 评估 RAG 系统
     */
    @PostMapping("/rag")
    public RAGEvaluationResult evaluateRAG(@RequestBody RAGEvaluationRequest request) {
        return evaluationService.evaluateRAG(
            request.getRagSystemId(),
            request.getTestData()
        );
    }
    
    /**
     * 比较多个模型
     */
    @PostMapping("/compare")
    public List<ModelComparisonResult> compareModels(@RequestBody ModelComparisonRequest request) {
        return evaluationService.compareModels(
            request.getModelIds(),
            request.getTestData(),
            request.getTaskType()
        );
    }
    
    /**
     * 生成评估报告
     */
    @PostMapping("/report")
    public EvaluationReport generateReport(@RequestBody ReportRequest request) {
        return evaluationService.generateReport(
            request.getModelId(),
            request.getTestData(),
            request.getTaskType()
        );
    }
}

/**
 * 评估服务接口
 */
interface EvaluationService {
    EvaluationResult evaluateClassification(String modelId, List<ClassificationExample> testData);
    EvaluationResult evaluateGeneration(String modelId, List<GenerationExample> testData);
    EvaluationResult evaluateQA(String modelId, List<QAExample> testData);
    RAGEvaluationResult evaluateRAG(String ragSystemId, List<RAGExample> testData);
    List<ModelComparisonResult> compareModels(List<String> modelIds, List<? extends Example> testData, String taskType);
    EvaluationReport generateReport(String modelId, List<? extends Example> testData, String taskType);
}

/**
 * 分类评估请求
 */
class ClassificationEvaluationRequest {
    private String modelId;
    private List<ClassificationExample> testData;
    
    public String getModelId() {
        return modelId;
    }
    
    public void setModelId(String modelId) {
        this.modelId = modelId;
    }
    
    public List<ClassificationExample> getTestData() {
        return testData;
    }
    
    public void setTestData(List<ClassificationExample> testData) {
        this.testData = testData;
    }
}

/**
 * 生成评估请求
 */
class GenerationEvaluationRequest {
    private String modelId;
    private List<GenerationExample> testData;
    
    public String getModelId() {
        return modelId;
    }
    
    public void setModelId(String modelId) {
        this.modelId = modelId;
    }
    
    public List<GenerationExample> getTestData() {
        return testData;
    }
    
    public void setTestData(List<GenerationExample> testData) {
        this.testData = testData;
    }
}

/**
 * 问答评估请求
 */
class QAEvaluationRequest {
    private String modelId;
    private List<QAExample> testData;
    
    public String getModelId() {
        return modelId;
    }
    
    public void setModelId(String modelId) {
        this.modelId = modelId;
    }
    
    public List<QAExample> getTestData() {
        return testData;
    }
    
    public void setTestData(List<QAExample> testData) {
        this.testData = testData;
    }
}

/**
 * RAG 评估请求
 */
class RAGEvaluationRequest {
    private String ragSystemId;
    private List<RAGExample> testData;
    
    public String getRagSystemId() {
        return ragSystemId;
    }
    
    public void setRagSystemId(String ragSystemId) {
        this.ragSystemId = ragSystemId;
    }
    
    public List<RAGExample> getTestData() {
        return testData;
    }
    
    public void setTestData(List<RAGExample> testData) {
        this.testData = testData;
    }
}

/**
 * 模型比较请求
 */
class ModelComparisonRequest {
    private List<String> modelIds;
    private List<? extends Example> testData;
    private String taskType;
    
    public List<String> getModelIds() {
        return modelIds;
    }
    
    public void setModelIds(List<String> modelIds) {
        this.modelIds = modelIds;
    }
    
    public List<? extends Example> getTestData() {
        return testData;
    }
    
    public void setTestData(List<? extends Example> testData) {
        this.testData = testData;
    }
    
    public String getTaskType() {
        return taskType;
    }
    
    public void setTaskType(String taskType) {
        this.taskType = taskType;
    }
}

/**
 * 报告请求
 */
class ReportRequest {
    private String modelId;
    private List<? extends Example> testData;
    private String taskType;
    
    public String getModelId() {
        return modelId;
    }
    
    public void setModelId(String modelId) {
        this.modelId = modelId;
    }
    
    public List<? extends Example> getTestData() {
        return testData;
    }
    
    public void setTestData(List<? extends Example> testData) {
        this.testData = testData;
    }
    
    public String getTaskType() {
        return taskType;
    }
    
    public void setTaskType(String taskType) {
        this.taskType = taskType;
    }
}

/**
 * 基础示例类
 */
class Example {
    private String id;
    
    public String getId() {
        return id;
    }
    
    public void setId(String id) {
        this.id = id;
    }
}

/**
 * 分类示例
 */
class ClassificationExample extends Example {
    private String input;
    private String expectedOutput;
    
    public String getInput() {
        return input;
    }
    
    public void setInput(String input) {
        this.input = input;
    }
    
    public String getExpectedOutput() {
        return expectedOutput;
    }
    
    public void setExpectedOutput(String expectedOutput) {
        this.expectedOutput = expectedOutput;
    }
}

/**
 * 生成示例
 */
class GenerationExample extends Example {
    private String input;
    private String expectedOutput;
    
    public String getInput() {
        return input;
    }
    
    public void setInput(String input) {
        this.input = input;
    }
    
    public String getExpectedOutput() {
        return expectedOutput;
    }
    
    public void setExpectedOutput(String expectedOutput) {
        this.expectedOutput = expectedOutput;
    }
}

/**
 * 问答示例
 */
class QAExample extends Example {
    private String question;
    private String context;
    private String expectedAnswer;
    
    public String getQuestion() {
        return question;
    }
    
    public void setQuestion(String question) {
        this.question = question;
    }
    
    public String getContext() {
        return context;
    }
    
    public void setContext(String context) {
        this.context = context;
    }
    
    public String getExpectedAnswer() {
        return expectedAnswer;
    }
    
    public void setExpectedAnswer(String expectedAnswer) {
        this.expectedAnswer = expectedAnswer;
    }
}

/**
 * RAG 示例
 */
class RAGExample extends Example {
    private String question;
    private List<String> expectedDocuments;
    private String expectedAnswer;
    
    public String getQuestion() {
        return question;
    }
    
    public void setQuestion(String question) {
        this.question = question;
    }
    
    public List<String> getExpectedDocuments() {
        return expectedDocuments;
    }
    
    public void setExpectedDocuments(List<String> expectedDocuments) {
        this.expectedDocuments = expectedDocuments;
    }
    
    public String getExpectedAnswer() {
        return expectedAnswer;
    }
    
    public void setExpectedAnswer(String expectedAnswer) {
        this.expectedAnswer = expectedAnswer;
    }
}

/**
 * 评估结果
 */
class EvaluationResult {
    private Map<String, Double> metrics;
    private Map<String, Object> details;
    
    public Map<String, Double> getMetrics() {
        return metrics;
    }
    
    public void setMetrics(Map<String, Double> metrics) {
        this.metrics = metrics;
    }
    
    public Map<String, Object> getDetails() {
        return details;
    }
    
    public void setDetails(Map<String, Object> details) {
        this.details = details;
    }
}

/**
 * RAG 评估结果
 */
class RAGEvaluationResult extends EvaluationResult {
    private double retrievalQuality;
    private double generationQuality;
    private double overallQuality;
    
    public double getRetrievalQuality() {
        return retrievalQuality;
    }
    
    public void setRetrievalQuality(double retrievalQuality) {
        this.retrievalQuality = retrievalQuality;
    }
    
    public double getGenerationQuality() {
        return generationQuality;
    }
    
    public void setGenerationQuality(double generationQuality) {
        this.generationQuality = generationQuality;
    }
    
    public double getOverallQuality() {
        return overallQuality;
    }
    
    public void setOverallQuality(double overallQuality) {
        this.overallQuality = overallQuality;
    }
}

/**
 * 模型比较结果
 */
class ModelComparisonResult {
    private String modelId;
    private Map<String, Double> metrics;
    private int rank;
    
    public String getModelId() {
        return modelId;
    }
    
    public void setModelId(String modelId) {
        this.modelId = modelId;
    }
    
    public Map<String, Double> getMetrics() {
        return metrics;
    }
    
    public void setMetrics(Map<String, Double> metrics) {
        this.metrics = metrics;
    }
    
    public int getRank() {
        return rank;
    }
    
    public void setRank(int rank) {
        this.rank = rank;
    }
}

/**
 * 评估报告
 */
class EvaluationReport {
    private String modelId;
    private String taskType;
    private Map<String, Double> metrics;
    private String summary;
    private List<String> recommendations;
    
    public String getModelId() {
        return modelId;
    }
    
    public void setModelId(String modelId) {
        this.modelId = modelId;
    }
    
    public String getTaskType() {
        return taskType;
    }
    
    public void setTaskType(String taskType) {
        this.taskType = taskType;
    }
    
    public Map<String, Double> getMetrics() {
        return metrics;
    }
    
    public void setMetrics(Map<String, Double> metrics) {
        this.metrics = metrics;
    }
    
    public String getSummary() {
        return summary;
    }
    
    public void setSummary(String summary) {
        this.summary = summary;
    }
    
    public List<String> getRecommendations() {
        return recommendations;
    }
    
    public void setRecommendations(List<String> recommendations) {
        this.recommendations = recommendations;
    }
}
