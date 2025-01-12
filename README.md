# README for M.A.A.Y.A. (My Assistant and young android)

## Project Overview
M.A.A.Y.A. (Modular AI Assistant for Your Assistance) is a Python-based virtual assistant capable of performing various tasks such as responding to user queries, searching the internet, playing music, and managing system security. It leverages voice recognition, text-to-speech, and modular programming principles to create a dynamic and interactive user experience.

---

## Features

### 1. **Authentication**
- Ensures secure access by authenticating users.
- Unauthorized access triggers security protocols and terminates the application.

### 2. **Voice-Activated Commands**
- The assistant uses text-to-speech (TTS) to communicate with users.
- Includes a speech recognition module for seamless interaction.

### 3. **Core Functionalities**
- **User Interaction**: Wishes the user based on the time of the day.
- **Introduction**: Provides a self-introduction when prompted.
- **Internet Search**: Searches Wikipedia and general internet queries.
- **Music Playback**: Plays music and lists available songs.

### 4. **Web Access**
- Opens popular websites like YouTube, Gmail, Stack Overflow, and WhatsApp Web via voice commands.

### 5. **System Logs**
- Maintains a logfile to record user queries and interactions for analysis and debugging.

### 6. **Shutdown Protocol**
- Securely shuts down the assistant with a goodbye message.
- Cleans temporary files and uploads log files to a remote repository.

---

## How It Works
1. The system begins by authenticating the user using the `authentication()` function.
2. Upon successful authentication, M.A.A.Y.A. is activated and ready to accept commands.
3. Users can provide voice commands, which are processed and executed based on predefined functionalities.
4. Log files record all interactions for future reference.

---

## Setup and Usage

### Prerequisites
- Python 3.8 or later
- Required Python libraries:
  - `random`
  - `webbrowser`
  - Custom modules like `functions`, `speakcommand`, `introduce`, etc.

### Installation
1. Clone this repository:
   ```bash
   git clone <repository-url>
   ```
2. Install the required Python packages using:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the `main.py` file to start the assistant:
   ```bash
   python main.py
   ```

### How to Use
- Interact with the assistant through voice or text commands.
- Use keywords like:
  - "introduce yourself" for an introduction.
  - "search from wikipedia" or "search internet" for web queries.
  - "play music" or "show all available songs" for music-related tasks.
  - "open [website name]" for quick access to popular websites.
  - "shutdown the system" to terminate the assistant.

---

## Future Enhancements
- Add support for more advanced NLP features.
- Integrate with smart home systems.
- Include task scheduling and reminders.
- Develop a graphical user interface (GUI) for improved usability.

---

## Credits
Developed by **[Shivraj Anand]**.

---

