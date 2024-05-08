var kue =  require('kue')
    , queue = kue.createQueue();

var job = queue.create('push_notification_code', {
    phoneNumber: String,
    message: string
});

job.on('complete', function(result){
    console.log('Notification job created', jobId);
})
.on('complete', function(result){
    console.log('Notification job completed')
})
.on('failing', function(result){
    console.log('Notification job failed')
});