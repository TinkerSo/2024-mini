# Exercise: Response time measurement and cloud upload

The LED blinks at random intervals.
The exercise_game.py script measures response time.

## Questions

1. Edit the exercise_game.py code to compute average, minimum, maximum response time for 10 flashes total.
2. Upload the response time data to a cloud service of your choice.


##Solution
1. We used the native built in math functions min and max to take the min and max of the list of scores. Additionally, we used the values of N and the native sum function to ultimately calculate the mean and the score. We then saved these values to a json file prepared to for part 2.

2. We used Google Firebase to host our server and store our json file. We interefaced with the Firebase through the Rest API by first connecting to the BU guest wifi. We used the BU guest wifi so we did not have to put our BU kerberos password within the GitHub while still having access to the cloud. 

The response to these questions is your unique code and results in Report.md in your team's forked GitHub repository.
<img width="1507" alt="Screenshot 2024-09-13 at 5 21 52 PM" src="https://github.com/user-attachments/assets/1c5b97fc-ef11-40eb-b5b6-09692982e384">
