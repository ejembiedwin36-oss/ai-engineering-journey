Phase 00 — Learning Journal

Purpose of this file

This file is my personal reflection journal for Phase 00 of my AI Engineering journey.

It is different from the other documentation in this repository:

README.md explains the Phase 00 lessons in simple language so another beginner can learn from them.

LEARNING_JOURNAL.md records my personal experience: my challenges, mistakes, failures, fixes, strengths, lessons learned, and areas I need to improve.

The root LEARNING.md tracks my overall course progress and completed lessons.

In simple terms:

README = What I learned and how to understand it

LEARNING_JOURNAL = How I personally learned it

LEARNING.md = My overall progress record

This journal is not meant to pretend that I have mastered everything. It is an honest record of my growth, including the things that went wrong, the commands and tools I encountered, and what I learned from fixing problems.

Phase: Setup and Tooling
Status: ✅ Completed

This journal records my personal experience during Phase 00: my challenges, failures, fixes, strengths, and areas I still need to improve.

My Biggest Challenges

Working on Different Computers

One major challenge was working on school/lab computers where my local setup could disappear after a reset, logout, or shutdown.

This taught me that important work should not exist only on one computer.

How I solved it

I started committing and pushing important progress to GitHub regularly.

When I returned to a fresh computer, I could clone my repository and continue from my last pushed work.

What I learned

GitHub is not only a place to display projects.

It can also protect my work and allow me to continue from another computer.

Environment Problems

Sometimes packages or tools that worked previously were unavailable when I moved to another computer or recreated my environment.

For example, NumPy was missing when I needed it during Lesson 13.

How I solved it

I learned how to create a virtual environment:

python3 -m venv .venv

Then activate it:

source .venv/bin/activate

Then install the package I needed:

python -m pip install numpy

What I learned

Sometimes the code is correct and the real problem is the environment.

I also learned that I should check which environment I am using before assuming that my program is broken.

Git and GitHub

At the beginning, Git commands were unfamiliar.

I had to repeatedly use commands such as:

git status
git add
git commit
git push
git pull

Through repetition, they started becoming more familiar.

I also learned how Git can track files when they are moved into different folders.

What I learned

I do not need to memorize every Git command immediately.

I need to understand what each command is trying to do and become more comfortable through practice.

Understanding Generators

Generators were initially confusing.

I learned that a generator produces values one at a time instead of creating and storing all the values in memory at once.

I also learned that a generator can become exhausted after its values have been consumed.

Why this matters in AI

AI programs can work with very large datasets.

Loading everything into memory at the same time may use too much memory.

Generators can help process data gradually.

What I learned

Memory efficiency is important when working with large amounts of data.

Performance and Memory

During Lesson 13, I compared different ways of calculating a dot product.

My machine produced results approximately like:

Index loop: 9.69 ms

Generator version: 10.14 ms

map() version: 6.41 ms

I also compared memory usage:

List peak: about 4,000,456 bytes

Generator peak: about 464 bytes

What I learned

Two programs can produce the same answer but use very different amounts of time and memory.

This means an AI engineer should sometimes think about:

Correctness

Readability

Speed

Memory usage

NumPy Broadcasting

I first wrote feature standardization using pure Python.

Later, I performed the same type of calculation using NumPy broadcasting.

The result was approximately:

[[-1.225 -1.225]
 [ 0.     0.   ]
 [ 1.225  1.225]]

What I learned

Writing the pure-Python version first helped me understand what NumPy was doing.

NumPy can then perform numerical operations more efficiently over entire arrays.

My Strengths

Persistence

When something does not work, I usually keep working on it until I understand what happened.

This became especially important when environments disappeared or commands failed.

Asking Questions

I prefer to understand why something works instead of only copying code.

I often ask:

What does this command mean?

Why are we using it?

What happens if I remove it?

Why did this error happen?

This helps me build understanding instead of only following instructions.

Learning by Doing

I understand concepts better when I:

Type the command myself

Run the program

See the output

Make mistakes

Fix the mistakes

Explain what happened

Willingness to Start Again

Working on different computers forced me to rebuild environments several times.

Although this was frustrating, it helped me become more familiar with:

Git

