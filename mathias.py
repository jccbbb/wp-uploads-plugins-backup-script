import shutil
import datetime
import os
import time

###############################################
# Step 1 - Make a backup of the folders #
###############################################

# The directory the backup folders should be saved in
directory = "wp_welandaluminium"

# Compare directories and delete those who were created more than 5 days ago (86400 = 24h*60min*60sec)
five_days_ago = time.time() - (5 * 86400)

# Get the date and time to name the backup folder
x = datetime.datetime.now()
current_date_and_time = x.strftime("%Y-%m-%d_%H-%M-%S")

# For Wordpress do we need to copy the /plugins and /uploads folder
source_dir_plugins = r"/home/jacob/TEST/oldwordpress/plugins"
source_dir_uploads = r"/home/jacob/TEST/oldwordpress/uploads"

# Destination path where the backups should be saved
destination_dir_plugins = r"/home/jacob/TEST/newwordpress/{}/{}/plugins".format(directory, current_date_and_time)
destination_dir_uploads = r"/home/jacob/TEST/newwordpress/{}/{}/uploads".format(directory, current_date_and_time)

# Copy the folders from the source to the destination
print("STEP 1")
print("Moving the uploads folder. This might take some time.")
shutil.copytree(source_dir_uploads, destination_dir_uploads, dirs_exist_ok=True)
print("Uploads folder done.")
print("Moving the plugins folder. This might take some time.")
shutil.copytree(source_dir_plugins, destination_dir_plugins, dirs_exist_ok=True)
print("Plugins folder done.")


###############################################
# Step 2 - Removing folders older than 5 days #
###############################################

print("STEP 2")

# Root path to the backup path
root = "/home/jacob/TEST/newwordpress/wp_welandaluminium"

no_folders_to_remove = False

# Find all backup folders older than 5 days and delete them
for item in os.listdir(root):
    path = os.path.join(root, item)

    # Checks if the directory is more than 5 days old
    if (os.stat(path).st_mtime <= five_days_ago) and os.path.isdir(path):
        no_folders_to_remove = True

        # Try to delete the folder
        try:
            shutil.rmtree(path)
            print("Removed folder {} successfully :)".format(item))

        # If the folder can't be deleted - throw an error
        except Exception as e:
            print(e)
            print("Could not remove folder :(")

if not no_folders_to_remove:
    print("No folders has been removed since there are no older than 5 days.")
