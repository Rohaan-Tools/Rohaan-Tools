#!/bin/bash

# Custom welcome message
welcome_message="Welcome to Termux, Rohan! This is a custom Termux ornament."

# Custom prompt
custom_prompt="\033[1;32mRohan@Termux: \033[0m"

# Custom command execution
execute_command() {
    local command=$1
    echo "Executing command: $command"
    # Add your custom command execution logic here
    # For example, you can use eval to execute the command
    eval "$command"
}

# Main function
main() {
    clear
    echo -e "$welcome_message"
    echo

    while true; do
        read -p "$custom_prompt" command
        if [[ $command == "exit" ]]; then
            break
        else
            execute_command "$command"
        fi
    done
}

# Start the script
main
