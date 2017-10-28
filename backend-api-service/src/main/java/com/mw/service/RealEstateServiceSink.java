package com.mw.service;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.mw.domain.RealEstate;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.cloud.stream.annotation.EnableBinding;
import org.springframework.cloud.stream.messaging.Sink;
import org.springframework.integration.annotation.ServiceActivator;

import java.io.IOException;

@EnableBinding(Sink.class)
@Slf4j
public class RealEstateServiceSink {

    @Autowired
    private RealEstateService realEstateService;

    @Autowired
    private NotificationService notificationService;

    @Autowired
    private ObjectMapper objectMapper;

    @ServiceActivator(inputChannel = Sink.INPUT)
    public void execute(String input) throws IOException {
        log.info("input message: " + input);
        RealEstate realEstate = objectMapper.readValue(input, RealEstate.class);
        realEstateService.save(realEstate);
        notificationService.publish(realEstate);
    }
}
