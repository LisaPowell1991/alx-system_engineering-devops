# How to use SFTP to move your local screenshots to the sandbox environment

### Steps you can follow:

#### 1. Open a Terminal or Command Prompt:
- Open a terminal or command prompt on your local machine. You'll use this to run SFTP commands.

#### 2. Connect to the Sandbox Environment:
Type sftp followed by your username and the sandbox address. It will look like this: sftp username@sandbox.example.com. Press Enter.

#### 3. Enter Your Password
It might ask you for a password. Just type it in and press Enter. Don't worry if you don't see any characters while typing - that's normal.

#### 4. Find Your Screenshot
Use the cd command to go to the folder where your screenshots are. For example, if your screenshots are in the "Pictures" folder, you can type cd Pictures and press Enter.

#### 5. Upload the Screenshot
Type put filename.jpg (replace "filename.jpg" with the actual name of your screenshot). This will send your screenshot to the sandbox. Press Enter.

#### 6. Check If It's There
To make sure your screenshot got to the sandbox, type ls and press Enter. This will show you a list of files. Look for your screenshot's name.

#### 7. Finish the Session
Once you're done, type exit and press Enter. This will close the SFTP session.
