#!/usr/bin/python3

class CleaningRobot:
    def clean(self):
        print("I can clean")

class CookingRobot:
    def cook(self):
        print("I can cook")

class MultiTaskRobot(CleaningRobot, CookingRobot):
    pass

multi_task_robot = MultiTaskRobot()
multi_task_robot.clean()
multi_task_robot.cook()
