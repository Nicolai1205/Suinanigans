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
**Answer is no.**

---

## 2. Can we verify Light’s numbers or claims about investor selling?  

---

## 3. Can we estimate how much insiders sold after Light’s post?  

---

## 4. Can we chart team or foundation sales over time?  

---

## Final answer  
Based on everything above—public data, third-party tools, tokenomics, article claims—the answer remains: **no**.  
There is no reliable way to identify team or investor wallets, no way to verify the claims made, and no basis for building meaningful charts. (AT THE VERY LEAST NOT IN A SHORT AMOUNT OF TIME)



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

There is a limitation to researching in SUI as you can send tokens to an address and that address won't have any traces until it signs a transaction itself. E.g., staking or sending tokens to another address.


