def score_token(t):
    trend = 1.0 if t["ema_fast"] > t["ema_slow"] else 0.0
    rsi_score = 0.7 if 45 <= t["rsi"] <= 68 else (0.35 if t["rsi"] < 75 else 0.1)
    macd_score = 0.8 if t["macd"] > 0 else 0.2
    vol_penalty = min(t["atr_pct"] / 30.0, 1.0)
    sentiment = max(0.0, min(1.0, t.get("sentiment", 0.5)))
    news_penalty = max(0.0, min(1.0, t.get("news_risk", 0.0)))
    score = 0.30 * trend + 0.20 * rsi_score + 0.20 * macd_score + 0.20 * sentiment + 0.10 * (1 - vol_penalty) - 0.15 * news_penalty
    regime = "risk_on" if score >= 0.68 else ("selective" if score >= 0.55 else "risk_off")
    return {
        "symbol": t["symbol"],
        "score": round(score, 4),
        "regime": regime,
        "thesis": f"{t['symbol']} trend={'up' if trend else 'down'}, RSI={t['rsi']}, ATR={t['atr_pct']}%, sentiment={t.get('sentiment')}, news_risk={t.get('news_risk')}"
    }

def rank_tokens(tokens):
    scored = [score_token(t) for t in tokens]
    return sorted(scored, key=lambda x: x["score"], reverse=True)
