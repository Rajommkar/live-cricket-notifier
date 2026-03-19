import requests
from plyer import notification

# Your API details
RAPID_API_KEY = "Enter_Your_API_Key_Here"
RAPID_API_HOST = "Enter_Your_API_Host_Here"
URL = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/live"

def trigger_popup(title, message):
    # This function uses plyer to push the desktop notification
    notification.notify(
        title=title,
        message=message,
        app_name="Cricket Notifier",
        timeout=10 # The pop-up will stay on screen for 10 seconds
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
            
            # --- THE EXTRACTION LOGIC ---
            # Digging through the nested dictionaries to find a live match
            for type_match in data.get("typeMatches", []):
                for series in type_match.get("seriesMatches", []):
                    if "seriesAdWrapper" in series:
                        for match in series["seriesAdWrapper"].get("matches", []):
                            match_info = match.get("matchInfo", {})
                            
                            # Check if the match is currently happening
                            if match_info.get("state") == "In Progress":
                                team1 = match_info["team1"]["teamName"]
                                team2 = match_info["team2"]["teamName"]
                                status = match_info.get("status", "Score updating...")
                                
                                # Format what the notification will say
                                popup_title = f"{team1} vs {team2}"
                                popup_message = status
                                
                                print(f"Found live match: {popup_title}")
                                trigger_popup(popup_title, popup_message)
                                
                                match_found = True
                                break # Stop after finding the first live match
                        
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
    get_live_scores()