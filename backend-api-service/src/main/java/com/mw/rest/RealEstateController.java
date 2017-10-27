package com.mw.rest;

import com.mw.domain.Notification;
import com.mw.domain.RealEstate;
import com.mw.repository.NotificationRepository;
import com.mw.service.RealEstateService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RequestMapping(value="/realestates")
@RestController
public class RealEstateController {

    @Autowired
    RealEstateService realEstateService;

    @Autowired
    NotificationRepository notificationRepository;

    @RequestMapping(value="", method = RequestMethod.GET)
    @CrossOrigin(origins = "http://127.0.0.1:54209")
    public List<RealEstate> getAllRealEstates(){
        return realEstateService.findAll();
    }

    @RequestMapping(value="/notification/add", method= RequestMethod.POST)
    @ResponseStatus(HttpStatus.CREATED)
    @CrossOrigin(origins = "http://127.0.0.1:54209")
    public void addNotification(@RequestBody Notification notification){
        notificationRepository.save(notification);
    }

    @RequestMapping(value="/notifications/", method=RequestMethod.GET)
    @CrossOrigin(origins = "http://127.0.0.1:54209")
    public List<Notification> getAllNotifications(){
        return notificationRepository.findAll();
    }
}
