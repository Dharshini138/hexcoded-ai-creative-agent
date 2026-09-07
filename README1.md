# 🎬 HexCoded AI Creative Director Agent

An AI-powered **Creative Director Agent** that transforms a creative brief into a structured advertising production workflow using generative AI.

The system helps creative professionals move from **idea → concept → storyboard → visual prompts → voiceover → captions** through an interactive node-based workflow.

---

## 🚀 Live Demo

**Live Demo:** `YOUR_NETLIFY_URL`

> Replace the URL above with your deployed Netlify URL.

---

## 📌 Project Overview

Creative professionals often need to convert a simple idea into a complete production plan involving multiple steps such as scripting, scene planning, visual generation, voiceover creation, and captions.

This project provides an AI-powered workflow that takes a natural-language creative brief and automatically generates a structured creative production plan.

The generated workflow is visualized as connected nodes, making the creative process easier to understand and iterate on.

---

## 🎯 Problem

Creating an advertisement or short-form video usually requires multiple creative decisions:

* What is the campaign concept?
* Who is the target audience?
* What should happen in each scene?
* What should the visuals look like?
* What should the voiceover say?
* What text should appear on screen?

These decisions are often handled manually and across multiple tools.

### 💡 Solution

The **AI Creative Director Agent** brings these steps into a single workflow.

A user provides a creative brief, and the AI generates:

* Campaign concept
* Target audience
* Tone and visual style
* Platform
* Duration
* Aspect ratio
* Three-scene storyboard
* Visual generation prompts
* Voiceover
* Captions
* Final voiceover
* Final caption

---

## ✨ Key Features

### 🧠 AI Creative Director

Converts a natural-language creative brief into a structured advertising plan using an LLM.

### 🔗 Node-Based Workflow

The creative process is represented as an interactive node-based workflow.

Example:

```text
Creative Brief
      ↓
Creative Director
      ↓
Script / Scene Planner
      ↓
   ┌──┴──┐
   ↓     ↓
Visual Voice
   ↓     ↓
Caption
   ↓
Final Advertisement
```

### 🎬 Scene-Based Storyboard

The AI generates three individual scenes containing:

* Scene description
* Duration
* Visual prompt
* Voiceover
* Caption

### 🎨 Visual Generation Prompts

Each scene receives a detailed prompt that can be used with an image or video generation model.

### 🎙️ Voiceover Generation

Each scene contains AI-generated narration suitable for the intended advertisement.

### 📝 Caption Generation

The system generates short on-screen text for each scene.

### 🔍 Scene Inspector

Clicking a scene allows the user to inspect its:

* Description
* Visual Prompt
* Voiceover
* Caption
* Duration

### ⚡ Local LLM Support

The project uses **Ollama** with `llama3.2` for local AI generation.

---

## 🏗️ Architecture

```text
                    ┌─────────────────────┐
                    │   Creative Brief    │
                    │      (User)         │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Next.js Frontend  │
                    │                     │
                    │ Interactive Workflow│
                    └──────────┬──────────┘
                               │
                         HTTP Request
                               │
                               ▼
                    ┌─────────────────────┐
                    │    FastAPI Backend  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Creative Director   │
                    │      Agent          │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │      Ollama         │
                    │      Llama 3.2      │
                    └──────────┬──────────┘
                               │
                         Structured JSON
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Creative Workflow   │
                    │                     │
                    │ Scenes + Prompts +  │
                    │ Voiceover + Captions│
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ React Flow Canvas   │
                    │                     │
                    │ Interactive Nodes   │
                    └─────────────────────┘
```

---

## 🛠️ Tech Stack

### Frontend

* Next.js
* React
* TypeScript
* Tailwind CSS
* React Flow (`@xyflow/react`)
* Lucide React

### Backend

* Python
* FastAPI
* Pydantic
* Ollama

### AI

* Llama 3.2
* Ollama
* Structured JSON generation

### Development

* Git
* GitHub
* Netlify

---

## 📂 Project Structure

```text
hexcoded-creative-director/
│
├── frontend/
│   ├── app/
│   │   ├── page.tsx
│   │   ├── layout.tsx
│   │   └── ...
│   │
│   ├── public/
│   ├── package.json
│   ├── next.config.ts
│   └── ...
│
├── backend/
│   └── app/
│       ├── agents/
│       │   └── creative_director.py
│       │
│       ├── routes/
│       │   └── creative.py
│       │
│       └── main.py
│
└── README.md
```

---

# ⚙️ How It Works

## 1. User enters a creative brief

Example:

