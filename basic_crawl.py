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

async def basic_crawl():
    async with AsyncWebCrawler(config=BrowserConfig(
        viewport_height=800,
        viewport_width=1200,
        headless=True,
        verbose=True,

    )) as crawler:
        results: List[CrawlResult]= await crawler.arun(
            url="https://news.ycombinator.com/"
        )
        for i, result in enumerate(results):
            print(f"Result{i+1}:")
            print(f"Success:{result.success}")
            if result.success:
                print(f"Markdown len: {len(result.markdown.raw_markdown)} chars")
                print(f"First 100 chars: {result.markdown.raw_markdown[:100]}...")
            else:
                print("Failed")
async def main():
    await basic_crawl()
if __name__=="__main__":
    asyncio.run(main())