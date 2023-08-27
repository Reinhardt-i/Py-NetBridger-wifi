import subprocess
import time


def run_simulation():
    # Run the server.py script in a separate process
    server_process = subprocess.Popen(["python", "server.py"])
    time.sleep(1)

    # Run two client.py scripts in separate processes
    client1_process = subprocess.Popen(["python", "client.py"])
    client2_process = subprocess.Popen(["python", "client.py"])

    # Let the simulation run for a while
    time.sleep(10)

    server_process.terminate()
    client1_process.terminate()
    client2_process.terminate()


if __name__ == "__main__":
    run_simulation()
