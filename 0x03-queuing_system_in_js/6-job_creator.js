var kue =  require('kue')
    , queue = kue.createQueue();

var job = queue.create('push_notification_code', {
    phoneNumber: String,
    message: string
});

job.on('complete', function(result){
    console.log(`Notification job created ${jobid}`);
})
.on('complete', function(result){
    console.log(`Notification job completed ${jobid}`)
})
.on('failing', function(result){
    console.log(`Notification job failed`)
});