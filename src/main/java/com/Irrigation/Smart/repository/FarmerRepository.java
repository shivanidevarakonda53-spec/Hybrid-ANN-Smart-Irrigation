package com.Irrigation.Smart.repository;

import com.Irrigation.Smart.entity.Farmer;
import org.springframework.data.jpa.repository.JpaRepository;

public interface FarmerRepository extends JpaRepository<Farmer, Long> {
}