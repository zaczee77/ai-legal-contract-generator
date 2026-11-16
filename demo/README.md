# Demo: AI legal contract generator

A small reference demo of the pattern behind an AI legal contract generator. It reviews two invented sample agreements against a checklist of required clauses, flags risky wording, extracts the key terms, then generates a third agreement from a template and reviews it the same way.

## How to run it

From the repository root, or from this folder:

```
python3 demo/contract_demo.py
```

Plain Python, no external packages, no network calls.

## What it does

1. Review agreement A. A nearly complete invented services agreement. It carries 6 of 7 required clauses, is missing only the liability cap, and carries 2 high risk flags, no liability cap and unlimited indemnification. Key terms extracted: Acme Analytics LLC and Northwind Retail Inc, 12 month term, 5000 dollar monthly fee, 30 day notice period, New York law.
2. Review agreement B. A thin invented vendor agreement. It carries 4 of 7 required clauses, is missing confidentiality, termination, and the liability cap, and carries 3 risk flags, no liability cap, no termination clause, and vague payment wording. Key terms extracted: Acme Analytics LLC and Harbor Foods Inc, 6 month term, California law, and no stated fee, because the agreement never names an amount.
3. Generate a new agreement. Built from the template for invented parties, Acme Analytics LLC and Cedar Health Inc, a 12 month term, a 7500 dollar monthly fee, and New York law. It carries 7 of 7 required clauses, with 0 missing and 0 risk flags.

## What it printed when it was tested

Agreement A: 6 of 7 clauses present, 1 missing, 2 risk flags. Agreement B: 4 of 7 clauses present, 3 missing, 3 risk flags. Generated: 7 of 7 clauses present, 0 missing, 0 risk flags.

## What the sample data is

Every company name, amount, and clause in `contract_demo.py` is invented sample data written only to exercise the pattern. Nothing here is a real contract, a real agreement, or legal advice, and no generated text here is a finished agreement. A real generator would call a language model to draft the text, and a lawyer would review every draft before it is signed. Neither the model nor the review is modeled here.

## Files

1. `contract_demo.py`: the demo. The checklist review, the risk flags, the key term extraction, and the template generator.
2. `README.md`: this file.
