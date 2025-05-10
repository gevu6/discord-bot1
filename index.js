require('dotenv').config();
const { Client, GatewayIntentBits, Partials } = require('discord.js');

const client = new Client({
  intents: [
    GatewayIntentBits.Guilds,
    GatewayIntentBits.GuildMessages,
    GatewayIntentBits.MessageContent
  ],
  partials: [Partials.Message, Partials.Channel, Partials.Reaction]
});

const TARGET_CHANNEL_ID = '1370494607661727794'; // ← заміни на свій ID

client.once('ready', () => {
  console.log(`✅ Бот запущено як ${client.user.tag}`);
});

client.on('messageCreate', async (message) => {
  if (message.channel.id !== TARGET_CHANNEL_ID || message.author.bot) return;

  if (message.attachments.size > 0) {
    console.log('Зображення знайдено!');
    try {
      await message.react('<:win:1370773118767075531>'); 
      await message.react('<:lose:1370737479090700408>'); 
      await message.react('<:kakashka:1370736094638772234>'); 
    } catch (error) {
      console.error('Не вдалося поставити реакції:', error);
    }
  }
});

client.login(process.env.DISCORD_TOKEN);
