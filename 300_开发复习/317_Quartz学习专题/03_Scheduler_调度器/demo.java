package com.example.quartz.scheduler;

import org.quartz.*;
import org.quartz.impl.StdSchedulerFactory;

import java.util.Date;
import java.util.Set;

public class SchedulerDemo {

    public static void main(String[] args) {
        System.out.println("=== Quartz调度器示例 ===");

        try {
            schedulerLifecycleDemo();
            scheduleOperationsDemo();
            pauseResumeDemo();
            schedulerMetaDataDemo();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void schedulerLifecycleDemo() throws SchedulerException, InterruptedException {
        System.out.println("\n--- 1. Scheduler生命周期演示 ---");

        Scheduler scheduler = StdSchedulerFactory.getDefaultScheduler();

        System.out.println("Scheduler是否启动: " + scheduler.isStarted());
        System.out.println("Scheduler是否待机: " + scheduler.isInStandbyMode());
        System.out.println("Scheduler是否关闭: " + scheduler.isShutdown());

        scheduler.start();
        System.out.println("\n调用start()后");
        System.out.println("Scheduler是否启动: " + scheduler.isStarted());

        scheduler.standby();
        System.out.println("\n调用standby()后");
        System.out.println("Scheduler是否待机: " + scheduler.isInStandbyMode());

        scheduler.start();
        System.out.println("\n再次调用start()后");
        System.out.println("Scheduler是否待机: " + scheduler.isInStandbyMode());

        JobDetail job = JobBuilder.newJob(LifecycleJob.class)
                .withIdentity("lifecycleJob", "lifecycleGroup")
                .build();

        Trigger trigger = TriggerBuilder.newTrigger()
                .withIdentity("lifecycleTrigger", "lifecycleGroup")
                .startNow()
                .withSchedule(SimpleScheduleBuilder.simpleSchedule()
                        .withIntervalInSeconds(2)
                        .repeatForever())
                .build();

        scheduler.scheduleJob(job, trigger);
        System.out.println("\n任务已调度");

        Thread.sleep(5000);

        scheduler.shutdown();
        System.out.println("\n调用shutdown()后");
        System.out.println("Scheduler是否关闭: " + scheduler.isShutdown());
    }

    private static void scheduleOperationsDemo() throws SchedulerException, InterruptedException {
        System.out.println("\n--- 2. 调度操作演示 ---");

        Scheduler scheduler = StdSchedulerFactory.getDefaultScheduler();
        scheduler.start();

        JobDetail job1 = JobBuilder.newJob(OperationJob.class)
                .withIdentity("job1", "operationGroup")
                .usingJobData("name", "任务1")
                .storeDurably()
                .build();

        Trigger trigger1 = TriggerBuilder.newTrigger()
                .withIdentity("trigger1", "operationGroup")
                .startNow()
                .withSchedule(SimpleScheduleBuilder.simpleSchedule()
                        .withIntervalInSeconds(2)
                        .repeatForever())
                .build();

        Date firstRunTime = scheduler.scheduleJob(job1, trigger1);
        System.out.println("任务1已调度，首次执行时间: " + firstRunTime);

        JobDetail job2 = JobBuilder.newJob(OperationJob.class)
                .withIdentity("job2", "operationGroup")
                .usingJobData("name", "任务2")
                .storeDurably()
                .build();

        scheduler.addJob(job2, false);
        System.out.println("任务2已添加（无触发器）");

        System.out.println("\n检查job1是否存在: " + scheduler.checkExists(job1.getKey()));
        System.out.println("检查job2是否存在: " + scheduler.checkExists(job2.getKey()));

        System.out.println("\n立即触发job2");
        scheduler.triggerJob(job2.getKey());

        Thread.sleep(3000);

        System.out.println("\n取消job1的调度");
        boolean unscheduled = scheduler.unscheduleJob(trigger1.getKey());
        System.out.println("是否取消成功: " + unscheduled);

        System.out.println("\n删除job2");
        boolean deleted = scheduler.deleteJob(job2.getKey());
        System.out.println("是否删除成功: " + deleted);

        Thread.sleep(3000);

        scheduler.shutdown();
    }

    private static void pauseResumeDemo() throws SchedulerException, InterruptedException {
        System.out.println("\n--- 3. 暂停/恢复演示 ---");

        Scheduler scheduler = StdSchedulerFactory.getDefaultScheduler();
        scheduler.start();

        JobDetail job = JobBuilder.newJob(PauseResumeJob.class)
                .withIdentity("pauseJob", "pauseGroup")
                .build();

        Trigger trigger = TriggerBuilder.newTrigger()
                .withIdentity("pauseTrigger", "pauseGroup")
                .startNow()
                .withSchedule(SimpleScheduleBuilder.simpleSchedule()
                        .withIntervalInSeconds(1)
                        .repeatForever())
                .build();

        scheduler.scheduleJob(job, trigger);
        System.out.println("任务已调度并开始执行");

        Thread.sleep(3000);

        System.out.println("\n暂停任务");
        scheduler.pauseJob(job.getKey());

        Thread.sleep(3000);

        System.out.println("\n恢复任务");
        scheduler.resumeJob(job.getKey());

        Thread.sleep(3000);

        System.out.println("\n暂停触发器组");
        scheduler.pauseTriggers(GroupMatcher.triggerGroupEquals("pauseGroup"));

        Thread.sleep(3000);

        System.out.println("\n恢复触发器组");
        scheduler.resumeTriggers(GroupMatcher.triggerGroupEquals("pauseGroup"));

        Thread.sleep(3000);

        scheduler.shutdown();
    }

    private static void schedulerMetaDataDemo() throws SchedulerException {
        System.out.println("\n--- 4. Scheduler元数据演示 ---");

        Scheduler scheduler = StdSchedulerFactory.getDefaultScheduler();
        SchedulerMetaData metaData = scheduler.getMetaData();

        System.out.println("Scheduler名称: " + metaData.getSchedulerName());
        System.out.println("Scheduler实例ID: " + metaData.getSchedulerInstanceId());
        System.out.println("Quartz版本: " + metaData.getVersion());
        System.out.println("是否持久化: " + metaData.isJobStoreClustered());
        System.out.println("是否集群: " + metaData.isJobStoreClustered());
        System.out.println("线程池大小: " + metaData.getThreadPoolSize());
        System.out.println("是否启动: " + metaData.isStarted());
        System.out.println("是否待机: " + metaData.isInStandbyMode());
        System.out.println("是否关闭: " + metaData.isShutdown());

        scheduler.shutdown();
    }
}

class LifecycleJob implements Job {

    public LifecycleJob() {
    }

    @Override
    public void execute(JobExecutionContext context) throws JobExecutionException {
        System.out.println("[" + new Date() + "] 生命周期任务执行");
    }
}

class OperationJob implements Job {

    public OperationJob() {
    }

    @Override
    public void execute(JobExecutionContext context) throws JobExecutionException {
        JobDataMap dataMap = context.getJobDetail().getJobDataMap();
        String name = dataMap.getString("name");
        System.out.println("[" + new Date() + "] " + name + " 执行");
    }
}

class PauseResumeJob implements Job {

    public PauseResumeJob() {
    }

    @Override
    public void execute(JobExecutionContext context) throws JobExecutionException {
        System.out.println("[" + new Date() + "] 暂停/恢复任务执行");
    }
}