GitHub

Python environments

Package installation

Terminal commands

Repository setup

Areas I Need to Improve

I still need to improve in:

Writing Python independently

Reading error messages carefully before asking for help

Remembering common terminal commands

Understanding mathematics

Writing tests

Explaining code without looking at notes

Breaking large problems into smaller steps

Remembering when to use different Git commands

Becoming more confident using Linux

Solving problems with less guidance over time

These are not failures.

They are areas I will continue practicing during the remaining phases.

Most Important Lesson From Phase 00

AI Engineering is not only about training AI models.

An AI engineer also needs to understand things such as:

Development environments

Python

Source control

GitHub

Data

Linux

Terminal commands

APIs

Dependencies

Docker

Debugging

Profiling

Performance

Memory

Reproducibility

Phase 00 gave me an introduction to these foundations.

I do not claim to have mastered all of them yet.

The purpose of Phase 00 was to introduce these tools and give me enough practical experience to continue learning.

Commands and Tools I Encountered in Phase 00

During Phase 00, I encountered many terminal, Git, Python, Docker, Linux, API, GPU, and development commands.

I do not yet remember every command without checking my notes.

This section is my beginner-friendly reference so I can remember:

What the command is called

What it does

Why I might use it

The goal is not to memorize everything at once.

The goal is to understand what the commands are for and become more comfortable with them through repeated use.

Basic Terminal Commands

pwd

Means: Print Working Directory

pwd

Shows the folder I am currently inside.

Example:

/home/student/ai-engineering-journey

I use this when I am unsure where I am in the terminal.

ls

Means: List

ls

Shows files and folders inside the current directory.

Example:

ls phase00

Shows the contents of the phase00 folder.

cd

Means: Change Directory

cd phase00

Moves into the phase00 directory.

To move back one level:

cd ..

mkdir

Means: Make Directory

mkdir practice

Creates a folder named practice.

Example with -p:

mkdir -p phase01/01-example

-p allows the command to create parent folders if they do not already exist.

touch

touch notes.md

Creates an empty file if the file does not already exist.

If the file already exists, touch does not open it for editing.

This helped me understand why touch was not the right command when I wanted to edit my existing journal.

rm

Means: Remove

rm file.txt

Deletes a file.

I should use this carefully because terminal deletion normally does not send the file to a recycle bin.

mv

Means: Move

mv old.txt new.txt

Can move a file or rename it.

cp

Means: Copy

cp file.txt backup.txt

Creates a copy of a file.

cat

Means: Concatenate

Example:

cat README.md

Displays the contents of a text file directly in the terminal.

head

head -n 40 README.md

Shows the beginning of a file.

-n 40 means:

Show the first 40 lines.

tail

tail -n 50 README.md

Shows the end of a file.

-n 50 means:

Show the last 50 lines.

find

find phase00 -maxdepth 1 -type d

Searches for files or directories.

In this example:

phase00 = where to search

-maxdepth 1 = search only one level deep

-type d = show directories

grep

grep "Python" README.md

Searches text for a word or pattern.

This example searches for lines containing Python.

which

which python

Shows which Python executable the terminal will use.

This can help me confirm that Python is coming from my virtual environment.

clear

clear

Clears previous text from the terminal screen.

It does not delete files or commands.

It only cleans the visible terminal screen.

history

history

Shows commands that were previously entered in the shell.

This can help me remember a command I used earlier.

Editing Files

nano

nano README.md

Opens a file using the Nano terminal editor.

Important Nano shortcuts:

Ctrl + O    Save
Enter       Confirm filename
Ctrl + X    Exit

code

code README.md

Opens a file using Visual Studio Code when the code command is available.

I find this easier when editing larger Markdown files.

Shell Concepts

source

source .venv/bin/activate

Runs commands from a file inside the current shell.

I mainly used it to activate my Python virtual environment.

>

Example:

echo "Hello" > file.txt

Sends output into a file.

> normally replaces the existing contents of the file.

>>

Example:

echo "Another line" >> file.txt

Adds output to the end of a file instead of replacing it.

|

Called a pipe.

Example:

history | grep git

It takes the output from the command on the left and sends it into the command on the right.

