import unittest
import subprocess
import time
import os
import random
import string

class TestSimulation(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.server_process = subprocess.Popen(["python", "server.py"])
        time.sleep(3)

    @classmethod
    def tearDownClass(cls):
        cls.server_process.terminate()
        cls.server_process.wait()

    def test_simulation(self):
        client1_process = subprocess.Popen(["python", "client.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        client2_process = subprocess.Popen(["python", "client.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        time.sleep(7)

        usernames = [''.join(random.choices(string.ascii_letters, k=8)) for _ in range(2)]
        messages = ['Hello!', 'How are you?', 'Random message']

        # Input random usernames and send random texts to the client subprocesses
        for i in range(2):
            client1_process.stdin.write(usernames[i] + '\n')
            client2_process.stdin.write(usernames[i] + '\n')
            client1_process.stdin.flush()
            client2_process.stdin.flush()

        for _ in range(10):
            message = random.choice(messages)
            client1_process.stdin.write(message + '\n')
            client2_process.stdin.write(message + '\n')
            client1_process.stdin.flush()
            client2_process.stdin.flush()
            time.sleep(1)

        client1_process.terminate()
        client2_process.terminate()
        client1_process.communicate()  # Wait for process to finish
        client2_process.communicate()  # Wait for process to finish

        time.sleep(10)

        log_file_path = "server.log"  # Check if the log file length has changed
        initial_log_size = os.path.getsize(log_file_path)

        # Assert that the log file size has increased
        new_log_size = os.path.getsize(log_file_path)
        self.assertGreater(new_log_size, initial_log_size)

        # Add specific assertions here, like checking for specific log entries
        # Example: Check if a certain username and message exist in the log.
        with open(log_file_path, "r") as log_file:
            log_contents = log_file.read()
            for username in usernames:
                self.assertIn(f"{username} connected from", log_contents)
            for message in messages:
                self.assertIn(f"Received from - !", log_contents)

if __name__ == "__main__":
    unittest.main()
    