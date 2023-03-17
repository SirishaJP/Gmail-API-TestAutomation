#  GMail API by Sirisha Jotheeswaran Padmasekhar

### Introduction 

This project is focused on setting up a test Gmail account and enabling the necessary APIs to allow for programmatically sending emails and searching for specific messages in the mailbox based on keywords in the subject or body text. The goal of this project is to provide a simple guide for setting up a Gmail API connection in Python and demonstrating the basic functionalities that it offers. To get started, you will need to follow a few basic steps to set up a test Gmail account and enable the necessary APIs.

### Creating a test Gmail Account 

To create a Gmail Test account, follow the steps below:

1. Go to the Gmail website (https://mail.google.com/) and click on the "Create account" button.

2. Fill out the registration form with your personal information, such as your name, birthdate, and location. You will also need to choose a username and password.

3. For security reasons, you may be required to provide a phone number or an alternate email address for verification purposes while creating an Gmail Account. 

4. Once you have set up your new Gmail account, you can use it to send and receive test emails, as well as to enable and test the Gmail API functionality.

### GMail API: Authentication with OAuth

1. Go to [Google Cloud Console](https://console.cloud.google.com/getting-started) and click Create project and select the project. 

2. To enable API, Go to navigation bar > APIs & Services > Library, go to GMail API and click on the enable button. 

3. Go to navigation bar > APIs & Services > OAuth Consent Screen 

4. Add the scope https://mail.google.com/ and add test users (i.e.,Email ID), and check test user and scopes in summary section. 

5. To create  OAuth Client ID -  go to navigation bar > APIs & Services > Create Credentials > OAuth Client ID. Choose Application type as Desktop App and click on create. 

6. OAuth client ID is sucessfully created. Download the json file and rename the file as 'credentials.json'. Now move the file to the python code's working directory (i.,e, location at which src.py file exists)


# Requirements 
   
         Python3.11.2

To check if the specific version of python has been installed in your system 

1. Go to terminal / command prompt, and type,  python --version   
2. The python version will be displayed on the screen. Update the version 3.11.2. 
3. If python is not installed in your system, please follow the steps in this [document](https://packaging.python.org/en/latest/tutorials/installing-packages/) 
4. You have now successfully installed / updated python! 

### Installations 

To install the required packages, follow the steps below: 

1. Open a command-line interface (e.g. Terminal on macOS, Command Prompt on Windows).

2. Navigate to the directory where the requirements.txt file is located using the cd command.
               for example: cd foldername 

3. Run the following command to install the packages listed in the requirements.txt file:
               pip install -r requirements.txt

4. This command will read the requirements.txt file and install all the packages listed in it, along with their dependencies, if they are not already installed.

5. Wait for the installation process to complete. 

6. Once the installation is complete, you should be able to use the installed packages. 


### Run

To run the above code, 

1. Replace the reciever email ID in the create_message(), In addition, you can also make changes in the header, body of the email as well as the query in search_email(), based on requirements.  

2. Open the terminal on your computer. On Windows, this is the Command Prompt, On macOS it is terminal. 

3. Navigate to the directory where the Python file is located using the "cd" command. For example, if the file is located on your Desktop, you can navigate to it by typing "cd Desktop" in the terminal.

4. Once you are in the correct directory, type "python" followed by the name of the Python file you want to run. For example, if your file is named "src.py", you would type "python src.py" in the terminal / command prompt.

5. Press Enter to run the file.

### Output

If this is the first time running the code, you'll need to authorize the user in the redirected sign-in page. To do so, sign in to your Google account using your Gmail login credentials. Once you've authorized the user, you should be able to see the relevant emails in your inbox, and the terminal will display a list of emails that contain the keyword 'recommendation service' or the keyword specified in the query.

### Aknowledgement 

I wanted to take a moment to express my gratitude for the opportunity to participate in the coding challenge as part of the application process at Haensel AMS for Data Engineer position. It was a great experience, and I enjoyed tackling the challenges presented to me. I appreciate the time and effort that you and the team have put into reviewing my application, and I am eagerly looking forward to hearing from you about the next steps in the process. Thank you once again for this opportunity, and I look forward to the possibility of working together in the future.














