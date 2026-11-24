
package com.Irrigation.Smart.entity;

import jakarta.persistence.*;
import java.time.LocalDate;
import java.time.LocalDateTime;

@Entity
@Table(name = "irrigation_history")
public class IrrigationHistory {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private LocalDate lastIrrigationDate;

    private Double waterApplied;

    private String growthStage;

    private LocalDateTime createdAt;

    @ManyToOne
    @JoinColumn(name = "field_id", nullable = false)
    private Field field;

    public IrrigationHistory() {
    }

    @PrePersist
    public void onCreate() {
        createdAt = LocalDateTime.now();
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public LocalDate getLastIrrigationDate() {
        return lastIrrigationDate;
    }

    public void setLastIrrigationDate(LocalDate lastIrrigationDate) {
        this.lastIrrigationDate = lastIrrigationDate;
    }

    public Double getWaterApplied() {
        return waterApplied;
    }

    public void setWaterApplied(Double waterApplied) {
        this.waterApplied = waterApplied;
    }

    public String getGrowthStage() {
        return growthStage;
    }

    public void setGrowthStage(String growthStage) {
        this.growthStage = growthStage;
    }

    public LocalDateTime getCreatedAt() {
        return createdAt;
    }

    public void setCreatedAt(LocalDateTime createdAt) {
        this.createdAt = createdAt;
    }

    public Field getField() {
        return field;
    }

    public void setField(Field field) {
        this.field = field;
    }
}
