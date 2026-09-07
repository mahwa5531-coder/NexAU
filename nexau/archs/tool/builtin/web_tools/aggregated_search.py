# Copyright (c) Nex-AGI. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""AggregatedWebSearch —  Web 。

 Nexau  WebSearch(`nexau.archs.tool.builtin.web_tools` 
`google_web_search` + `web_tool.SerperSearch`)，：

- gemini-cli (`content` / `returnDisplay` / `sources` / `error`)
- retrystrategy(default 3 ，`2 ** attempt` )
- error(errorstring，package error dict，exception)

：

1. ** Serper**， Serper / Seed / Baidu / XiaoBei ；
2. ****(、、、、…)，
   defaultvalue， WebSearch 。

# ：Provider vs Engine

，：

- **Provider()** ——  API：`Serper` / `Seed` / `Baidu` / `XiaoBei`。
- **Engine()** —— search results：`google` / `bing` / `baidu`。
   Provider( `XiaoBei`)； Provider 
  (Serper=Google、Seed=package、Baidu=)。

# 

|  |  | default |  |
|------|------|------|------|
| `SEARCH_PROVIDER` |  | `Serper` | ：`Serper` / `Seed` / `Baidu` / `XiaoBei`， |
| `SEARCH_API_KEY` |  | — |  |
| `SEARCH_ENGINE` |  | (default) | ， `google`、`google\\|baidu`； |
| `SEARCH_BASE_URL` |  |  | ( / ) |
| `SEARCH_TIMEOUT` |  | `30` | timeout |
| `SEARCH_MAX_RETRIES` |  | `3` | ****()， 1 |

**，**， `SEARCH_API_KEY`，
。 `SEARCH_PROVIDER` + `SEARCH_API_KEY`。

`SEARCH_ENGINE` value，`google`、`google|bing`、`google,bing`、
`["google","bing"]` ；**defaultvalue**， `search_engine` 。

`SEARCH_PROVIDER` value，
``/``/`Orchestrator`→XiaoBei、`package`→Seed /。

# 

| Provider |  |  |
|------|------|------|
| `Serper` | `https://google.serper.dev/{search_type}` | `X-API-KEY`  |
| `Seed` | package Custom  `https://open.feedcoopapi.com/search_api/web_search` | `Authorization: Bearer` |
| `Baidu` |  AI  `https://qianfan.baidubce.com/v2/ai_search/web_search` | `Authorization: Bearer` |
| `XiaoBei` |  `https://search.xiaobei.top/tools/web_research`( `http://search.iqjzf.com`) | `X-API-Key`  |

# 

、value、——，
****：
- **Serper** ——  <https://serper.dev>；
   <https://serper.dev/playground>；Key  <https://serper.dev/api-keys>
- **Seed（package）** —— Custom  <https://docs.volcengine.com/docs/87772/2272953>；
  Global  <https://docs.volcengine.com/docs/87772/2548026>； <https://console.volcengine.com/>
- **Baidu（ AI ）** —— 「」API <https://cloud.baidu.com/doc/qianfan-api/s/Wmbq4z7e5>；
  API Key  <https://cloud.baidu.com/doc/BAIDU_AI_SEARCH/s/5mkmgi38d>；
   <https://console.bce.baidu.com/ai-search/home>
- **XiaoBei（）** ——  <https://search.xiaobei.top/docs>；
  OpenAPI <https://search.xiaobei.top/openapi.json>

Google (`site:` / `-site:` / `tbs` )
<https://support.google.com/websearch/answer/2466433>。

⚠️ package SPA， Quill delta JSON  HTML ，
——****。

# 

，****(，)：

|  | Serper | Seed | Baidu | XiaoBei |
|------|:------:|:----:|:-----:|:-------:|
| `num_results` | ✅ `num` | ✅ `Count` | ✅ `top_k` | ⚠️ ， |
| `search_type` | ✅  | ⚠️  web/image | ⚠️  | ⚠️  |
| `time_range`  | ✅ `tbs=qdr:*` | ✅  | ✅ `search_recency_filter` | ✅ `day/week/month/year` |
| `time_range`  | ✅ `tbs=cdr:*` | ✅  | ✅ `search_filter.range.page_time` | ❌ |
| `sites` | ✅  | ✅ `Filter.Sites` | ✅ `match.site` | ✅ + |
| `block_hosts` | ✅  | ✅ `Filter.BlockHosts` | ⚠️ ， | ✅ + |
| `authority_only` | ❌ | ✅ `AuthInfoLevel` | ❌ | ❌ |
| `industry` | ❌ | ✅ `Industry` | ❌ | ❌ |
| `query_rewrite` | ✅ `autocorrect` | ✅ `QueryRewrite` | ❌ | ❌ |
| `need_content` | ❌ | ✅ `NeedContent` | ❌ | ❌ |
| `full_content` | ❌ | ✅ `Content` | ⚠️ no-op( `snippet`  `content` ) | ✅ `scrape_top_n`  |
| `content_format` | ❌ | ✅ `ContentFormats` | ❌ | ❌ ( markdown) |
| `country` / `location` / `page` | ✅ `gl` / `location` / `page` | ❌ | ❌ | ❌ |
| `language` | ✅ `hl` | ❌ | ❌ | ✅ (BCP-47) |
| `search_engine` | ❌ | ❌ | ❌ | ✅ `engines`  |
| `render_js` | ❌ | ❌ | ❌ | ✅ `fast_mode`  |
| `max_content_chars` | ✅  | ✅  | ✅  | ✅ + |

# （****）

。：XiaoBei  OpenAPI schema，Seed package Custom 
，Serper 。****，：

|  |  |  |
|------|-----------|------|
| Seed | `NeedSummary` |  `web_summary` type， 2026-06-23  |
| Seed | `ImageWidth/Height{Max,Min}`、`ImageShapes` |  `search_type=images` ，； |
| Baidu | `safe_search`、`config_id`、`search_filter.geo/image` | ；`geo.city`  `location` ， |

****、：
`Seed.Filter.NeedUrl`( true，)、
`XiaoBei.wait_for_result` / `timeout_s`(/timeout)、
`XiaoBei.scrape_top_n`( `full_content` )。

Serper  9  100% 。

# 

**，tool callsuccess**——。
"" `warning` ( Serper  `search_engine`、
 XiaoBei )，""。

 0 ，**success `sources: []`**
(content  "No results found.")， error——""，
retry。

# 

success::

    {
      "content": 'Web search results for "LLM " (provider: XiaoBei):\\n\\n[1]  (https://…)\\n    ',
      "returnDisplay": 'Search results for "LLM " via XiaoBei returned (5 results).',
      "sources": [{"title": …, "link": …, "snippet": …,
                   "provider": "XiaoBei", "engine": "baidu"}, …],
      "provider": "XiaoBei"
    }

