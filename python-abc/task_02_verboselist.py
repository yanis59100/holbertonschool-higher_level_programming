#!/usr/bin/env python3
class VerboseList(list):
    def append(self, item):
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, item):
        super().extend(item)
        print("Extended the list with [{}] items.".format(len(item)))

    def remove(self, item):
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        try:
            print("Popped [{}] from the list.".format(self[index]))
            return super().pop(index)
        except IndexError:
            print("Item doesn’t exist in the list.")
