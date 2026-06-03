#!/usr/bin/env python3
import json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from signal_engine import rank_tokens, score_token
from backtest_runner import run_backtest
from risk_gate import evaluate
from report_renderer import render

fixture = json.loads((ROOT / "examples/cmc_fixture.json").read_text())
policy = json.loads((ROOT / "config/risk_policy.json").read_text())
ranked = rank_tokens(fixture["tokens"])
by_symbol = {t["symbol"]: t for t in fixture["tokens"]}
rows = []
for sig in ranked:
    token = by_symbol[sig["symbol"]]
    bt = run_backtest(token, fee_bps=policy["fee_bps"])
    gate = evaluate(token, sig, bt, policy)
    rows.append({"symbol": sig["symbol"], "signal": sig, "backtest": bt, "risk_gate": gate})
allowed = [r for r in rows if r["risk_gate"]["passed"]]
result = {
    "generated_at": fixture["generated_at"],
    "portfolio_verdict": "TRADE_ALLOWED" if allowed else "NO_TRADE_PORTFOLIO",
    "candidates": rows,
    "source_refs": fixture["source_refs"],
    "valid_until": policy["valid_until"],
    "falsifiers": [
        "Live CMC data contradicts fixture momentum/sentiment.",
        "Liquidity drops below policy threshold before execution.",
        "Backtest max drawdown exceeds policy cap on refreshed data.",
        "News/token risk rises above max_news_risk.",
        "TWAK/BNB execution adapter cannot enforce user-defined limits."
    ],
    "next_research_action": "Replace fixture with live CMC MCP/API adapter and run the same report on BNB Chain liquid assets before any TWAK execution wrapper."
}
render(result, ROOT / "reports/demo_report.md", ROOT / "reports/demo_report.json")
print("Wrote reports/demo_report.md and reports/demo_report.json")
print("Portfolio verdict:", result["portfolio_verdict"])