failure::

    {"content": "Error: …", "returnDisplay": "Error performing web search.", "error": {"message": "…", "type": "WEB_SEARCH_FAILED"}}
"""

from __future__ import annotations

import logging
import os
import re
import time
from abc import ABC, abstractmethod
from dataclasses import asdict, dataclass
from datetime import UTC, datetime
from typing import Any, cast
from urllib.parse import urlsplit

import httpx

logger = logging.getLogger(__name__)


def _host_of(url: str) -> str:
    """ URL  host(、)，。"""
    try:
        return (urlsplit(url).netloc or "").lower().split(":")[0]
    except ValueError:
        return ""


def _host_matches(host: str, pattern: str) -> bool:
    """host ：。"""
    return bool(host) and (host == pattern or host.endswith("." + pattern))


def _apply_site_operators(query: str, sites: list[str], block_hosts: list[str]) -> str:
    """/ Google 。

    (Serper、)。
    ： `arxiv.org`  1/28 ，
     `site:arxiv.org`  20/20。
    """
    parts = [query]
    if sites:
        parts.append("(" + " OR ".join(f"site:{s}" for s in sites) + ")")
    parts.extend(f"-site:{h}" for h in block_hosts)
    return " ".join(parts)


# ---------------------------------------------------------------- defaultvalue
# defaultvalue tools/AggregatedWebSearch.tool.yaml  `default` ，
# ，「」「defaultvalue」。

DEFAULT_NUM_RESULTS = 10
DEFAULT_SEARCH_TYPE = "search"
DEFAULT_TIME_RANGE = ""  #  = 
DEFAULT_SITES = ""  #  = 
DEFAULT_BLOCK_HOSTS = ""  #  = 
DEFAULT_AUTHORITY_ONLY = False
DEFAULT_INDUSTRY = "all"  # 'all' = 
DEFAULT_QUERY_REWRITE = False
DEFAULT_NEED_CONTENT = False
DEFAULT_FULL_CONTENT = False
DEFAULT_CONTENT_FORMAT = "text"
DEFAULT_MAX_CONTENT_CHARS = 1000
DEFAULT_COUNTRY = ""  #  = default
DEFAULT_LANGUAGE = ""  #  = default
DEFAULT_LOCATION = ""  #  = 
DEFAULT_PAGE = 1
DEFAULT_SEARCH_ENGINE = ""  #  =  SEARCH_ENGINE ，default
DEFAULT_RENDER_JS = False  # default HTTP ，

# defaultvalue()
DEFAULT_TIMEOUT = 30.0
DEFAULT_MAX_RETRIES = 3

# ---------------------------------------------------------------- 
# **defaultvalue**，：
#
# SEARCH_ + ； `search_` 
#     content_format → SEARCH_CONTENT_FORMAT
#     num_results    → SEARCH_NUM_RESULTS
# search_engine  → SEARCH_ENGINE      ( SEARCH_SEARCH_ENGINE)
# search_type    → SEARCH_TYPE        ()
#
# ：** >  > defaultvalue**。
#
# """defaultvalue"：defaultvalue
# ( content_format="text")，"valuedefault"，
# default。function None ，None ""。
PARAM_DEFAULTS: dict[str, Any] = {
    "num_results": DEFAULT_NUM_RESULTS,
    "search_type": DEFAULT_SEARCH_TYPE,
    "time_range": DEFAULT_TIME_RANGE,
    "sites": DEFAULT_SITES,
    "block_hosts": DEFAULT_BLOCK_HOSTS,
    "authority_only": DEFAULT_AUTHORITY_ONLY,
    "industry": DEFAULT_INDUSTRY,
    "query_rewrite": DEFAULT_QUERY_REWRITE,
    "need_content": DEFAULT_NEED_CONTENT,
    "full_content": DEFAULT_FULL_CONTENT,
    "content_format": DEFAULT_CONTENT_FORMAT,
    "max_content_chars": DEFAULT_MAX_CONTENT_CHARS,
    "country": DEFAULT_COUNTRY,
    "language": DEFAULT_LANGUAGE,
    "location": DEFAULT_LOCATION,
    "page": DEFAULT_PAGE,
    "search_engine": DEFAULT_SEARCH_ENGINE,
    "render_js": DEFAULT_RENDER_JS,
}

# ，()
PROVIDER_ENV_KEYS = frozenset(
    {
        "SEARCH_PROVIDER",
        "SEARCH_API_KEY",
        "SEARCH_BASE_URL",
        "SEARCH_TIMEOUT",
        "SEARCH_MAX_RETRIES",
    }
)

# value( False)
_TRUE_LITERALS = frozenset({"1", "true", "yes", "on", "y", "t"})
_FALSE_LITERALS = frozenset({"0", "false", "no", "off", "n", "f"})


def param_env_name(param: str) -> str:
    """ -> 。

    `SEARCH_` + ； `search_` ，
     `SEARCH_SEARCH_ENGINE` 。
    """
    stem = param[len("search_") :] if param.startswith("search_") else param
    return f"SEARCH_{stem.upper()}"


def _coerce_env_value(raw: str, default: Any, env_name: str) -> Any:
    """defaultvaluetypestring。

    default warning——
    。
    """
    text = raw.strip()
    if isinstance(default, bool):
        low = text.lower()
        if low in _TRUE_LITERALS:
            return True
        if low in _FALSE_LITERALS:
            return False
        logger.warning(
            " %s=%r value( true/false)，default %r",
            env_name,
            raw,
            default,
        )
        return default
    if isinstance(default, int):
        try:
            return int(text)
        except ValueError:
            logger.warning(" %s=%r integer，default %r", env_name, raw, default)
            return default
    return text


def resolve_param(param: str, value: Any) -> Any:
    """「 >  > default」value。"""
    if value is not None:
        return value
    default = PARAM_DEFAULTS[param]
    env_name = param_env_name(param)
    raw = os.getenv(env_name)
    if raw is None or not raw.strip():
        return default
    return _coerce_env_value(raw, default, env_name)


# search_type=news  time_range ，default
NEWS_FALLBACK_TIME_RANGE = "OneWeek"

# (package)； `YYYY-MM-DD..YYYY-MM-DD` 
TIME_RANGE_PRESETS = ("OneDay", "OneWeek", "OneMonth", "OneYear")


class SearchProviderError(Exception):
    """**retry**error： key、、///。

    classretry，configuration，
    class， `WEB_SEARCH_CONFIG_ERROR`。
    """


class RetryableUpstreamError(Exception):
    """**retry**：error、QPS 。

    classretry；retryerrorstring。
    """


