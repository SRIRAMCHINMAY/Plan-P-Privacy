import asyncio
import os
import json
import base64
from pathlib import Path
from typing import List
from crawl4ai import ProxyConfig

from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode, CrawlResult
from crawl4ai import RoundRobinProxyStrategy
from crawl4ai import JsonCssExtractionStrategy, LLMExtractionStrategy
from crawl4ai import LLMConfig
from crawl4ai import PruningContentFilter, BM25ContentFilter
from crawl4ai import DefaultMarkdownGenerator
from crawl4ai import BFSDeepCrawlStrategy, DomainFilter, FilterChain
from crawl4ai import BrowserConfig

async def parallel_crawl():
    urls=[
        "https://news.ycombinator.com/",
        "https://example.com/",
        "https://httpbin.org/html",
    ]
    async with AsyncWebCrawler() as crawler:
        results:list[CrawlResult]=await crawler.arun_many(
            urls=urls,
        )
        print(f"Crawled {len(results)} URL's in parallel:")
        for i, result in enumerate(results):
            print(
                f" {i+1}.{result.url} - {'Success' if result.success else 'Failed'}"
            )
async def main():
    await parallel_crawl()
if __name__=="__main__":
     asyncio.run(main())

