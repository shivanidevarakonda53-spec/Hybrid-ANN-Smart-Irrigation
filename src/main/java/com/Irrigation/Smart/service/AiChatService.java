package com.Irrigation.Smart.service;

import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;
import java.util.Map;

@Service
public class AiChatService {

    private final RestTemplate restTemplate = new RestTemplate();

    public String askQuestion(String question) {

        String url = "http://127.0.0.1:8000/chat";

        Map<String, String> request = Map.of(
            "question", question
        );

        Map response = restTemplate.postForObject(
            url, request, Map.class
        );

        return (String) response.get("answer");
    }
}