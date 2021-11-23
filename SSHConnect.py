import paramiko
# output_file = "paramiko.log"


class SSH_operation:
    def __init__(self):
        self.client = None
        self.cmd_output = None

    def ssh_con(self, hostn, usern, passwd):
        self.client = paramiko.SSHClient()
        self.client.load_system_host_keys()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(hostname=hostn, username=usern, password=passwd)

    def ssh_command(self, command):


            (stdin, stdout, stderr) = self.client.exec_command(command)
            self.cmd_output = stdout.readlines()
            print("Log:::::", command, self.cmd_output)
            # with open(output_file, "w+") as file:
            #     file.write(str(self.cmd_output))
            # return output_file


# ssh_obj = SSH_operation()
# ssh_obj.ssh_con("pwd")