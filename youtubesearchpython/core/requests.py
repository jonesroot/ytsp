import os

import httpx

from youtubesearchpython.core.constants import userAgent


class RequestCore:
    def __init__(self):
        self.url = None
        self.data = None
        self.timeout = 2
        # self.proxies = None

        """
        http_proxy = os.environ.get("HTTP_PROXY")
        https_proxy = os.environ.get("HTTPS_PROXY")

        if http_proxy or https_proxy:
            proxy_mounts = {}
            if http_proxy:
                proxy_mounts["http://"] = httpx.HTTPTransport(proxy=http_proxy)
            if https_proxy:
                proxy_mounts["https://"] = httpx.HTTPTransport(proxy=https_proxy)
            self.proxies = proxy_mounts
        """

    def syncPostRequest(self) -> httpx.Response:
        with httpx.Client() as client:
            return client.post(
                self.url,
                headers={"User-Agent": userAgent},
                json=self.data,
                timeout=self.timeout,
            )

    async def asyncPostRequest(self) -> httpx.Response:
        async with httpx.AsyncClient() as client:
            return await client.post(
                self.url,
                headers={"User-Agent": userAgent},
                json=self.data,
                timeout=self.timeout,
            )

    def syncGetRequest(self) -> httpx.Response:
        with httpx.Client() as client:
            return client.get(
                self.url,
                headers={"User-Agent": userAgent},
                timeout=self.timeout,
                cookies={"CONSENT": "YES+1"},
            )

    async def asyncGetRequest(self) -> httpx.Response:
        async with httpx.AsyncClient() as client:
            return await client.get(
                self.url,
                headers={"User-Agent": userAgent},
                timeout=self.timeout,
                cookies={"CONSENT": "YES+1"},
            )
