import requests
import time
from plyer import notification
RAPID_API_KEY = "ENTER_YOUR_API_KEY_HERE"
RAPID_API_HOST = "ENTER_YOUR_API_HOST_HERE"
URL = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/live"

def trigger_popup(title, message):
    
    notification.notify(
        title=title,
        message=message,
        app_name="Cricket Notifier",
        timeout=10 
    )

def get_live_scores():
    print("Fetching live data...")
    headers = {
        "X-RapidAPI-Key": RAPID_API_KEY,
        "X-RapidAPI-Host": RAPID_API_HOST
    }

    try:
        response = requests.get(URL, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            match_found = False
            
           
            for type_match in data.get("typeMatches", []):
                for series in type_match.get("seriesMatches", []):
                    if "seriesAdWrapper" in series:
                        for match in series["seriesAdWrapper"].get("matches", []):
                            match_info = match.get("matchInfo", {})
                            
                          
                            if match_info.get("state") == "In Progress":
                                team1 = match_info["team1"]["teamName"]
                                team2 = match_info["team2"]["teamName"]
                                status = match_info.get("status", "Score updating...")
                                
                              
                                popup_title = f"{team1} vs {team2}"
                                popup_message = status
                                
                                print(f"Found live match: {popup_title}")
                                trigger_popup(popup_title, popup_message)
                                
                                match_found = True
                                break
                        
                        if match_found:
                            break
                if match_found:
                    break
            
            if not match_found:
                print("No matches are currently in progress right now.")
                
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
            
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("Starting Cricket Notifier... (Press Ctrl+C in the terminal to stop)")
    
    while True:
        get_live_scores()
        print("Waiting for 5 minutes before checking again...\n")
        
       
        time.sleep(300)
