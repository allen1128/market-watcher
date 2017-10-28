package com.mw;

import com.mw.domain.RealEstate;
import com.mw.service.EmailService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.client.circuitbreaker.EnableCircuitBreaker;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;

@SpringBootApplication
public class Application {

    public static void main(String[] args){

        EmailService emailService = new EmailService();
        emailService.sendNotification(new RealEstate(), "as.allen1128@gmail.com");
        SpringApplication.run(Application.class, args);
    }
}
