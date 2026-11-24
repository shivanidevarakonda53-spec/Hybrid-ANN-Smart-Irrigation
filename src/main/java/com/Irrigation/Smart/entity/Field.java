
package com.Irrigation.Smart.entity;

import jakarta.persistence.*;

@Entity
@Table(name = "fields")
public class Field {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String fieldName;

    private String location;

    private String cropName;

    private Double landArea;

    private String soilType;

    @ManyToOne
    @JoinColumn(name = "farmer_id")
    private Farmer farmer;

    public Field() {
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getFieldName() {
        return fieldName;
    }

    public void setFieldName(String fieldName) {
        this.fieldName = fieldName;
    }

    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }

    public String getCropName() {
        return cropName;
    }

    public void setCropName(String cropName) {
        this.cropName = cropName;
    }

    public Double getLandArea() {
        return landArea;
    }

    public void setLandArea(Double landArea) {
        this.landArea = landArea;
    }

    public String getSoilType() {
        return soilType;
    }

    public void setSoilType(String soilType) {
        this.soilType = soilType;
    }

    public Farmer getFarmer() {
        return farmer;
    }

    public void setFarmer(Farmer farmer) {
        this.farmer = farmer;
    }
}
