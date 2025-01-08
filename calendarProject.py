import os.path
import datetime as dt
import google.auth
import google_auth_oauthlib
import googleapiclient.discovery

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/calendar", "https://www.googleapis.com/auth/calendar.events"]

def get_user_input():
    events = []
    print("Welcome to the Google Calendar Scheduler!")
    print("You will be prompted to provide details for your schedule.")
    print("Type 'done' when you have finished adding events.")

    while True:
        summary = input("Enter the event name (or 'done' to finish): ")
        if summary.lower() == 'done':
            break

        location = input("Enter the event location: ")
        description = input("Enter the event description (e.g., instructor or additional details): ")
        start_date = input("Enter the start date (YYYY-MM-DD): ")
        start_time = input("Enter the start time (HH:MM, 24-hour format): ")
        end_date = input("Enter the end date (YYYY-MM-DD, same as start date if not recurring): ")
        end_time = input("Enter the end time (HH:MM, 24-hour format): ")
        time_zone = "US/Eastern"

        recurrence = input("Enter recurrence rule (e.g., 'WEEKLY;BYDAY=MO,WE,FR;UNTIL=YYYYMMDDT235959Z') or press Enter for none: ")

        event = {
            "summary": summary,
            "location": location,
            "description": description,
            "start": {
                "dateTime": f"{start_date}T{start_time}:00-05:00",
                "timeZone": time_zone
            },
            "end": {
                "dateTime": f"{end_date}T{end_time}:00-05:00",
                "timeZone": time_zone
            },
        }

        if recurrence:
            event["recurrence"] = [f"RRULE:FREQ={recurrence}"]

        events.append(event)

    return events

def main():
    creds = None

    # Checks if token.json exists
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    # If there are no (valid) credentials available, let the user log in
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())

        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        service = build("calendar", "v3", credentials=creds)

        # Get user input for events
        events = get_user_input()

        # Add events to the calendar
        for event in events:
            added_event = service.events().insert(calendarId="primary", body=event).execute()
            print(f"Event added: {added_event.get('htmlLink')}")

        print("All events have been successfully added to your Google Calendar!")

    except HttpError as error:
        print(f"An error occurred: {error}")

if __name__ == "__main__":
    main()



if __name__ == "__main__":
    main()
