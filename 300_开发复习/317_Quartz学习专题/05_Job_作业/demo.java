package com.example.quartz.job;

import org.quartz.*;
import org.quartz.impl.StdSchedulerFactory;
import org.quartz.impl.matchers.KeyMatcher;

import java.util.Date;

public class JobDemo {

    public static void main(String[] args) {
        System.out.println("=== Quartz作业示例 ===");

        try {
            basicJobDemo();
            statefulJobDemo();
            exceptionHandlingDemo();
            jobListenerDemo();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void basicJobDemo() throws SchedulerException, InterruptedException {
        System.out.println("\n--- 1. 基础Job演示 ---");

        Scheduler scheduler = StdSchedulerFactory.getDefaultScheduler();
        scheduler.start();

        JobDetail job = JobBuilder.newJob(BasicJob.class)
                .withIdentity("basicJob", "jobGroup")
                .usingJobData("message", "Hello from JobDataMap!")
                .build();

        Trigger trigger = TriggerBuilder.newTrigger()
                .withIdentity("basicTrigger", "jobGroup")
                .startNow()
                .withSchedule(SimpleScheduleBuilder.simpleSchedule()
                        .withIntervalInSeconds(2)
                        .withRepeatCount(2))
                .build();

        scheduler.scheduleJob(job, trigger);

        Thread.sleep(7000);

        scheduler.shutdown();
    }

    private static void statefulJobDemo() throws SchedulerException, InterruptedException {
        System.out.println("\n--- 2. 有状态Job演示 ---");

        Scheduler scheduler = StdSchedulerFactory.getDefaultScheduler();
        scheduler.start();

        JobDetail job = JobBuilder.newJob(StatefulJob.class)
                .withIdentity("statefulJob", "jobGroup")
                .usingJobData("count", 0)
                .storeDurably()
                .build();

        Trigger trigger = TriggerBuilder.newTrigger()
                .withIdentity("statefulTrigger", "jobGroup")
                .startNow()
                .withSchedule(SimpleScheduleBuilder.simpleSchedule()
                        .withIntervalInSeconds(2)
                        .withRepeatCount(4))
                .build();

        scheduler.scheduleJob(job, trigger);

        Thread.sleep(11000);

        scheduler.shutdown();
    }

    private static void exceptionHandlingDemo() throws SchedulerException, InterruptedException {
        System.out.println("\n--- 3. 异常处理演示 ---");

        Scheduler scheduler = StdSchedulerFactory.getDefaultScheduler();
        scheduler.start();

        JobDetail job1 = JobBuilder.newJob(ExceptionJob.class)
                .withIdentity("exceptionJob1", "jobGroup")
                .usingJobData("strategy", "refire")
                .build();

        Trigger trigger1 = TriggerBuilder.newTrigger()
                .withIdentity("exceptionTrigger1", "jobGroup")
                .startNow()
                .build();

        scheduler.scheduleJob(job1, trigger1);

        Thread.sleep(3000);

        JobDetail job2 = JobBuilder.newJob(ExceptionJob.class)
                .withIdentity("exceptionJob2", "jobGroup")
                .usingJobData("strategy", "unschedule")
                .build();

        Trigger trigger2 = TriggerBuilder.newTrigger()
                .withIdentity("exceptionTrigger2", "jobGroup")
                .startNow()
                .build();

        scheduler.scheduleJob(job2, trigger2);

        Thread.sleep(3000);

        scheduler.shutdown();
    }

    private static void jobListenerDemo() throws SchedulerException, InterruptedException {
        System.out.println("\n--- 4. Job监听器演示 ---");

        Scheduler scheduler = StdSchedulerFactory.getDefaultScheduler();

        JobListener listener = new MyJobListener();
        scheduler.getListenerManager().addJobListener(
                listener,
                KeyMatcher.keyEquals(JobKey.jobKey("listenerJob", "jobGroup"))
        );

        scheduler.start();

        JobDetail job = JobBuilder.newJob(ListenerJob.class)
                .withIdentity("listenerJob", "jobGroup")
                .build();

        Trigger trigger = TriggerBuilder.newTrigger()
                .withIdentity("listenerTrigger", "jobGroup")
                .startNow()
                .withSchedule(SimpleScheduleBuilder.simpleSchedule()
                        .withIntervalInSeconds(2)
                        .withRepeatCount(2))
                .build();

        scheduler.scheduleJob(job, trigger);

        Thread.sleep(7000);

        scheduler.shutdown();
    }
}

class BasicJob implements Job {

    public BasicJob() {
    }

    @Override
    public void execute(JobExecutionContext context) throws JobExecutionException {
        JobDataMap dataMap = context.getJobDetail().getJobDataMap();
        String message = dataMap.getString("message");
        JobKey jobKey = context.getJobDetail().getKey();
        TriggerKey triggerKey = context.getTrigger().getKey();
        Date fireTime = context.getFireTime();

        System.out.println("[" + new Date() + "] BasicJob执行");
        System.out.println("  Job: " + jobKey);
        System.out.println("  Trigger: " + triggerKey);
        System.out.println("  触发时间: " + fireTime);
        System.out.println("  消息: " + message);
    }
}

@DisallowConcurrentExecution
@PersistJobDataAfterExecution
class StatefulJob implements Job {

    public StatefulJob() {
    }

    @Override
    public void execute(JobExecutionContext context) throws JobExecutionException {
        JobDataMap dataMap = context.getJobDetail().getJobDataMap();
        int count = dataMap.getInt("count");
        count++;
        dataMap.put("count", count);

        System.out.println("[" + new Date() + "] StatefulJob执行，第" + count + "次");
    }
}

class ExceptionJob implements Job {

    public ExceptionJob() {
    }

    @Override
    public void execute(JobExecutionContext context) throws JobExecutionException {
        JobDataMap dataMap = context.getJobDetail().getJobDataMap();
        String strategy = dataMap.getString("strategy");

        System.out.println("[" + new Date() + "] ExceptionJob执行，策略: " + strategy);

        JobExecutionException e = new JobExecutionException("模拟异常");

        if ("refire".equals(strategy)) {
            e.setRefireImmediately(true);
            System.out.println("  设置立即重试");
        } else if ("unschedule".equals(strategy)) {
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

class MyJobListener implements JobListener {

    @Override
    public String getName() {
        return "MyJobListener";
    }

    @Override
    public void jobToBeExecuted(JobExecutionContext context) {
        System.out.println("[" + new Date() + "] [Listener] jobToBeExecuted: " + context.getJobDetail().getKey());
    }

    @Override
    public void jobExecutionVetoed(JobExecutionContext context) {
        System.out.println("[" + new Date() + "] [Listener] jobExecutionVetoed: " + context.getJobDetail().getKey());
    }

    @Override
    public void jobWasExecuted(JobExecutionContext context, JobExecutionException jobException) {
        System.out.println("[" + new Date() + "] [Listener] jobWasExecuted: " + context.getJobDetail().getKey());
        if (jobException != null) {
            System.out.println("  异常: " + jobException.getMessage());
        }
    }
}
