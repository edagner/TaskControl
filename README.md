# Task Control Rest API

This application will allow users to track tasks and any associated steps with carrying out that task. Like any REST API, 
users can send standard http requests to the api to add, update, and delete steps. This can be done with the included Taskmaster module.
Within it, users can invoke methods to view all tasks and their associated task steps. Below are instructions on how to best use it.


__to import and initialize__ <br />
```from Taskmaster import TaskMaster```<br />
```task = TaskMaster("url", "username", "password")```


__View all tasks__ <br />
```task.view_all()```

__Add a task__ <br />
```task.add_task("Do taxes")```

__Update the name of a task__ <br />
```task.update_taskname(task_id, "Complete 2018 Taxes")```

__Delete the task entry__ <br />
```task.delete_task(task_id)```


This is just a sample of the methods that can be invoked. Feel free to inspect Taskmaster.py for the complete list.
