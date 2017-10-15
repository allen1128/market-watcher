package com.mw.domain;

import com.fasterxml.jackson.annotation.JsonInclude;
import lombok.AccessLevel;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;
import java.util.Date;

@Data
@Entity
@Table(name="REAL_ESTATE")
@AllArgsConstructor(access = AccessLevel.PUBLIC)
@NoArgsConstructor(access = AccessLevel.PUBLIC)
@JsonInclude(JsonInclude.Include.NON_NULL)
public class RealEstate {
    @Id
    private Long reId;
    private String title;
    private String hood;
    private Float price;
    private Integer bedroomNr;
    private Integer size;
    private Integer category;

    private Date datePosted;
    private Date dateCreated = new Date();

    @Column(name="DETAIL_URL")
    private String detailedUrl;
    private String city;

    @Override
    public String toString() {
        return "RealEstate{" +
                "reId=" + reId +
                ", title='" + title + '\'' +
                ", hood='" + hood + '\'' +
                ", price=" + price +
                ", bedroomNr=" + bedroomNr +
                ", size=" + size +
                ", category=" + category +
                ", datePosted=" + datePosted +
                ", dateCreated=" + dateCreated +
                ", detailedUrl='" + detailedUrl + '\'' +
                ", city='" + city + '\'' +
                '}';
    }
}
