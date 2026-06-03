def run_backtest(token, fee_bps=25):
    equity = 100.0
    peak = equity
    max_dd = 0.0
    trades = 0
    for r in token.get("returns", []):
        # simple demo: only takes positive momentum days; fee charged per simulated entry/exit day
        if r > 0:
            trades += 1
            equity *= (1 + (r / 100.0))
            equity *= (1 - fee_bps / 10000.0)
        peak = max(peak, equity)
        dd = (peak - equity) / peak * 100.0
        max_dd = max(max_dd, dd)
    total_return = equity - 100.0
    return {
        "trades": trades,
        "total_return_pct": round(total_return, 2),
        "max_drawdown_pct": round(max_dd, 2),
        "ending_equity": round(equity, 2)
    }
