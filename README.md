# 👨‍💻 Lakshan's Learning Log (2025)

**Goal:** Become a Chief AI Architect ($1,000/hr) by 2030.

---

## 🛡️ Day 7: Web Sentinel
**Status:** ✅ Deployed | **Tech:** Python, Sys, Requests

A CLI tool that monitors the health of websites. It takes multiple URLs as arguments and reports if they are Online (200 OK) or Down.

* **Usage:** `python day07_sentinel.py google.com my-broken-site.com`
* **Features:** Auto-adds `https://`, handles timeouts, and reports status codes.


----

## 💱 Day 6: Global Currency Converter
**Status:** ✅ Deployed | **Tech:** Python, API, Math

A universal converter that uses a "Cross-Rate" formula to swap between any two world currencies.
* **Smart Math:** Calculates `(Amount / From_Rate) * To_Rate` to bridge currencies.
* **Safety:** Auto-detects network failures and prevents crashes.
* **User-Friendly:** Loops until valid currency codes are entered.

**Usage:**
```bash
python day06_converter.py


----

## 🪙 Day 6: Bitcoin ROI Calculator
**Status:** ✅ Deployed

A tool that checks real-time Bitcoin prices to calculate profit.
* **Usage:** `python bitcoin.py 50000`

---

## 🚀 Day 4: Bitcoin Price Tracker
**Status:** ✅ Deployed

My first API tool that tracks prices automatically.
* **Usage:** `python day04_api.py`

---

## 🛠️ Installation
1. `git clone https://github.com/lakshan-gunawardhane/learning-log.git`
2. `pip install requests`