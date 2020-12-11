import asyncio


def done_future(result):
    print(result)


async def command(cmd, encoding):
    proc = await asyncio.create_subprocess_shell(
        cmd=cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)
    stdout, stderr = await proc.communicate()
    print(f'[{cmd} exited with {proc.returncode}]\n')
    if stdout:
        print(f'[stdout]\n {stdout.decode(encoding=encoding)}')
    if stderr:
        print(f'[stderr]\n {stderr.decode(encoding=encoding)}')


if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    future = asyncio.ensure_future(command('ping www.sina.com', 'gbk'))
    future.add_done_callback(done_future())
