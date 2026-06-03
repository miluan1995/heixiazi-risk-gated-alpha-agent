# Heixiazi Risk-Gated Alpha Agent

A risk-gated AI trading agent concept for **BNB Hack: AI Trading Agent Edition**.

It turns CoinMarketCap-style market data into:

1. a backtestable strategy spec,
2. a deterministic risk-gate decision,
3. a trade/no-trade report with falsifiers,
4. an optional execution plan for Trust Wallet Agent Kit / BNB AI Agent SDK.

> Core idea: the agent is rewarded not just for profitable trades, but for knowing when **not** to trade.

## Status

Local scaffold only. No wallet, no portal login, no real trades.

## Demo

```bash
python3 scripts/run_demo.py
```

Outputs:

```text
reports/demo_report.md
reports/demo_report.json
```

## Architecture

```text
CMC-like fixture data
-> signal_engine.py: regime + momentum + sentiment scoring
-> risk_gate.py: liquidity / volatility / drawdown / source freshness checks
-> backtest_runner.py: simulated strategy performance with fees
-> report_renderer.py: markdown + JSON report
```

## Hackathon tracks

- Track 2 Strategy Skills: primary target.
- Track 1 Autonomous Trading Agent: optional wrapper after user approval, using TWAK + BNB SDK with strict limits.

## Safety

This repo is not financial advice. The current demo never broadcasts transactions.
