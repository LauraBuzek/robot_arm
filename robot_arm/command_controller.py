#!/usr/local/bin/python

import copy

from box_manipulator import BoxManipulator
import validate


class CommandController(object):
    EMPTY_SLOT = ''
    FULL_SLOT = 'X'

    def __init__(self):
        self.command_stack = []
        self.is_first = True

        self.box_manipulator = BoxManipulator()

    def run(self):
        while(True):
            input_var = input('>')
            input_elements = input_var.rsplit(' ')

            orig_command = copy.deepcopy(input_elements)
            boxes_state_after_command = self.execute_command(input_elements)
            if boxes_state_after_command is not None:
                self.print_state(boxes_state_after_command)
                self.command_stack.append({'boxes': copy.deepcopy(boxes_state_after_command), 'command': orig_command})

    def execute_command(self, input_elem):
        first_arg = input_elem.pop(0)

        if self.is_first:
            if first_arg != "size":
                print("You must establish the number of boxes with the 'size' command before running other commands")
                return None
            self.is_first = False

        command = None
        try:
            if first_arg == "replay" or first_arg == "undo":
                command = getattr(self, first_arg)
            else:
                command = getattr(self.box_manipulator, first_arg)
        except:
            print("Sorry, {} is not a valid box command".format(first_arg))
            return None

        boxes_state = None
        try:
            boxes_state = command(input_elem)
        except:
            print("Sorry, the parameters specified are invalid")
            return

        return boxes_state

    def replay(self, arg_list):
        validate.validate_list_of_numeric_arg(arg_list, 1, len(self.command_stack))

        n = int(arg_list[0])
        commands_to_replay = self.command_stack[-n:]

        for elem in commands_to_replay:
            command = copy.deepcopy(elem['command'])
            #Assuming you can't replay a replay because that would cause an infinite loop, skipping those
            if command[0] != 'replay':
                self.execute_command(command)

        return self.box_manipulator.boxes

    def undo(self, arg_list):
        validate.validate_list_of_numeric_arg(arg_list, 1, len(self.command_stack))

        n = int(arg_list[0])
        try:
            self.box_manipulator.boxes = self.command_stack[len(self.command_stack)-(n+1)]['boxes']
        except:
            print (str(self.command_stack[len(self.command_stack)-n]['boxes']))
        self.command_stack = self.command_stack[:-n]

        return self.box_manipulator.boxes

    def print_state(self, boxes_state):
        size = int(self.box_manipulator.boxes_size)
        for num in range(1,size+1):
            try:
                contains_string = self.FULL_SLOT if boxes_state[num] else self.EMPTY_SLOT
            except:
                raise Exception
            print(str(num) + ": " + contains_string)
