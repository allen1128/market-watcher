package com.mw.service;

import com.mw.domain.RealEstate;

import java.util.List;

public interface RealEstateService {
    List<RealEstate> findAll();
    void save(RealEstate realEstate);
}
