// create a redis client and display default messages:
    // upon errors and upon success

import { createClient } from 'redis';

const client = createClient().on('error', (err) => 
    console.log('Redis client not connected to the server:', err.message)
);
console.log('Redis has connected to the server');
