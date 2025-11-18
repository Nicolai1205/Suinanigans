# Suinanigans  
A quick look at whether the allegations are anything more than circumstantial.

## 1. Can SUI team or investor wallets be labeled with high confidence?  
**Short answer: no.**

### Why the answer is no  
**No public disclosures**  
The team has never released official team or investor addresses. We start from exactly zero known wallets.

**No third-party confirmation**  
Platforms that specialize in address labelling (Nansen, Dune dashboards, Arkham, etc.) also have no verified team or investor SUI wallets. If any existed, these platforms would likely show them—they don’t.

**Tokenomics don’t map cleanly to wallets**  
You can review tokenomics, unlock schedules, launchpools, IDOs, etc., but none of these map to specific on-chain addresses. Current holder distributions also do not obviously align with the published tokenomics—it’s possible the team/treasury funds are intentionally spread across many smaller wallets.

**Deep tracing is possible but not conclusive**  
In theory you could trace every transaction back to genesis and attempt to label wallets—but in practice this is extremely time-consuming, and still does not yield high-confidence attributions on Sui. Attempted further down.

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
**Answer is no.** BUT, it is possible to see wallets taht were funded in the very beginning and have somve naive assumption that is is team or investor related (without knowing who).

---

## 2. Can we verify Light’s numbers or claims about investor selling?  
We can verify the fact that a wallet (assumed to be the correct one which sent about 400M tokens) did send many tokens out.

The wallet in question received first large transfer from here:
https://suiscan.xyz/mainnet/tx/GCNXkR4mSbR1ikSyu3pyTauxC8LsuPznJ5WxHtSMQR8r

The address in the transaction above got funds here:
https://suiscan.xyz/mainnet/tx/FdvGyjbAUUxwqHi1TzyoNWvSWocBSD6BhewNzi9Ssiq1

Leading us to wallet: https://suiscan.xyz/mainnet/account/0x341fa71e4e58d63668034125c3152f935b00b0bb5c68069045d8c646d017fae1/activity

Which is one of the first wallets funded from the genesys as per the following query I did.
https://dune.com/queries/6225434

Ultimately, the investor, team or early participant (infrastructure partner) as quoted by the SUI foundation, did in fact obscure funds by sending "smaller" transfers to intermediary addresses, that 
then transferred funds to various CEXs. Example: 
https://suiscan.xyz/mainnet/account/0xbe9e8a62a74d1246924e10c46b3de0a22ec20998f66d1562c615d3ee846e922e/activity

## 3. Can we estimate how much insiders sold after Light’s post?  
With time constraints in mind (and lited dune credits), here is the relevant table:
https://dune.com/queries/6225655

Showscases wallets that have transferred at least 5 million tokens to exchanges.
This includes larger whales that could have come in later, but ultimately showcases how over certain timeframes, there was an increase in tokens being sent to exchanges.

Most tokens by far were
---

## 4. Can we chart team or foundation sales over time?  
again due to time limitatoins and running out of Dune credits here is my answer:

It is possible to make assumptions and guesstimates, but as many assets were often split into several wallets (likely to obscure ownership) it is tricky to fully determine who investors are and what team allocations look like.
Regardless, with the dune queries shared at the end, it would be possible to build a case for how many tokens with meaningful relations, have been sold over time.
---

## Final answer  
Based on everything above—public data, third-party tools, tokenomics, article claims—the answer remains: **no**.  
There is no reliable way to identify team or investor wallets 100%. (AT THE VERY LEAST NOT IN A SHORT AMOUNT OF TIME)

It is however possible to make assumptions bases on initial chain data, but a deeper analysis requires more resources and time.

---
---

## 5. Final comments on feasibility, process and tests

### 5.1 First attempt ever at using Graphql
Attempted programmatic transaction tracing using [Sui's GraphQL Beta endpoint](https://docs.sui.io/guides/developer/advanced/graphql-rpc).
While checkpoint metadata exists from genesis (April 2023), transaction details (sender addresses, balance changes) are pruned from historical data. 
Only recent transactions (~2-4 weeks) retain full details.Run the test yourself:python test_sui_graphql.py
Result: Cannot trace genesis wallets or track historical money flows (May 2023 - Nov 2024) needed to verify insider selling allegations.

---
### 5.2 Insider wallets on Dune?

Found 2 examples of peolpe attemtping to find insider wallets on SUI. Perhaps for this very job application.
A quick search on X made it fairly easy to debunk some of these.

Example of wallet being mentioned as an insider:0xcb2812891bc31768768bf56077b13039f0f17088cf9ad212332ca6ee2a744730
Belongs to a small X account from back in 2023. https://x.com/search?q=from%3Aozigoyeng96%200xcb2812891bc31768768bf56077b13039f0f17088cf9ad212332ca6ee2a744730&src=typed_query
confirmed to be owned by same person looking at suiscan: https://suiscan.xyz/mainnet/account/@ojigoyeng/activity

There is also an address mentioed but it turns out to HTX (huobi). https://suiscan.xyz/mainnet/account/0x1f7b27844f2c4a0262b2c481f7ab956d10ace524c5a7b06c3742cfb8701db714.

--

Now what we really care about is if we ourselves can query Dune data ourselves.
The first available date point is 2023-04-12 with the 0x000000.... address.
The first 100 addresses (senders) from that date onwards can be found here: https://dune.com/queries/6224491

1 month historica balances for first 100 addresses (senders): https://dune.com/queries/6224337

Transaction history (with row limit) for first 100 addresses (senders): https://dune.com/queries/6225198

First wallets with 1M tokens from 0x00000...: https://dune.com/queries/6225434

Sender history wallets to cex min 5M tokens: https://dune.com/queries/6225655

Balance+5M ever, static june 1st,October 14th, November 15th: https://dune.com/queries/6225525 <- This should still get double checked on the logic.

Verification of numbers (+5m balances sending to exchanges) http://dune.com/queries/6226022

Wallets that sent min 5M to CEXs and were directly funded by genesys wallets: https://dune.com/queries/6226329


