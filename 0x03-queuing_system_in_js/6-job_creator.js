var kue =  require('kue')
    , queue = kue.createQueue();

var job = queue.create('push_notification_code', {
    phoneNumber: String,
    message: string
});

job.on('complete', function(result){
    console.log(`Notification job: ${jobid} created`);
})
.on('complete', function(result){
    console.log(`Notification job: ${jobid} completed`)
})
.on('failed', function(result){
    console.log(`Notification job: ${jobid} failed`)
});