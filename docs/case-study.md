# AI legal contract generator case study

## What the generator is

An AI legal contract generator built by Nirmeet Rao and presented on his portfolio at nirmeetrao.com. It turns a short brief into a first draft services agreement, then reviews the draft against a checklist of required clauses and flags risky wording before anyone signs. This case study describes the problem it addresses, the pattern at its center, and the design choices behind it. It invents no metrics, users, or outcomes for the product, because none are part of its public record.

## The problem in plain terms

A small company that needs a services agreement usually faces two bad options. It can pay a lawyer for a routine document, which costs more than the deal is worth at the start, or it can copy an old agreement and edit it by hand, which is how the wrong names, the missing clauses, and the unlimited liability survive into the signed copy. The cost is not the drafting. The cost is what the draft leaves out.

The mistakes repeat because they are quiet. A liability cap is missing, so one bad month can cost more than the whole contract is worth. Indemnification is unlimited, so a small vendor carries a risk it never agreed to in plain terms. Payment says promptly instead of naming a date, so every invoice becomes a negotiation. Termination has no notice period, so ending the agreement becomes a dispute instead of a letter. None of these show up on the day of signing. All of them show up later, when the money is already at stake.

## Generate, then review

The generator works in two steps, and the second step is the product.

Generation takes a short brief, the parties, the term, the fee, and the governing law, and produces a short services agreement. The template covers every required clause, caps liability at the fees paid in the prior 12 months, states a clear payment term of net 30 days, and gives a 30 day notice period for termination. The template is deliberately plain. A first draft should be readable by the people signing it, not only by a lawyer.

Review is the check that the draft is complete and safe to read. It runs the same review on a generated draft as on any contract handed to it: a checklist of the seven clauses a simple services agreement is expected to carry, a read of the clause wording for risky terms, and an extraction of the key terms as plain text. A generator that only produces text is a typing machine. A generator that reviews its own output is a tool a founder can trust with a first draft.

## The checklist

The seven required clauses are parties, term, payment, confidentiality, termination, governing law, and a liability cap. Each one answers a question the signed agreement must answer: who is bound, for how long, for how much and when, what stays private, how it ends, whose law governs it, and how much is at stake if it goes wrong. A missing clause is not a gap in the document. It is a question with no answer, and the answer gets decided later, by the party with more leverage.

In the demo that ships with this case study, agreement A carries 6 of the 7 clauses and is missing only the liability cap, while agreement B carries 4 of the 7 and is missing confidentiality, termination, and the liability cap. The generated agreement carries all 7. The checklist does not judge the business terms. It only says whether the questions are answered.

## The risk flags

The risk checks read the clause wording and flag the terms that cost money later.

1. No liability cap. Without a cap, liability is uncapped, and one bad month can cost more than the whole contract is worth. This is a high risk.
2. Unlimited indemnification. Indemnity without a limit makes a small vendor carry a risk it never agreed to in plain terms. This is a high risk.
3. No termination clause. Without one, there is no stated exit path, and ending the agreement becomes a dispute. This is a medium risk.
4. Termination with no notice period. A right to end the agreement that names no notice period leaves both sides guessing how fast the exit happens. This is a medium risk.
5. Vague payment wording. Payment that says promptly, or in due course, names no date, so every invoice becomes a negotiation. This is a medium risk.
6. Auto renewal with less than 30 days notice. A contract that renews itself on short notice locks a party into another term before it has time to decide. This is a medium risk.

In the demo, agreement A carries 2 high risk flags, no liability cap and unlimited indemnification, while agreement B carries 3 flags, no liability cap, no termination clause, and vague payment wording. The generated agreement carries 0 flags, because the template is written to avoid every one of these terms.

## Extracting the key terms

The review also pulls the key terms out of the contract as plain text: the parties, the term in months, the monthly fee, the notice period in days, and the governing law. The point is speed. A founder deciding whether to sign should be able to read the deal at a glance, without opening the full document and hunting for the numbers. In the demo, the extraction finds the parties, a 12 month term, a 5000 dollar monthly fee, a 30 day notice period, and New York law for agreement A, and a 6 month term with California law and no stated fee for agreement B, because agreement B never names an amount. A term the contract never states cannot be extracted, and that absence is itself a finding.

## Design principles

1. A draft is a checklist first. Generating text is easy. Knowing whether the text is complete is the work. Every generated draft is reviewed against the same checklist as any other contract.
2. The risk travels with the draft. A missing cap or an unlimited indemnity is not a footnote. It is printed next to the draft, in plain language, before anyone signs.
3. Vague wording is a finding, not a style choice. Payment that says promptly is flagged, because a payment term that names no date will be argued about later.
4. Nothing is a finished agreement. A generated draft is a starting point. A lawyer reviews it before it is signed, every time, without exception.
5. The demo is honest about what it models. The demo uses fixed sample text and plain pattern matching. It shows the shape of the work, not a language model and not a legal review.

## What the demo shows, and what it does not show

The demo in this repository shows the generator pattern at miniature scale: a template that produces a complete draft, a checklist review that names what is missing, risk flags that catch wording that would cost money later, and a key term extraction that reads the deal at a glance. It runs over invented sample agreements, and the generated agreement is built from invented parties and amounts. It does not show a language model, a real contract, real terms from a real deal, or a legal review, and it does not show the generator product itself. Real drafting, real negotiation, and real legal review are all real parts of contract work, and none of them are modeled in the demo. The demo is a reference implementation of the pattern, written in plain Python with no external packages.

## Links

1. Portfolio: https://nirmeetrao.com
2. GitHub: https://github.com/Zaczee77
3. LinkedIn: https://www.linkedin.com/in/nirmeet-rao
