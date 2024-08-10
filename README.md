# TCP Chat Room

A simple TCP-based chat room application built with Python using `tkinter` for the GUI. This project allows users to connect to a chat server and communicate with others in real-time.

## Features

- **Graphical User Interface (GUI)**: Built with `tkinter` for an interactive chat experience.
- **Multi-client Support**: Multiple users can connect to the chat server and send messages.
- **Real-time Messaging**: Messages are sent and received in real-time.
- **Socket Programming**: Utilizes Python's `socket` library for handling network connections between the client and server.

## Requirements

- Python 3.x
- The required Python libraries are specified in the `requirements.txt` file.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/TCP-Chat-Room.git
   cd TCP-Chat-Room
   ```
2. **Setup environment:**
   ```bash
   python3 -m venv myenv
   source myenv/bin/activate
   ```
3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. **Start the server:**
   ```bash
   python server.py
   ```
2. **Run the client GUI:**
   ```bash
   python client_gui.py
   ```
3. **Join the chat room:**
   ```bash
   Enter your alias (username) when prompted.
   Start chatting with other connected users.
   ```
