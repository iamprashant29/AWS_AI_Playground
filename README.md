You need to be logged in as an **AWS IAM user** to execute any files in the given folder.

**Steps to run the files:-**

1. Install AWS CLI on your machine - https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html (Ignore the first step if you have already installed AWS CLI in your local machine).
2. Login to the **AWS console** and in the profile section, go to **Credentials -> Create Access Key**. Downlaod the csv file containing your credentials (Ignore this step if you already have a Access Key Id & Secret Access Key).
3. Open terminal and run commmand `aws configure` and enter your **Access Key Id & Secret Access Key** to login as an IAM user.
4. Once logged in, navigate to the file location or provide the path_to_file in the command, you can run the python file with the command -
   `python3 your_file_name.py`
