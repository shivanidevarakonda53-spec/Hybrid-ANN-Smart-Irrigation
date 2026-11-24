package com.Irrigation.Smart.controller;

import com.Irrigation.Smart.service.AiChatService;
import org.springframework.web.bind.annotation.*;
import java.util.Map;

@RestController
@RequestMapping("/api")
public class AiChatController {

    private final AiChatService aiChatService;

    public AiChatController(AiChatService aiChatService) {
        this.aiChatService = aiChatService;
    }

    @PostMapping("/chat")
    public Map<String, String> chat(@RequestBody Map<String, String> request) {

        String question = request.get("question");

        String answer = aiChatService.askQuestion(question);

        return Map.of("answer", answer);
    }
}