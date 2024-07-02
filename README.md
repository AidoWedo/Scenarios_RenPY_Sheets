# Scenarios Generator
## CSV Files
This contains a number of content. Example csv files for the characters, scenes, text, dialogue etc.
Import these into Google Sheets (ensure you choose the option to import and import into the existing sheet. The sheets should be named Characters, Dialogue etc not Scenes - Characters. The Sheet itself (whole sheet is called Scenes) ). If these are not named correctly then the Google App Script code won't work.
![[Pasted image 20240702090304.png]]

## Google Sheets App Script Code
Extensions - App Script (copy javascript code) into the Appscript code (code.gs) and run the code ensure there aren't any errors.
![[Pasted image 20240702090520.png]]

Deploy Code - Click Deploy to the right - New Deployment call it a name. Ensure you are run it as you and who has access will be anyone (you can restrict this to anyone with a google account or just you)

![[Pasted image 20240702090848.png]]

Test it works. Click on the url and you should see some json based on your google sheets.

![[Pasted image 20240702091008.png]]

## RenPY

Download a version of RenPy from renypy dot org (as of writing 8.2.3)

Unzip the file, run the Ren'Py Launcher (.exe). I would recommend that you run the The Question first and make sure you can see the images/ characters and hear the sound. If you can create a new project.
Edit the script.rpy file (i.e. copy over the file from this github repo) update the url with your url from the google sheets deployment and launch the project

![[Pasted image 20240702091441.png]]
