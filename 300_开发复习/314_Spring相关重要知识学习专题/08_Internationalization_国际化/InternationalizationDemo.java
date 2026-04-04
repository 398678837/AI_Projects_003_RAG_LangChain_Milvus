package com.example.spring.internationalization;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.MessageSource;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.support.ResourceBundleMessageSource;
import org.springframework.web.servlet.LocaleResolver;
import org.springframework.web.servlet.config.annotation.InterceptorRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;
import org.springframework.web.servlet.i18n.LocaleChangeInterceptor;
import org.springframework.web.servlet.i18n.SessionLocaleResolver;

import java.util.Date;
import java.util.Locale;

/**
 * Spring 国际化示例
 */
public class InternationalizationDemo {
    
    public static void main(String[] args) {
        // 测试消息解析
        System.out.println("=== 测试消息解析 ===");
        MessageSourceConfig messageSourceConfig = new MessageSourceConfig();
        MessageSource messageSource = messageSourceConfig.messageSource();
        
        // 英文消息
        Locale enLocale = Locale.US;
        String helloEn = messageSource.getMessage("hello", null, enLocale);
        String welcomeEn = messageSource.getMessage("welcome", null, enLocale);
        System.out.println("English:");
        System.out.println("  hello: " + helloEn);
        System.out.println("  welcome: " + welcomeEn);
        
        // 中文消息
        Locale zhLocale = Locale.SIMPLIFIED_CHINESE;
        String helloZh = messageSource.getMessage("hello", null, zhLocale);
        String welcomeZh = messageSource.getMessage("welcome", null, zhLocale);
        System.out.println("\nChinese:");
        System.out.println("  hello: " + helloZh);
        System.out.println("  welcome: " + welcomeZh);
        
        // 测试带参数的消息
        System.out.println("\n=== 测试带参数的消息 ===");
        String greetingEn = messageSource.getMessage("greeting", new Object[]{"Alice"}, enLocale);
        String greetingZh = messageSource.getMessage("greeting", new Object[]{"Alice"}, zhLocale);
        System.out.println("English greeting: " + greetingEn);
        System.out.println("Chinese greeting: " + greetingZh);
        
        // 测试数字参数
        String itemCountEn = messageSource.getMessage("item.count", new Object[]{5}, enLocale);
        String itemCountZh = messageSource.getMessage("item.count", new Object[]{5}, zhLocale);
        System.out.println("\nEnglish item count: " + itemCountEn);
        System.out.println("Chinese item count: " + itemCountZh);
    }
}

/**
 * 消息源配置
 */
@Configuration
class MessageSourceConfig {
    
    @Bean
    public MessageSource messageSource() {
        ResourceBundleMessageSource messageSource = new ResourceBundleMessageSource();
        messageSource.setBasename("messages");
        messageSource.setDefaultEncoding("UTF-8");
        messageSource.setCacheSeconds(3600);
        return messageSource;
    }
}

/**
 * 区域设置配置
 */
@Configuration
class LocaleConfig implements WebMvcConfigurer {
    
    @Bean
    public LocaleResolver localeResolver() {
        SessionLocaleResolver resolver = new SessionLocaleResolver();
        resolver.setDefaultLocale(Locale.US);
        return resolver;
    }
    
    @Bean
    public LocaleChangeInterceptor localeChangeInterceptor() {
        LocaleChangeInterceptor interceptor = new LocaleChangeInterceptor();
        interceptor.setParamName("lang");
        return interceptor;
    }
    
    @Override
    public void addInterceptors(InterceptorRegistry registry) {
        registry.addInterceptor(localeChangeInterceptor());
    }
}

/**
 * 国际化服务
 */
class I18nService {
    
    private final MessageSource messageSource;
    
    @Autowired
    public I18nService(MessageSource messageSource) {
        this.messageSource = messageSource;
    }
    
    /**
     * 获取消息
     */
    public String getMessage(String code, Object[] args, Locale locale) {
        return messageSource.getMessage(code, args, locale);
    }
    
    /**
     * 获取消息（使用默认区域设置）
     */
    public String getMessage(String code, Object[] args) {
        return messageSource.getMessage(code, args, Locale.getDefault());
    }
    
    /**
     * 格式化日期
     */
    public String formatDate(Date date, Locale locale) {
        java.text.DateFormat dateFormat = java.text.DateFormat.getDateInstance(java.text.DateFormat.LONG, locale);
        return dateFormat.format(date);
    }
    
    /**
     * 格式化时间
     */
    public String formatTime(Date date, Locale locale) {
        java.text.DateFormat timeFormat = java.text.DateFormat.getTimeInstance(java.text.DateFormat.MEDIUM, locale);
        return timeFormat.format(date);
    }
}

/**
 * 控制器示例
 */
class HomeController {
    
    private final I18nService i18nService;
    
    @Autowired
    public HomeController(I18nService i18nService) {
        this.i18nService = i18nService;
    }
    
    /**
     * 首页
     */
    public String home(Locale locale) {
        String hello = i18nService.getMessage("hello", null, locale);
        String welcome = i18nService.getMessage("welcome", null, locale);
        
        // 实际应用中，这里会返回视图并传递消息
        System.out.println(hello);
        System.out.println(welcome);
        
        return "home";
    }
    
    /**
     * 用户页面
     */
    public String userProfile(String username, Locale locale) {
        String greeting = i18nService.getMessage("greeting", new Object[]{username}, locale);
        String lastLogin = i18nService.getMessage("last.login", new Object[]{i18nService.formatDate(new Date(), locale)}, locale);
        
        System.out.println(greeting);
        System.out.println(lastLogin);
        
        return "user/profile";
    }
}
