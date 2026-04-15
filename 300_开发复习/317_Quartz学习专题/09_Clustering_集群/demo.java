package com.example.quartz.cluster;

import org.quartz.*;
import org.quartz.impl.StdSchedulerFactory;

import java.util.Date;
import java.util.Properties;

public class ClusteringDemo {

    public static void main(String[] args) {
        System.out.println("=== Quartz集群示例 ===");

        try {
            showClusterConfigDemo();
            clusterNodeDemo("Node1");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void showClusterConfigDemo() {
        System.out.println("\n--- 1. 集群配置示例 ---");

        System.out.println("Quartz集群配置:");
        System.out.println("  org.quartz.scheduler.instanceName = MyClusteredScheduler");
        System.out.println("  org.quartz.scheduler.instanceId = AUTO");
        System.out.println("  org.quartz.threadPool.class = org.quartz.simpl.SimpleThreadPool");
        System.out.println("  org.quartz.threadPool.threadCount = 10");
        System.out.println("  org.quartz.jobStore.class = org.quartz.impl.jdbcjobstore.JobStoreTX");
        System.out.println("  org.quartz.jobStore.driverDelegateClass = org.quartz.impl.jdbcjobstore.StdJDBCDelegate");
        System.out.println("  org.quartz.jobStore.dataSource = myDS");
        System.out.println("  org.quartz.jobStore.tablePrefix = QRTZ_");
        System.out.println("  org.quartz.jobStore.isClustered = true");
        System.out.println("  org.quartz.jobStore.clusterCheckinInterval = 20000");
        System.out.println("  org.quartz.dataSource.myDS.driver = com.mysql.cj.jdbc.Driver");
        System.out.println("  org.quartz.dataSource.myDS.URL = jdbc:mysql://localhost:3306/quartz");
        System.out.println("  org.quartz.dataSource.myDS.user = root");
        System.out.println("  org.quartz.dataSource.myDS.password = password");
        System.out.println("  org.quartz.dataSource.myDS.maxConnections = 10");

        System.out.println("\n关键点说明:");
        System.out.println("  - isClustered = true: 启用集群");
        System.out.println("  - instanceId = AUTO: 自动生成实例ID");
        System.out.println("  - clusterCheckinInterval: 集群节点检入间隔（毫秒）");
        System.out.println("  - 所有节点使用相同的Scheduler名称");
        System.out.println("  - 所有节点使用相同的数据库");
    }

    private static void clusterNodeDemo(String nodeName) throws SchedulerException, InterruptedException {
        System.out.println("\n--- 2. 集群节点演示 (" + nodeName + ") ---");

        Properties props = new Properties();
        props.setProperty("org.quartz.scheduler.instanceName", "ClusteredScheduler");
        props.setProperty("org.quartz.scheduler.instanceId", "AUTO");
        props.setProperty("org.quartz.threadPool.class", "org.quartz.simpl.SimpleThreadPool");
        props.setProperty("org.quartz.threadPool.threadCount", "5");
        props.setProperty("org.quartz.jobStore.class", "org.quartz.impl.jdbcjobstore.JobStoreTX");
        props.setProperty("org.quartz.jobStore.driverDelegateClass", "org.quartz.impl.jdbcjobstore.StdJDBCDelegate");
        props.setProperty("org.quartz.jobStore.tablePrefix", "QRTZ_");
        props.setProperty("org.quartz.jobStore.isClustered", "true");
        props.setProperty("org.quartz.jobStore.clusterCheckinInterval", "20000");
        props.setProperty("org.quartz.jobStore.useProperties", "true");

        SchedulerFactory factory = new StdSchedulerFactory(props);
        Scheduler scheduler = factory.getScheduler();

        SchedulerMetaData metaData = scheduler.getMetaData();
        System.out.println("节点信息:");
        System.out.println("  Scheduler名称: " + metaData.getSchedulerName());
        System.out.println("  Scheduler实例ID: " + metaData.getSchedulerInstanceId());
        System.out.println("  集群模式: " + (metaData.isJobStoreClustered() ? "是" : "否"));

        scheduler.start();
        System.out.println("\n调度器已启动");

        JobDetail job = JobBuilder.newJob(ClusterJob.class)
                .withIdentity("clusterJob", "clusterGroup")
                .usingJobData("nodeName", nodeName)
                .storeDurably()
                .requestRecovery()
                .build();

        Trigger trigger = TriggerBuilder.newTrigger()
                .withIdentity("clusterTrigger", "clusterGroup")
                .startNow()
                .withSchedule(SimpleScheduleBuilder.simpleSchedule()
                        .withIntervalInSeconds(5)
                        .repeatForever())
                .build();

        if (!scheduler.checkExists(job.getKey())) {
            scheduler.scheduleJob(job, trigger);
            System.out.println("集群任务已调度");
        } else {
            System.out.println("集群任务已存在");
        }

        System.out.println("\n等待30秒观察调度...");
        Thread.sleep(30000);

        scheduler.shutdown();
        System.out.println("\n调度器已关闭");
    }
}

@DisallowConcurrentExecution
@PersistJobDataAfterExecution
class ClusterJob implements Job {

    public ClusterJob() {
    }

    @Override
    public void execute(JobExecutionContext context) throws JobExecutionException {
        JobDataMap dataMap = context.getJobDetail().getJobDataMap();
        String nodeName = dataMap.getString("nodeName");

        try {
            Scheduler scheduler = context.getScheduler();
            SchedulerMetaData metaData = scheduler.getMetaData();

            System.out.println("[" + new Date() + "] ClusterJob执行");
            System.out.println("  当前节点: " + nodeName);
            System.out.println("  Scheduler: " + metaData.getSchedulerName());
            System.out.println("  实例ID: " + metaData.getSchedulerInstanceId());
            System.out.println("  Trigger: " + context.getTrigger().getKey());
            System.out.println("  下次执行: " + context.getNextFireTime());

        } catch (SchedulerException e) {
            e.printStackTrace();
        }
    }
}
