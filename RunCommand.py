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
ssh_obj.ssh_command("pwd")