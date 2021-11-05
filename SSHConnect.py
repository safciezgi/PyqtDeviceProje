import paramiko
import os, sys, time

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import socket


class Ssh_Util:
    "Class to connect to remote server"

    def __init__(self):
        self.ssh_output = None
        self.ssh_error = None
        self.client = None
        self.host = None
        self.username = None
        self.password = None
        self.timeout = 50000
        self.commands = None



    def connect(self):
        "Login to the remote server"
        try:
            # Paramiko.SSHClient can be used to make connections to the remote server and transfer files
            print("Establishing ssh connection")
            self.client = paramiko.SSHClient()
            # Parsing an instance of the AutoAddPolicy to set_missing_host_key_policy() changes it to allow any host.
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            # Connect to the server
            if (self.password == ''):

                self.client.connect(hostname=self.host, username=self.username, timeout=self.timeout, allow_agent=False, look_for_keys=False)
                print("Connected to the server", self.host)
            else:
                self.client.connect(hostname=self.host, username=self.username, password=self.password,
                                    timeout=self.timeout, allow_agent=False, look_for_keys=False)
                print("Connected to the server", self.host)
        except paramiko.AuthenticationException:
            print("Authentication failed, please verify your credentials")
            result_flag = False
        except paramiko.SSHException as sshException:
            print("Could not establish SSH connection: %s" % sshException)
            result_flag = False
        except socket.timeout as e:
            print("Connection timed out")
            result_flag = False
        else:
            result_flag = True

        return result_flag

    def execute_command(self, commands):
        """Execute a command on the remote host.Return a tuple containing
        an integer status and a two strings, the first containing stdout
        and the second containing stderr from the command."""
        global command
        self.ssh_output = None
        result_flag = True
        try:
            if self.connect():
                for command in commands:
                    print("Executing command --> {}".format(command))
                    stdin, stdout, stderr = self.client.exec_command(command, timeout=10)
                    self.ssh_output = stdout.read()
                    self.ssh_error = stderr.read()
                    if self.ssh_error:
                        print("Problem occurred while running command:" + command + " The error is " + self.ssh_error)
                        result_flag = False
                    else:
                        print("Command execution completed successfully", command)
                    self.client.close()
            else:
                print("Could not establish SSH connection")
                result_flag = False
        except socket.timeout as e:
            print("Command timed out.", command)
            self.client.close()
            result_flag = False
        except paramiko.SSHException:
            print("Failed to execute the command!", command)
            self.client.close()
            result_flag = False

        return result_flag