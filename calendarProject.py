import os.path
import datetime as dt

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/calendar.readonly", "https://www.googleapis.com/auth/calendar.events"]

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
        
        # Call the Calendar API
        # now = dt.datetime.now().isoformat() + "Z"

        # #
        # print("What would you like to do?\n1. Print out future events")
        # num = input("Type option number here: ")
        # if num == 1:
        #     n = input("How many future events would you like to see?")
        #     event_result = service.events().list(calendarId="primary", timeMin=now, maxResults=n, singleEvents=True, orderBy="startTime").execute()
        #     events = event_result.get("items", [])

        #     if not events:
        #         print("No upcoming events found!")
        #         return
        #     # Print the start and name of the next n amount events
        #     for event in events:
        #         start = event["start"].get("dateTime", event["start"].get("date"))
        #         print(start, event["summary"])
        option = input("Are you sure you want to add Jeremy's Fall 2024 Class Schedule to your Calendar? (Y/N): ")
        if option == "y" or option == "Y":
            events = [
                {
                    "summary": "Computer Science-360",
                    "location": "Kern Grad Bldg 112",
                    "description": "Instructor: Mahfuza Farooque",
                    "start": {
                        "dateTime": "2024-08-26T10:35:00-05:00",
                        "timeZone": "US/Eastern",
                    },
                    "end": {
                        "dateTime": "2024-08-26T11:50:00-05:00",
                        "timeZone": "US/Eastern",
                    },
                    "recurrence": ["RRULE:FREQ=WEEKLY;BYDAY=TU,TH;UNTIL=20241213T235959Z"]
                },
                {
                    "summary": "Comm Arts and Sciences-100A",
                    "location": "Thomas Bldg 210",
                    "description": "",
                    "start": {
                        "dateTime": "2024-08-26T12:20:00-05:00",
                        "timeZone": "US/Eastern",
                    },
                    "end": {
                        "dateTime": "2024-08-26T13:10:00-05:00",
                        "timeZone": "US/Eastern",
                    },
                    "recurrence": ["RRULE:FREQ=WEEKLY;BYDAY=MO,WE,FR;UNTIL=20241213T235959Z"]
                },
                {
                    "summary": "Geography-1N",
                    "location": "Kern Grad Bldg 112",
                    "description": "Instructor: Erica Smithwick",
                    "start": {
                        "dateTime": "2024-08-26T13:25:00-05:00",
                        "timeZone": "US/Eastern",
                    },
                    "end": {
                        "dateTime": "2024-08-26T14:15:00-05:00",
                        "timeZone": "US/Eastern",
                    },
                    "recurrence": ["RRULE:FREQ=WEEKLY;BYDAY=TH;UNTIL=20241213T235959Z"]
                },
                {
                    "summary": "Engineering-287",
                    "location": "Sackett Bldg 207",
                    "description": "Instructor: William Lippert, Kimberly",
                    "start": {
                        "dateTime": "2024-08-26T14:30:00-05:00",
                        "timeZone": "US/Eastern",
                    },
                    "end": {
                        "dateTime": "2024-08-26T15:20:00-05:00",
                        "timeZone": "US/Eastern",
                    },
                    "recurrence": ["RRULE:FREQ=WEEKLY;BYDAY=TU;UNTIL=20241213T235959Z"]
                },
                {
                    "summary": "Computer Science-311",
                    "location": "Chambers Bldg 112",
                    "description": "Instructor: Shagufta Mehnaz",
                    "start": {
                        "dateTime": "2024-08-26T15:35:00-05:00",
                        "timeZone": "US/Eastern",
                    },
                    "end": {
                        "dateTime": "2024-08-26T16:25:00-05:00",
                        "timeZone": "US/Eastern",
                    },
                    "recurrence": ["RRULE:FREQ=WEEKLY;BYDAY=MO,WE,FR;UNTIL=20241213T235959Z"]
                },
                {
                    "summary": "Physics-212 - LAB",
                    "location": "Osmond Lab 313",
                    "description": "Instructor: Douglas Cowen",
                    "start": {
                        "dateTime": "2024-08-26T16:40:00-05:00",
                        "timeZone": "US/Eastern",
                    },
                    "end": {
                        "dateTime": "2024-08-26T17:55:00-05:00",
                        "timeZone": "US/Eastern",
                    },
                    "recurrence": ["RRULE:FREQ=WEEKLY;BYDAY=MO;UNTIL=20241213T235959Z"]
                },
                {
                    "summary": "Physics-212 - Lecture",
                    "location": "Thomas Bldg 101",
                    "description": "Instructor: Douglas Cowen",
                    "start": {
                        "dateTime": "2024-08-26T16:40:00-05:00",
                        "timeZone": "US/Eastern",
                    },
                    "end": {
                        "dateTime": "2024-08-26T17:55:00-05:00",
                        "timeZone": "US/Eastern",
                    },
                    "recurrence": ["RRULE:FREQ=WEEKLY;BYDAY=TU,TH;UNTIL=20241213T235959Z"]
                },
                {
                    "summary": "Physics-212 - Recitation",
                    "location": "Osmond Lab 104",
                    "description": "Instructor: Douglas Cowen",
                    "start": {
                        "dateTime": "2024-08-26T16:40:00-05:00",
                        "timeZone": "US/Eastern",
                    },
                    "end": {
                        "dateTime": "2024-08-26T17:55:00-05:00",
                        "timeZone": "US/Eastern",
                    },
                    "recurrence": ["RRULE:FREQ=WEEKLY;BYDAY=WE;UNTIL=20241213T235959Z"]
                }
            ]

            for event in events:
                event = service.events().insert(calendarId="40bed7dc61fd45260285e8cb6444cbe45454756eb22e77ee12d2c436c5cde1ba@group.calendar.google.com", body=event).execute()

            print(f"Events has been added {event.get('htmlLink')}")
        else:
            print("Okay, have a nice day")

    except HttpError as error:
        print(f"An error occurred: {error}")


if __name__ == "__main__":
    main()