
# Dall-E 2 Discord Bot

This project is a Discord bot that uses the powerful Dall-E 2 model from OpenAI to generate content based on user requests. The bot is designed to provide a fun and easy-to-use content generation experience for members of a Discord server.




## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`DISCORD_TOKEN`

`OPENAI_API_KEY`


## Installation

* Download or clone the repository.
* Create an application and bot on the **[Discord Developer Portal](https://discord.com/developers/applications)** and obtain the bot's token.
* Obtain an OpenAI API key.
* Add the Discord token and OpenAI API key as environment variables with the names `DISCORD_TOKEN` and `OPENAI_API_KEY` respectively.
* Invite the bot to the server where you want to use it.
* Install necessary dependencies using the command

```bash
  pip install -r requirements.txt
```
    
## Deployment

To deploy this project run

```bash
  py main.py
```


## Usage

Once the bot is online on the server, users can interact with it using the command `!create` followed by a request. For example, `!create create a story about a robot in the future`. The bot will respond by generating a story based on the user's request.

![App Screenshot](https://i.postimg.cc/1zvdk5Nr/Screenshot-2023-01-17-030535.png)

## Contributing

Contributions are always welcome! If you would like to help improve this project, please create an issue or pull request on GitHub. If you have any questions or suggestions, you can contact me.


## License

This project is available under the [MIT](https://choosealicense.com/licenses/mit/) license.

