from SSHConnect import SSH_operation

# output_file = "paramiko.log"
# class Send_Command:
#
#     def cmd(self, command):
#         self.cmd_output = None
#         (stdin, stdout, stderr) = self.client.exec_command(command)
#         self.cmd_output = stdout.read()
#         print("Log:::::", command, self.cmd_output)
#         with open(output_file, "w+") as file:
#             file.write(str(cmd_output))
#         return output_file
ssh_obj = SSH_operation()
ssh_obj.ssh_con("10.1.3.75", "ezgi", "0000")
ip = "10.1.3.60"
hostname = "onur"
gw = "1.1.1.1"
sn = "/24"
# stuff = "sed -i '$a " + ip + "\n" + hostname + "\n" + gw + "\n" + sn + "' /home/ezgi/Desktop/sedsil.txt"
stuf = "sed -i '$d' /home/ezgi/Desktop/sedsil.txt"
ssh_obj.ssh_command(stuf)
ssh_obj.ssh_command("sed -i '$a Trailor' /home/ezgi/Desktop/sedsil.txt")