@dataclass
class SearchOptions:
    """。

    defaultvalue `DEFAULT_*` 、tool YAML  `default` 。
    ，module docstring 。

    ，
    **value /  / ，**(module docstring
    「」)。
    """

    # 。/type(package web≤50、image≤5；≤30)
    # → Serper `num` / package `Count` /  `top_k` /  `max_results`
    num_results: int = DEFAULT_NUM_RESULTS
    # type：search  / news  / images  / places  / videos / scholar
    # → Serper ( https://serper.dev/playground)；package web / image  SearchType
    search_type: str = DEFAULT_SEARCH_TYPE
    # ：OneDay / OneWeek / OneMonth / OneYear / YYYY-MM-DD..YYYY-MM-DD
    # → Serper  Google `tbs`(qdr:*  cdr:*，
    #   https://support.google.com/websearch/answer/2466433)
    # → package `TimeRange`(，)
    # →  `search_recency_filter` /  `time_range`(day/week/month/year)
    time_range: str = DEFAULT_TIME_RANGE
    # ，'|' ， 20 ， "arxiv.org|nature.com"
    # → package `Filter.Sites`()；Serper /  `site:` 
    sites: str = DEFAULT_SITES
    # ，'|' ， 5 
    # → package `Filter.BlockHosts`()；Serper /  `-site:` 
    block_hosts: str = DEFAULT_BLOCK_HOSTS
    # ""(//)，
    # → package `Filter.AuthInfoLevel=1`。package「」
    authority_only: bool = DEFAULT_AUTHORITY_ONLY
    # ：finance  / game  / gov 
    # → package `Filter.Industry`(package Custom )
    industry: str = DEFAULT_INDUSTRY
    # (，)
    # → Serper `autocorrect`(Google ) / package `QueryControl.QueryRewrite`
    query_rewrite: bool = DEFAULT_QUERY_REWRITE
    # ""()
    # → package `Filter.NeedContent`
    need_content: bool = DEFAULT_NEED_CONTENT
    # (，)
    # → package `WebItem.Content`  `Summary`； `scrape_top_n` 
    full_content: bool = DEFAULT_FULL_CONTENT
    # ：text / markdown， full_content=True 
    # → package `ContentFormats`
    content_format: str = DEFAULT_CONTENT_FORMAT
    # /，(，)
    max_content_chars: int = DEFAULT_MAX_CONTENT_CHARS
    # (ISO 3166-1 ， cn / us)
    # → Serper `gl`，value https://serper.dev/playground 
    country: str = DEFAULT_COUNTRY
    # (BCP-47， zh-cn / en)
    # → Serper `hl` /  `language`
    language: str = DEFAULT_LANGUAGE
    # ( "Tokyo, Japan")，/
    # → Serper `location`；value https://serper.dev/playground 
    location: str = DEFAULT_LOCATION
    # ， 1 ；
    # → Serper `page`
    page: int = DEFAULT_PAGE
    # ，'|' ， "google|baidu"； SEARCH_ENGINE 
    # →  `options.engines`( https://search.xiaobei.top/docs)
    search_engine: str = DEFAULT_SEARCH_ENGINE
    # ( JS ，)
    # →  `fast_mode`(：render_js=True  fast_mode=False)
    render_js: bool = DEFAULT_RENDER_JS

    def __post_init__(self) -> None:
        # search_type=news ""packagetype，
        # time_range 
        if self.search_type == "news" and not self.time_range:
            self.time_range = NEWS_FALLBACK_TIME_RANGE
        # ， 0 / 
        self.num_results = max(1, int(self.num_results))
        self.max_content_chars = max(100, int(self.max_content_chars))
        self.page = max(1, int(self.page))

    def parse_custom_range(self) -> tuple[str, str] | None:
        """ `YYYY-MM-DD..YYYY-MM-DD`  (, )； None。"""
        if ".." not in self.time_range:
            return None
        start, _, end = self.time_range.partition("..")
        start, end = start.strip(), end.strip()
        return (start, end) if start and end else None

    def as_dict(self) -> dict[str, Any]:
        """value。

        「」—— `getattr` property
        （ CLAUDE.md「Type Safety Guidelines」）， dataclass 。
        """
        return asdict(self)

    def split_sites(self) -> list[str]:
        """list()。"""
        return [s.strip() for s in self.sites.split("|") if s.strip()]

    def split_block_hosts(self) -> list[str]:
        """list()。"""
        return [s.strip() for s in self.block_hosts.split("|") if s.strip()]

    def split_engines(self) -> list[str]:
        """list(、)。

        ，`google`、`google|bing`、`google,bing`、`["google","bing"]`
        —— LLM 。
        """
        raw = self.search_engine.strip().strip("[]")
        return [part.strip().strip("\"'").lower() for part in re.split(r"[|,\s]+", raw) if part.strip().strip("\"'")]


class SearchProviderBase(ABC):
    """adapterclass。

    class `_do_search`( + )，
    retry、、exception、class `search` 。
    """

    # ， `engine` 
    name: str = "base"
    # configuration SEARCH_BASE_URL 
    default_base_url: str = ""

    def __init__(
        self,
        api_key: str,
        base_url: str | None = None,
        timeout: float = DEFAULT_TIMEOUT,
        max_retries: int = DEFAULT_MAX_RETRIES,
    ) -> None:
        if not api_key:
            raise SearchProviderError(
                f"{self.name} API key is required.  SEARCH_API_KEY( {_LEGACY_API_KEY_ENV})。"
            )
        self.api_key = api_key
        self.base_url = (base_url or self.default_base_url).rstrip("/")
        self.timeout = timeout
        # ****( web_tool.SerperSearch ，error
        # "after N attempts")。 >=1：`range(0)` ，
        # `_do_search` ， 100% failure。
        self.max_retries = max(1, max_retries)

    # ---------------------------------------------------------------- class

    @abstractmethod
    def _do_search(
        self,
        client: httpx.Client,
        query: str,
        options: SearchOptions,
    ) -> list[dict[str, Any]]:
        """，****list。

         `title` / `link` / `snippet`，
         `date` / `source` / `position` / `authority` 。
        """

    # ---------------------------------------------------------------- 

    # ""()
    supports_engine_choice: bool = False
    # ""
    supports_render_js: bool = False
    # **、**。defaultvalue——
    # ""，class
    IGNORED_PARAMS: frozenset[str] = frozenset()

    def search(self, query: str, options: SearchOptions) -> list[dict[str, Any]] | str:
        """retry。

        successlist；failureerrorstring(exception)——
         `SerperSearch.search` ，success/failure。
        """
        # ，——
        # " SEARCH_ENGINE=baidu"
        if options.split_engines() and not self.supports_engine_choice:
            logger.warning(
                "%s ，search_engine=%r ",
                self.name,
                options.search_engine,
            )
        supplied = options.as_dict()
        for param in sorted(self.IGNORED_PARAMS):
            value = supplied.get(param)
            if value != PARAM_DEFAULTS.get(param):
                logger.warning("%s  %s， %r ", self.name, param, value)
        if options.render_js and not self.supports_render_js:
            logger.warning("%s ，render_js=True ", self.name)
        elif options.render_js and not options.full_content:
            # ； full_content ，
            # render_js ——""
            logger.warning(
                "%s: render_js=True  full_content=False，，",
                self.name,
            )

        timeout = httpx.Timeout(
            connect=self.timeout,
            read=self.timeout,
            write=self.timeout,
            pool=self.timeout,
        )

        for attempt in range(self.max_retries):
            try:
                with httpx.Client(timeout=timeout) as client:
                    results = self._do_search(client, query, options)
                # max_content_chars 
                for item in results:
                    item["provider"] = self.name
                    snippet = item.get("snippet")
                    if isinstance(snippet, str) and len(snippet) > options.max_content_chars:
                        item["snippet"] = snippet[: options.max_content_chars] + "..."
                return results[: options.num_results]

            except SearchProviderError:
                # configuration / classerrorretry，
                raise

            except RetryableUpstreamError as e:
                # ，retry
                if attempt == self.max_retries - 1:
                    return f"Upstream error after {self.max_retries} attempts: {str(e)}"
                time.sleep(2**attempt)

            except httpx.ConnectTimeout as e:
                if attempt == self.max_retries - 1:
                    return f"Connection timeout after {self.max_retries} attempts: {str(e)}"
                time.sleep(2**attempt)  # 

            except httpx.TimeoutException as e:
                if attempt == self.max_retries - 1:
                    return f"Request timeout after {self.max_retries} attempts: {str(e)}"
                time.sleep(2**attempt)

            except httpx.HTTPStatusError as e:
                # 4xx  429 error，retry
                status = e.response.status_code
                detail = e.response.text[:300]
                if 400 <= status < 500 and status != 429:
                    return f"HTTP error {status}: {detail}"
                if attempt == self.max_retries - 1:
                    return f"HTTP error {status}: {detail}"
                time.sleep(2**attempt)

            except Exception as e:  # noqa: BLE001 — errorstring，
                if attempt == self.max_retries - 1:
                    return f"Unexpected error: {type(e).__name__}: {str(e)}"
                time.sleep(2**attempt)

        return f"Failed to complete search after {self.max_retries} attempts"


