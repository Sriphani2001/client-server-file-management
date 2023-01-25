import asyncio
import signal



from backend import *


signal.signal(signal.SIGINT,signal.SIG_DFL)

async def handle_echo(reader,writer):
    """
        server function that handles the client"
    """
    addr = writer.get_extra_info('peername')
    message = f"{addr} is connected!!!!"
    users_loggedin = []
    print(message)
    while True:
        # request from client
        msg = await reader.read(5000)
        choice = msg.decode().strip()
        line_split = choice.split(" ")
        choice = line_split[0]

        # working out user choice
        if choice == "1":
            msg = login(line_split[1],line_split[2])
            if msg == "logged in":
                obj = User(line_split[1])
                username = line_split[1]

        elif choice == "2":
            msg = register(line_split[1],line_split[2])
            if msg == "user created":
                obj = User(line_split[1])

        elif choice == "3":
            msg = obj.create_directory(line_split[1])

        elif choice == "4":
            msg = obj.write_to_file(line_split[1],line_split[2:])

        elif choice == "5":
            msg = obj.read_from_file(line_split[1])

        elif choice == "6":
            msg = obj.location
        elif choice == "7":
            msg = obj.change_directory(line_split[1])
        elif choice == "8":
            msg =logout(username)
        else:
            msg = "wrong choice reconnect to the server"

        # replying to client
        writer.write(msg.encode())
        await writer.drain()


async def main():
    server = await asyncio.start_server(handle_echo,'127.0.0.1',8888)
    addr = server.sockets[0].getsockname()
    print(f"serving on {addr}")
    async with server:
        await server.serve_forever()

asyncio.run(main())