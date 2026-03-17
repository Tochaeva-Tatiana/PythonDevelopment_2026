import asyncio
import cowsay
import shlex

users = {}
available_cows = set(cowsay.list_cows())

async def send(writer, text):
    writer.write((text + '\n').encode())
    await writer.drain()

async def handler(reader, writer):
    peer = writer.get_extra_info('peername')
    print(f'New client: {peer}')

    my_name = None
    my_queue = asyncio.Queue()

    read_task = asyncio.create_task(reader.readline())
    recv_task = asyncio.create_task(my_queue.get())

    try:
        while True:
            done, pending = await asyncio.wait(
                [read_task, recv_task],
                return_when=asyncio.FIRST_COMPLETED
            )

            if read_task in done:
                raw = read_task.result()

                if raw == b'':
                    break

                read_task = asyncio.create_task(reader.readline())

                line = raw.decode().strip()
                if not line:
                    continue

                print(f'{peer}: {line}')

                try:
                    args = shlex.split(line)
                except ValueError as exc:
                    await send(writer, f'ParseError: {exc}')
                    continue

                match args:
                    case ['who']:
                        if users:
                            await send(writer, ' '.join(sorted(users.keys())))
                        else:
                            await send(writer, 'No one is online')

                    case ['cows']:
                        free = sorted(available_cows - set(users.keys()))
                        if free:
                            await send(writer, ' '.join(free))
                        else:
                            await send(writer, 'No free cows')


                    case ['quit']:
                        await send(writer, 'Bye')
                        break

                    case _:
                        await send(writer, 'Unknown command')

            if recv_task in done:
                msg = recv_task.result()
                recv_task = asyncio.create_task(my_queue.get())
                await send(writer, msg)

    finally:
        read_task.cancel()
        recv_task.cancel()

        if my_name is not None and my_name in users:
            del users[my_name]
            print(f'{my_name} logged out')

        writer.close()
        await writer.wait_closed()
        print(f'{peer} left')

async def main():
    server = await asyncio.start_server(handler, '0.0.0.0', 1337)
    print('Server started on 1337')
    async with server:
        await server.serve_forever()

asyncio.run(main(), debug=True)