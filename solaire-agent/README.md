# ☀️ Solaire — Embodied AI Agent

> *"Praise the Sun! ...Oh, don't be embarrassed. No need to be modest. Here, let me share it with you."*

A fully local, offline-first AI conversational agent built into a 3D-printed Solaire of Astora (Dark Souls) figure. Powered by a Raspberry Pi 5, custom PCB, and a fully local AI pipeline — no cloud, no API fees.

**University of Westminster — Final Year Dissertation Project 2026/27**
*Software Engineering with Electronics — Nicholas Nicolaou*

---

## Project Overview

Solaire is an embodied AI agent housed in a 3D-printed knight figure. He listens for a wake word, processes speech locally, reasons using an on-device LLM, and responds in character — complete with reactive face animations, Dark Souls sound effects, and amber LED eyes.

This project combines:
- **Embedded systems** — Raspberry Pi 5, custom PCB, GPIO, camera
- **AI pipeline** — Wake word detection, STT, local LLM, TTS, vision
- **Mechanical design** — Fusion 360 CAD, 3D printing, enclosure engineering
- **Software engineering** — Python agent, state machine, personality system

---

## Repository Structure

```
solaire-agent/
├── docs/                          # Dissertation documents
│   ├── proposal.docx              # Initial project proposal
│   ├── ethics-form.docx           # Ethics/approval form
│   ├── dissertation.docx          # Final dissertation (WIP)
│   └── weekly-log.md              # Weekly progress notes
│
├── hardware/
│   ├── pcb-design/                # Eagle PCB files (power, audio, GPIO)
│   └── cad-files/                 # Fusion 360 files (helmet, torso)
│
├── software/
│   ├── agent/                     # Main Python agent code
│   │   ├── agent.py               # Core agent loop
│   │   ├── config.json            # Model + hardware config
│   │   └── requirements.txt       # Python dependencies
│   ├── faces/                     # PNG sequences for face states
│   │   ├── idle/                  # Sun symbol idle animation
│   │   ├── listening/             # Eyes open / attentive
│   │   ├── thinking/              # Processing animation
│   │   ├── speaking/              # Mouth/expression animation
│   │   └── error/                 # Confused/error state
│   └── sounds/                    # Dark Souls WAV sound effects
│       ├── greeting/              # Startup / bonfire rest sound
│       ├── thinking/              # Looping ambient sounds
│       ├── ack/                   # "I heard you" sounds
│       └── error/                 # Error sounds
│
└── research/
    └── benchmarks/                # Latency data, evaluation results
```

---

## System Architecture

| Layer | Component | Technology |
|---|---|---|
| Wake word | Detects "Hey Solaire" | OpenWakeWord (.onnx) |
| Speech → Text | Transcribes voice | Whisper.cpp (local) |
| Brain / LLM | Generates responses | Ollama (local) |
| Text → Speech | Solaire's voice | Piper TTS (fine-tuned) |
| Vision | Describes environment | Moondream (local) |
| Display | Face animations | LCD + PNG sequences |
| Hardware | Processing | Raspberry Pi 5 |
| Power/Audio | Regulation + amp | Custom PCB |
| Enclosure | Physical form | 3D printed (Fusion 360) |

---

## Hardware Bill of Materials (Planned)

| Component | Purpose | Est. Cost |
|---|---|---|
| Raspberry Pi 5 (8GB) | Main compute | ~£168 |
| Small HDMI/DSI LCD | Face display | ~£25 |
| USB Microphone | Voice input | ~£10 |
| Speaker + PAM8403 amp | Voice output | ~£12 |
| Pi Camera Module 3 | Vision | ~£15 |
| PIR Motion Sensor | Presence detection | ~£5 |
| Amber LEDs + resistors | Eye glow effect | ~£3 |
| Custom PCB (JLCPCB) | Power + audio routing | ~£10 |
| 3D print filament | Enclosure | ~£15 |
| Misc (wiring, connectors) | Assembly | ~£10 |
| **Total (estimated)** | | **~£273** |

---

## Dissertation Research Question

*"What are the performance characteristics and design trade-offs of a fully local, embedded AI conversational agent deployed on consumer single-board hardware?"*

### Evaluation Metrics
- End-to-end response latency (wake word → speech output)
- Per-stage latency breakdown (STT / LLM / TTS)
- LLM model comparison (Gemma 2B vs Llama 3.2 1B on Pi 5)
- Pi 4 vs Pi 5 performance comparison
- Custom PCB vs off-the-shelf HAT reliability

---

## Inspiration

This project is inspired by [be-more-agent](https://github.com/brenpoly/be-more-agent) by brenpoly — a BMO-themed AI agent for Raspberry Pi. Solaire extends this concept with custom PCB electronics, a fully original character design, and a formal academic evaluation component.

---

## Progress Log

See [`docs/weekly-log.md`](docs/weekly-log.md) for week-by-week updates.

---

## License

- Code: MIT License
- CAD/3D files: CC BY-NC-SA 4.0
- *Dark Souls / Solaire of Astora are trademarks of FromSoftware. This is a non-commercial fan project.*
