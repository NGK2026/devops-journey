#!/bin/bash

SESSION="devops"

# Start a new session, name the first window 'workstation', and detach
tmux new-session -d -s $SESSION -n 'main'

# Create the server windows
tmux new-window -t $SESSION:1 -n 'arch-srv1'
tmux new-window -t $SESSION:2 -n 'ubu-22-srv2'
tmux new-window -t $SESSION:3 -n 'ubu-26-srv3'
tmux new-window -t $SESSION:4 -n 'cent-srv4'

# Optional: Send SSH commands to the server windows (ctrl + m) = 'Enter'
tmux send-keys -t $SESSION:1 'ssh 192.168.0.38' C-m
tmux send-keys -t $SESSION:2 'ssh 192.168.0.124' C-m 
tmux send-keys -t $SESSION:3 'ssh 192.168.0.3' C-m
tmux send-keys -t $SESSION:4 'ssh 192.168.0.171' C-m

# Select the first window and attach
tmux select-window -t $SESSION:0
tmux attach-session -t $SESSION