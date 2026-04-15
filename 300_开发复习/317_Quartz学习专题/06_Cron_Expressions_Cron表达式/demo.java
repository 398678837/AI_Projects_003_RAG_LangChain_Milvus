package com.example.quartz.cron;

import org.quartz.*;
import org.quartz.impl.StdSchedulerFactory;

import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.TimeZone;

public class CronExpressionDemo {

    public static void main(String[] args) {
        System.out.println("=== Quartz Cron表达式示例 ===");

        try {
            cronExpressionExamples();
            cronTriggerDemo();
            timeZoneDemo();
            nextFireTimesDemo();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void cronExpressionExamples() {
        System.out.println("\n--- 1. Cron表达式示例 ---");

        List<CronExample> examples = new ArrayList<>();
        examples.add(new CronExample("每秒执行", "* * * * * ?"));
        examples.add(new CronExample("每分钟执行", "0 * * * * ?"));
        examples.add(new CronExample("每小时执行", "0 0 * * * ?"));
        examples.add(new CronExample("每天中午12点", "0 0 12 * * ?"));
        examples.add(new CronExample("每天早上8点", "0 0 8 * * ?"));
        examples.add(new CronExample("每周一上午10点", "0 0 10 ? * MON"));
        examples.add(new CronExample("每月1号早上9点", "0 0 9 1 * ?"));
        examples.add(new CronExample("每5分钟执行", "0 0/5 * * * ?"));
        examples.add(new CronExample("工作日早上9点", "0 0 9 ? * MON-FRI"));
        examples.add(new CronExample("每月最后一天下午6点", "0 0 18 L * ?"));
        examples.add(new CronExample("每月第三个周五上午10点", "0 0 10 ? * FRI#3"));
        examples.add(new CronExample("每天9点到18点，每小时执行", "0 0 9-18 * * ?"));

        System.out.println("常用Cron表达式:");
        for (CronExample example : examples) {
            System.out.println("  " + example.description + ": " + example.expression);
        }
    }

    private static void cronTriggerDemo() throws SchedulerException, InterruptedException {
        System.out.println("\n--- 2. CronTrigger演示 ---");

        Scheduler scheduler = StdSchedulerFactory.getDefaultScheduler();
        scheduler.start();

        JobDetail job = JobBuilder.newJob(CronJob.class)
                .withIdentity("cronJob", "cronGroup")
                .build();

        Trigger trigger = TriggerBuilder.newTrigger()
                .withIdentity("cronTrigger", "cronGroup")
                .withSchedule(CronScheduleBuilder.cronSchedule("0/3 * * * * ?"))
                .build();

        scheduler.scheduleJob(job, trigger);
        System.out.println("CronTrigger已调度，每3秒执行一次");
        System.out.println("Cron表达式: " + ((CronTrigger) trigger).getCronExpression());

        Thread.sleep(10000);

        scheduler.shutdown();
    }

    private static void timeZoneDemo() throws SchedulerException, InterruptedException {
        System.out.println("\n--- 3. 时区演示 ---");

        Scheduler scheduler = StdSchedulerFactory.getDefaultScheduler();
        scheduler.start();

        JobDetail job = JobBuilder.newJob(CronJob.class)
                .withIdentity("timezoneJob", "cronGroup")
                .build();

        TimeZone timeZone = TimeZone.getTimeZone("Asia/Shanghai");

        Trigger trigger = TriggerBuilder.newTrigger()
                .withIdentity("timezoneTrigger", "cronGroup")
                .withSchedule(CronScheduleBuilder.cronSchedule("0/5 * * * * ?")
                        .inTimeZone(timeZone))
                .build();

        scheduler.scheduleJob(job, trigger);
        System.out.println("带时区的CronTrigger已调度");
        System.out.println("时区: " + timeZone.getID());

        Thread.sleep(6000);

        scheduler.shutdown();
    }

    private static void nextFireTimesDemo() throws SchedulerException {
        System.out.println("\n--- 4. 下次执行时间演示 ---");

        CronTrigger trigger = TriggerBuilder.newTrigger()
                .withIdentity("nextFireTrigger", "cronGroup")
                .withSchedule(CronScheduleBuilder.cronSchedule("0 0 9 * * ?"))
                .build();

        System.out.println("Cron表达式: " + trigger.getCronExpression());
        System.out.println("接下来10次执行时间:");

        Date nextFireTime = trigger.getNextFireTime();
        SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");

        for (int i = 0; i < 10 && nextFireTime != null; i++) {
            System.out.println("  " + (i + 1) + ". " + sdf.format(nextFireTime));
            nextFireTime = trigger.getFireTimeAfter(nextFireTime);
        }
    }

    static class CronExample {
        String description;
        String expression;

        CronExample(String description, String expression) {
            this.description = description;
            this.expression = expression;
        }
    }
}

class CronJob implements Job {

    public CronJob() {
    }

    @Override
    public void execute(JobExecutionContext context) throws JobExecutionException {
        Trigger trigger = context.getTrigger();
        String cronExpression = trigger instanceof CronTrigger ?
                ((CronTrigger) trigger).getCronExpression() : "N/A";

        System.out.println("[" + new Date() + "] CronJob执行");
        System.out.println("  Cron表达式: " + cronExpression);
    }
}
