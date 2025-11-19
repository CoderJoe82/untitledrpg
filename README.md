# [PROJECT NAME] (Currently Untitled RPG Game)
![Version](https://img.shields.io/badge/version-0.0.1-blue)

> A dynamic, menu-driven RPG engine built with Python and Pygame, featuring AI-assisted content generation.

## 📖 About
[PROJECT NAME] is a text-heavy Role Playing Game that blends traditional OOP game architecture with modern Generative AI. 

**The Core Concept:** 
The game engine handles the hard logic (health, stats, combat math, inventory), while an AI "Toolbox" generates dynamic flavor text, zone descriptions, and unique encounters on the fly. This ensures the rules are rigid and fair, but the world feels infinite and responsive.

## 🏗 Architecture & Design Philosophy
This project adheres to strict separation of concerns to ensure scalability:

- **The Engine:** Pure Python logic. Handles the Game Loop and State Management.
- **The Models:** The "Source of Truth." All RPG data (Player, Items, World) lives here. No rendering code allowed.
- **The UI:** Pygame-based rendering. It observes the Models and draws them. It never modifies data directly.
- **The AI Toolbox:** An asynchronous worker system that fetches content in the background without freezing the main game loop.

*See `docs/DESIGN_PHILOSOPHY.md` for the full architectural standards.*

## 📂 Project Structure
The codebase is organized to prevent circular dependencies and spaghetti code:

```text
/src
  /engine   # Game Loop, State Manager, Asset Loading
  /models   # RPG Data (Player, Zones, Stats) - The Logic
  /ui       # Pygame Rendering & Widgets - The View
  /systems  # Mechanics (Combat, Event resolution)
  /ai       # API Clients and Async Workers
```

## 🛠 Getting Started

### Prerequisites
- Python 3.10+
- `pip` (Python Package Manager)

### Installation
1. Clone the repository:
   ```bash
   git clone [YOUR_REPO_URL]
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Game
```bash
python src/main.py
```

## 🗺 Development Roadmap

### Phase 1: The Engine Core 🚧
- [ ] Project Structure & Environment Setup
- [ ] Basic Game Loop (Pygame Window)
- [ ] State Manager (Menu -> Game transitions)
- [ ] Custom UI Renderer (Text Wrapping, Buttons)

### Phase 2: The Data Model
- [ ] Entity/Player OOP Base Classes
- [ ] World & Zone Data Structures
- [ ] Stat System Implementation

### Phase 3: Gameplay Loop
- [ ] Character Creation UI
- [ ] Navigation Logic (Node-to-Node)
- [ ] Basic Combat System (Math only)

### Phase 4: The AI "Toolbox" Integration
- [ ] Async Worker Threads
- [ ] OpenAI/LLM API Client
- [ ] Dynamic Zone Generation
- [ ] Flavor Text Injection