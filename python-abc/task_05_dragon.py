#!/usr/bin/env python3
"""The Dragon class inherits both swimming and flying abilities from SwimMixinand FlyMixin"""


class SwimMixin:
    def swim(self):
        print("The creature swims!")

class FlyMixin:
    def fly(self):
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")