In this example:

history produces previous commands.

grep git keeps lines containing git.

Git and GitHub

git

Git is a version-control system.

It keeps track of changes made to files over time.

Git and GitHub are related, but they are not the same thing.

Git manages repository history.

GitHub stores Git repositories online and provides collaboration tools.

git status

git status

Shows the current state of my repository.

It can tell me:

Which branch I am using

Which files changed

Which files are staged

Whether there are uncommitted changes

Whether my branch is synced with GitHub

This is one of the most useful Git commands for me.

git add

git add file.py

Places a changed file into Git's staging area.

The staging area contains the changes I want to include in my next commit.

Example:

git add .

The . means the current directory and its changes.

I should still check git status so I know what I am staging.

git commit

git commit -m "docs: update learning journal"

Creates a saved checkpoint in Git history.

-m means that I am providing a commit message.

The message should briefly explain what changed.

git push

git push

Sends my local commits to the remote repository, such as GitHub.

This is especially important for me because the school computers I use can reset.

A commit that exists only locally can still be lost if the computer is reset.

Pushing sends it to GitHub.

git pull

git pull

Downloads newer changes from the remote repository and integrates them into my local branch.

I may use this when GitHub contains changes that my local computer does not have yet.

git clone

git clone <repository-url>

Downloads a repository onto a computer.

This is especially useful when I return to a fresh computer.

After cloning, I can continue from work that I previously pushed to GitHub.

git branch --show-current

git branch --show-current

Shows which Git branch I am currently using.

Example:

main

git log

git log

Shows previous commits.

It can display:

Commit ID

Author

Date

Commit message

git diff

git diff

Shows changes that have not been committed.

For one file:

git diff -- README.md

This is useful for checking exactly what changed before committing.

git restore

git restore file.txt

Restores an uncommitted file to its previous Git version.

I should use this carefully because it can discard work that has not been committed.

git rm

git rm file.txt

Deletes a Git-tracked file and stages the deletion.

This is useful when I intentionally want Git to record that a file was removed.

git mv

git mv old.py folder/old.py

Moves or renames a Git-tracked file.

I used this when organizing my Phase 00 files into lesson folders.

Python Commands

python3

python3 program.py

Runs a Python program using Python 3.

python

python program.py

Also runs Python.

Inside an activated virtual environment, python normally points to the Python interpreter inside that environment.

python -m

Example:

python -m pip

-m tells Python to run a Python module as a program.

Using:

python -m pip

helps make sure I am using pip that belongs to the selected Python interpreter.

Python Virtual Environments

python3 -m venv .venv

python3 -m venv .venv

Creates a Python virtual environment called .venv.

A virtual environment gives a project its own Python environment and installed packages.

This helps prevent different projects from interfering with each other.

Activating .venv

source .venv/bin/activate

Activates the virtual environment on Linux.

After activation, my terminal usually shows:

(.venv)

Example:

(.venv) ➜ ai-engineering-journey git:(main)

Python Package Management

pip

pip is Python's package installation tool.

Example:

python -m pip install numpy

Installs NumPy into the current Python environment.

pip install -r requirements.txt

python -m pip install -r requirements.txt

Installs packages listed inside requirements.txt.

-r tells pip to read package requirements from a file.

NumPy

numpy

NumPy is a Python library used for numerical computing.

It provides efficient arrays and mathematical operations commonly used in:

AI

Machine learning

Data science

Scientific computing

Example:

import numpy as np

numbers = np.array([1, 2, 3])
print(numbers * 2)

Output:

[2 4 6]

Docker

docker

Docker allows applications to run in isolated environments called containers.

A Docker container can package:

Code

Dependencies

Runtime environment

This helps make applications behave more consistently across different machines.

docker build

docker build .

Builds a Docker image using instructions from a Dockerfile.

The . tells Docker to use the current directory as the build context.

docker run

docker run <image-name>

Creates and starts a container from a Docker image.

docker ps

docker ps

Shows Docker containers that are currently running.

docker images

docker images

Shows Docker images stored on the computer.

docker compose

Docker Compose helps manage multiple related containers using a file such as:

compose.yaml

Example:

docker compose up

Starts services defined inside the Compose file.

