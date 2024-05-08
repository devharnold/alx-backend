import { createClient } from 'redis';
import { promisify } from 'Util'
const redis = require('redis');

const client = createClient().on('error', (err) => 
    console.log('Redis client not connected to the server:', err.message)
);
console.log('Redis has connected to the server');

const hs = {
    "Portland": 50,
    "Seattle": 80,
    "New York": 20,
    "Bogota": 20,
    "Cali": 40,
    "Paris": 2
};

for (let key in hs) client.hSet("HolbertonSchools", key, hs[key], redis.print);
client.hGetAll("HolbertonSchools", (err, res) => console.log(res));