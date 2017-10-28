package com.mw.service;

import com.mw.domain.Notification;
import com.mw.domain.RealEstate;
import com.mw.repository.NotificationRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class NotificationServiceImpl implements NotificationService {
    @Autowired
    NotificationRepository notificationRepository;

    @Autowired
    EmailService emailService;

    @Override
    public List<Notification> findAll() {
        return notificationRepository.findAll();
    }

    @Override
    public void publish(RealEstate realEstate) {
        List<Notification> notifications = findAll();

        for (Notification notification : notifications){
            if (notification.getMaxPrice() >= realEstate.getPrice() &&
                    notification.getMinPrice() <= realEstate.getPrice() &&
                    notification.getCity().equalsIgnoreCase(realEstate.getCity()) &&
                    notification.getMaxRoomNr() >= realEstate.getBedroomNr() &&
                    notification.getMinRoomNr() <= realEstate.getBedroomNr() ){
                    emailService.sendNotification(realEstate, notification.getEmail());
            }
        }
    }
}