class SerperProvider(SearchProviderBase):
    """Serper(google.serper.dev)—— Nexau  WebSearch 。

    Serper /class， `sites` / `block_hosts`
     Google (`site:` / `-site:`)，`time_range`  `tbs`。

    :
        - : https://serper.dev
        - (): https://serper.dev/playground
        - API Key : https://serper.dev/api-keys
        - Google `tbs` : https://support.google.com/websearch/answer/2466433
    """

    name = "Serper"
    default_base_url = "https://google.serper.dev"
    IGNORED_PARAMS = frozenset({"authority_only", "industry", "need_content", "full_content", "content_format"})

    # search_type -> (URL , )
    # ， scholar  `organic`，
    ENDPOINT_FOR_TYPE = {
        "search": ("search", "organic"),
        "news": ("news", "news"),
        "images": ("images", "images"),
        "places": ("places", "places"),
        "videos": ("videos", "videos"),
        "scholar": ("scholar", "organic"),
    }
    # time_range  -> Google `tbs` 
    TBS_FOR_TIME_RANGE = {
        "OneDay": "qdr:d",
        "OneWeek": "qdr:w",
        "OneMonth": "qdr:m",
        "OneYear": "qdr:y",
    }

    @staticmethod
    def _to_google_date(iso_date: str) -> str:
        """`YYYY-MM-DD` -> Google `tbs`  `M/D/YYYY`()。"""
        y, m, d = iso_date.split("-")
        return f"{int(m)}/{int(d)}/{int(y)}"

    def _build_tbs(self, options: SearchOptions) -> str | None:
        """ time_range  Google `tbs` 。

         `qdr:*`；`YYYY-MM-DD..YYYY-MM-DD` 
        `cdr:1,cd_min:…,cd_max:…`()。
        """
        preset = self.TBS_FOR_TIME_RANGE.get(options.time_range)
        if preset:
            return preset
        custom = options.parse_custom_range()
        if not custom:
            return None
        try:
            start, end = (self._to_google_date(d) for d in custom)
        except ValueError:
            # ，
            logger.warning(" time_range=%r，", options.time_range)
            return None
        return f"cdr:1,cd_min:{start},cd_max:{end}"

    def _do_search(
        self,
        client: httpx.Client,
        query: str,
        options: SearchOptions,
    ) -> list[dict[str, Any]]:
        # 1. 
        endpoint_conf = self.ENDPOINT_FOR_TYPE.get(options.search_type)
        if endpoint_conf is None:
            raise SearchProviderError(
                f"Invalid search type: {options.search_type}. Serper search type should be one of {list(self.ENDPOINT_FOR_TYPE)}"
            )
        path, result_key = endpoint_conf

        # 2. Serper ， Google 
        payload: dict[str, Any] = {
            "q": _apply_site_operators(query, options.split_sites(), options.split_block_hosts()),
            "num": options.num_results,
            # query_rewrite  Serper  Google 
            "autocorrect": options.query_rewrite,
        }
        # 3. ，value，default
        tbs = self._build_tbs(options)
        if tbs:
            payload["tbs"] = tbs
        if options.country:
            payload["gl"] = options.country
        if options.language:
            payload["hl"] = options.language
        if options.location:
            payload["location"] = options.location
        if options.page > 1:
            payload["page"] = options.page

        # 4. 
        response = client.post(
            f"{self.base_url}/{path}",
            headers={"X-API-KEY": self.api_key, "Content-Type": "application/json"},
            json=payload,
        )
        response.raise_for_status()
        parsed: dict[str, Any] = response.json()
        raw: list[dict[str, Any]] = parsed.get(result_key) or []

        # 5. places ( link/snippet，)，
        if options.search_type == "places":
            return [self._normalize_place(item) for item in raw[: options.num_results]]

        # 6. ， base64 ()
        results: list[dict[str, Any]] = []
        for item in raw[: options.num_results]:
            if str(item.get("imageUrl", "")).startswith("data:"):
                item.pop("imageUrl", None)
            results.append(
                {
                    "title": item.get("title", "Untitled"),
                    "link": item.get("link") or item.get("url", ""),
                    "snippet": item.get("snippet") or item.get("description", ""),
                    "date": _clean_date(item.get("date")),
                    "source": item.get("source"),
                    "position": item.get("position"),
                }
            )
        return results

    @staticmethod
    def _normalize_place(item: dict[str, Any]) -> dict[str, Any]:
        """。

        Serper  places ** link **， `cid`(Google Maps  ID)。
        ， cid ，
         / class /  snippet——。
        """
        cid = item.get("cid")
        link = item.get("website") or (f"https://www.google.com/maps?cid={cid}" if cid else "")

        bits = [item.get("address"), item.get("category")]
        rating = item.get("rating")
        if rating:
            count = item.get("ratingCount")
            bits.append(f" {rating}" + (f"({count} )" if count else ""))
        if item.get("phoneNumber"):
            bits.append(str(item["phoneNumber"]))

        return {
            "title": item.get("title", "Untitled"),
            "link": link,
            "snippet": " · ".join(b for b in bits if b),
            "date": None,
            "source": item.get("category"),
            "position": item.get("position"),
        }


