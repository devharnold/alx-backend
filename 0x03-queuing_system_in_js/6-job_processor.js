// creating the one redis server we will use
import { createClient } from 'redis';

const client = createClient().on('error', (err) => 
    console.log('Redis client not connected to the server:', err.message)
);
console.log('Redis has connected to the server');

// queue and job
var kue = require('kue')
    , queue = kue.createQueue();

function sendNotification(phoneNumber, message){
    console.log('sending Notification to PHONE_NUMBER, with message:', MESSAGE);
}

queue.process('push_notification_code', function(job, done) {
    const { phoneNumber, message } = job.data;
    sendNotification(phoneNumber, message);
    done();
});