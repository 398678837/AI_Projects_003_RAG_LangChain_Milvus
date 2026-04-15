package com.example.quartz.core;

import org.quartz.*;
import org.quartz.impl.StdSchedulerFactory;

import java.util.Date;

public class CoreComponentsDemo {

    public static void main(String[] args) {
        System.out.println("=== Quartz核心组件示例 ===");

        try {
            jobDetailDemo();
            jobDataMapDemo();
            triggerIdentityDemo();
            concurrentJobDemo();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void jobDetailDemo() throws SchedulerException, InterruptedException {
        System.out.println("\n--- 1. JobDetail演示 ---");

        Scheduler scheduler = StdSchedulerFactory.getDefaultScheduler();
        scheduler.start();

        JobDetail job = JobBuilder.newJob(MyJob.class)
                .withIdentity("myJob", "demoGroup")
                .withDescription("这是一个演示Job")
                .storeDurably()
                .requestRecovery()
                .build();

        System.out.println("Job名称: " + job.getKey().getName());
        System.out.println("Job组: " + job.getKey().getGroup());
        System.out.println("Job描述: " + job.getDescription());
        System.out.println("Job类: " + job.getJobClass().getName());
        System.out.println("是否持久化: " + job.isDurable());
        System.out.println("是否请求恢复: " + job.requestsRecovery());

        Trigger trigger = TriggerBuilder.newTrigger()
                .withIdentity("myTrigger", "demoGroup")
                .startNow()
                .withSchedule(SimpleScheduleBuilder.simpleSchedule()
                        .withIntervalInSeconds(2)
                        .withRepeatCount(2))
                .build();

        scheduler.scheduleJob(job, trigger);

        Thread.sleep(7000);

        scheduler.shutdown();
    }

    private static void jobDataMapDemo() throws SchedulerException, InterruptedException {
        System.out.println("\n--- 2. JobDataMap演示 ---");

        Scheduler scheduler = StdSchedulerFactory.getDefaultScheduler();
        scheduler.start();

        JobDetail job = JobBuilder.newJob(DataJob.class)
                .withIdentity("dataJob", "dataGroup")
                .usingJobData("name", "李四")
                .usingJobData("age", 25)
                .usingJobData("salary", 10000.0)
                .build();

        Trigger trigger = TriggerBuilder.newTrigger()
                .withIdentity("dataTrigger", "dataGroup")
                .usingJobData("bonus", 5000.0)
                .startNow()
                .withSchedule(SimpleScheduleBuilder.simpleSchedule()
                        .withIntervalInSeconds(2)
                        .withRepeatCount(1))
                .build();

        scheduler.scheduleJob(job, trigger);

        Thread.sleep(5000);

        scheduler.shutdown();
    }

    private static void triggerIdentityDemo() throws SchedulerException, InterruptedException {
        System.out.println("\n--- 3. Trigger标识演示 ---");

        Scheduler scheduler = StdSchedulerFactory.getDefaultScheduler();
        scheduler.start();

        JobDetail job = JobBuilder.newJob(TriggerJob.class)
                .withIdentity("triggerJob", "triggerGroup")
                .build();

        Trigger trigger1 = TriggerBuilder.newTrigger()
                .withIdentity("trigger1", "triggerGroup")
                .withDescription("触发器1")
                .startNow()
                .withSchedule(SimpleScheduleBuilder.simpleSchedule()
                        .withIntervalInSeconds(2)
                        .repeatForever())
                .build();

        Trigger trigger2 = TriggerBuilder.newTrigger()
                .withIdentity("trigger2", "triggerGroup")
                .withDescription("触发器2")
                .startAt(DateBuilder.futureDate(3, DateBuilder.IntervalUnit.SECOND))
                .withSchedule(SimpleScheduleBuilder.simpleSchedule()
                        .withIntervalInSeconds(3)
                        .repeatForever())
                .forJob(job)
                .build();

        scheduler.scheduleJob(job, trigger1);
        scheduler.scheduleJob(trigger2);

        System.out.println("Trigger1: " + trigger1.getKey());
        System.out.println("Trigger2: " + trigger2.getKey());

        Thread.sleep(8000);

        scheduler.shutdown();
    }

    private static void concurrentJobDemo() throws SchedulerException, InterruptedException {
        System.out.println("\n--- 4. 并发Job演示 ---");

        Scheduler scheduler = StdSchedulerFactory.getDefaultScheduler();
        scheduler.start();

        JobDetail job1 = JobBuilder.newJob(NonConcurrentJob.class)
                .withIdentity("nonConcurrentJob", "concurrentGroup")
                .build();

        Trigger trigger1 = TriggerBuilder.newTrigger()
                .withIdentity("nonConcurrentTrigger", "concurrentGroup")
                .startNow()
                .withSchedule(SimpleScheduleBuilder.simpleSchedule()
                        .withIntervalInSeconds(1)
                        .repeatForever())
                .build();

        JobDetail job2 = JobBuilder.newJob(ConcurrentJob.class)
                .withIdentity("concurrentJob", "concurrentGroup")
                .build();

        Trigger trigger2 = TriggerBuilder.newTrigger()
                .withIdentity("concurrentTrigger", "concurrentGroup")
                .startNow()
                .withSchedule(SimpleScheduleBuilder.simpleSchedule()
                        .withIntervalInSeconds(1)
                        .repeatForever())
                .build();

        scheduler.scheduleJob(job1, trigger1);
        scheduler.scheduleJob(job2, trigger2);

        System.out.println("并发任务已启动");

        Thread.sleep(5000);

        scheduler.shutdown();
    }
}

class MyJob implements Job {

    public MyJob() {
    }

    @Override
    public void execute(JobExecutionContext context) throws JobExecutionException {
        JobKey jobKey = context.getJobDetail().getKey();
        System.out.println("[" + new Date() + "] Job执行: " + jobKey);
    }
}

class DataJob implements Job {

    public DataJob() {
    }

    @Override
    public void execute(JobExecutionContext context) throws JobExecutionException {
        JobDataMap jobDataMap = context.getMergedJobDataMap();

        String name = jobDataMap.getString("name");
        int age = jobDataMap.getInt("age");
        double salary = jobDataMap.getDouble("salary");
        double bonus = jobDataMap.getDouble("bonus");

        System.out.println("[" + new Date() + "] 姓名: " + name);
        System.out.println("年龄: " + age);
        System.out.println("薪资: " + salary);
        System.out.println("奖金: " + bonus);
        System.out.println("总收入: " + (salary + bonus));
    }
}

class TriggerJob implements Job {

    public TriggerJob() {
    }

    @Override
    public void execute(JobExecutionContext context) throws JobExecutionException {
        TriggerKey triggerKey = context.getTrigger().getKey();
        System.out.println("[" + new Date() + "] 触发: " + triggerKey);
    }
}

@DisallowConcurrentExecution
@PersistJobDataAfterExecution
class NonConcurrentJob implements Job {

    public NonConcurrentJob() {
    }

    @Override
    public void execute(JobExecutionContext context) throws JobExecutionException {
        System.out.println("[" + new Date() + "] 非并发任务开始");
        try {
            Thread.sleep(2000);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
        System.out.println("[" + new Date() + "] 非并发任务结束");
    }
}

class ConcurrentJob implements Job {

    public ConcurrentJob() {
    }

    @Override
    public void execute(JobExecutionContext context) throws JobExecutionException {
        System.out.println("[" + new Date() + "] 并发任务开始");
        try {
            Thread.sleep(2000);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
        System.out.println("[" + new Date() + "] 并发任务结束");
    }
}
