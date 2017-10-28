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
    private Long nfId;
    private String email;

    private String city;
    private Integer minPrice;
    private Integer maxPrice;
    private Integer minRoomNr;
    private Integer maxRoomNr;
    private Date dateCreated = new Date();

    @Override
    public String toString() {
        return "Notification{" +
                "nfId=" + nfId +
                ", email='" + email + '\'' +
                ", dateCreated=" + dateCreated +
                '}';
    }
}
