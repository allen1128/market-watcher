package com.mw.util;

import org.springframework.mail.SimpleMailMessage;
import org.springframework.mail.javamail.JavaMailSenderImpl;

import java.util.Properties;

public class MailUtil {
    static public void send(SimpleMailMessage mailMessage){
        JavaMailSenderImpl senderImpl = new JavaMailSenderImpl();
        senderImpl.setUsername("as.allen1128@gmail.com");
        Properties prop = new Properties();
        prop.put("mail.smtp.auth", "true");
        prop.put("mail.smtp.timeout", "25000");
        prop.put("mail.smtp.starttls.enable", true);
        prop.put("mail.smtp.host", "smtp.gmail.com");
        prop.put("mail.smtp.port", "587");
        senderImpl.setJavaMailProperties(prop);

        senderImpl.send(mailMessage);
    }
}
