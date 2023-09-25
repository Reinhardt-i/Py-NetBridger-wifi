import subprocess
import time


def run_simulation():

    server_process = subprocess.Popen(["python", "server.py"])
    time.sleep(1)

    # Run two client.py scripts in separate processes
    client1_process = subprocess.Popen(["python", "client.py"])
    client2_process = subprocess.Popen(["python", "client.py"])

    time.sleep(3)


    # TODO :
    #       input random usernames (preferably from a list of (2/3step)usernames)
    #       into client.py, then send soome random texts, check log file to see 
    #       if length has changed since the beggining of the program.

    server_process.terminate()
    client1_process.terminate()
    client2_process.terminate()

    time.sleep(10)

if __name__ == "__main__":
    run_simulation()
