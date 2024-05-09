import { createClient } from 'redis';
import { promisify } from 'Util';
const redis = require('redis');

const client = createClient().on('error', (err) => 
    console.log('Redis client not connected to the server:', err.message)
);
console.log('Redis has connected to the server');

client.subscribe('holberton school');
client.on('message', (channel, message) => {
    console.log(`Received message on channel ${channel}: ${message}`);
    if (message === 'KILL_SERVER') {
        client.unsubscribe();
        client.quit();
    }
});
