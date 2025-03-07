import os

import httpx

from youtubesearchpython.core.constants import userAgent


class RequestCore:
    def __init__(self):
        self.url = None
        self.data = None
        self.timeout = 2
        self.proxies = None

        http_proxy = os.environ.get("HTTP_PROXY")
        https_proxy = os.environ.get("HTTPS_PROXY")

        if http_proxy or https_proxy:
            self.proxies = {"http://": http_proxy, "https://": https_proxy}

    def syncPostRequest(self) -> httpx.Response:
        with httpx.Client(proxies=self.proxies) as client:
            return client.post(
                self.url,
                headers={"User-Agent": userAgent},
                json=self.data,
                timeout=self.timeout,
            )

    async def asyncPostRequest(self) -> httpx.Response:
        async with httpx.AsyncClient(proxies=self.proxies) as client:
            return await client.post(
                self.url,
                headers={"User-Agent": userAgent},
                json=self.data,
                timeout=self.timeout,
            )

    def syncGetRequest(self) -> httpx.Response:
        with httpx.Client(proxies=self.proxies) as client:
            return client.get(
                self.url,
                headers={"User-Agent": userAgent},
                timeout=self.timeout,
                cookies={"CONSENT": "YES+1"},
            )

    async def asyncGetRequest(self) -> httpx.Response:
        async with httpx.AsyncClient(proxies=self.proxies) as client:
            return await client.get(
                self.url,
                headers={"User-Agent": userAgent},
                timeout=self.timeout,
                cookies={"CONSENT": "YES+1"},
            )
