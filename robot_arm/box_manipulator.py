#!/usr/local/bin/python

import validate


class BoxManipulator(object):
    def __init__(self):
        self.boxes = {}
        self.boxes_size = 0

    #needs to error if boxes remains empty
    def size(self, arg_list):
        validate.validate_list_of_numeric_arg(arg_list, 1, None)

        n = int(arg_list[0])

        #Assuming that if the number of boxes changes, boxes that continue to exist will keep their values, and new
        #boxes will be initialized with no value in them. Boxes will be erased if size shrinks
        new_boxes = {}
        for num in range(1,n+1):
            if num in self.boxes:
                new_boxes[num] = self.boxes[num]
            else:
                new_boxes[num] = False

        self.boxes = new_boxes
        self.boxes_size = n

        return self.boxes

    def add(self, arg_list):
        validate.validate_list_of_numeric_arg(arg_list, 1, len(self.boxes))

        slot = int(arg_list[0])
        self.boxes[slot] = True

        return self.boxes

    def mv(self, arg_list):
        #Assumes that this command switched the contents of the two boxes
        validate.validate_list_of_numeric_arg(arg_list, 2, len(self.boxes))

        slot_one = int(arg_list[0])
        slot_two = int(arg_list[1])
        temp_slot_two = self.boxes[slot_two]
        self.boxes[slot_two] = self.boxes[slot_one]
        self.boxes[slot_one] = temp_slot_two

        return self.boxes

    def rm(self, arg_list):
        validate.validate_list_of_numeric_arg(arg_list, 1, len(self.boxes))

        slot = int(arg_list[0])
        self.boxes[slot] = False

        return self.boxes

