#!/bin/bash

SESSION="devops"

# Start a new session, name the first window 'workstation', and detach
tmux new-session -d -s $SESSION -n 'main'

# Create the server windows
tmux new-window -t $SESSION:1 -n 'arch-sv1'
tmux new-window -t $SESSION:2 -n 'cent-sv2'
tmux new-window -t $SESSION:3 -n 'ubu22-sv3'
tmux new-window -t $SESSION:4 -n 'ubu26-sv4'
tmux new-window -t $SESSION:5 -n 'ubu-22-srv5'
# tmux new-window -t $SESSION:5 -n 'ubu-26-srv5'

# Optional: Send SSH commands to the server windows (ctrl + m) = 'Enter'
tmux send-keys -t $SESSION:1 'ssh 192.168.0.38' C-m
tmux send-keys -t $SESSION:2 'ssh 192.168.0.171' C-m
tmux send-keys -t $SESSION:3 'ssh 192.168.0.124' C-m 
tmux send-keys -t $SESSION:4 'ssh 192.168.0.3' C-m
tmux send-keys -t $SESSION:5 'ssh 192.168.0.139' C-m 
# tmux send-keys -t $SESSION:5 'ssh 192.168.0.66' C-m

# Select the first window and attach
tmux select-window -t $SESSION:0
tmux attach-session -t $SESSION