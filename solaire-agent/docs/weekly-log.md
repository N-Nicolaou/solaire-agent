# Weekly Progress Log — Solaire AI Agent

_University of Westminster — Dissertation 2026/27_
_Nicholas Nicolaou — Software Engineering with Electronics_

---

## Pre-Year 3 (Summer 2026)

### Week 1 — Project Concept & Planning
- Identified dissertation concept: embodied AI agent based on Solaire of Astora (Dark Souls)
- Researched be-more-agent (brenpoly) as inspiration project
- Defined system architecture: wake word → STT → LLM → TTS pipeline, fully local
- Created GitHub repository and project structure
- Drafted initial proposal document
- Supervisor meeting held with Mohammed project approved
- Provisional title agreed: "Solaire: Design, Implementation and 
  Benchmarking of an Offline Embedded AI Agent on Consumer 
  Single-Board Hardware"
- Hardware ordered: Raspberry Pi 5 8GB, Active Cooler, 
  27W Power Supply, 128GB microSD
- Catch up meeting with Mohammed scheduled in two weeks
- Objectives have been refined into core and stretch goals ready for catch up meeting.
## Week 2 — Software Stack Testing (Summer 2026)

### Completed this week
- Installed Ollama on Windows laptop and ran Gemma 2B locally
- Developed and refined Solaire personality system prompt (V2)
- Tested personality across 4 scenarios: jolly cooperation, weather, 
  Age of Fire lore, AI deflection — all passing
- Installed Git, CMake, Visual Studio Build Tools on Windows
- Built Whisper.cpp from source on Windows laptop
- Downloaded ggml-base.en model (147MB)
- Successfully transcribed voice locally using Whisper.cpp
- Proved core pipeline works on laptop before Pi arrives:
  OpenWakeWord (pending) → Whisper.cpp ✅ → Ollama ✅ → Piper TTS (pending)

### Key findings
- Whisper.cpp transcription time: ~1400-1800ms on laptop CPU
- Gemma 2B handles Solaire personality well with correct prompting
- "Solaire" transcribed as "Salah" — expected, OpenWakeWord handles 
  wake phrase separately so Whisper never needs to recognise the name
- Pi 5 estimated transcription time: 3-4 seconds for base.en model

### Still to do before Pi arrives
- [ ] Install and test Piper TTS on laptop
- [ ] Browse Thingiverse/Printables for enclosure reference models
- [ ] Read research papers and complete notes template
- [ ] Fusion 360 tutorials for enclosure confidence

### Ongoing Summer Tasks
- [ ] Clone and run be-more-agent on a Raspberry Pi — get familiar with the stack
- [ ] Set up Ollama locally and test Gemma 2B / Llama 3.2 1B response quality
- [ ] Start Fusion 360 concept sketches for Solaire helmet form factor
- [ ] Research Piper TTS voice fine-tuning process
- [ ] Complete ethics form ready for Year 3 submission

---

## Year 3 — Semester 1 (Sep 2026 – Jan 2027)

### Target milestones
- [ ] Ethics form approved (Oct 2026)
- [ ] Core Python agent running on Pi with basic pipeline (Oct 2026)
- [ ] Face animations designed and rendering (Nov 2026)
- [ ] Dark Souls sound effects integrated (Nov 2026)
- [ ] Helmet CAD v1 complete, first 3D print (Dec 2026)
- [ ] Custom PCB designed in Eagle, sent for fabrication (Dec 2026)
- [ ] Preliminary latency benchmarks recorded (Jan 2027)

---

## Year 3 — Semester 2 (Feb 2027 – May/Jun 2027)

### Target milestones
- [ ] PCB assembled and integrated (Feb 2027)
- [ ] Full system integration test (Mar 2027)
- [ ] Benchmark evaluation complete: Pi 4 vs Pi 5, model comparisons (Mar 2027)
- [ ] Dissertation writing: literature review + methodology (Mar/Apr 2027)
- [ ] Dissertation writing: results + evaluation + conclusion (Apr/May 2027)
- [ ] Submission (May/Jun 2027)

---

_Add new weekly entries below as the project progresses._
