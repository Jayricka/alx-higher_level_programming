#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

if (!apiUrl) {
  console.error('Please provide the API URL.');
  process.exit(1);
}

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Failed to retrieve data. Status code:', response.statusCode);
  } else {
    const tasks = JSON.parse(body);

    const completedTasksByUser = tasks.reduce((userTasks, task) => {
      if (task.completed) {
        if (!userTasks[task.userId]) {
          userTasks[task.userId] = 1;
        } else {
          userTasks[task.userId]++;
        }
      }
      return userTasks;
    }, {});

    console.log(completedTasksByUser);
  }
});
