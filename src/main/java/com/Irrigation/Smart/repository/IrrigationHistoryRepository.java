
package com.Irrigation.Smart.repository;

import com.Irrigation.Smart.entity.IrrigationHistory;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface IrrigationHistoryRepository
        extends JpaRepository<IrrigationHistory, Long> {

    List<IrrigationHistory> findByFieldIdOrderByCreatedAtDesc(Long fieldId);

}
