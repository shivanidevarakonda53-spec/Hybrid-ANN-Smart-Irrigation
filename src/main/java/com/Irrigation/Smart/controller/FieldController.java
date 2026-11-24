
package com.Irrigation.Smart.controller;

import com.Irrigation.Smart.entity.Field;
import com.Irrigation.Smart.entity.Farmer;
import com.Irrigation.Smart.repository.FieldRepository;
import com.Irrigation.Smart.repository.FarmerRepository;

import org.springframework.web.bind.annotation.*;
import org.springframework.http.HttpStatus;
import org.springframework.web.server.ResponseStatusException;

import java.util.List;

@RestController
@RequestMapping("/api/fields")
public class FieldController {

    private final FieldRepository fieldRepository;
    private final FarmerRepository farmerRepository;

    public FieldController(
            FieldRepository fieldRepository,
            FarmerRepository farmerRepository) {

        this.fieldRepository = fieldRepository;
        this.farmerRepository = farmerRepository;
    }

    @PostMapping("/{farmerId}")
    public Field addField(
            @PathVariable Long farmerId,
            @RequestBody Field field) {

        Farmer farmer = farmerRepository.findById(farmerId)
                .orElseThrow(() -> new ResponseStatusException(
                        HttpStatus.NOT_FOUND, "Farmer not found"));

        field.setFarmer(farmer);

        return fieldRepository.save(field);
    }

    @GetMapping
    public List<Field> getAllFields() {
        return fieldRepository.findAll();
    }

    @GetMapping("/{farmerId}")
    public List<Field> getFieldsByFarmer(
            @PathVariable Long farmerId) {

        return fieldRepository.findAll().stream()
                .filter(field -> field.getFarmer() != null
                        && field.getFarmer().getId().equals(farmerId))
                .toList();
    }
}
