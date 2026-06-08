"""
Solaire AI Agent — Main Entry Point
University of Westminster Dissertation 2026/27
Nicholas Nicolaou

Fully local AI pipeline:
OpenWakeWord -> Whisper.cpp -> Ollama LLM -> Piper TTS -> Moondream (vision)

TODO: Implement each stage — this is the scaffold.
"""

import json
import time
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
log = logging.getLogger("solaire")

def load_config(path="config.json"):
    with open(path) as f:
        return json.load(f)

def main():
    config = load_config()
    log.info("Solaire agent starting up...")
    log.info(f"LLM model: {config['ollama_model']}")
    log.info(f"Wake word: {config['wake_word_model']}")

    # TODO Stage 1: Initialise display and show idle face
    # TODO Stage 2: Start OpenWakeWord listener
    # TODO Stage 3: On wake word -> capture audio -> Whisper STT
    # TODO Stage 4: Pass transcript -> Ollama LLM with system prompt
    # TODO Stage 5: Pass response -> Piper TTS -> play audio
    # TODO Stage 6: On "look" command -> Moondream vision description

    log.info("Praise the Sun! ☀️  Agent ready.")

if __name__ == "__main__":
    main()
