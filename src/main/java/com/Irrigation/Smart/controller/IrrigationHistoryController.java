
package com.Irrigation.Smart.controller;

import com.Irrigation.Smart.entity.Field;
import com.Irrigation.Smart.entity.IrrigationHistory;
import com.Irrigation.Smart.repository.FieldRepository;
import com.Irrigation.Smart.repository.IrrigationHistoryRepository;

import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.server.ResponseStatusException;

import java.util.List;

@RestController
@RequestMapping("/api/irrigation-history")
public class IrrigationHistoryController {

    private final IrrigationHistoryRepository historyRepository;
    private final FieldRepository fieldRepository;

    public IrrigationHistoryController(
            IrrigationHistoryRepository historyRepository,
            FieldRepository fieldRepository) {

        this.historyRepository = historyRepository;
        this.fieldRepository = fieldRepository;
    }

    // Save irrigation history for a registered field
    @PostMapping("/{fieldId}")
    public IrrigationHistory saveHistory(
            @PathVariable Long fieldId,
            @RequestBody IrrigationHistory history) {

        Field field = fieldRepository.findById(fieldId)
                .orElseThrow(() -> new ResponseStatusException(
                        HttpStatus.NOT_FOUND, "Field not found"));

        history.setField(field);

        return historyRepository.save(history);
    }

    // Get all irrigation history
    @GetMapping
    public List<IrrigationHistory> getAllHistory() {
        return historyRepository.findAll();
    }

    // Get irrigation history for a particular field
    @GetMapping("/{fieldId}")
    public List<IrrigationHistory> getHistoryByField(
            @PathVariable Long fieldId) {

        return historyRepository
                .findByFieldIdOrderByCreatedAtDesc(fieldId);
    }
}
