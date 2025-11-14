import json

# Flow Manager class to manage the initialization and execution of the flow of various tasks.
class FlowManager:
    def __init__(self, flowFile_json):
        # JSON file loaded into the variable
        self.flowFile_json = flowFile_json
        # Extracting the condition key out of JSON
        self.conditions = self.flowFile_json['flow']['conditions']
        self.tasks = self.flowFile_json['flow']['tasks']
        # to save all the names of the tasks.
        self.tasks_map = []
        for each_task in self.tasks:
            self.tasks_map.append(each_task['name'])
        print("===================================================")
        print("Task List Loaded")
        print("===================================================")
        # A map to save all the conditions with respect to each task.
        self.condition_map = {}
        # The starting task with which we will start our executio.
        self.start_task = self.flowFile_json['flow']['start_task']
        # To make sure task execution do not fall in an infinite loop.
        self.execution_set = set()
        for each_condition in self.conditions:
            if each_condition['source_task'] not in self.condition_map:
                self.condition_map[each_condition['source_task']] = {}
                self.condition_map[each_condition['source_task']]['success'] = [each_condition['target_task_success']]
                self.condition_map[each_condition['source_task']]['failure'] = [each_condition['target_task_failure']]
                self.condition_map[each_condition['source_task']]['outcome'] = [each_condition['outcome']]
            else:
                self.condition_map[each_condition['source_task']]['success'].append([each_condition['target_task_success']])
                self.condition_map[each_condition['source_task']]['failure'].append([each_condition['target_task_failure']])
        # print(self.condition_map)
        # print(self.tasks_map)

    # This function is responsible for execution of tasks.
    def execute(self):
        '''
        curr_task = Current task being executed.
        next_task = Next task to execute.
        curr_output = what is the outcome of the current task execution.
        '''
        curr_task = self.start_task
        print(f"Executing First Task -> {curr_task}")
        self.execution_set.add(curr_task)
        curr_output = self.condition_map[curr_task]['outcome'][0]
        next_task = self.condition_map[curr_task][curr_output][0]
        while(next_task != "end" and next_task not in self.execution_set):
            self.execution_set.add(curr_task)
            if curr_task not in self.tasks_map:
                print(f"The target task {curr_task} is not in the task list. Exiting.")
                break
            if curr_task != self.start_task:
                print(f"Executing target {curr_task}")
            if curr_task not in self.condition_map:
                break
            next_task = self.condition_map[curr_task][curr_output][0]
            
            # print(f"Executing next target as {next_task}")
            curr_task = next_task
            if curr_task in self.condition_map:
                curr_output = self.condition_map[curr_task]['outcome'][0]
        print("Execution Complete")

# the json of task execution is stored in a separate file called "flowmanager.py"
with open('flow.json', 'r') as file:
    flowFile_json = json.load(file)

task = FlowManager(flowFile_json)
task.execute()