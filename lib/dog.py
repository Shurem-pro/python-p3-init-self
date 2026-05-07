#!/usr/bin/env python3

class Dog:

    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed = breed
        print(f"{name} is born!")

    def bark(self):
        print(f"{self.name} says Woof!")

fido = Dog("Fido")
# Fido is born!

snoopy = Dog("Snoopy")
# Snoopy is born!