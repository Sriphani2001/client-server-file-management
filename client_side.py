import asyncio
import os
import time

from backend import display_list

async def tcp_echo_client():
    """a defined function is running in loop"""
    reader,writer = await asyncio.open_connection('127.0.0.1',8888)
    message=''
    while True:

        # displaying list of commands
        print("1.login\n2.Register\n3.create_folder")
        print("4.write_file\n5.read_file\n6.list\n7.change_folder\n8.logout")
        print("please enter your choice\n")
        # request to server
        choice = input()
        if choice == 'exit':
           break
        writer.write(choice.encode())
        # reply from client
        data = await reader.read(5000)
        msg = data.decode().strip()
        if choice == "6":
            display_list(msg)
            msg = "--------------------------"
        print(msg)
        if choice == 8:
            break
    writer.close()
asyncio.run(tcp_echo_client())
