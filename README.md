# Key-logger-final
! NOTE ! - Educational Purpose Only!
I created this program to upload a recorded keystrokes in a text file to google drive without signing in (again and again)
set tp upload text file every 5 seconds.
1) this program uploads the already existing text.txt file to the google drive
2) to run test.py we should have the credentials.json file which needs to be downloaded from https://console.cloud.google.com/apis
3) the credential-fake.json file is only a dummy (we should have the original one to run)
4) you have to sign in the very first time, it will generate the token.pickle file
5) Refresh token is also included in the token.pickle file
6) After getting that token.pickle file you will never want to sign in again. even you can run the program in another computer.


! NOTE ! - credential.json file have sensitive date so don't publish that publicaly, KEEP IT SAFE.
! NOTE ! - Token.pickle file have sensitive date so don't publish that publicaly, KEEP IT SAFE.

-remember to install the relevant libraries before running.