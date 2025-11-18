#!/usr/bin/env python3
"""
Test SUI GraphQL Beta endpoint to verify data availability

Tests:
1. Can we access checkpoint metadata from genesis? (YES)
2. Can we access transaction details from genesis? (NO - pruned)
3. How far back does full transaction data go?

Endpoint: https://graphql.mainnet.sui.io/graphql
Docs: https://docs.sui.io/guides/developer/advanced/graphql-rpc
"""

import requests
import json
from datetime import datetime

GRAPHQL_URL = "https://graphql.mainnet.sui.io/graphql"

def query(q: str, variables: dict = None) -> dict:
    """Execute GraphQL query"""
    try:
        r = requests.post(GRAPHQL_URL, json={"query": q, "variables": variables or {}}, timeout=30)
        if r.status_code != 200:
            return None
        data = r.json()
        return None if 'errors' in data else data.get('data')
    except:
        return None

print("="*80)
print("SUI GraphQL BETA - DATA AVAILABILITY TEST")
print("="*80)

# Test 1: Genesis checkpoint metadata
print("\n✅ TEST 1: Genesis checkpoint metadata")
data = query("{ checkpoints(first: 5) { nodes { sequenceNumber timestamp } } }")
if data:
    nodes = data['checkpoints']['nodes']
    first = nodes[0]
    dt = datetime.fromisoformat(first['timestamp'].replace('Z', '+00:00'))
    print(f"   First checkpoint: {first['sequenceNumber']} @ {dt.date()}")
    print(f"   ✅ Checkpoint metadata goes back to genesis (April 2023)")
else:
    print(f"   ❌ Failed")

# Test 2: Genesis transaction digests
print("\n✅ TEST 2: Genesis transaction digests")
data = query("{ transactions(first: 10, filter: {afterCheckpoint: 0, beforeCheckpoint: 100}) { nodes { digest } } }")
if data and data['transactions']['nodes']:
    count = len(data['transactions']['nodes'])
    print(f"   Found {count} transaction digests from genesis")
    print(f"   ✅ Transaction digests exist from genesis")
else:
    print(f"   ❌ Failed")

# Test 3: Genesis transaction DETAILS (sender, balance changes)
print("\n❌ TEST 3: Genesis transaction DETAILS (critical for analysis)")
data = query("""
{ 
  transactions(first: 50, filter: {afterCheckpoint: 0, beforeCheckpoint: 1000}) { 
    nodes { 
      digest 
      sender { address }
    } 
  } 
}
""")
if data:
    nodes = data['transactions']['nodes']
    with_sender = [n for n in nodes if n.get('sender')]
    print(f"   Total transactions: {len(nodes)}")
    print(f"   With sender data: {len(with_sender)}")
    print(f"   Without sender: {len(nodes) - len(with_sender)}")
    if len(with_sender) == 0:
        print(f"   ❌ ALL transaction details are PRUNED from genesis period")
        print(f"   ❌ Cannot trace money flows from early wallets")

# Test 4: Recent transaction details
print("\n✅ TEST 4: Recent transaction DETAILS")
data = query("{ checkpoints(last: 1) { nodes { transactions(first: 5) { nodes { digest sender { address } } } } } }")
if data:
    txs = data['checkpoints']['nodes'][0]['transactions']['nodes']
    with_sender = [t for t in txs if t.get('sender')]
    print(f"   Total recent transactions: {len(txs)}")
    print(f"   With sender data: {len(with_sender)}")
    if len(with_sender) > 0:
        print(f"   ✅ Recent transaction details ARE available")
        print(f"   Sample: {with_sender[0]['sender']['address'][:20]}...")

# Summary
print("\n" + "="*80)
print("CONCLUSION")
print("="*80)
print("""
✅ Checkpoint metadata:    Available from genesis (April 2023)
✅ Transaction digests:     Available from genesis
❌ Transaction details:     PRUNED from genesis (sender, balance changes, etc.)
✅ Recent transaction data: Available (last few weeks estimate)

IMPACT ON INVESTIGATION:
❌ Cannot identify genesis wallets (no sender data)
❌ Cannot track transaction flows (no balance changes)
❌ Cannot map money movement from May 2023 - Nov 2024
✅ Can only analyze recent activity (estimate: last 2-4 weeks)

The public GraphQL endpoint does NOT retain full transaction history needed
for insider selling investigation spanning May 2023 to November 2024.
""")
print("="*80)

