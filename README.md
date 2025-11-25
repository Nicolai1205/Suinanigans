# Suinanigans  
A quick look at whether the allegations are anything more than circumstantial. C

## 1. Can SUI team or investor wallets be labeled with high confidence?  
**Short answer: no.** BUT..

**No public disclosures**  
The team has never released official team or investor addresses. We start from exactly zero known wallets.

**No third-party confirmation**  
Platforms that specialize in address labelling (Nansen, Dune dashboards, Arkham, etc.) also have no verified team or investor SUI wallets. If any existed, these platforms would likely show them. They don’t.

**Tokenomics don’t map cleanly to wallets**  
You can review tokenomics, unlock schedules, launchpools, IDOs, etc., but none of these map to specific on-chain addresses. Current holder distributions also do not obviously align with the published tokenomics. It’s possible the team or treasury funds are intentionally spread across many smaller wallets.

**Deep tracing is possible but not conclusive**  
In theory you can trace every transaction back to genesis and attempt to label wallets, but in practice this is extremely time-consuming and still does not yield high-confidence attributions on Sui. Attempted further down.

**Behaviour ≠ proof**  
Arguments like “staking dropped when price rose, so insiders must have sold” are weak. Staking changes for many reasons, and this alone is not evidence of insider selling.

### What about the article and the wallet the article mentions?

An article from Finbold reports that an account (0xbe90...aa8) is allegedly an “infrastructure partner” of the Sui Foundation and that it has executed a selling spree of about USD 400 million in SUI, and may dump another USD 20 million.

The wallet in question is:  
https://suivision.xyz/account/0xbe90dbe25c747f23e7b93f8948f240a90aa106597b7dab0b33e852b0b1950aa8?tab=Activity

The article claims the address received tokens from two origin addresses (each with hundreds of millions in SUI, allegedly under vesting contracts) and then initiated large outflows.

**But:**  
No public confirmation of this wallet belonging to the team or investors, no proof of insider trading, and no reliable attribution. This keeps the situation firmly in the domain of circumstantial evidence.

### Why this matters

The allegations are built on circumstantial evidence. Light did not provide a list of wallets. The article uses speculative language like “infrastructure partner”, “allegedly”, “likely”. The whole situation resembles recent high-profile allegations (for example Justin Sun) where everything looked bad but nothing was proven. If this were in court, it would not hold up.

### Conclusion for Question 1

It is not possible to label the SUI team or investor wallets with high confidence based on any available information. Meaning I can't say "yes this is the community wallet, this is team etc.)  
**Answer is no.** But it is possible to see wallets that were funded in the very beginning and make some naive assumptions that they are team or investor related (without knowing who).

---

## 2. Can we verify Light’s numbers or claims about investor selling?

We can verify the fact that a wallet (assumed to be the correct one which sent about 400M tokens) did send many tokens out.

The wallet in question received its first large transfer from here:  
https://suiscan.xyz/mainnet/tx/GCNXkR4mSbR1ikSyu3pyTauxC8LsuPznJ5WxHtSMQR8r

The address in the transaction above got funds here:  
https://suiscan.xyz/mainnet/tx/FdvGyjbAUUxwqHi1TzyoNWvSWocBSD6BhewNzi9Ssiq1

Leading us to wallet:  
https://suiscan.xyz/mainnet/account/0x341fa71e4e58d63668034125c3152f935b00b0bb5c68069045d8c646d017fae1/activity

This is one of the first wallets funded from genesis as per the following query:  
https://dune.com/queries/6225434

Ultimately, the investor, team or early participant (infrastructure partner) as quoted by the SUI Foundation, did obscure funds by sending smaller transfers to intermediary addresses that then transferred funds to various CEXs. Example:  
https://suiscan.xyz/mainnet/account/0xbe9e8a62a74d1246924e10c46b3de0a22ec20998f66d1562c615d3ee846e922e/activity

---

## 3. Can we estimate how much insiders sold after Light’s post?

