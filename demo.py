#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/12/16 11:01 上午
# @Author: yanmiexingkong
# @email : yanmiexingkong@gmail.com
# @File  : demo.py


import asyncio
import logging
from datetime import datetime
from aiowebsocket.converses import AioWebSocket


async def startup(uri):
    async with AioWebSocket(uri) as aws:
        converse = aws.manipulator
        message = b'AioWebSocket - Async WebSocket Client'
        while True:
            await converse.send(message)
            print('{time}-Client send: {message}'.format(time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                                         message=message))
            mes = await converse.receive()
            print('{time}-Client receive: {rec}'.format(time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), rec=mes))


if __name__ == '__main__':
    remote = 'wa://echo.websocket.org'
    try:
        asyncio.get_event_loop().run_until_complete(startup(remote))
    except KeyboardInterrupt as exc:
        logging.info('Quit.')
