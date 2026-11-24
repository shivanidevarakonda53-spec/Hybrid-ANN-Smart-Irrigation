
package com.Irrigation.Smart.controller;

import com.Irrigation.Smart.repository.FarmerRepository;
import com.Irrigation.Smart.repository.FieldRepository;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class HomeController {

    private final FarmerRepository farmerRepository;
    private final FieldRepository fieldRepository;

    public HomeController(
            FarmerRepository farmerRepository,
            FieldRepository fieldRepository) {

        this.farmerRepository = farmerRepository;
        this.fieldRepository = fieldRepository;
    }

    @GetMapping("/")
    public String home() {
        return "index";
    }

    @GetMapping("/fields")
    public String fieldManagement(Model model) {

        model.addAttribute("farmers", farmerRepository.findAll());

        model.addAttribute("fields", fieldRepository.findAll());

        return "field-management";
    }
    @GetMapping("/irrigation-prediction")
public String irrigationPrediction() {
    return "irrigation-prediction";
}
}
