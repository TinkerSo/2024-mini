## Teammate's Name: Lang Gui, Christian So

# Excercise 1
1) The "max_bright" value we found were about 550 - 600. This was accomplished by putting a phone light directly on top of the photoresistor.
   
The "min_bright" values we found were 50000 - 51000. 

Some design consideration we took into account was the orientation of the photoresistor. We bent it upwards to allow for more ambient light to be detected which is more characteristic of the rooms actual light. Additionally, we had to be cautious about the leads of the photoresistor and the LED do not intersect as we did a minimalist approch by attaching them directly to the rpi pico rather than a bread board. 

![ezgif com-optimize (2)](https://github.com/user-attachments/assets/fb768809-1583-42fd-b7ed-fe8caf5f0542)

# Excercise 2
## Solution
1. Referencing [frequency to notes chart](https://muted.io/note-frequencies/) we defined each note as key and its values as frequency in a dictionary. Then, we search up from the song "Not Like Us" by kendrick Lamar and convert the melody into a list of notes.

Additionally, we played each note for about 0.5 seconds and longer notes we added them twice to the list of notes. We play all the notes through a for loop for 3 times to demonstrate the backing track of "Not Like Us" sufficiently. 

Before playing any of the notes, we also jsut tested if a single frequency worked, utilizing the integration testing methodology. After we verified a single note worked, we tested thte range of notes and verified pico and the speaker was capable of outputting various frequencies. We then verified the song through the speaker and outputting the target note in the output logs. 

### [Demo Video](https://drive.google.com/file/d/1n-NT6gc6mlYI_GhmT9WiNHLh_GMzf1pI/view?usp=sharing)

# Excercise 3
## User-Story
The game that is implemented on the RPi Pico tests the user's reaction speed and scores them. The game starts by three flashes on the Pico. After that, every time the LED flashes, the user must press the button as fast as they can. The user only has 500ms to react or it will be considered a miss. If you press the button within 500ms, the time it took you to press the button. You will have 10 attempts, which means the LED will flash 10 times. Your score is calculated by a percentage of how many times out of the 10 times you did not miss to press. The goal of the game is to generate the lowest average possible and highest percentage score.

## Solution
1. We used the native built in math functions min and max to take the min and max of the list of scores. Additionally, we used the values of N and the native sum function to ultimately calculate the mean and the score. We then saved these values to a json file prepared to for part 2.

2. We used Google Firebase to host our server and store our json file. We interefaced with the Firebase through the Rest API by first connecting to the BU guest wifi. We used the BU guest wifi so we did not have to put our BU kerberos password within the GitHub while still having access to the cloud. 

3. Create a project and real database in Firebase. Enable the firebase API and modify the code to upload the json file to the realtime database URL.

4. In order to determine different games, we keep track the day and time as a json file name. 

### An image of the json data in the firebase see through the browser
<img width="1507" alt="Screenshot 2024-09-13 at 5 21 52 PM" src="https://github.com/user-attachments/assets/1c5b97fc-ef11-40eb-b5b6-09692982e384">

### An image of the values in the json file directly from the pico in the logs
<img width="577" alt="Screenshot 2024-09-13 at 5 53 30 PM" src="https://github.com/user-attachments/assets/58aa3c38-5a31-462a-989e-8de0a560c7fa">

## [Demo Video](https://drive.google.com/file/d/1mXKVypnZKJxnBAjuwhKc_toemvPJ2VOq/view?usp=sharing)