With time constraints in mind (and limited Dune credits), here is the relevant table:  
https://dune.com/queries/6225655

This showcases wallets that have transferred at least 5 million tokens to exchanges. This includes larger whales that could have come in later, but it shows how over certain timeframes there was an increase in tokens being sent to exchanges.

Most tokens by far were from a small group of early wallets.

---

## 4. Can we chart team or foundation sales over time?

Due to time limitations and running out of Dune credits, here is my answer:

It is possible to make assumptions and guesstimates, but since assets were often split across several wallets (likely to obscure ownership), it is tricky to fully determine who investors are and what team allocations look like. With the Dune queries shared at the end, it would be possible to build a case for how many tokens with meaningful relations have been sold over time.
The queries built can be expanded upon to better isolate this once specific wallets are identified and "jumps" are taken into account.

---

## Final answer

Based on everything above (public data, third-party tools, tokenomics, article claims), the answer remains: **no**.  
There is no reliable way to identify team or investor wallets 100 percent.  
At the very least not in a short amount of time.

It is possible to make assumptions based on initial chain data, but a deeper analysis requires more resources and time.

---

## 5. Final comments on feasibility, process and tests

### 5.1 First attempt ever at using GraphQL

Attempted programmatic transaction tracing using Sui's GraphQL Beta endpoint:  
https://docs.sui.io/guides/developer/advanced/graphql-rpc

While checkpoint metadata exists from genesis (April 2023), transaction details (sender addresses, balance changes) are pruned from historical data. Only recent transactions (about 2 to 4 weeks) retain full details.

Run the test yourself:  
`python test_sui_graphql.py`

Result: Cannot trace genesis wallets or track historical money flows (May 2023 to Nov 2024) needed to verify insider selling allegations.

---

### 5.2 Insider wallets on Dune?

Found 2 examples of people attempting to find insider wallets on SUI. A quick search on X made it fairly easy to debunk some of these.

Example of wallet being mentioned as an insider:  
`0xcb2812891bc31768768bf56077b13039f0f17088cf9ad212332ca6ee2a744730`  
Belongs to a small X account from back in 2023:  
https://x.com/search?q=from%3Aozigoyeng96%200xcb2812891bc31768768bf56077b13039f0f17088cf9ad212332ca6ee2a744730  
Confirmed on Suiscan:  
https://suiscan.xyz/mainnet/account/@ojigoyeng/activity

Another address that was mentioned actually belongs to HTX (Huobi):  
https://suiscan.xyz/mainnet/account/0x1f7b27844f2c4a0262b2c481f7ab956d10ace524c5a7b06c3742cfb8701db714

---

### Dune queries used

First available date point (genesis):  
https://dune.com/queries/6224491

1 month historical balances for first 100 addresses:  
https://dune.com/queries/6224337

Transaction history (with row limit) for first 100 addresses:  
https://dune.com/queries/6225198

First wallets with 1M tokens from genesis:  
https://dune.com/queries/6225434

Wallets sending at least 5M tokens to CEXs:  
https://dune.com/queries/6225655

Balance +5M snapshots (June 1, Oct 14, Nov 15):  
https://dune.com/queries/6225525

Verification of numbers (+5M balances sending to exchanges):  
https://dune.com/queries/6226022

Wallets that sent at least 5M to CEXs and were funded by genesis wallets:  
https://dune.com/queries/6226329

Track genesys wallets (early wallets) that transferred to other wallets before sending to exchanges (regardless of amount sent). Incldue 1 and 2 hops before exchange is hit:

https://dune.com/queries/6228762

---

**If I didn't run out of credits I would do the following**:
1. Check 3-4-5 hops from genesys wallets.
2. Track genesys wallets that had sent the most
3. Visualize funds sends to exchanges over time from top 20 or 30 addresses (showcase how many hops it took to get there).
4. Set up alerts for said addresses.
5. Check if there are connections between any of the wallets that were "hopped" between.
6. See which wallets are receiving funds from XYZ wallet at unlock times.
