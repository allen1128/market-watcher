package com.mw.rest;

import com.mw.domain.RealEstate;
import com.mw.service.RealEstateService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RequestMapping(value="/realestates")
@RestController
public class RealEstateController {

    @Autowired
    RealEstateService realEstateService;

    @RequestMapping(value="", method = RequestMethod.GET)
    List<RealEstate> findAll(){
        return realEstateService.findAll();
    }
}
