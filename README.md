# Message Beautifier Bot

The Message Beautifier Bot is a simple Telegram bot that beautifies messages by adding a start and end tag to the text. It uses the Telethon library to interact with the Telegram API.

## Prerequisites

Before running the bot, make sure you have the following:

- Python 3.x installed on your system.
- `telethon` library installed. You can install it using `pip`:

  ```
  pip install -r requirements.txt
  ```

## Setup

1. Clone this repository to your local machine.

2. Obtain your `api_id` and `api_hash` from [my.telegram.org](https://my.telegram.org). Replace the empty strings in `config.py` with your actual `api_id` and `api_hash`.

3. If you are using a userbot, set `userbot` to `True` in `config.py`.

4. Set the `start` and `end` variables to what you would like to see in your message

---

If `userbot` is set to `True` in the configuration, any message starting with a dot (.) will be ignored by the bot. 

For any other message, the bot will add the defined `start` and `end` tag to the text.


## How to Use

1. Run the `main.py` script:

   ```
   python main.py
   ```

2. The bot will now be running and listening for new messages.


## Example

Input message: `Hello, this is a test message.`

Output message:
```
START #bold
Hello, this is a test message.
END #bold
```


The message will be sent back to the sender in HTML format, making it bold between the `START` and `END` tags.

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to modify and use it according to your needs! If you encounter any issues or have suggestions, please feel free to create an issue or pull request.

Enjoy beautifying your messages with the tg-message-beautifier! 😊