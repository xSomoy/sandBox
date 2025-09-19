import os
import requests

instraction_file = open("ins", "r")

instra = []
for i in instraction_file:
    temp = str(i).strip()
    instra.append(temp)

total_commands = len(instra)

stepcounter = 0


def next_step(stepcounter):
    if stepcounter < total_commands:
        return instra[stepcounter]
    else:
        return "EOF"


def create_file(stepcounter):
    file_name = next_step(stepcounter)
    file = open(file_name, "w")
    file.close()
    stepcounter += 1
    step_analyzer(stepcounter)


def create_directory(stepcounter):
    directory_name = next_step(stepcounter)
    os.mkdir(directory_name)
    stepcounter += 1
    step_analyzer(stepcounter)


def create(stepcounter):
    step = next_step(stepcounter)
    if step == "FILE":
        stepcounter += 1
        create_file(stepcounter)
    elif step == "DIR":
        stepcounter += 1
        create_directory(stepcounter)


def step_analyzer(stepcounter):
    step = next_step(stepcounter)
    if step == "CREATE":
        stepcounter += 1
        create(stepcounter)


step_analyzer(stepcounter)
