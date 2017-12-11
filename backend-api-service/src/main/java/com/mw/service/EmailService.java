package com.mw.service;

import com.mw.domain.RealEstate;
import com.mw.util.MailUtil;
import lombok.extern.slf4j.Slf4j;
import org.springframework.mail.SimpleMailMessage;
import org.springframework.mail.javamail.JavaMailSenderImpl;
import org.springframework.stereotype.Service;

import java.util.Properties;

@Service
@Slf4j
public class EmailService {

    public void sendNotification(RealEstate realEstate, String recipient) {
        SimpleMailMessage mailMessage = new SimpleMailMessage();
        mailMessage.setTo(recipient);
        mailMessage.setFrom("as.allen1128@gmail.com");
        mailMessage.setSubject("New Real Estate Post Alert");
        mailMessage.setText("Note that there is a new post on craiglist that fits your subscription criteria. \n\n For details check " + realEstate.getDetailedUrl());
        MailUtil.send(mailMessage);
    }
}
