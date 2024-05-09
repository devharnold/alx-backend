var kue =  require('kue')
    , queue = kue.createQueue();

function createPushNotificationJobs(jobs, queue) {
    if (jobs !== Array) {
        console.error("Jobs is not an array");
    }
    jobs.forEach(job => {
        const newJob = queue.create('push_notification_code_3')
        .save(function(err) {
            if(!err) {
                console.log(`Notification job created ${jobid}`);
            } else {
                console.error(`Error creating job`);
            }
        });
    });

    newJob.on('created', function() {
        console.log(`Notification job: ${jobid} created`);
    });
    newJob.on('completed', function() {
        console.log(`Notification job: ${jobib} completed`);
    });
    newJob.on('failed', function() {
        console.log(`Notification job: ${jobid} failed`);
    });
    newJob.on('progress', function() {
        console.log(`Notification job ${newJob.id} ${progress}% complete`);
    })
}

createPushNotificationJobs(jobs);