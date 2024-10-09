import pandas as pd
import os
import subprocess
import time

# Path to your CSV file
csv_file = "phone-numbers.csv"

# Path to the optional image or video you want to send (use absolute path, or None)
image_file = os.path.abspath("./mesh-gradient.png")  # Set this to None if no image should be sent
# image_file = None  # Uncomment this line to disable image sending

# Check if the image file exists (if provided)
if image_file and not os.path.exists(image_file):
    print(f"Image file not found: {image_file}")
    exit()

# Load phone numbers from the CSV file
df = pd.read_csv(csv_file)

# Function to send image (if present) and then multiple messages via AppleScript
def send_messages_via_applescript(phone, messages, image_path=None):
    # Construct AppleScript to send messages, and image if provided
    applescript = f'''
    tell application "Messages" to activate -- Bring Messages app to foreground

    tell application "System Events"
        delay 1
        keystroke "n" using {{command down}} -- Start new message
        delay 1
        keystroke "{phone}"
        delay 0.5
        keystroke return -- Select the conversation
        delay 0.5
        keystroke tab -- Navigate to the message field
        delay 0.5
    '''

    # If an image path is provided, add AppleScript to attach and send it
    if image_path:
        applescript += f'''
        set the clipboard to (POSIX file "{image_path}") -- Copy the file to clipboard
        delay 0.5
        keystroke "v" using {{command down}} -- Paste the file into the message field
        delay 1 -- Give time for the file to paste
        keystroke return -- Press Return to send the image or video
        delay 2 -- Wait to ensure the image/video is sent
        '''

    # Add multiple messages to be sent in sequence
    for message in messages:
        applescript += f'''
        delay 0.5
        keystroke "{message}"
        delay 0.5
        keystroke return -- Press Return to send the message
        delay 1
        '''

    # Close the AppleScript block
    applescript += '''
    end tell
    '''

    # Run the constructed AppleScript
    subprocess.run(["osascript", "-e", applescript])

# Array of formatted messages
messages_to_send = [
    "message",
    "message",
    "message",
    "message",
]

# Iterate over each phone number
for index, row in df.iterrows():
    phone = str(row['Phone'])
    print(f"Sending messages to: {phone}")

    # Send messages and optionally an image if provided
    try:
        send_messages_via_applescript(phone, messages_to_send)
        print(f"Messages sent to {phone}")
    except Exception as e:
        print(f"Error sending messages to {phone}: {e}")

print("All messages (and images if provided) sent.")
