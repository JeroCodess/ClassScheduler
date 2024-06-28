<h1>SchedyeSync AKA ClassScheduler</h1>

 ### [YouTube Demonstration](link) (To Be Made)

<h2>Description</h2>
<b>ClassScheduler</b> is a Python-based application designed to simplify the process of managing and synchronizing academic schedules with Google Calendar. This tool leverages the Google Calendar API to allow students to automatically add their class schedules to their Google Calendar, ensuring they stay organized and never miss a class.
<br />


<h2>Features:</h2>

- <b>Google Calendar Integration</b>: Seamlessly integrates with Google Calendar to manage and display your class schedules.
- <b>Automatic Event Creation</b>: Automatically adds detailed events to your calendar, including course names, locations, instructors, and timings.
- <b>Recurring Events</b>: Supports the creation of recurring events for classes that happen multiple times a week.
- <b>User-Friendly Input</b>: Simple prompts guide users through the process of adding their schedule to their calendar.
- <b>Credential Management</b>: Securely handles Google API credentials, with easy refresh and re-authentication processes.

<h2>How It Works: </h2>

1. <b>Authentication</b>: The program first checks for existing Google API credentials. If none are found or they are invalid, the user is prompted to authenticate via OAuth2.
2. <b>Event Creation</b>: Users are prompted to confirm if they want to add a predefined schedule of classes to their calendar.
3. <b>Confirmation</b>: Upon confirmation, the program adds the events to the specified Google Calendar, including details like course name, location, time, and recurrence rules.
4. <b>Feedback</b>: Users receive a confirmation with a link to the added events.

This tool is ideal for students looking to streamline their schedule management, allowing them to focus more on their studies and less on manual calendar entries.

<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>
