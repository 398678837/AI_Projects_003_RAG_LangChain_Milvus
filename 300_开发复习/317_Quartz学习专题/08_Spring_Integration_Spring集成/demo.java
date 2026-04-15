package com.example.quartz.spring;

import org.quartz.*;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.scheduling.annotation.EnableScheduling;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.scheduling.quartz.*;

import java.util.Date;
import java.util.HashMap;
import java.util.Map;

public class SpringIntegrationDemo {

    public static void main(String[] args) throws InterruptedException {
        System.out.println("=== Quartz Spring集成示例 ===");

        try {
            springJavaConfigDemo();
            springScheduledAnnotationDemo();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void springJavaConfigDemo() throws InterruptedException {
        System.out.println("\n--- 1. Spring Java配置演示 ---");

        AnnotationConfigApplicationContext context =
                new AnnotationConfigApplicationContext(QuartzConfig.class);

        System.out.println("Spring容器已启动");
        System.out.println("等待10秒观察调度...");

        Thread.sleep(10000);

        context.close();
        System.out.println("Spring容器已关闭");
    }

    private static void springScheduledAnnotationDemo() throws InterruptedException {
        System.out.println("\n--- 2. @Scheduled注解演示 ---");

        AnnotationConfigApplicationContext context =
                new AnnotationConfigApplicationContext(ScheduledConfig.class);

        System.out.println("Spring容器已启动");
        System.out.println("等待10秒观察调度...");

        Thread.sleep(10000);

        context.close();
        System.out.println("Spring容器已关闭");
    }
}

@Configuration
class QuartzConfig {

    @Bean
    public SchedulerFactoryBean schedulerFactoryBean() {
        SchedulerFactoryBean schedulerFactoryBean = new SchedulerFactoryBean();
        schedulerFactoryBean.setJobDetails(myJobDetail());
        schedulerFactoryBean.setTriggers(myCronTrigger(), mySimpleTrigger());
        return schedulerFactoryBean;
    }

    @Bean
    public JobDetailFactoryBean myJobDetail() {
        JobDetailFactoryBean jobDetailFactoryBean = new JobDetailFactoryBean();
        jobDetailFactoryBean.setJobClass(MySpringJob.class);
        jobDetailFactoryBean.setDurability(true);
        Map<String, Object> jobDataMap = new HashMap<>();
        jobDataMap.put("message", "Hello from Spring!");
        jobDetailFactoryBean.setJobDataAsMap(jobDataMap);
        return jobDetailFactoryBean;
    }

    @Bean
    public CronTriggerFactoryBean myCronTrigger() {
        CronTriggerFactoryBean cronTriggerFactoryBean = new CronTriggerFactoryBean();
        cronTriggerFactoryBean.setJobDetail(myJobDetail().getObject());
        cronTriggerFactoryBean.setCronExpression("0/3 * * * * ?");
        return cronTriggerFactoryBean;
    }

    @Bean
    public SimpleTriggerFactoryBean mySimpleTrigger() {
        SimpleTriggerFactoryBean simpleTriggerFactoryBean = new SimpleTriggerFactoryBean();
        simpleTriggerFactoryBean.setJobDetail(myJobDetail().getObject());
        simpleTriggerFactoryBean.setStartDelay(1000);
        simpleTriggerFactoryBean.setRepeatInterval(5000);
        simpleTriggerFactoryBean.setRepeatCount(SimpleTrigger.REPEAT_INDEFINITELY);
        return simpleTriggerFactoryBean;
    }
}

class MySpringJob implements Job {

    private String message;

    public void setMessage(String message) {
        this.message = message;
    }

    @Override
    public void execute(JobExecutionContext context) throws JobExecutionException {
        Trigger trigger = context.getTrigger();
        System.out.println("[" + new Date() + "] MySpringJob执行");
        System.out.println("  Trigger: " + trigger.getKey());
        System.out.println("  消息: " + message);
    }
}

@Configuration
@EnableScheduling
class ScheduledConfig {

    @Bean
    public ScheduledTask scheduledTask() {
        return new ScheduledTask();
    }
}

class ScheduledTask {

    @Scheduled(fixedRate = 3000)
    public void fixedRateTask() {
        System.out.println("[" + new Date() + "] fixedRate任务执行（每3秒）");
    }

    @Scheduled(fixedDelay = 4000, initialDelay = 2000)
    public void fixedDelayTask() {
        System.out.println("[" + new Date() + "] fixedDelay任务执行（延迟2秒，间隔4秒）");
    }

    @Scheduled(cron = "0/5 * * * * ?")
    public void cronTask() {
        System.out.println("[" + new Date() + "] cron任务执行（每5秒）");
    }
}
