import subprocess

# Check to ensure oc CLI is installed on host, and list the nodes.
subprocess.run('oc get nodes', shell=True)

# Determine the node group from user
role = input(str("\nPlease enter the node group to apply NTP to: "))
if role == 'master':
    role = 'master'
elif role == 'worker':
    role = 'worker'
elif role == 'infra':
    role = 'infra'
else:
    print("Please enter a valid node role. You can use master, infra, or worker.")
    exit(0)


# Generate the machine configuration from the provided default
def standard_config():
    print(f"\nGenerating the machine configuration for {role} node group...\n")
    # replace default role in the file (infra) with whichever role was specified
    #
    with open('ntp_machine_config.yaml', 'r') as file:
        filedata = file.read()

    # Replace the target string
    subprocess.run(f'touch ntp_machine_config_{role}.yaml', shell=True, stdout=None)
    filedata = filedata.replace('infra', f'{role}')
    filedata = filedata.replace("chrony-configuration", f'{role}-chrony-configuration')

    # Write the file out again
    with open(f'ntp_machine_config_{role}.yaml', 'w') as file:
        file.write(filedata)


def check_config():
    subprocess.run(f'cat ntp_machine_config_{role}.yaml', shell=True)
    is_correct = input('\nIs the above machine configuration correct? (YES or NO) ')
    if is_correct == "YES":
        print("\nApplying the configuration to your cluster...\n")
        subprocess.run("oc create -f ntp_machine_config.yaml", shell=True)
    elif is_correct == "NO":
        print("\nExiting...\n")
        exit(0)
    else:
        print("Please enter YES or NO.")
        exit(0)


# Run the tiny program!
standard_config()
check_config()
