# AI Legal Contract Generator

An AI legal contract generator built by Nirmeet Rao and presented on his portfolio at nirmeetrao.com. It turns a short brief into a first draft services agreement, then reviews the draft against a checklist of required clauses and flags risky wording before anyone signs.

## The problem

A small company that needs a services agreement usually faces two bad options. It can pay a lawyer for a routine document, which costs more than the deal is worth at the start, or it can copy an old agreement and edit it by hand, which is how the wrong names, the missing clauses, and the unlimited liability survive into the signed copy. The cost is not the drafting. The cost is what the draft leaves out.

The mistakes repeat. A liability cap is missing, so one bad month can cost more than the whole contract is worth. Indemnification is unlimited, so a small vendor carries a risk it never agreed to in plain terms. Payment says promptly instead of naming a date, so every invoice becomes a negotiation. Termination has no notice period, so ending the agreement becomes a dispute instead of a letter.

## Who it serves

The generator is aimed at founders and small teams that sign simple services agreements often and need a sound first draft fast. It fits the deals where the terms are standard and the risk sits in the wording, not in the business model: consulting work, vendor services, and software work done for a fee.

## What it does

1. Generate from a brief. Given the parties, the term, the fee, and the governing law, it produces a short services agreement that covers every required clause, caps liability at the fees paid in the prior 12 months, states a clear payment term, and gives a 30 day notice period for termination.
2. Review against a checklist. It checks a contract for the seven clauses a simple services agreement is expected to carry: parties, term, payment, confidentiality, termination, governing law, and a liability cap. Anything missing is named.
3. Flag risky terms. It reads the clause wording and flags the risks that cost money later: no liability cap, unlimited indemnification, vague payment wording, a missing termination clause, a termination clause with no notice period, and auto renewal with less than 30 days notice.
4. Extract the key terms. It pulls the parties, the term in months, the monthly fee, the notice period, and the governing law out of the contract as plain text, so the deal can be read at a glance without opening the full document.

## Design principles

1. A draft is a checklist first. Generating text is easy. Knowing whether the text is complete is the work. Every generated draft is reviewed against the same checklist as any other contract.
2. The risk travels with the draft. A missing cap or an unlimited indemnity is not a footnote. It is printed next to the draft, in plain language, before anyone signs.
3. Vague wording is a finding, not a style choice. Payment that says promptly is flagged, because a payment term that names no date will be argued about later.
4. Nothing is a finished agreement. A generated draft is a starting point. A lawyer reviews it before it is signed, every time, without exception.
5. The demo is honest about what it models. The demo uses fixed sample text and plain pattern matching. It shows the shape of the work, not a language model and not a legal review.

## The demo in this repository

The demo folder contains a small reference demo in plain Python with no external packages. It reviews two invented sample agreements, then generates a third from the template and reviews it the same way. Agreement A is nearly complete, 6 of 7 clauses present, with 1 missing and 2 high risk flags, no liability cap and unlimited indemnification. Agreement B is thin, 4 of 7 clauses present, with 3 missing and 3 risk flags, no liability cap, no termination clause, and vague payment wording. The generated agreement is complete, 7 of 7 clauses present, with 0 missing and 0 risk flags. The docs folder describes the concept and its design without inventing metrics or outcomes for it.

## What this is not

This demo is not the contract generator product, and it is not legal advice. No generated text here is a finished agreement, and no clause in the sample data is a real term from a real deal. The sample companies, amounts, and clauses are invented and exist only so the pattern can be run and read. A real generator would call a language model to draft the text, and a lawyer would review every draft before it is signed. Neither the model nor the review is modeled here. The full case study in the docs folder describes the concept and its design without claiming anything beyond what is on the portfolio.

## Links

1. Portfolio: https://nirmeetrao.com
2. GitHub: https://github.com/Zaczee77
3. LinkedIn: https://www.linkedin.com/in/nirmeet-rao
