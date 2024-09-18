Excersize 1:
	1. What are the "max_bright" and "min_bright" values you found?
The max-bright value found was 55000, the min-bright value was 1100. The tests were being done in a fairly lit room but not bright, with the blinds drawn. We had some troubles with the onboard LED. We are sure the Pico W was running the correct firmware, and we tried referencing the onboard LED pin directly (25) and we tried running a script meant solely to turn on the onboard LED. None of these work, so we suspect some malfunction. However in the demo you can see that the ADC input is working and responding to input into the light sensor. The monitor shows that the value decreases to 1100 when we shined a light on the sensor, and increases to 55000 when I hold it into my pant.
- [Link to light demo](https://drive.google.com/file/d/1W-zhcyNIjvdQbRYpcltr392ZtkWKOine/view?usp=sharing).

Excersize 2:
	2. Using the code in exercise_sound.py as a starting point, modify the code to play several notes in a sequence from a song of your choosing.
We chose to make our own song using the interactive note to frequency table:
- [Link to song demo](https://drive.google.com/file/d/19Uq9blisrXyyjdNyYGA63GBbGnnNggkw/view?usp=sharing).

Excersize 3:
	1. Edit the exercise_game.py code to compute average, minimum, maximum response time for 10 flashes total.
	2. Have the Pi Pico automatically upload the response time data (say via HTTP POST to a REST server to a cloud server of your choice (e.g. Firebase, Heroku, etc.)
We added Key - value pairs to the dictionary and changed N to 10, so the game lasts 10 flashes at random time intervals before printing the score data (min, max, avg, and score) and writing the dictionary to JSON. We created a firebase firestore as our service to upload the data to. We then created a service token and imported it to the pico pi. We managed to get the wifi connection working however when starting the program with the firebase upload on the pico, it fried my laptop and so it was unable to gain a connection, luckily my laptop is still under warrenty. The game does work though and the json file is still saved locally to the pico. we had to install an extra library for the firebase connection, we think it may perhaps be this extra file that caused the issue.
- [Link to game demo]().

Useful Links:
- [Python list operators](https://www.w3schools.com/python/python_lists.asp).

