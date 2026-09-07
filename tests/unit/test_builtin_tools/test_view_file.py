# Copyright 2026 NexAU Engine
# SPDX-License-Identifier: Apache-2.0
import pytest
from pathlib import Path
from nexau.archs.tool.builtin import view_file
from nexau.archs.tool import Tool

def test_view_file_schema_load():
    schema_path = Path(__file__).resolve().parents[3] / "nexau" / "archs" / "tool" / "builtin" / "schemas" / "view_file.tool.yaml"
    tool = Tool.from_yaml(str(schema_path), binding=view_file)
    assert tool.name == "view_file"
    props = tool.input_schema.get("properties", {})
    assert "AbsolutePath" in props
    assert "StartLine" in props
    assert "EndLine" in props
    assert "ContentOffset" in props
    assert "toolAction" in props
    assert "toolSummary" in props

def test_view_file_directory():
    res = view_file(AbsolutePath=".")
    assert "returnDisplay" in res
    assert "content" in res
    assert not res.get("isError", False)

def test_view_file_text_slicing(tmp_path):
    f = tmp_path / "sample.py"
    lines = [f"line_{i} = {i}" for i in range(1, 51)]
    f.write_text("\n".join(lines), encoding="utf-8")

    # Slice lines 10 to 15
    res = view_file(AbsolutePath=str(f), StartLine=10, EndLine=15)
    assert "returnDisplay" in res
    content = res["content"]
    assert "   10 | line_10 = 10" in content
    assert "   15 | line_15 = 15" in content
    assert "line_9" not in content
    assert "line_16" not in content

def test_view_file_alias_tolerance(tmp_path):
    f = tmp_path / "sample_alias.py"
    f.write_text("hello\nworld\n!", encoding="utf-8")

    res = view_file(file_path=str(f), start_line=2, end_line=3)
    assert "returnDisplay" in res
    content = res["content"]
    assert "    2 | world" in content
    assert "    3 | !" in content
