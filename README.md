# deltacap
####
Please note that the default branch is master and not main


## How do the tasks depend on one another?
### Tasks depend on each other based on the conditions given. If the condition do not specify the task, it will execute and the program execution will stop. If a task is not listed in the tasks key of the json, the task will not be executed. The next task is determined by the outcome and the attached task to that outcome. For instance, if the outcome is success then the next task will be executed attached to the "Success" key.

## How is the success or failure of a task evaluated?
### It depends on the conditions given. The outcome key determines the success or failure.

## What happens if a task fails or succeeds?
### In a case of success or failure of task, the next task is looked for in the success or failure key. The next task is executed accordingly. For instance, if the outcome is success and "task2" is to be executed on success, then that task is executed.

