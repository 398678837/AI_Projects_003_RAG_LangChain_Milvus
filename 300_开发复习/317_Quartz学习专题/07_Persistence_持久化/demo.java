package com.example.quartz.persistence;

import org.quartz.*;
import org.quartz.impl.StdSchedulerFactory;

import java.io.IOException;
import java.io.InputStream;
import java.util.Date;
import java.util.Properties;

public class PersistenceDemo {

    public static void main(String[] args) {
        System.out.println("=== Quartz持久化示例 ===");

        try {
            showConfigDemo();
            ramJobStoreDemo();
            jdbcJobStoreDemo();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void showConfigDemo() {
        System.out.println("\n--- 1. 持久化配置示例 ---");

        System.out.println("RAMJobStore配置:");
        System.out.println("  org.quartz.jobStore.class = org.quartz.simpl.RAMJobStore");

        System.out.println("\nJDBCJobStore配置:");
        System.out.println("  org.quartz.jobStore.class = org.quartz.impl.jdbcjobstore.JobStoreTX");
        System.out.println("  org.quartz.jobStore.driverDelegateClass = org.quartz.impl.jdbcjobstore.StdJDBCDelegate");
        System.out.println("  org.quartz.jobStore.dataSource = myDS");
        System.out.println("  org.quartz.jobStore.tablePrefix = QRTZ_");
        System.out.println("  org.quartz.jobStore.isClustered = false");
        System.out.println("  org.quartz.dataSource.myDS.driver = com.mysql.cj.jdbc.Driver");
        System.out.println("  org.quartz.dataSource.myDS.URL = jdbc:mysql://localhost:3306/quartz");
        System.out.println("  org.quartz.dataSource.myDS.user = root");
        System.out.println("  org.quartz.dataSource.myDS.password = password");
        System.out.println("  org.quartz.dataSource.myDS.maxConnections = 5");
    }

    private static void ramJobStoreDemo() throws SchedulerException, InterruptedException {
        System.out.println("\n--- 2. RAMJobStore演示 ---");

        Properties props = new Properties();
        props.setProperty("org.quartz.scheduler.instanceName", "RamScheduler");
        props.setProperty("org.quartz.scheduler.instanceId", "AUTO");
        props.setProperty("org.quartz.threadPool.class", "org.quartz.simpl.SimpleThreadPool");
        props.setProperty("org.quartz.threadPool.threadCount", "3");
        props.setProperty("org.quartz.jobStore.class", "org.quartz.simpl.RAMJobStore");

        SchedulerFactory factory = new StdSchedulerFactory(props);
        Scheduler scheduler = factory.getScheduler();
        scheduler.start();

        JobDetail job = JobBuilder.newJob(PersistenceJob.class)
                .withIdentity("ramJob", "ramGroup")
                .usingJobData("type", "RAMJobStore")
                .build();

        Trigger trigger = TriggerBuilder.newTrigger()
                .withIdentity("ramTrigger", "ramGroup")
                .startNow()
                .withSchedule(SimpleScheduleBuilder.simpleSchedule()
                        .withIntervalInSeconds(2)
                        .withRepeatCount(2))
                .build();

        scheduler.scheduleJob(job, trigger);
        System.out.println("RAMJobStore任务已调度");

        Thread.sleep(7000);

        scheduler.shutdown();
        System.out.println("RAMJobStore: 重启后任务会丢失");
    }

    private static void jdbcJobStoreDemo() throws SchedulerException, InterruptedException, IOException {
        System.out.println("\n--- 3. JDBCJobStore演示 ---");

        Properties props = new Properties();
        try (InputStream is = PersistenceDemo.class.getClassLoader().getResourceAsStream("quartz.properties")) {
            if (is != null) {
                props.load(is);
            } else {
                props.setProperty("org.quartz.scheduler.instanceName", "JdbcScheduler");
                props.setProperty("org.quartz.scheduler.instanceId", "AUTO");
                props.setProperty("org.quartz.threadPool.class", "org.quartz.simpl.SimpleThreadPool");
                props.setProperty("org.quartz.threadPool.threadCount", "3");
                props.setProperty("org.quartz.jobStore.class", "org.quartz.impl.jdbcjobstore.JobStoreTX");
                props.setProperty("org.quartz.jobStore.driverDelegateClass", "org.quartz.impl.jdbcjobstore.StdJDBCDelegate");
                props.setProperty("org.quartz.jobStore.tablePrefix", "QRTZ_");
                props.setProperty("org.quartz.jobStore.isClustered", "false");
            }
        }

        SchedulerFactory factory = new StdSchedulerFactory(props);
        Scheduler scheduler = factory.getScheduler();
        scheduler.start();

        JobDetail job = JobBuilder.newJob(PersistenceJob.class)
                .withIdentity("jdbcJob", "jdbcGroup")
                .usingJobData("type", "JDBCJobStore")
                .storeDurably()
                .requestRecovery()
                .build();

        Trigger trigger = TriggerBuilder.newTrigger()
                .withIdentity("jdbcTrigger", "jdbcGroup")
                .startNow()
                .withSchedule(SimpleScheduleBuilder.simpleSchedule()
                        .withIntervalInSeconds(3)
                        .repeatForever())
                .build();

        scheduler.scheduleJob(job, trigger);
        System.out.println("JDBCJobStore任务已调度");
        System.out.println("JDBCJobStore: 重启后任务会恢复");

        Thread.sleep(8000);

        scheduler.shutdown();
    }
}

class PersistenceJob implements Job {

    public PersistenceJob() {
    }

    @Override
    public void execute(JobExecutionContext context) throws JobExecutionException {
        JobDataMap dataMap = context.getJobDetail().getJobDataMap();
        String type = dataMap.getString("type");
        SchedulerMetaData metaData = null;
        try {
            metaData = context.getScheduler().getMetaData();
        } catch (SchedulerException e) {
            e.printStackTrace();
        }

        System.out.println("[" + new Date() + "] " + type + " 任务执行");
        if (metaData != null) {
            System.out.println("  Scheduler: " + metaData.getSchedulerName());
            System.out.println("  持久化: " + (metaData.isJobStoreSupportsPersistence() ? "是" : "否"));
            System.out.println("  集群: " + (metaData.isJobStoreClustered() ? "是" : "否"));
        }
    }
}
