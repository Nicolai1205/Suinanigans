# Suinanigans  
A quick look at whether the allegations are anything more than circumstantial.

## 1. Can SUI team or investor wallets be labeled with high confidence?  
**Short answer: no.**

### Why the answer is no  
**No public disclosures**  
The team has never released official team or investor addresses. We start from exactly zero known wallets.

**No third-party confirmation**  
Platforms that specialize in address labelling (Nansen, Dune dashboards, Arkham, etc.) also have no verified team or investor SUI wallets. If any existed, these platforms would likely show them—they don’t.

**Sui’s object model makes tracing messy**  
Sui is object-based rather than account-based, which makes it much harder to follow simple “wallet received X at time Y” patterns.  
For example:  
This wallet often cited has **no initial token receipt** on record. Its first visible transaction is staking.  
https://suivision.xyz/txblock/FF41d1kjiB55MAMX6LujqMFhpznpCAiGpYQ5bwmsUXpK?tab=Overview

**Tokenomics don’t map cleanly to wallets**  
You can review tokenomics, unlock schedules, launchpools, IDOs, etc., but none of these map to specific on-chain addresses. Current holder distributions also do not obviously align with the published tokenomics—it’s possible the team/treasury funds are intentionally spread across many smaller wallets.

**Deep tracing is possible but not conclusive**  
In theory you could trace every transaction back to genesis and attempt to label wallets—but in practice this is extremely time-consuming, and still does not yield high-confidence attributions on Sui.

**Behaviour ≠ proof**  
Arguments like “staking dropped when price rose, so insiders must have sold” are weak. Staking changes for many reasons, and this alone is not evidence of insider selling.

### What about the article and the wallet the article mentions?  
An article from Finbold reports that an account (0x be90… aa8) is allegedly an “infrastructure partner” of the Sui Foundation and that it has executed a selling spree of about USD 400 million in SUI, and may dump another USD 20 million.
The wallet in question is:  
https://suivision.xyz/account/0xbe90dbe25c747f23e7b93f8948f240a90aa106597b7dab0b33e852b0b1950aa8?tab=Activity  
That article claims the address received tokens from two origin addresses (each with hundreds of millions in SUI, allegedly under vesting contracts) and then initiated large outflows.
**But**: No public confirmation of this wallet belonging to the team or investors, no proof of insider trading, and no reliable attribution. This keeps the situation firmly in the domain of circumstantial evidence.

### Why this matters  
The allegations are built on circumstantial evidence. Light did not provide a list of wallets. The article uses speculative language (“infrastructure partner”, “allegedly”, “the account . . . is likely”). The whole situation resembles recent high-profile allegations (e.g., Justin Sun) where everything “looked” bad but nothing was proven. If this were in court, it would not hold up.

### Conclusion for Question 1  
It is not possible to label the SUI team or investor wallets with high confidence based on any available information.  
**Answer is no.**

---

## 2. Can we verify Light’s numbers or claims about investor selling?  
No. Without knowing which wallets belong to the team or investors, we cannot validate any of the numbers or alleged sales.

---

## 3. Can we estimate how much insiders sold after Light’s post?  
No. Without wallet attribution any estimate would be guesswork at best.

---

## 4. Can we chart team or foundation sales over time?  
Also no. To chart something meaningfully we need to know which wallets to track. We don’t have that.

---

## Final answer  
Based on everything above—public data, third-party tools, tokenomics, article claims—the answer remains: **no**.  
There is no reliable way to identify team or investor wallets, no way to verify the claims made, and no basis for building meaningful charts.



## 5. Final comments on feasibility, process and tests

**Short answer: no — not for historical analysis.**

## What We Did
We built a transaction-flow tracker to:
- Identify the first 1000 genesis wallets (May 2023)
- Track their transactions through November 2024
- Follow multi-hop flows between wallets
- Detect exchange-like behavior
- Map paths from genesis wallets to exchanges

All queries functioned correctly against the [Sui GraphQL Beta endpoint](https://docs.sui.io/guides/developer/advanced/graphql-rpc).

## Why It Fails
The public GraphQL endpoint  
`https://sui-mainnet.mystenlabs.com/graphql`  
retains only **~3 days of transaction history** (verified Nov 18, 2025).

Observed:
- Works for recent data (last ~72 hours)
- No data for checkpoints 0+
- No genesis data (May 2023)
- No data from 2024
- Only returns mid-Nov 2025 onward

## Implications
- Cannot analyze genesis activity  
- Cannot investigate autumn 2024 events  
- Cannot verify the $400M allegation timeline  
- Cannot reconstruct historical money flows  

## What’s Required Instead
- Running a full Sui archival node  
- Using a commercial data provider  
- Partnering with an entity that stores full Sui history  

## Why This Matters
The public GraphQL service does not provide historical data.  
The [official documentation](https://docs.sui.io/guides/developer/advanced/graphql-rpc) also does not mention these retention limits, making it easy to assume full-chain access when it is not available.

## Conclusion for Question 5
Public GraphQL access cannot support historical transaction tracing.  
**Answer: no.**

