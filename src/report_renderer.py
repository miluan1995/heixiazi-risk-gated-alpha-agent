import json
from pathlib import Path

def render(result, out_md, out_json):
    Path(out_md).parent.mkdir(parents=True, exist_ok=True)
    Path(out_json).parent.mkdir(parents=True, exist_ok=True)
    lines = []
    lines.append("# Heixiazi Risk-Gated Alpha Agent — Demo Report")
    lines.append("")
    lines.append("Status: demo / no real trading / not financial advice")
    lines.append(f"Generated at: {result['generated_at']}")
    lines.append("")
    lines.append("## Verdict")
    lines.append("")
    lines.append(f"`{result['portfolio_verdict']}`")
    lines.append("")
    lines.append("## Candidate table")
    lines.append("")
    lines.append("| Symbol | Score | Regime | Backtest return | Max DD | Risk gate | Position |")
    lines.append("|---|---:|---|---:|---:|---|---:|")
    for row in result["candidates"]:
        lines.append(f"| {row['symbol']} | {row['signal']['score']} | {row['signal']['regime']} | {row['backtest']['total_return_pct']}% | {row['backtest']['max_drawdown_pct']}% | {row['risk_gate']['verdict']} | ${row['risk_gate']['position_usd']} |")
    lines.append("")
    lines.append("## Risk gate details")
    for row in result["candidates"]:
        lines.append(f"\n### {row['symbol']}")
        lines.append(f"Thesis: {row['signal']['thesis']}")
        for c in row["risk_gate"]["checks"]:
            lines.append(f"- {'✅' if c['ok'] else '❌'} {c['name']}: {c['detail']}")
    lines.append("")
    lines.append("## Source refs")
    for s in result["source_refs"]:
        lines.append(f"- `{s['id']}` ({s['trust_level']}): {s['claim_supported']} — {s['url_or_path']}")
    lines.append("")
    lines.append("## Valid until")
    lines.append(result["valid_until"])
    lines.append("")
    lines.append("## Falsifiers / invalidation")
    for f in result["falsifiers"]:
        lines.append(f"- {f}")
    lines.append("")
    lines.append("## Next research action")
    lines.append(result["next_research_action"])
    Path(out_md).write_text("\n".join(lines) + "\n", encoding="utf-8")
    Path(out_json).write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
