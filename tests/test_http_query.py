import asyncio
import json
import unittest
from typing import Dict

from fxsdk.client.http import HttpRpcClient, AsyncHttpRpcClient
from fxsdk.client.websockets import WebsocketRpcClient
from fxsdk.msg import event

rpc_url = "http://127.0.0.1:26657"
rpc_client = HttpRpcClient(rpc_url)


class TestHttpRpcClient(unittest.TestCase):

    def test_get_block_result(self):
        block_res = rpc_client.get_block_results(1)
        print(block_res)
        assert block_res

    def test_get_block(self):
        block = rpc_client.get_block()
        print(json.dumps(block, indent=2))
        assert block

    def test_avg_block_time_interval(self):
        res = rpc_client.avg_block_time_interval()
        print(res)
        assert res


class TestWebsocketRpcClient(unittest.IsolatedAsyncioTestCase):

    @staticmethod
    async def callback(msg: Dict):
        print("msg", json.dumps(msg))

    async def test_get_block_result(self):
        loop = asyncio.get_event_loop()
        ws_client = await WebsocketRpcClient.create(endpoint_url=rpc_url, loop=loop, callback=self.callback)
        await ws_client.get_status()
        await ws_client.subscribe(event.EVENT_NEW_BLOCK)
        await asyncio.sleep(5)
        ws_client.close()


class TestAsyncHttpRpcClient(unittest.IsolatedAsyncioTestCase):
    async def test_get_block_result(self):
        rcp_client = await AsyncHttpRpcClient.create(rpc_url)
        block_results = await rcp_client.get_block_results(1)
        print(block_results)


if __name__ == '__main__':
    unittest.main()
