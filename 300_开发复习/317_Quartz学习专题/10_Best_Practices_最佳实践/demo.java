package com.example.quartz.bestpractice;

import org.quartz.*;
import org.quartz.impl.StdSchedulerFactory;
import org.quartz.impl.matchers.EverythingMatcher;

import java.util.Date;

public class BestPracticeDemo {

    public static void main(String[] args) {
        System.out.println("=== Quartz最佳实践示例 ===");

        try {
            wellDesignedJobDemo();
            errorHandlingDemo();
            listenerDemo();
            schedulerConfigDemo();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void wellDesignedJobDemo() throws SchedulerException, InterruptedException {
        System.out.println("\n--- 1. 设计良好的Job演示 ---");

        Scheduler scheduler = StdSchedulerFactory.getDefaultScheduler();

        JobListener jobListener = new MonitoringJobListener();
        scheduler.getListenerManager().addJobListener(jobListener, EverythingMatcher.allJobs());

        TriggerListener triggerListener = new MonitoringTriggerListener();
        scheduler.getListenerManager().addTriggerListener(triggerListener, EverythingMatcher.allTriggers());

        scheduler.start();

        JobDetail job = JobBuilder.newJob(WellDesignedJob.class)
                .withIdentity("wellDesignedJob", "bestPracticeGroup")
                .usingJobData("serviceName", "UserService")
                .usingJobData("methodName", "cleanup")
                .storeDurably()
                .build();

        Trigger trigger = TriggerBuilder.newTrigger()
                .withIdentity("wellDesignedTrigger", "bestPracticeGroup")
                .startNow()
                .withSchedule(SimpleScheduleBuilder.simpleSchedule()
                        .withIntervalInSeconds(3)
                        .withRepeatCount(2)
                        .withMisfireHandlingInstructionFireNow())
                .build();

        scheduler.scheduleJob(job, trigger);
        System.out.println("设计良好的Job已调度");

        Thread.sleep(10000);

        scheduler.shutdown();
    }

    private static void errorHandlingDemo() throws SchedulerException, InterruptedException {
        System.out.println("\n--- 2. 错误处理演示 ---");

        Scheduler scheduler = StdSchedulerFactory.getDefaultScheduler();
        scheduler.start();

        JobDetail job1 = JobBuilder.newJob(ErrorHandlingJob.class)
                .withIdentity("errorJob1", "bestPracticeGroup")
                .usingJobData("errorType", "retry")
                .build();

        Trigger trigger1 = TriggerBuilder.newTrigger()
                .withIdentity("errorTrigger1", "bestPracticeGroup")
                .startNow()
                .build();

        scheduler.scheduleJob(job1, trigger1);
        System.out.println("错误处理Job1已调度（重试策略）");

        Thread.sleep(3000);

        JobDetail job2 = JobBuilder.newJob(ErrorHandlingJob.class)
                .withIdentity("errorJob2", "bestPracticeGroup")
                .usingJobData("errorType", "unschedule")
                .build();

        Trigger trigger2 = TriggerBuilder.newTrigger()
                .withIdentity("errorTrigger2", "bestPracticeGroup")
                .startNow()
                .build();

        scheduler.scheduleJob(job2, trigger2);
        System.out.println("\n错误处理Job2已调度（取消策略）");

        Thread.sleep(3000);

        scheduler.shutdown();
    }

    private static void listenerDemo() throws SchedulerException, InterruptedException {
        System.out.println("\n--- 3. 监听器演示 ---");

        Scheduler scheduler = StdSchedulerFactory.getDefaultScheduler();

        SchedulerListener schedulerListener = new MonitoringSchedulerListener();
        scheduler.getListenerManager().addSchedulerListener(schedulerListener);

        scheduler.start();

        JobDetail job = JobBuilder.newJob(ListenerJob.class)
                .withIdentity("listenerJob", "bestPracticeGroup")
                .build();

        Trigger trigger = TriggerBuilder.newTrigger()
                .withIdentity("listenerTrigger", "bestPracticeGroup")
                .startNow()
                .withSchedule(SimpleScheduleBuilder.simpleSchedule()
                        .withIntervalInSeconds(2)
                        .withRepeatCount(1))
                .build();

        scheduler.scheduleJob(job, trigger);

        Thread.sleep(6000);

        scheduler.shutdown();
    }

    private static void schedulerConfigDemo() {
        System.out.println("\n--- 4. 调度器配置最佳实践 ---");

        System.out.println("线程池配置:");
        System.out.println("  org.quartz.threadPool.class = org.quartz.simpl.SimpleThreadPool");
        System.out.println("  org.quartz.threadPool.threadCount = 10");
        System.out.println("  org.quartz.threadPool.threadPriority = 5");

        System.out.println("\nJobStore配置（生产环境）:");
        System.out.println("  org.quartz.jobStore.class = org.quartz.impl.jdbcjobstore.JobStoreTX");
        System.out.println("  org.quartz.jobStore.driverDelegateClass = org.quartz.impl.jdbcjobstore.StdJDBCDelegate");
        System.out.println("  org.quartz.jobStore.tablePrefix = QRTZ_");
        System.out.println("  org.quartz.jobStore.isClustered = true");
        System.out.println("  org.quartz.jobStore.clusterCheckinInterval = 20000");
        System.out.println("  org.quartz.jobStore.useProperties = true");
        System.out.println("  org.quartz.jobStore.misfireThreshold = 60000");

        System.out.println("\n数据源配置:");
        System.out.println("  org.quartz.dataSource.myDS.driver = com.mysql.cj.jdbc.Driver");
        System.out.println("  org.quartz.dataSource.myDS.URL = jdbc:mysql://localhost:3306/quartz");
        System.out.println("  org.quartz.dataSource.myDS.user = root");
        System.out.println("  org.quartz.dataSource.myDS.password = password");
        System.out.println("  org.quartz.dataSource.myDS.maxConnections = 15");
        System.out.println("  org.quartz.dataSource.myDS.validationQuery = SELECT 1");

        System.out.println("\n最佳实践要点:");
        System.out.println("  1. Job保持简单，业务逻辑放Service层");
        System.out.println("  2. 使用@DisallowConcurrentExecution防止并发");
        System.out.println("  3. 合理配置线程池大小");
        System.out.println("  4. 生产环境使用JDBC持久化");
        System.out.println("  5. 使用集群提高可用性");
        System.out.println("  6. 配置合适的Misfire策略");
        System.out.println("  7. 使用监听器监控执行");
        System.out.println("  8. 完善的日志记录");
        System.out.println("  9. 定期清理历史数据");
        System.out.println(" 10. 监控和告警机制");
    }
}

@DisallowConcurrentExecution
@PersistJobDataAfterExecution
class WellDesignedJob implements Job {

    public WellDesignedJob() {
    }

    @Override
    public void execute(JobExecutionContext context) throws JobExecutionException {
        long startTime = System.currentTimeMillis();
        System.out.println("[" + new Date() + "] WellDesignedJob开始执行");

        try {
            JobDataMap dataMap = context.getJobDetail().getJobDataMap();
            String serviceName = dataMap.getString("serviceName");
            String methodName = dataMap.getString("methodName");

            System.out.println("  Service: " + serviceName);
            System.out.println("  Method: " + methodName);

            businessLogic(serviceName, methodName);

            long duration = System.currentTimeMillis() - startTime;
            System.out.println("  WellDesignedJob执行成功，耗时: " + duration + "ms");

        } catch (Exception e) {
            System.err.println("  WellDesignedJob执行失败: " + e.getMessage());
            throw new JobExecutionException(e, false);
        }
    }

    private void businessLogic(String serviceName, String methodName) {
        System.out.println("  执行业务逻辑...");
        try {
            Thread.sleep(500);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }
}

class ErrorHandlingJob implements Job {

    public ErrorHandlingJob() {
    }

    @Override
    public void execute(JobExecutionContext context) throws JobExecutionException {
        JobDataMap dataMap = context.getJobDetail().getJobDataMap();
        String errorType = dataMap.getString("errorType");

        System.out.println("[" + new Date() + "] ErrorHandlingJob执行，类型: " + errorType);

        JobExecutionException e = new JobExecutionException("模拟错误");

        if ("retry".equals(errorType)) {
            e.setRefireImmediately(true);
            System.out.println("  设置立即重试");
        } else if ("unschedule".equals(errorType)) {
            e.setUnscheduleFiringTrigger(true);
            System.out.println("  设置取消调度");
        }

        throw e;
    }
}

class ListenerJob implements Job {

    public ListenerJob() {
    }

    @Override
    public void execute(JobExecutionContext context) throws JobExecutionException {
        System.out.println("[" + new Date() + "] ListenerJob执行");
    }
}

class MonitoringJobListener implements JobListener {

    @Override
    public String getName() {
        return "MonitoringJobListener";
    }

    @Override
    public void jobToBeExecuted(JobExecutionContext context) {
        System.out.println("[JobListener] jobToBeExecuted: " + context.getJobDetail().getKey());
    }

    @Override
    public void jobExecutionVetoed(JobExecutionContext context) {
        System.out.println("[JobListener] jobExecutionVetoed: " + context.getJobDetail().getKey());
    }

    @Override
    public void jobWasExecuted(JobExecutionContext context, JobExecutionException jobException) {
        System.out.println("[JobListener] jobWasExecuted: " + context.getJobDetail().getKey());
        if (jobException != null) {
            System.err.println("  异常: " + jobException.getMessage());
        }
    }
}

class MonitoringTriggerListener implements TriggerListener {

    @Override
    public String getName() {
        return "MonitoringTriggerListener";
    }

    @Override
    public void triggerFired(Trigger trigger, JobExecutionContext context) {
        System.out.println("[TriggerListener] triggerFired: " + trigger.getKey());
    }

    @Override
    public boolean vetoJobExecution(Trigger trigger, JobExecutionContext context) {
        return false;
    }

    @Override
    public void triggerMisfired(Trigger trigger) {
        System.out.println("[TriggerListener] triggerMisfired: " + trigger.getKey());
    }

    @Override
    public void triggerComplete(Trigger trigger, JobExecutionContext context, Trigger.CompletedExecutionInstruction triggerInstructionCode) {
        System.out.println("[TriggerListener] triggerComplete: " + trigger.getKey());
    }
}

class MonitoringSchedulerListener implements SchedulerListener {

    @Override
    public void jobScheduled(Trigger trigger) {
        System.out.println("[SchedulerListener] jobScheduled: " + trigger.getKey());
    }

    @Override
    public void jobUnscheduled(TriggerKey triggerKey) {
        System.out.println("[SchedulerListener] jobUnscheduled: " + triggerKey);
    }

    @Override
    public void triggerFinalized(Trigger trigger) {
        System.out.println("[SchedulerListener] triggerFinalized: " + trigger.getKey());
    }

    @Override
    public void triggerPaused(TriggerKey triggerKey) {
        System.out.println("[SchedulerListener] triggerPaused: " + triggerKey);
    }

    @Override
    public void triggersPaused(String triggerGroup) {
        System.out.println("[SchedulerListener] triggersPaused: " + triggerGroup);
    }

    @Override
    public void triggerResumed(TriggerKey triggerKey) {
        System.out.println("[SchedulerListener] triggerResumed: " + triggerKey);
    }

    @Override
    public void triggersResumed(String triggerGroup) {
        System.out.println("[SchedulerListener] triggersResumed: " + triggerGroup);
    }

    @Override
    public void jobAdded(JobDetail jobDetail) {
        System.out.println("[SchedulerListener] jobAdded: " + jobDetail.getKey());
    }

    @Override
    public void jobDeleted(JobKey jobKey) {
        System.out.println("[SchedulerListener] jobDeleted: " + jobKey);
    }

    @Override
    public void jobPaused(JobKey jobKey) {
        System.out.println("[SchedulerListener] jobPaused: " + jobKey);
    }

    @Override
    public void jobsPaused(String jobGroup) {
        System.out.println("[SchedulerListener] jobsPaused: " + jobGroup);
    }

    @Override
    public void jobResumed(JobKey jobKey) {
        System.out.println("[SchedulerListener] jobResumed: " + jobKey);
    }

    @Override
    public void jobsResumed(String jobGroup) {
        System.out.println("[SchedulerListener] jobsResumed: " + jobGroup);
    }

    @Override
    public void schedulerError(String msg, SchedulerException cause) {
        System.err.println("[SchedulerListener] schedulerError: " + msg);
    }

    @Override
    public void schedulerInStandbyMode() {
        System.out.println("[SchedulerListener] schedulerInStandbyMode");
    }

    @Override
    public void schedulerStarted() {
        System.out.println("[SchedulerListener] schedulerStarted");
    }

    @Override
    public void schedulerStarting() {
        System.out.println("[SchedulerListener] schedulerStarting");
    }

    @Override
    public void schedulerShutdown() {
        System.out.println("[SchedulerListener] schedulerShutdown");
    }

    @Override
    public void schedulerShuttingdown() {
        System.out.println("[SchedulerListener] schedulerShuttingdown");
    }

    @Override
    public void schedulingDataCleared() {
        System.out.println("[SchedulerListener] schedulingDataCleared");
    }
}
