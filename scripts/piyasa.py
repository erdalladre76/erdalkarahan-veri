# BIST 100, altın, Brent, BTC verisini Yahoo Finance'ten alıp piyasa.json'a yazar.
import json, urllib.request, datetime
S = {"BIST": "XU100.IS", "XAU": "GC=F", "BRENT": "BZ=F", "USDTRY": "TRY=X", "BTC": "BTC-USD"}
def q(sym):
    u = f"https://query1.finance.yahoo.com/v8/finance/chart/{sym}?interval=1d&range=7d"
    r = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"})
    res = json.load(urllib.request.urlopen(r, timeout=20))["chart"]["result"][0]
    m = res["meta"]
    closes = [c for c in res["indicators"]["quote"][0]["close"] if c]
    # önceki işlem gününün kapanışı = son günlük çubuktan bir önceki
    p = closes[-2] if len(closes) >= 2 else m.get("chartPreviousClose")
    return m["regularMarketPrice"], p
out = {}
for k, s in S.items():
    try:
        v, p = q(s); out[k] = {"v": v, "p": p}
    except Exception as e:
        print(k, e)
try:
    usd = out["USDTRY"]
    g = out["XAU"]
    out["GRAM"] = {"v": g["v"] * usd["v"] / 31.1034768, "p": g["p"] * usd["p"] / 31.1034768}
except Exception as e:
    print("gram", e)
if "BIST" not in out and "GRAM" not in out:
    raise SystemExit("veri yok")
out["t"] = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
json.dump(out, open("piyasa.json", "w"), ensure_ascii=False, indent=1)
print(out)
