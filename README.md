# live-cricket-notifier
"A Python script that fetches real-time cricket scores via RapidAPI and triggers desktop notifications."
# Live Cricket Score Notifier 🏏

A lightweight, automated Python script that fetches real-time cricket match data and delivers live score updates directly to your desktop via native OS notifications.

This project was built to combine a passion for the sport with backend software development, focusing on extracting and organizing live sports data.

## 🚀 Features
* **Real-Time API Integration:** Connects to the Cricbuzz API via RapidAPI to pull live match data.
* **JSON Parsing:** Efficiently navigates complex, heavily nested JSON dictionaries to locate active matches and extract specific team scores and status updates.
* **Cross-Platform Notifications:** Uses the `plyer` library to push non-intrusive desktop alerts (works on Windows, macOS, and Linux).
* **Automated Polling:** Runs as a continuous background process, automatically querying the server for fresh data every 5 minutes.

## 🛠️ Technologies Used
* **Language:** Python 3
* **Libraries:** `requests` (HTTP requests), `plyer` (Desktop GUI notifications), `time` (Loop management), `json` (Data handling)
* **API:** Cricbuzz Cricket API (via RapidAPI)

## ⚙️ Setup and Installation

**1. Clone the repository**
```bash
git clone [https://github.com/YOUR_USERNAME/live-cricket-notifier.git](https://github.com/YOUR_USERNAME/live-cricket-notifier.git)
cd live-cricket-notifier
