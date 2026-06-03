def evaluate(token, signal, backtest, policy):
    checks = []
    def add(name, ok, detail):
        checks.append({"name": name, "ok": bool(ok), "detail": detail})

    add("liquidity", token["liquidity_usd"] >= policy["min_liquidity_usd"], f"liquidity_usd={token['liquidity_usd']} >= {policy['min_liquidity_usd']}")
    add("volatility", token["atr_pct"] <= policy["max_volatility_pct"], f"atr_pct={token['atr_pct']} <= {policy['max_volatility_pct']}")
    add("drawdown", backtest["max_drawdown_pct"] <= policy["max_drawdown_pct"], f"backtest_max_dd={backtest['max_drawdown_pct']} <= {policy['max_drawdown_pct']}")
    add("signal_score", signal["score"] >= policy["min_signal_score"], f"score={signal['score']} >= {policy['min_signal_score']}")
    add("news_risk", token.get("news_risk", 0) <= policy["max_news_risk"], f"news_risk={token.get('news_risk', 0)} <= {policy['max_news_risk']}")

    passed = all(c["ok"] for c in checks)
    return {
        "passed": passed,
        "verdict": "TRADE_ALLOWED" if passed else "NO_TRADE",
        "checks": checks,
        "position_usd": policy["max_position_usd"] if passed else 0,
        "reason": "all risk gates passed" if passed else "one or more risk gates failed"
    }
