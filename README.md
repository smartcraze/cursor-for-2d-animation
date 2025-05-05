
# Manim Cursor MVP

Welcome to the **Manim Cursor MVP** project! This tool allows for natural language or code-based animation creation, inspired by **Manim**, the mathematical animation engine. The goal is to provide a simple, customizable way to create 2D animations with a live preview, making animation more accessible for developers and designers alike.

## Introduction

Manim Cursor is a **minimal viable product (MVP)** aimed at making animation creation as simple as possible. It leverages **Manim** for rendering animations, and incorporates a real-time preview feature, which allows users to see changes immediately. The tool is primarily targeted at developers and creators who want to build animations for educational content, tutorials, or presentations with little effort.

### Features:

* **Natural language input**: Allow users to generate animations with plain text instructions.
* **Code-based creation**: Full programmatic control using Python code.
* **Live preview**: See the animation progress in real-time as you write.

## Architecture

The **Manim Cursor MVP** follows a modular architecture, making it easy to extend and maintain. Below is a brief overview of the main components and their interactions:

### 1. **User Interface (UI)**

The UI handles user interactions. It includes the text input for natural language commands and code. It also integrates with the backend for live preview rendering.

* **Frontend**: A minimal web or desktop-based UI that supports text-based inputs and real-time updates.
* **Live Preview**: A section of the UI that updates every time the user changes the input, providing immediate feedback on the animation.

### 2. **Backend**

The backend is responsible for processing the input and rendering the animation. It connects to the **Manim** library and handles the logic for creating scenes based on the user's commands or code.

* **Manim Rendering Engine**: The core rendering engine based on the [Manim library](https://www.manim.community/), which is responsible for generating animations from scenes.
* **Command Processor**: This processes the natural language or code inputs from the UI and converts them into Manim-friendly formats.

### 3. **Python Environment**

A Python environment is set up to manage dependencies and run the code. We use a **virtual environment** to isolate the project dependencies, and **pip** is used for dependency management.

* **Dependencies**: All required Python packages (e.g., `manim`, `numpy`) are installed in a virtual environment, which ensures a clean and reproducible environment.
* **Render Pipeline**: The backend handles rendering the scene to files (e.g., videos) using the Manim rendering engine.

## Setup

### Prerequisites

Before you get started, make sure you have the following installed:

* **Python 3.12+**
* **pip** (Python's package manager)

### Steps to set up the project:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/smartcraze/cursor-for-2d-animation.git
   cd cursor-for-2d-animation
   ```

2. **Set up a virtual environment**:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # For Linux/macOS
   .venv\Scripts\activate     # For Windows
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Install LaTeX (for rendering)**:

   To ensure that Manim can compile LaTeX expressions (used in animations), you need to install a TeX distribution.

   * **For Ubuntu/Debian**:

     ```bash
     sudo apt install texlive-latex-base texlive-fonts-recommended texlive-latex-extra dvipng
     ```

   * **For macOS** (using Homebrew):

     ```bash
     brew install --cask mactex
     ```

5. **Run the project**:

   Once you’ve installed the dependencies, you can run the project. If it's a web app:

   ```bash
   python app.py
   ```

   If it's a CLI-based tool or desktop app, follow the specific command for starting the program.

## Usage


### Example commands:

```text
- "Create a ball that moves from left to right"
- "Draw a number line with points at -2, 0, 2"
```

These commands will be processed and translated into Manim scenes for rendering.

#tool will render your scenes and display a live preview of the animation as 
## Contributing

We welcome contributions! If you’d like to help improve the project, please feel free to fork the repository and submit a pull request. If you have a bug fix or a new feature in mind, open an issue to discuss it before proceeding.
