
package com.Irrigation.Smart.controller;

import com.Irrigation.Smart.service.WeatherService;
import org.springframework.web.bind.annotation.*;
import java.util.Map;

@RestController
@RequestMapping("/api/weather")
public class WeatherController {

    private final WeatherService weatherService;

    public WeatherController(WeatherService weatherService) {
        this.weatherService = weatherService;
    }

    @GetMapping
    public Map getWeather() {
        return weatherService.getWeather();
    }
}
