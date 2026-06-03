# Heixiazi Risk-Gated Alpha Agent — Demo Report

Status: demo / no real trading / not financial advice
Generated at: 2026-06-03T23:20:00+08:00

## Verdict

`TRADE_ALLOWED`

## Candidate table

| Symbol | Score | Regime | Backtest return | Max DD | Risk gate | Position |
|---|---:|---|---:|---:|---|---:|
| BNB | 0.7863 | risk_on | 1.75% | 0.05% | TRADE_ALLOWED | $10.0 |
| CAKE | 0.6798 | selective | 8.34% | 0.0% | TRADE_ALLOWED | $10.0 |
| LOWLIQ | 0.554 | selective | 87.65% | 0.0% | NO_TRADE | $0 |

## Risk gate details

### BNB
Thesis: BNB trend=up, RSI=56, ATR=3.2%, sentiment=0.62, news_risk=0.18
- ✅ liquidity: liquidity_usd=520000000 >= 5000000
- ✅ volatility: atr_pct=3.2 <= 12.0
- ✅ drawdown: backtest_max_dd=0.05 <= 8.0
- ✅ signal_score: score=0.7863 >= 0.62
- ✅ news_risk: news_risk=0.18 <= 0.45

### CAKE
Thesis: CAKE trend=up, RSI=71, ATR=8.6%, sentiment=0.58, news_risk=0.25
- ✅ liquidity: liquidity_usd=42000000 >= 5000000
- ✅ volatility: atr_pct=8.6 <= 12.0
- ✅ drawdown: backtest_max_dd=0.0 <= 8.0
- ✅ signal_score: score=0.6798 >= 0.62
- ✅ news_risk: news_risk=0.25 <= 0.45

### LOWLIQ
Thesis: LOWLIQ trend=up, RSI=83, ATR=31.0%, sentiment=0.91, news_risk=0.72
- ❌ liquidity: liquidity_usd=18000 >= 5000000
- ❌ volatility: atr_pct=31.0 <= 12.0
- ✅ drawdown: backtest_max_dd=0.0 <= 8.0
- ❌ signal_score: score=0.554 >= 0.62
- ❌ news_risk: news_risk=0.72 <= 0.45

## Source refs
- `cmc-agent-hub-fixture` (L0_fixture): Demo market data shaped like CMC Agent Hub output; replace with live CMC MCP/API before submission. — examples/cmc_fixture.json

## Valid until
next CMC live refresh / next 4h candle close / major BNB Chain market event

## Falsifiers / invalidation
- Live CMC data contradicts fixture momentum/sentiment.
- Liquidity drops below policy threshold before execution.
- Backtest max drawdown exceeds policy cap on refreshed data.
- News/token risk rises above max_news_risk.
- TWAK/BNB execution adapter cannot enforce user-defined limits.

## Next research action
Replace fixture with live CMC MCP/API adapter and run the same report on BNB Chain liquid assets before any TWAK execution wrapper.
