package com.mw.service;

import com.mw.domain.Notification;
import com.mw.domain.RealEstate;

import java.util.List;

public interface NotificationService  {
    void publish(RealEstate realEstate);
}
