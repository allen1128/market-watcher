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
    public void publish(RealEstate realEstate) {
        for (Notification notification : notificationRepository.findAll()){
            if (meetPriceReq(notification.getMaxPrice(), notification.getMinPrice(), realEstate.getPrice()) &&
                meetRoomReq(notification.getMaxRoomNr(), notification.getMinRoomNr(), realEstate.getBedroomNr())) {
                emailService.sendNotification(realEstate, notification.getEmail());
            }
        }
    }

    private boolean meetRoomReq(Integer maxRoom, Integer minRoom, Integer actualRoom) {
        if (actualRoom == null){
            return true;
        }

        boolean metMax = maxRoom == null || maxRoom >= actualRoom ? true : false;
        boolean metMin = minRoom == null || minRoom <= actualRoom ? true : false;
        return metMax && metMin;
    }

    private boolean meetPriceReq(Integer maxPrice, Integer minPrice, Float actualPrice) {
        if (actualPrice == null){
            return true;
        }

        boolean metMax = maxPrice == null || maxPrice >= actualPrice ? true : false;
        boolean metMin = minPrice == null || minPrice <= actualPrice ? true : false;
        return metMax && metMin;
    }
}
