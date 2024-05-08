// create a redis client and display default messages:
    // upon errors and upon success

import { createClient } from 'redis';
const redis = require('redis');

const client = createClient().on('error', (err) => 
    console.log('Redis client not connected to the server:', err.message)
);
console.log('Redis has connected to the server');


function setNewSchool(schoolName, value) {
    client.set(schoolName, value, redis.print);
}

function displaySchoolValue(schoolName){
    client.get(schoolName, (err, res) => {
        console.log(res);
    });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');