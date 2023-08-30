#!/usr/bin/env python3

#A pass statement reminds you that there is work to be done without interfering with your development.

from distro import name


def greet_programmer():
    print("Hello, programmer!")
greet_programmer()

def greet(name="Guido"):
    print(f"Hello, {name}!")
greet(name)    

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")
    return "Hello, programmer!"
greet_with_default(name)

def add(num1, num2):
    return num1 + num2
   

def halve(number):
    return number/2
