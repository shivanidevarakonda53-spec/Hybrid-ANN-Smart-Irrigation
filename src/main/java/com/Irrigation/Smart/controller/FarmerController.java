
package com.Irrigation.Smart.controller;

import com.Irrigation.Smart.entity.Farmer;
import com.Irrigation.Smart.repository.FarmerRepository;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.ModelAttribute;

@Controller
public class FarmerController {

    private final FarmerRepository farmerRepository;

    public FarmerController(FarmerRepository farmerRepository) {
        this.farmerRepository = farmerRepository;
    }

    @GetMapping("/register")
    public String showRegistrationForm(Model model) {
        model.addAttribute("farmer", new Farmer());
        return "register";
    }

    @PostMapping("/register")
    public String registerFarmer(@ModelAttribute Farmer farmer) {
        farmerRepository.save(farmer);
        return "redirect:/register?success";
    }
}