```text
Create a 20-second Instagram advertisement for a premium
skincare product targeting young professionals.
The ad should feel modern, luxurious and minimal.
```

---

## 2. Backend receives the brief

The frontend sends the creative brief to the FastAPI backend.

```http
POST /api/creative/generate
```

---

## 3. Creative Director Agent processes it

The Creative Director Agent sends a structured prompt to the LLM.

The model is instructed to generate a complete production plan.

---

## 4. AI generates structured JSON

The response contains information such as:

```json
{
  "campaign_name": "Glow Beyond",
  "target_audience": "Young professionals",
  "creative_concept": "Minimal luxury skincare",
  "tone": "Premium and modern",
  "platform": "Instagram",
  "duration_seconds": 20,
  "aspect_ratio": "9:16",
  "scenes": [
    {
      "scene_number": 1,
      "duration_seconds": 6,
      "description": "Opening product reveal",
      "visual_prompt": "Cinematic luxury skincare product...",
      "voiceover": "Your skin deserves more.",
      "caption": "Elevate your routine."
    }
  ]
}
```

---

## 5. Workflow is generated

The frontend converts the generated data into interactive React Flow nodes.

The user can visually explore the complete creative pipeline.

---

## 6. Scene inspection

Selecting a scene opens the Scene Inspector where the generated creative information can be reviewed.

---

# 🧩 API

### Generate Creative Workflow

```http
POST /api/creative/generate
```

### Request

```json
{
  "brief": "Create a 20-second advertisement for a premium skincare brand."
}
```

### Response

```json
{
  "success": true,
  "workflow": {
    "campaign_name": "...",
    "target_audience": "...",
    "creative_concept": "...",
    "tone": "...",
    "platform": "...",
    "duration_seconds": 20,
    "aspect_ratio": "9:16",
    "scenes": []
  }
}
```

---

# 💻 Local Setup

## Prerequisites

Install:

* Node.js
* Python 3.10+
* Ollama
* Git

---

## 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL

cd hexcoded-creative-director
```

---

# Backend Setup

Go to the backend:

```bash
cd backend
```

Create a virtual environment:

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Start Ollama

Install Ollama and pull the model:

```bash
ollama pull llama3.2
```

Make sure Ollama is running.

---

## Start FastAPI

From the backend directory:

```bash
uvicorn app.main:app --reload
```

Backend will run on:

```text
http://127.0.0.1:8000
```

---

# Frontend Setup

Open another terminal:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

Open:

```text
http://localhost:3000
```

---

# 🔄 End-to-End Flow

```text
User
 │
 │ Creative Brief
 ▼
Next.js UI
 │
 │ POST request
 ▼
FastAPI
 │
 ▼
Creative Director Agent
 │
 ▼
Ollama / Llama 3.2
 │
 │ Structured JSON
 ▼
Workflow Generator
 │
 ▼
React Flow
 │
 ├── Creative Brief
 ├── Creative Director
 ├── Scene Planner
 ├── Scene 1
 ├── Scene 2
 ├── Scene 3
 ├── Visual
 ├── Voiceover
 ├── Caption
 └── Final Advertisement
```

---

# 🎨 Why This Is Useful for Creative Professionals

The project is designed around the workflow of:

* Editors
* Designers
* Filmmakers
* Creative agencies
* Content teams
* AI content creators

Instead of treating AI generation as a single prompt-and-response interaction, the system turns the creative process into a **visual production workflow**.

This makes it easier to understand what the AI is producing and where each creative decision fits into the production pipeline.

---

# 🔮 Future Enhancements

Planned improvements include:

* Image generation for each scene
* AI video generation
* Voice synthesis
* Drag-and-drop workflow editing
* Scene regeneration
* Multi-agent creative collaboration
* Brand style memory
* Automatic storyboard previews
* Export workflow as JSON
* Export production plan as PDF
* Integration with external creative generation models
* Persistent project history
* Human approval checkpoints

---

# 🧠 Design Philosophy

The goal is not simply to generate content.

The goal is to create an **AI-native creative workflow** where professionals can:

```text
Think
  ↓
Plan
  ↓
Generate
  ↓
Review
  ↓
Iterate
  ↓
Produce
```

The node-based interface provides a visual representation of this process while the Creative Director Agent handles the initial creative planning.

---

# 👩‍💻 Author

**Dharshini M**

M.Sc. Software Systems

Interested in AI, Generative AI, Data Engineering, Analytics and AI-powered product development.

---

## 📄 License

This project is developed as a prototype for exploring AI-powered creative workflows.
