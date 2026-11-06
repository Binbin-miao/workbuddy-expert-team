#!/usr/bin/env python3
"""
跨平台辅助脚本：将本专家团内置的 46 个 SKILL.md 同步复制到本机全局或工作区 skills 目录（可选）。
即使不运行本脚本，专家团各 Agent 也已在提示词中 100% 内置了全部技能规则，可直接开箱即用。
"""
import os
import shutil
import sys
from pathlib import Path

def main():
    src_skills = Path(__file__).resolve().parent / "skills"
    if not src_skills.exists():
        print("未找到内置 skills 目录。")
        sys.exit(1)

    # 支持传入目标目录，默认安装到 ~/.workbuddy/skills
    if len(sys.argv) > 1:
        target_dir = Path(sys.argv[1]).expanduser().resolve()
    else:
        target_dir = Path.home() / ".workbuddy" / "skills"

    target_dir.mkdir(parents=True, exist_ok=True)
    count = 0
    for item in sorted(src_skills.iterdir()):
        if item.is_dir() and (item / "SKILL.md").exists():
            dest = target_dir / item.name
            if dest.exists():
                shutil.rmtree(dest)
            shutil.copytree(item, dest)
            count += 1
            print(f"[OK] 已安装内置技能: {item.name} -> {dest}")

    print(f"\n全部完成！共向 {target_dir} 同步了 {count} 个内置技能。")

if __name__ == "__main__":
    main()
