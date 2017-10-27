package com.mw.domain;

import com.fasterxml.jackson.annotation.JsonInclude;
import lombok.AccessLevel;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import javax.persistence.*;
import java.util.Date;

@Data
@Entity
@AllArgsConstructor(access = AccessLevel.PUBLIC)
@NoArgsConstructor(access = AccessLevel.PUBLIC)
@JsonInclude(JsonInclude.Include.NON_NULL)
public class Notification {
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    Long nfId;
    String email;
    
    String city;
    Integer minPrice;
    Integer maxPrice;
    Integer minRoomNr;
    Integer maxRoomNr;

    @Column(name="created_date")
    Date dateCreated = new Date();

    @Override
    public String toString() {
        return "Notification{" +
                "nfId=" + nfId +
                ", email='" + email + '\'' +
                ", dateCreated=" + dateCreated +
                '}';
    }
}