class SeedProvider(SearchProviderBase):
    """Seed(package Custom ，「 / 」)。

    : `POST https://open.feedcoopapi.com/search_api/web_search`
    : `Authorization: Bearer <API_KEY>`

    (⚠️ SPA ， Quill delta JSON，):
        - Custom  API (class，/error):
          https://docs.volcengine.com/docs/87772/2272953
        - Global  API : https://docs.volcengine.com/docs/87772/2548026
        - ( API Key / ): https://console.volcengine.com/

    (，): default 5 QPS ；
     500 ， Global 、。

    (，)：

    1. **failure HTTP 200**，error `ResponseMetadata.Error`
       (`CodeN` / `Code` / `Message`)。 HTTP failuresuccess。
    2. **`Snippet` **。 `Snippet`  200 ，
       "，search resultslist，
       "； `Summary`(500~1000 ，"")。
        `Summary`； `full_content`  `Content`。
    """

    name = "Seed"
    default_base_url = "https://open.feedcoopapi.com"
    IGNORED_PARAMS = frozenset({"country", "language", "location", "page"})

    # Query (：1~100 ，)
    MAX_QUERY_CHARS = 100
    # Count (：web  50 ；image  5 )
    MAX_COUNT_WEB = 50
    MAX_COUNT_IMAGE = 5
    # (：Sites  20 ，BlockHosts  5 )
    MAX_SITES = 20
    MAX_BLOCK_HOSTS = 5

    # search_type -> package SearchType。
    # package web / image type， + TimeRange 。
    SEARCH_TYPE_MAP = {
        "search": "web",
        "news": "web",  # ， TimeRange 
        "places": "web",
        "images": "image",
        "videos": "web",
        "scholar": "web",
    }

    # "retry"error：
    # 10500 InnerError(defaulterror)、700429  QPS 。
    # (10400  / 10402 type / 10403  / 10406  /
    # 10409·10410·10412 )，retry。
    RETRYABLE_ERROR_CODES = {"10500", "700429"}

    def _do_search(
        self,
        client: httpx.Client,
        query: str,
        options: SearchOptions,
    ) -> list[dict[str, Any]]:
        # 1. type，type Count 
        doubao_type = self.SEARCH_TYPE_MAP.get(options.search_type, "web")
        max_count = self.MAX_COUNT_IMAGE if doubao_type == "image" else self.MAX_COUNT_WEB
        count = max(1, min(options.num_results, max_count))

        # 2.  Filter：/， 10400
        filters: dict[str, Any] = {
            # True：，
            # ""()
            "NeedUrl": True,
            "NeedContent": options.need_content,
        }
        sites = options.split_sites()[: self.MAX_SITES]
        if sites:
            filters["Sites"] = "|".join(sites)
        block_hosts = options.split_block_hosts()[: self.MAX_BLOCK_HOSTS]
        if block_hosts:
            filters["BlockHosts"] = "|".join(block_hosts)
        if options.authority_only:
            filters["AuthInfoLevel"] = 1  # 1 = ""
        if options.industry:
            filters["Industry"] = options.industry

        # 3. ；Query ，
        payload: dict[str, Any] = {
            "Query": query[: self.MAX_QUERY_CHARS],
            "SearchType": doubao_type,
            "Count": count,
            "Filter": filters,
        }
        if options.time_range:
            payload["TimeRange"] = options.time_range
        if options.query_rewrite:
            payload["QueryControl"] = {"QueryRewrite": True}
        if options.full_content:
            payload["ContentFormats"] = options.content_format

        # 4. 
        response = client.post(
            f"{self.base_url}/search_api/web_search",
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            },
            json=payload,
        )
        response.raise_for_status()
        data: dict[str, Any] = response.json()

        # 5. key：error HTTP 200  ResponseMetadata.Error ，
        # HTTP failuresuccess
        metadata: dict[str, Any] = data.get("ResponseMetadata") or {}
        error: dict[str, Any] | None = metadata.get("Error")
        if error:
            code_n = error.get("CodeN")
            code = str(error.get("Code") or code_n or "unknown")
            detail = f"packageerror [{code}] {error.get('Message', '')}"
            # retry(error / )retry(··)
            if {code, str(code_n)} & self.RETRYABLE_ERROR_CODES:
                raise RetryableUpstreamError(detail)
            raise SearchProviderError(detail)

        result: dict[str, Any] = data.get("Result") or {}

        # 6.  ImageResults， WebResults
        if doubao_type == "image":
            return [
                {
                    "title": item.get("Title") or "Untitled",
                    "link": item.get("Url", ""),
                    "snippet": item.get("Category") or "",
                    "date": _clean_date(item.get("PublishTime")),
                    "source": item.get("SiteName"),
                }
                for item in (cast(list[dict[str, Any]], result.get("ImageResults") or []))[:count]
            ]

        # 7.  WebResults：
        # full_content=True  Content()， Summary()，
        # Snippet( 200 ，)
        results: list[dict[str, Any]] = []
        web_results: list[dict[str, Any]] = result.get("WebResults") or []
        for item in web_results[:count]:
            if options.full_content:
                snippet = item.get("Content") or item.get("Summary") or item.get("Snippet") or ""
            else:
                snippet = item.get("Summary") or item.get("Snippet") or ""
            results.append(
                {
                    "title": item.get("Title") or "Untitled",
                    "link": item.get("Url", ""),
                    "snippet": snippet,
                    "date": _clean_date(item.get("PublishTime")),
                    "source": item.get("SiteName"),
                    "position": item.get("SortId"),
                    "authority": item.get("AuthInfoDes"),
                }
            )
        return results


