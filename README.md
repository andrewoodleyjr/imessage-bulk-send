# Bulk iMessage Sender

This script allows you to send multiple iMessages to a list of phone numbers using AppleScript and the `Messages` app on macOS. You can optionally include an image or video file along with the messages. The phone numbers should be stored in a CSV file.

## Prerequisites

- macOS system with the `Messages` app.
- Python 3 installed.
- `pandas` package installed.
  - To install `pandas`, use the following command:

    ```bash
    pip install pandas
    ```

## Setup

1. **CSV File**: You need a CSV file (`phone-numbers.csv`) that contains a column named `Phone` where each row includes a phone number in international format (e.g., `+16505551234`).

2. **Optional Image/Video**: If you'd like to send an image or video, ensure the file is available locally, and update the path in the script. The path should be absolute (full path).

3. **Messages Array**: Modify the array `messages_to_send` in the script to include the messages you'd like to send. Each message will be sent one by one in sequence.

## How to Use

1. **Clone or Download the Script**:

   Save the script to your local machine.

2. **Prepare the CSV File**:

   Create a CSV file named `phone-numbers.csv` in the same directory as the script. It should have a column labeled `Phone` with the recipient phone numbers.

   Example CSV:
   ```csv
   Phone
   +16505551234
   +14405556789
   +13105554321
   ```

3. **Optional: Add Image/Video**:

   - If you want to send an image or video, specify the absolute path to the file by editing the `image_file` variable.
   - If no file should be sent, comment out or set `image_file` to `None`.

   ```python
   image_file = os.path.abspath("./your-image.png")  # Use None to disable image sending
   ```

4. **Edit Messages**:

   Update the `messages_to_send` array with the messages you'd like to send.

   Example:
   ```python
   messages_to_send = [
       "Hi! You've been invited to join the Beta Program.",
       "We'd love your feedback on our app.",
       "The app helps with booking, reminders, and more.",
       "Reply to this message to get started!"
   ]
   ```

5. **Run the Script**:

   Open Terminal, navigate to the directory where the script is saved, and run:

   ```bash
   python3 script.py
   ```

## How It Works

- The script uses `pandas` to load the CSV file containing phone numbers.
- For each phone number, it sends the messages (and optionally, an image/video) using AppleScript, which controls the macOS `Messages` app.
- Messages are sent sequentially, and there is a slight delay between each message to allow for proper processing.

## Customization

- **Image/Video Sending**: If you'd like to disable image/video sending, comment out the line where `image_file` is defined or set it to `None`:

  ```python
  image_file = None
  ```

- **Message Delays**: The delays in sending messages can be adjusted by modifying the `delay` values in the `applescript` portion of the script. The delays ensure that the messages are sent properly without glitches.

## Error Handling

If any error occurs while sending messages, the script will print an error message and continue to the next phone number. Ensure your phone numbers are in the correct format and that the image/video path is correct if you are sending media.

## License

This project is open-source and available under the [MIT License](LICENSE).
