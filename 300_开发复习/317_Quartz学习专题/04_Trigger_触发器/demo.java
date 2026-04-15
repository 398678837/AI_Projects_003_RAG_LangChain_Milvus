package com.example.quartz.trigger;

import org.quartz.*;
import org.quartz.impl.StdSchedulerFactory;

import java.util.Calendar;
import java.util.Date;
import java.util.HashSet;
import java.util.Set;

public class TriggerDemo {

    public static void main(String[] args) {
        System.out.println("=== Quartz触发器示例 ===");

        try {
            simpleTriggerDemo();
            cronTriggerDemo();
            calendarIntervalTriggerDemo();
            dailyTimeIntervalTriggerDemo();
            priorityDemo();
            misfireDemo();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void simpleTriggerDemo() throws SchedulerException, InterruptedException {
        System.out.println("\n--- 1. SimpleTrigger演示 ---");

        Scheduler scheduler = StdSchedulerFactory.getDefaultScheduler();
        scheduler.start();

        JobDetail job = JobBuilder.newJob(TriggerJob.class)
                .withIdentity("simpleJob", "triggerGroup")
                .usingJobData("type", "SimpleTrigger")
                .build();

        SimpleTrigger trigger = TriggerBuilder.newTrigger()
                .withIdentity("simpleTrigger", "triggerGroup")
                .startNow()
                .withSchedule(SimpleScheduleBuilder.simpleSchedule()
                        .withIntervalInSeconds(2)
                        .withRepeatCount(3))
                .build();

        scheduler.scheduleJob(job, trigger);
        System.out.println("SimpleTrigger已调度，每2秒执行一次，共执行4次");

        System.out.println("下次执行时间: " + trigger.getNextFireTime());
        System.out.println("最终执行时间: " + trigger.getFinalFireTime());
        System.out.println("重复次数: " + trigger.getRepeatCount());
        System.out.println("重复间隔: " + trigger.getRepeatInterval() + "ms");

        Thread.sleep(9000);

        scheduler.shutdown();
    }

    private static void cronTriggerDemo() throws SchedulerException, InterruptedException {
        System.out.println("\n--- 2. CronTrigger演示 ---");

        Scheduler scheduler = StdSchedulerFactory.getDefaultScheduler();
        scheduler.start();

        JobDetail job = JobBuilder.newJob(TriggerJob.class)
                .withIdentity("cronJob", "triggerGroup")
                .usingJobData("type", "CronTrigger")
                .build();

        CronTrigger trigger = TriggerBuilder.newTrigger()
                .withIdentity("cronTrigger", "triggerGroup")
                .withSchedule(CronScheduleBuilder.cronSchedule("0/2 * * * * ?"))
                .build();

        scheduler.scheduleJob(job, trigger);
        System.out.println("CronTrigger已调度，每2秒执行一次");
        System.out.println("Cron表达式: " + trigger.getCronExpression());

        Thread.sleep(7000);

        scheduler.shutdown();
    }

    private static void calendarIntervalTriggerDemo() throws SchedulerException, InterruptedException {
        System.out.println("\n--- 3. CalendarIntervalTrigger演示 ---");

        Scheduler scheduler = StdSchedulerFactory.getDefaultScheduler();
        scheduler.start();

        JobDetail job = JobBuilder.newJob(TriggerJob.class)
                .withIdentity("calendarJob", "triggerGroup")
                .usingJobData("type", "CalendarIntervalTrigger")
                .build();

        CalendarIntervalTrigger trigger = TriggerBuilder.newTrigger()
                .withIdentity("calendarTrigger", "triggerGroup")
                .startNow()
                .withSchedule(CalendarIntervalScheduleBuilder.calendarIntervalSchedule()
                        .withIntervalInSeconds(3))
                .build();

        scheduler.scheduleJob(job, trigger);
        System.out.println("CalendarIntervalTrigger已调度，每3秒执行一次");
        System.out.println("间隔: " + trigger.getRepeatInterval() + " " + trigger.getRepeatIntervalUnit());

        Thread.sleep(10000);

        scheduler.shutdown();
    }

    private static void dailyTimeIntervalTriggerDemo() throws SchedulerException, InterruptedException {
        System.out.println("\n--- 4. DailyTimeIntervalTrigger演示 ---");

        Scheduler scheduler = StdSchedulerFactory.getDefaultScheduler();
        scheduler.start();

        JobDetail job = JobBuilder.newJob(TriggerJob.class)
                .withIdentity("dailyJob", "triggerGroup")
                .usingJobData("type", "DailyTimeIntervalTrigger")
                .build();

        Set<Integer> daysOfWeek = new HashSet<>();
        daysOfWeek.add(Calendar.MONDAY);
        daysOfWeek.add(Calendar.TUESDAY);
        daysOfWeek.add(Calendar.WEDNESDAY);
        daysOfWeek.add(Calendar.THURSDAY);
        daysOfWeek.add(Calendar.FRIDAY);

        DailyTimeIntervalTrigger trigger = TriggerBuilder.newTrigger()
                .withIdentity("dailyTrigger", "triggerGroup")
                .startNow()
                .withSchedule(DailyTimeIntervalScheduleBuilder.dailyTimeIntervalSchedule()
                        .withIntervalInSeconds(2)
                        .onDaysOfTheWeek(daysOfWeek))
                .build();

        scheduler.scheduleJob(job, trigger);
        System.out.println("DailyTimeIntervalTrigger已调度，每2秒执行一次");
        System.out.println("执行星期: " + trigger.getDaysOfWeek());

        Thread.sleep(7000);

        scheduler.shutdown();
    }

    private static void priorityDemo() throws SchedulerException, InterruptedException {
        System.out.println("\n--- 5. Trigger优先级演示 ---");

        Scheduler scheduler = StdSchedulerFactory.getDefaultScheduler();
        scheduler.start();

        JobDetail job = JobBuilder.newJob(PriorityJob.class)
                .withIdentity("priorityJob", "priorityGroup")
                .build();

        Trigger trigger1 = TriggerBuilder.newTrigger()
                .withIdentity("trigger1", "priorityGroup")
                .withPriority(1)
                .startNow()
                .forJob(job)
                .build();

        Trigger trigger2 = TriggerBuilder.newTrigger()
                .withIdentity("trigger2", "priorityGroup")
                .withPriority(10)
                .startNow()
                .forJob(job)
                .build();

        Trigger trigger3 = TriggerBuilder.newTrigger()
                .withIdentity("trigger3", "priorityGroup")
                .withPriority(5)
                .startNow()
                .forJob(job)
                .build();

        scheduler.addJob(job, true);
        scheduler.scheduleJob(trigger1);
        scheduler.scheduleJob(trigger2);
        scheduler.scheduleJob(trigger3);

        System.out.println("Trigger1优先级: " + trigger1.getPriority());
        System.out.println("Trigger2优先级: " + trigger2.getPriority());
        System.out.println("Trigger3优先级: " + trigger3.getPriority());
        System.out.println("优先级高的先执行");

        Thread.sleep(3000);

        scheduler.shutdown();
    }

    private static void misfireDemo() throws SchedulerException, InterruptedException {
        System.out.println("\n--- 6. Misfire策略演示 ---");

        Scheduler scheduler = StdSchedulerFactory.getDefaultScheduler();
        scheduler.start();

        JobDetail job = JobBuilder.newJob(MisfireJob.class)
                .withIdentity("misfireJob", "misfireGroup")
                .storeDurably()
                .build();

        Trigger trigger = TriggerBuilder.newTrigger()
                .withIdentity("misfireTrigger", "misfireGroup")
                .startAt(DateBuilder.futureDate(2, DateBuilder.IntervalUnit.SECOND))
                .withSchedule(SimpleScheduleBuilder.simpleSchedule()
                        .withIntervalInSeconds(1)
                        .repeatForever()
                        .withMisfireHandlingInstructionNowWithExistingCount())
                .forJob(job)
                .build();

        scheduler.addJob(job, true);
        scheduler.scheduleJob(trigger);

        System.out.println("任务已调度，2秒后开始执行");
        System.out.println("先暂停调度器，制造misfire");

        scheduler.standby();
        Thread.sleep(5000);

        System.out.println("恢复调度器，观察misfire处理");
        scheduler.start();

        Thread.sleep(5000);

        scheduler.shutdown();
    }
}

class TriggerJob implements Job {

    public TriggerJob() {
    }

    @Override
    public void execute(JobExecutionContext context) throws JobExecutionException {
        JobDataMap dataMap = context.getJobDetail().getJobDataMap();
        String type = dataMap.getString("type");
        TriggerKey triggerKey = context.getTrigger().getKey();
        System.out.println("[" + new Date() + "] " + type + " - " + triggerKey + " 触发");
    }
}

class PriorityJob implements Job {

    public PriorityJob() {
    }

    @Override
    public void execute(JobExecutionContext context) throws JobExecutionException {
        TriggerKey triggerKey = context.getTrigger().getKey();
        int priority = context.getTrigger().getPriority();
        System.out.println("[" + new Date() + "] " + triggerKey + " 执行，优先级: " + priority);
    }
}

class MisfireJob implements Job {

    public MisfireJob() {
    }

    @Override
    public void execute(JobExecutionContext context) throws JobExecutionException {
        TriggerKey triggerKey = context.getTrigger().getKey();
        Date scheduledFireTime = context.getScheduledFireTime();
        Date actualFireTime = context.getFireTime();
        System.out.println("[" + new Date() + "] " + triggerKey + " 执行");
        System.out.println("  计划时间: " + scheduledFireTime);
        System.out.println("  实际时间: " + actualFireTime);
    }
}