Environment Variables

export

Example:

export API_KEY="example"

Creates or sets an environment variable for the current shell session.

Environment variables can be used for:

Configuration

API keys

Secrets

Environment-specific settings

Real API keys should not be committed to a public GitHub repository.

API and Network Tools

curl

curl https://example.com

curl is a command-line tool for sending and receiving data over networks.

It is commonly used for:

Testing APIs

Sending HTTP requests

Checking web endpoints

Linux Process Commands

ps

ps

Shows information about running processes.

ps is commonly understood as process status.

top

top

Shows running processes and system-resource usage continuously.

It can help me observe:

CPU usage

Memory usage

Running processes

kill

kill <PID>

Sends a signal to a running process.

PID means Process ID.

It can be used to stop a process.

Linux Storage Commands

df

df -h

Shows disk-space usage for filesystems.

-h means human-readable, so sizes appear in forms such as MB and GB.

du

du -sh folder-name

Shows how much disk space a file or folder is using.

-s = summary

-h = human-readable

Linux Permissions

chmod

chmod +x script.sh

Changes file permissions.

In this example:

+x

adds executable permission so the file can be run as a program or script.

Remote Computer and File Transfer Tools

ssh

Means: Secure Shell

Example:

ssh user@server

Allows me to securely connect to another computer over a network.

AI engineers often use SSH to connect to:

Cloud servers

GPU machines

Remote Linux systems

scp

Commonly described as Secure Copy.

It copies files securely between computers using SSH.

rsync

rsync

Synchronizes files and directories.

It can transfer only the files or parts that have changed instead of copying everything again.

Terminal Sessions

tmux

tmux means terminal multiplexer.

It allows terminal sessions to keep running even if I disconnect from a remote machine.

This can be useful for long-running tasks such as AI training.

GPU Commands

nvidia-smi

nvidia-smi

nvidia-smi means NVIDIA System Management Interface.

It displays information about NVIDIA GPUs, including:

GPU model

GPU memory

Driver information

GPU utilization

Processes using the GPU

It can help me check whether an NVIDIA GPU is available and being used.

Node.js and Tooling

node

Example:

node --version

Shows the installed Node.js version.

Node.js allows JavaScript to run outside a web browser.

npm

npm --version

npm is the package-management tool commonly used with Node.js.

It can install and manage JavaScript packages.

npx

npx <package>

Runs a package command without requiring me to install that command globally first.

I encountered npx while using the Skills CLI.

fnm

fnm means Fast Node Manager.

I used it to install and switch Node.js versions.

Example:

fnm install 24

Installs Node.js version 24.

Example:

fnm use 24

Switches the current shell to Node.js version 24.

Commands I Expect to Use Often

These are some commands I expect to use regularly as I continue learning:

pwd
ls
cd
mkdir

python
python3
python3 -m venv .venv
source .venv/bin/activate
python -m pip install <package>

git status
git add
git commit
git push
git pull
git clone
git diff
git log

I do not need to memorize every command immediately.

The important thing is to:

Understand what the command is used for.

Know how to find the command when I forget it.

Use it repeatedly.

Gradually become able to use it without guidance.

Going Into Phase 01

My next focus is:

Phase 01 — Math Foundations

My goal is not simply to memorize formulas.

I want to understand:

What the mathematics means

Why AI uses it

How to calculate it

How to represent it in Python

How it connects to real AI systems

I also want to continue improving my ability to explain what I am doing instead of only following instructions.

Reflection Template for Future Entries

I can reuse this section whenever I want to record an important learning experience.

Date

YYYY-MM-DD

Lesson / Topic

What was I studying?

What I Worked On

What did I practice, build, or study?

What I Understood

What can I now explain in my own words?

Challenge

What was difficult or confusing?

What Went Wrong

What failed or did not work as expected?

Why It Happened

What caused the problem?

How I Fixed It

What steps did I take to solve it?

What I Learned

What do I understand now that I did not understand before?

Commands or Tools I Used

Which commands, tools, libraries, or concepts did I encounter?

What did they do?

My Strength

What did I do well during this challenge?

What I Need to Improve

What should I practice more?

Next Action

What should I do next?