# Heixiazi Risk-Gated Alpha Agent

A risk-gated AI trading agent concept for **BNB Hack**.

It turns BNB Chain market data into:

1. a backtestable strategy spec,
2. a deterministic risk-gate decision,
3. a trade/no-trade report with falsifiers,
4. an optional execution plan for Trust Wallet Agent Kit / BNB AI Agent SDK,
5. an onchain proof hash that judges/users can verify on BSC or opBNB testnet.

> Core idea: the agent is rewarded not just for profitable trades, but for knowing when **not** to trade.

## Status

Local demo + onchain proof contract scaffold. No wallet, no portal login, no real trades.

Current submission target:

- BNB Hack: Online Edition
- AI Track
- Sponsor fit: Solidus AI Tech / APRO / ASI Alliance / NetMind.AI

## Demo

```bash
python3 scripts/run_demo.py
```

Outputs:

```text
reports/demo_report.md
reports/demo_report.json
```

Expected result:

- portfolio verdict: `TRADE_ALLOWED`
- high-risk/low-liquidity candidates are blocked by the risk gate even if simulated return is attractive.

## Architecture

```text
CMC-like fixture data
-> signal_engine.py: regime + momentum + sentiment scoring
-> risk_gate.py: liquidity / volatility / drawdown / source freshness checks
-> backtest_runner.py: simulated strategy performance with fees
-> report_renderer.py: markdown + JSON report
-> HeixiaziAgentProof.sol: optional onchain report-hash proof
```

## Onchain proof contract

`contracts/HeixiaziAgentProof.sol` is a minimal BSC/opBNB proof contract. It records report hashes and URIs for auditability.

It does **not**:

- custody user funds;
- execute trades;
- approve tokens;
- require private keys inside the agent.

Offline proof input generator from the OpenClaw workspace:

```bash
python3 ../../scripts/prepare_bnb_hack_proof.py
```

The BNB Hack requirement says the project should be deployed on or connected to BSC/opBNB mainnet or testnet and have at least two successful contract transactions. Deployment is intentionally left as a separate approval-gated step.

## Hackathon targets

- BNB Hack Online Edition AI Track: primary target.
- Solidus AI Tech sponsor track: AI-driven on-chain analytics / automated trading.
- APRO sponsor track: AI agent data verifiability.
- ASI / NetMind sponsor tracks: agent intelligence / DeAI agents.

## Safety

This repo is not financial advice. The current demo never broadcasts transactions.

Before any real wallet/payment/trading extension:

- use a dedicated limited hot wallet or credits account;
- set per-action and daily caps;
- avoid unlimited allowances;
- write preflight and post-action ledger entries;
- require explicit approval for first/risky actions.
