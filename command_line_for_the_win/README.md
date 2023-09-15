# Command line for the win

## Steps to follow how to use SFTP (Secure File Transfer Protocol) command-line tool to move your local screenshots to the sandbox environment.

#### Step 1: Open Command Prompt (CMD)
First, open the Command Prompt on your computer. You can do this by searching for "CMD" in the search bar and clicking on it.

#### Step 2: Connect to the Sandbox
Type sftp followed by your username and the sandbox address. It will look like this: sftp username@sandbox.example.com. Press Enter.

#### Step 3: Enter Your Password
It might ask you for a password. Just type it in and press Enter. Don't worry if you don't see any characters while typing - that's normal.

#### Step 4: Find Your Screenshot
Use the cd command to go to the folder where your screenshots are. For example, if your screenshots are in the "Pictures" folder, you can type cd Pictures and press Enter.

#### Step 5: Upload the Screenshot
Type put filename.jpg (replace "filename.jpg" with the actual name of your screenshot). This will send your screenshot to the sandbox. Press Enter.

#### Step 6: Check If It's There
To make sure your screenshot got to the sandbox, type ls and press Enter. This will show you a list of files. Look for your screenshot's name.

#### Step 7: Finish the Session
Once you're done, type exit and press Enter. This will close the SFTP session.
