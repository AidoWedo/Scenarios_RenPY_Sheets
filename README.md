# Scenarios Generator
## CSV Files
This contains several content. Example csv files for the characters, scenes, text, dialogue, etc.
Import these into Google Sheets (ensure you choose to import and import into the existing sheet. The sheets should be named Characters, Dialogue, etc, not Scenes - Characters. The Sheet itself (the whole sheet is called Scenes) ). The Google App Script code won't work if these are not named correctly.
![image](https://github.com/AidoWedo/Scenarios_RenPY_Sheets/assets/40786162/967ccfd9-77bb-4b09-8071-ecafd4411f45)


## Google Sheets App Script Code
Extensions - App Script (copy javascript code) into the Appscript code (code.gs) and run the code to ensure no errors.
![image](https://github.com/AidoWedo/Scenarios_RenPY_Sheets/assets/40786162/a879be7f-d481-4723-b5f5-037807a72fa0)


Deploy Code - Click Deploy to the right - New Deployment, and call it a name. Ensure you are running it as you and who has access will be anyone (you can restrict this to anyone with a Google account or just you)

![image](https://github.com/AidoWedo/Scenarios_RenPY_Sheets/assets/40786162/cca26aa6-bcac-4cf9-9199-a0c25f93a6b0)


Test it works. Click on the url and you should see some json based on your Google Sheets.

![image](https://github.com/AidoWedo/Scenarios_RenPY_Sheets/assets/40786162/efe6f67f-7524-4838-b325-eb56700f2eb9)


## RenPY

Download a version of RenPy from renypy dot org (as of writing, 8.2.3)

Unzip the file and run the Ren'Py Launcher (.exe). I recommend running The Question first to make sure you can see the images/ characters and hear the sound. If you can, create a new project.
Edit the script.rpy file (i.e. copy over the file from this GitHub repo) update the URL with your URL from the Google Sheets deployment, and launch the project

![image](https://github.com/AidoWedo/Scenarios_RenPY_Sheets/assets/40786162/d3169a06-309d-42a9-bc2c-f6a2ec0e442c)


## Credit
Inspired by this post https://marcin-rybicki.medium.com/no-code-game-dev-with-google-sheet-and-no-art-department-no-code-no-art-232ccecc85be
