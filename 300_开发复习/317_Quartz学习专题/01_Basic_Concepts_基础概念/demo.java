package com.example.quartz.basic;

import org.quartz.*;
import org.quartz.impl.StdSchedulerFactory;

import java.util.Date;

public class QuartzBasicDemo {

    public static void main(String[] args) {
        System.out.println("=== Quartz基础概念示例 ===");

        try {
            simpleJobDemo();
            jobWithDataDemo();
            multipleJobsDemo();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void simpleJobDemo() throws SchedulerException, InterruptedException {
        System.out.println("\n--- 1. 简单任务演示 ---");

        Scheduler scheduler = StdSchedulerFactory.getDefaultScheduler();
        scheduler.start();

        JobDetail job = JobBuilder.newJob(HelloJob.class)
                .withIdentity("helloJob", "group1")
                .build();

        Trigger trigger = TriggerBuilder.newTrigger()
                .withIdentity("helloTrigger", "group1")
                .startNow()
                .withSchedule(SimpleScheduleBuilder.simpleSchedule()
                        .withIntervalInSeconds(2)
                        .repeatForever())
                .build();

        scheduler.scheduleJob(job, trigger);
        System.out.println("任务已调度，每2秒执行一次");

        Thread.sleep(6000);

        scheduler.shutdown();
        System.out.println("调度器已关闭");
    }

    private static void jobWithDataDemo() throws SchedulerException, InterruptedException {
        System.out.println("\n--- 2. 带参数的任务演示 ---");

        Scheduler scheduler = StdSchedulerFactory.getDefaultScheduler();
        scheduler.start();

        JobDataMap jobDataMap = new JobDataMap();
        jobDataMap.put("name", "张三");
        jobDataMap.put("message", "这是一条定时消息");

        JobDetail job = JobBuilder.newJob(DataJob.class)
                .withIdentity("dataJob", "group2")
                .usingJobData(jobDataMap)
                .build();

        Trigger trigger = TriggerBuilder.newTrigger()
                .withIdentity("dataTrigger", "group2")
                .startNow()
                .withSchedule(SimpleScheduleBuilder.simpleSchedule()
                        .withIntervalInSeconds(3)
                        .withRepeatCount(2))
                .build();

        scheduler.scheduleJob(job, trigger);
        System.out.println("带参数的任务已调度，执行3次");

        Thread.sleep(10000);

        scheduler.shutdown();
        System.out.println("调度器已关闭");
    }

    private static void multipleJobsDemo() throws SchedulerException, InterruptedException {
        System.out.println("\n--- 3. 多任务演示 ---");

        Scheduler scheduler = StdSchedulerFactory.getDefaultScheduler();
        scheduler.start();

        JobDetail job1 = JobBuilder.newJob(Job1.class)
                .withIdentity("job1", "group3")
                .build();

        Trigger trigger1 = TriggerBuilder.newTrigger()
                .withIdentity("trigger1", "group3")
                .startNow()
                .withSchedule(SimpleScheduleBuilder.simpleSchedule()
                        .withIntervalInSeconds(2)
                        .repeatForever())
                .build();

        JobDetail job2 = JobBuilder.newJob(Job2.class)
                .withIdentity("job2", "group3")
                .build();

        Trigger trigger2 = TriggerBuilder.newTrigger()
                .withIdentity("trigger2", "group3")
                .startNow()
                .withSchedule(SimpleScheduleBuilder.simpleSchedule()
                        .withIntervalInSeconds(4)
                        .repeatForever())
                .build();

        scheduler.scheduleJob(job1, trigger1);
        scheduler.scheduleJob(job2, trigger2);
        System.out.println("多个任务已调度");

        Thread.sleep(10000);

        scheduler.shutdown();
        System.out.println("调度器已关闭");
    }
}

class HelloJob implements Job {

    public HelloJob() {
    }

    @Override
    public void execute(JobExecutionContext context) throws JobExecutionException {
        System.out.println("[" + new Date() + "] Hello, Quartz!");
    }
}

class DataJob implements Job {

    public DataJob() {
    }

    @Override
    public void execute(JobExecutionContext context) throws JobExecutionException {
        JobDataMap dataMap = context.getJobDetail().getJobDataMap();
        String name = dataMap.getString("name");
        String message = dataMap.getString("message");

        System.out.println("[" + new Date() + "] " + name + "，" + message);
    }
}

class Job1 implements Job {

    public Job1() {
    }

    @Override
    public void execute(JobExecutionContext context) throws JobExecutionException {
        System.out.println("[" + new Date() + "] 任务1执行中...");
    }
}

class Job2 implements Job {

    public Job2() {
    }

    @Override
    public void execute(JobExecutionContext context) throws JobExecutionException {
        System.out.println("[" + new Date() + "] 任务2执行中...");
    }
}
