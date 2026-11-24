

package com.Irrigation.Smart.service;

import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;
import java.util.Map;

@Service
public class WeatherService {

    private final RestTemplate restTemplate = new RestTemplate();

    public Map getWeather() {

        String url = "https://api.open-meteo.com/v1/forecast"
                + "?latitude=17.05439"
                + "&longitude=79.26707"
                + "&current=temperature_2m,relative_humidity_2m,precipitation,wind_speed_10m"
                + "&timezone=Asia/Kolkata";

        return restTemplate.getForObject(url, Map.class);
    }
}
