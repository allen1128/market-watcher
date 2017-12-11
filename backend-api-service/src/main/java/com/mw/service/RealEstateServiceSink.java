package com.mw.service;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.mw.domain.RealEstate;
import lombok.extern.slf4j.Slf4j;
import org.springframework.amqp.rabbit.annotation.RabbitListener;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.cloud.stream.annotation.EnableBinding;
import org.springframework.cloud.stream.messaging.Sink;
import org.springframework.integration.annotation.ServiceActivator;
import org.springframework.stereotype.Component;

import java.io.IOException;

@Component
@Slf4j
public class RealEstateServiceSink {

    @Autowired
    private RealEstateService realEstateService;

    @Autowired
    private NotificationService notificationService;

    @Autowired
    private ObjectMapper objectMapper;

    //@ServiceActivator(inputChannel = Sink.INPUT)
    @RabbitListener(queues = "real_estate_post_queue")
    public void execute(byte[] payload) throws IOException {
        String content = new String(payload);
        log.info("input message: " + content);
        RealEstate realEstate = objectMapper.readValue(content, RealEstate.class);
        realEstateService.save(realEstate);
        notificationService.publish(realEstate);
    }
}