class BaiduProvider(SearchProviderBase):
    """Baidu( AI  / )——`POST /v2/ai_search/web_search`， references。

    :
        - 「」API (class， search_filter ):
          https://cloud.baidu.com/doc/qianfan-api/s/Wmbq4z7e5
        - API Key : https://cloud.baidu.com/doc/BAIDU_AI_SEARCH/s/5mkmgi38d
        - ( API Key): https://console.bce.baidu.com/ai-search/home

    ⚠️ ：**401 **—— `/v2/ai_search` 
    ， `/v2/ai_search/definitely_not_exist`  401。 base_url
    ， key success，" 404"。
    """

    name = "Baidu"
    default_base_url = "https://qianfan.baidubce.com"
    # full_content  no-op(snippet  content )，
    IGNORED_PARAMS = frozenset(
        {
            "authority_only",
            "industry",
            "query_rewrite",
            "need_content",
            "full_content",
            "content_format",
            "country",
            "language",
            "location",
            "page",
        }
    )

    # ：messages[].content  72 
    MAX_QUERY_CHARS = 72

    # time_range  -> `search_recency_filter`。
    # value week / month / semiyear / year，** day**——
    # OneDay ， `search_filter.range.page_time` 。
    RECENCY_FOR_TIME_RANGE = {
        "OneWeek": "week",
        "OneMonth": "month",
        "OneYear": "year",
    }

    def _build_search_filter(self, options: SearchOptions) -> dict[str, Any]:
        """ `search_filter`：/。

        ：
            search_filter.match.site        -> array[str]  
            search_filter.block_websites    -> array[str]  
            search_filter.range.page_time   -> {gte, lte}  
        """
        search_filter: dict[str, Any] = {}

        sites = options.split_sites()
        if sites:
            search_filter["match"] = {"site": sites}
        blocked = options.split_block_hosts()
        if blocked:
            # ：****(，)，
            # ，；
            search_filter["block_websites"] = blocked

        # page_time；OneDay  day ，
        # ""
        page_time: dict[str, str] = {}
        custom = options.parse_custom_range()
        if custom:
            page_time["gte"], page_time["lte"] = custom
        elif options.time_range == "OneDay":
            today = datetime.now(UTC).astimezone().strftime("%Y-%m-%d")
            page_time["gte"] = today
        if page_time:
            search_filter["range"] = {"page_time": page_time}

        return search_filter

    def _do_search(
        self,
        client: httpx.Client,
        query: str,
        options: SearchOptions,
    ) -> list[dict[str, Any]]:
        # 1. ；query ，
        # ，
        blocked = options.split_block_hosts()
        top_k = min(options.num_results * 2, 50) if blocked else options.num_results
        payload: dict[str, Any] = {
            "messages": [{"role": "user", "content": query[: self.MAX_QUERY_CHARS]}],
            "search_source": "baidu_search_v2",
            "resource_type_filter": [{"type": "web", "top_k": top_k}],
        }

        # 2. ： search_recency_filter，
        # OneDay  search_filter.range.page_time
        recency = self.RECENCY_FOR_TIME_RANGE.get(options.time_range)
        if recency:
            payload["search_recency_filter"] = recency

        # 3. 
        search_filter = self._build_search_filter(options)
        if search_filter:
            payload["search_filter"] = search_filter

        # 4. 
        response = client.post(
            f"{self.base_url}/v2/ai_search/web_search",
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            },
            json=payload,
        )
        response.raise_for_status()
        data: dict[str, Any] = response.json()

        # 5. error：failure code / message
        if data.get("code") and not data.get("references"):
            raise SearchProviderError(f" AI error [{data.get('code')}] {data.get('message', '')}")

        # 6.  references。
        # `snippet`  `content` ****()，
        # `full_content`  no-op；。
        lowered = [b.lower() for b in blocked]
        results: list[dict[str, Any]] = []
        references: list[dict[str, Any]] = data.get("references") or []
        for ref in references:
            if len(results) >= options.num_results:
                break
            # ( block_websites )
            if lowered and any(_host_matches(_host_of(ref.get("url") or ""), b) for b in lowered):
                continue
            if options.full_content:
                snippet = ref.get("content") or ref.get("snippet") or ""
            else:
                snippet = ref.get("snippet") or ref.get("content") or ""
            results.append(
                {
                    "title": ref.get("title") or "Untitled",
                    "link": ref.get("url", ""),
                    "snippet": snippet,
                    "date": _clean_date(ref.get("date")),
                    # `web_anchor` 、`website`  ""，
                    # ， source="" 
                    "source": _clean_source(ref.get("web_anchor"), ref.get("website")),
                }
            )
        return results


