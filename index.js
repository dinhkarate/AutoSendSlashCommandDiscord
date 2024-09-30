const Discord = require("discord.js-selfbot-v13");
const data = require("./info.json");

const client = new Discord.Client();

let channel = data.channel
let command = data.command
let subcommand = data.subcommand
let bot_id = data.bot_id

client.on("ready", () => {
    console.log(`Logged in as ${client.user.tag}!`);
    client.channels.cache.get(channel).sendSlash(bot_id, command, subcommand);
});

client.login(data.token);