class XiaoBeiProvider(SearchProviderBase):
    """XiaoBei( Search Engine Orchestrator)—— + 。

    : `POST https://search.xiaobei.top/tools/web_research`( `http://search.iqjzf.com`)
    : `X-API-Key: <API_KEY>`

    :
        - ( /  /  / error): https://search.xiaobei.top/docs
        - OpenAPI schema: https://search.xiaobei.top/openapi.json
        - ( redis / searxng / firecrawl ): https://search.xiaobei.top/health

    ():  Key 300 req/min、 500 req/min；
     Key 300 req/min、 600 req/min。

    ： google / bing / baidu，，
     Firecrawl  N 。：

    1. **`max_results` ""**， 5  14 、 30  27 ，
        `num_results` 。
    2. ****： `timeout` / `empty_results` ， 502
       (`searxng timeout`)。"HTTP 200 + 0  +  engine_errors"****
       ""，retry，。
    3. **`status="failed"` "**failure"，failure**( `search_failed`)。
        `results` ，error。
    4.  15~25 ， `SEARCH_TIMEOUT`(default 30s)，
       。
    """

    name = "XiaoBei"
    default_base_url = "https://search.xiaobei.top"
    IGNORED_PARAMS = frozenset(
        {
            "authority_only",
            "industry",
            "query_rewrite",
            "need_content",
            "content_format",
            "country",
            "location",
            "page",
        }
    )
    supports_engine_choice = True
    supports_render_js = True

    # ：max_results 1~30、scrape_top_n 0~10、max_content_chars 100~50000
    MAX_RESULTS_CAP = 30
    MAX_SCRAPE_TOP_N = 10
    MAX_CONTENT_CHARS_CAP = 50000
    # 
    SUPPORTED_ENGINES = ("google", "bing", "baidu")

    # HTTP 。，** 180s  504**，
    # ——。
    # 15~40s，100s 。
    HTTP_TIMEOUT_CEILING = 100
    # timeout_s  HTTP timeout，
    BUDGET_MARGIN = 25
    # ()。，。
    # Firecrawl  2~30s ； 60s ，
    # ，tool call。
    SCRAPE_POLL_BUDGET = 60
    # 
    POLL_INTERVAL = 8

    # time_range  -> 
    TIME_RANGE_MAP = {
        "OneDay": "day",
        "OneWeek": "week",
        "OneMonth": "month",
        "OneYear": "year",
    }

    # / classerror，retry
    NON_RETRYABLE_STATUS = {401, 403, 422}
    # 、
    TERMINAL_STATUSES = {"complete", "partial", "failed", "search_failed"}

    def _headers(self) -> dict[str, str]:
        return {"X-API-Key": self.api_key, "Content-Type": "application/json"}

    @staticmethod
    def _parse_json(response: httpx.Response) -> dict[str, Any]:
        """/ JSON，error JSONDecodeError。"""
        try:
            return response.json()
        except ValueError as exc:
            raise RetryableUpstreamError(f" JSON (HTTP {response.status_code}): {response.text[:120]!r}") from exc

    def _check_status(self, response: httpx.Response) -> None:
        """ 401/403/422 retryconfigurationerror，class。"""
        if response.status_code in self.NON_RETRYABLE_STATUS:
            detail = response.text[:200]
            raise SearchProviderError(f" HTTP {response.status_code}: {detail}")
        response.raise_for_status()

    def _do_search(
        self,
        client: httpx.Client,
        query: str,
        options: SearchOptions,
    ) -> list[dict[str, Any]]:
        # 1. 。
        # -> ，；
        # -> ****：completed(~15~40s)，
        # 。 180s 。
        scrape_top_n = min(options.num_results, self.MAX_SCRAPE_TOP_N) if options.full_content else 0
        http_timeout = float(min(max(self.timeout, 60.0), self.HTTP_TIMEOUT_CEILING))
        upstream_timeout = max(5, min(600, int(http_timeout) - self.BUDGET_MARGIN))

        # 2. ， query  google/bing/baidu，
        # `site:` / `-site:` ( 1/28 → 20/20)，
        # host ——。
        sites = options.split_sites()
        block_hosts = options.split_block_hosts()
        effective_query = _apply_site_operators(query, sites, block_hosts)

        # ，
        want_filter = bool(sites or block_hosts)
        max_results = self.MAX_RESULTS_CAP if want_filter else options.num_results
        max_results = max(1, min(self.MAX_RESULTS_CAP, max_results))

        upstream_options: dict[str, Any] = {
            "max_results": max_results,
            "scrape_top_n": scrape_top_n,
            "max_content_chars": min(options.max_content_chars, self.MAX_CONTENT_CHARS_CAP),
            "wait_for_result": not scrape_top_n,
            "timeout_s": upstream_timeout,
            # ：fast_mode=False 
            "fast_mode": not options.render_js,
        }
        # 3. 
        requested = options.split_engines()
        engines = [e for e in requested if e in self.SUPPORTED_ENGINES]
        for unknown in set(requested) - set(engines):
            logger.warning(" %r，( %s)", unknown, self.SUPPORTED_ENGINES)
        if engines:
            upstream_options["engines"] = engines
        if options.language:
            upstream_options["language"] = options.language
        mapped_range = self.TIME_RANGE_MAP.get(options.time_range)
        if mapped_range:
            upstream_options["time_range"] = mapped_range
        elif options.time_range:
            # day/week/month/year，，
            logger.warning(" time_range=%r，", options.time_range)

        # 4. ( client timeout)
        response = client.post(
            f"{self.base_url}/tools/web_research",
            headers=self._headers(),
            json={"query": effective_query, "options": upstream_options},
            timeout=http_timeout,
        )
        self._check_status(response)
        data = self._parse_json(response)

        # 5. ，
        if scrape_top_n and not self._scrape_settled(data):
            data = self._poll_task(client, data, self.SCRAPE_POLL_BUDGET)

        return self._normalize(data, options)

    @staticmethod
    def _scrape_settled(data: dict[str, Any]) -> bool:
        """(， scrape )。"""
        if data.get("status") in XiaoBeiProvider.TERMINAL_STATUSES:
            return True
        pending = {"queued", "scraping", "pending"}
        items: list[dict[str, Any]] = data.get("results") or []
        for item in items:
            scrape: dict[str, Any] = item.get("scrape") or {}
            if scrape.get("status") in pending:
                return False
        return True

    def _poll_task(
        self,
        client: httpx.Client,
        data: dict[str, Any],
        budget: int,
    ) -> dict[str, Any]:
        """ `GET /tasks/{id}` 。

        ——search results，
        successfailure。
        """
        task_id = data.get("task_id")
        if not task_id:
            return data
        deadline = time.monotonic() + budget
        latest = data
        while time.monotonic() < deadline:
            time.sleep(self.POLL_INTERVAL)
            try:
                resp = client.get(
                    f"{self.base_url}/tasks/{task_id}",
                    headers=self._headers(),
                    timeout=30.0,
                )
                self._check_status(resp)
                latest = self._parse_json(resp)
            except SearchProviderError:
                raise
            except Exception as exc:  # noqa: BLE001 — failure
                logger.warning(" %s failure: %s", task_id, exc)
                return latest
            if self._scrape_settled(latest):
                break
        return latest

    def _normalize(
        self,
        data: dict[str, Any],
        options: SearchOptions,
    ) -> list[dict[str, Any]]:
        results: list[dict[str, Any]] = data.get("results") or []
        engine_errors: list[dict[str, Any]] = data.get("engine_errors") or []
        failure_reason = data.get("failure_reason")
        status = data.get("status")

        # 6. failure → ( status="failed" failure，)
        if status == "search_failed" or failure_reason == "all_engines_error":
            raise RetryableUpstreamError(f"failure status={status} failure_reason={failure_reason} engine_errors={engine_errors}")

        # 7. ：( engine_errors，valueretry) vs ()
        if not results:
            if engine_errors:
                raise RetryableUpstreamError(f"， {engine_errors}，retry")
            return []

        # 8. /：， host 
        sites = [s.lower() for s in options.split_sites()]
        blocked = [b.lower() for b in options.split_block_hosts()]
        normalized: list[dict[str, Any]] = []
        for item in results:
            url = item.get("url") or ""
            host = _host_of(url)
            if sites and not any(_host_matches(host, s) for s in sites):
                continue
            if blocked and any(_host_matches(host, b) for b in blocked):
                continue

            # ，
            scrape: dict[str, Any] = item.get("scrape") or {}
            markdown: str = scrape.get("markdown") or ""
            snippet: str = markdown if (options.full_content and markdown) else (item.get("snippet") or "")

            normalized.append(
                {
                    "title": item.get("title") or "Untitled",
                    "link": url,
                    "snippet": snippet,
                    "date": _clean_date(item.get("published_date")),
                    # ：，
                    "engine": item.get("engine"),
                    "position": item.get("rank"),
                }
            )
        return normalized


# ：value()-> adapterclass
_PROVIDER_REGISTRY: dict[str, type[SearchProviderBase]] = {
    "serper": SerperProvider,
    "seed": SeedProvider,
    "baidu": BaiduProvider,
    "xiaobei": XiaoBeiProvider,
}

# ，
_PROVIDER_ALIASES = {
    "": "xiaobei",
    "orchestrator": "xiaobei",
    "": "xiaobei",
    "doubao": "seed",
    "package": "seed",
    "": "baidu",
}

# ，key configuration——configuration，
_provider_cache: dict[tuple[str, ...], SearchProviderBase] = {}


def _resolve_provider_name() -> str:
    """ `SEARCH_PROVIDER`——****， Serper。"""
    return (os.getenv("SEARCH_PROVIDER") or "").strip() or "Serper"


# backward compatibility： RFC  SERPER_API_KEY。
# configuration， SEARCH_API_KEY 。
_LEGACY_API_KEY_ENV = "SERPER_API_KEY"


def _resolve_api_key() -> str:
    """ `SEARCH_API_KEY`； `SERPER_API_KEY`(backward compatibility)。"""
    value = (os.getenv("SEARCH_API_KEY") or "").strip()
    if value:
        return value
    return (os.getenv(_LEGACY_API_KEY_ENV) or "").strip()


def _get_provider() -> SearchProviderBase:
    """()。"""
    # 1. 
    raw_name = _resolve_provider_name()
    provider_key = raw_name.strip().lower()
    provider_key = _PROVIDER_ALIASES.get(provider_key, provider_key)
    provider_cls = _PROVIDER_REGISTRY.get(provider_key)
    if provider_cls is None:
        raise SearchProviderError(f"Unsupported SEARCH_PROVIDER: {raw_name!r}. Supported providers: Serper / Seed / Baidu / XiaoBei.")

    # 2. 
    api_key = _resolve_api_key()
    base_url = (os.getenv("SEARCH_BASE_URL") or "").strip() or None
    timeout = float(os.getenv("SEARCH_TIMEOUT") or DEFAULT_TIMEOUT)
    max_retries = int(os.getenv("SEARCH_MAX_RETRIES") or DEFAULT_MAX_RETRIES)

    # 3. configuration
    signature = (provider_key, api_key, base_url or "", str(timeout), str(max_retries))
    cached = _provider_cache.get(signature)
    if cached is not None:
        return cached

    # 4. 
    engine = provider_cls(
        api_key=api_key,
        base_url=base_url,
        timeout=timeout,
        max_retries=max_retries,
    )
    _provider_cache[signature] = engine
    return engine


def _clean_source(*candidates: Any) -> str | None:
    """。

     `web_anchor` 、`website`  ""——
    ， `source=""` 。
    """
    junk = {"", "", "", "null", "none"}
    for value in candidates:
        if isinstance(value, str) and value.strip().lower() not in junk:
            return value.strip()
    return None


def _clean_date(value: Any) -> str | None:
    """：() 1970 epoch，。"""
    if not value or not isinstance(value, str):
        return None
    return None if value.startswith("1970") else value


def _results_to_llm_content(results: list[dict[str, Any]]) -> str:
    """list gemini-cli ( WebSearch )。"""
    lines: list[str] = []
    for idx, item in enumerate(results, 1):
        title = item.get("title", "Untitled")
        link = item.get("link") or item.get("url") or "No URL"
        lines.append(f"[{idx}] {title} ({link})")
        if item.get("snippet"):
            lines.append(f"    {item['snippet']}")
        meta = [
            f"date: {item['date']}" if item.get("date") else "",
            f"authority: {item['authority']}" if item.get("authority") else "",
        ]
        meta_line = ", ".join(m for m in meta if m)
        if meta_line:
            lines.append(f"    ({meta_line})")
    return "\n".join(lines) if lines else "No results found."


def _error_result(message: str, error_type: str = "WEB_SEARCH_FAILED") -> dict[str, Any]:
    """error， `google_web_search` 。"""
    return {
        "content": f"Error: {message}",
        "returnDisplay": "Error performing web search.",
        "error": {"message": message, "type": error_type},
    }


def web_search(
    query: str,
    num_results: int | None = None,
    search_type: str | None = None,
    time_range: str | None = None,
    sites: str | None = None,
    block_hosts: str | None = None,
    authority_only: bool | None = None,
    industry: str | None = None,
    query_rewrite: bool | None = None,
    need_content: bool | None = None,
    full_content: bool | None = None,
    content_format: str | None = None,
    max_content_chars: int | None = None,
    country: str | None = None,
    language: str | None = None,
    location: str | None = None,
    page: int | None = None,
    search_engine: str | None = None,
    render_js: bool | None = None,
) -> dict[str, Any]:
    """Execute web search using the configured SEARCH_PROVIDER.

    Args:
        query: Search query keywords.
        num_results: Number of results to return (default: 10).
        search_type: Search type ('search', 'news', 'images', 'places', 'videos', 'scholar').
        time_range: Time filter ('OneDay', 'OneWeek', 'OneMonth', 'OneYear' or date range).
        sites: Filter by domains separated by '|' (e.g. 'arxiv.org|nature.com').
        block_hosts: Block domains separated by '|'.
        authority_only: Restrict results to high-authority domains.
        industry: Domain industry context filter ('finance', 'tech', 'gov').
        query_rewrite: Whether to enable automatic query rewriting.
        need_content: Whether to scrape full page content for top results.
        full_content: Return complete un-truncated page text.
        content_format: Output format ('markdown', 'text', 'html').
        max_content_chars: Maximum characters per result page (default: 1000).
        country: ISO 3166-1 country code (e.g. 'us', 'in').
        language: Language code (e.g. 'en', 'zh-cn').
        location: Geographic location for localized results.
        page: Page number for pagination.
        search_engine: Specific search engine override ('google', 'bing').
        render_js: Whether to render JavaScript via headless browser.

    Returns:
        Dictionary containing search results, sources, and metadata.
    """
    try:
        # 1. (， query )
        if not query or not query.strip():
            return {
                "content": "The 'query' parameter cannot be empty.",
                "returnDisplay": "Error: Empty search query.",
                "error": {
                    "message": "The 'query' parameter cannot be empty.",
                    "type": "INVALID_QUERY",
                },
            }

        # 2. 「 >  > default」， options
        # （__post_init__  news→ ）
        supplied = {
            "num_results": num_results,
            "search_type": search_type,
            "time_range": time_range,
            "sites": sites,
            "block_hosts": block_hosts,
            "authority_only": authority_only,
            "industry": industry,
            "query_rewrite": query_rewrite,
            "need_content": need_content,
            "full_content": full_content,
            "content_format": content_format,
            "max_content_chars": max_content_chars,
            "country": country,
            "language": language,
            "location": location,
            "page": page,
            "search_engine": search_engine,
            "render_js": render_js,
        }
        options = SearchOptions(**{name: resolve_param(name, value) for name, value in supplied.items()})

        # 3. (retry；failureerrorstring)
        provider = _get_provider()
        results = provider.search(query=query, options=options)
        if isinstance(results, str):
            return _error_result(f"[{provider.name}] {results}")

        if not results:
            return {
                "content": f'Web search results for "{query}":\n\nNo results found.',
                "returnDisplay": f'Search results for "{query}" returned (0 results).',
                "sources": [],
                "provider": provider.name,
            }

        # 4.  gemini-cli 
        formatted = _results_to_llm_content(results)
        return {
            "content": f'Web search results for "{query}" (provider: {provider.name}):\n\n{formatted}',
            "returnDisplay": (f'Search results for "{query}" via {provider.name} returned ({len(results)} results).'),
            "sources": results,
            "provider": provider.name,
        }

    except SearchProviderError as e:
        # configurationclasserror( key /  / )，type
        return _error_result(str(e), error_type="WEB_SEARCH_CONFIG_ERROR")

    except Exception as e:  # noqa: BLE001 — ，exception Runtime
        logger.exception("web_search failed")
        return _error_result(f"{type(e).__name__}: {str(e)}")