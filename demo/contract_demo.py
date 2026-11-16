"""AI legal contract generator, a small reference demo.

This demo shows the pattern behind an AI legal contract generator:
generate a short contract from a template, review a contract against
a checklist of required clauses, and flag risky terms before anyone
signs. It also extracts the key terms from a contract as plain text.

Every company name, person name, amount, date, and clause in this
file is invented sample data written only to exercise the pattern.
Nothing here is a real contract, a real agreement, or legal advice.
The demo uses plain Python with no external packages and makes no
network calls. A real contract generator would call a language model
and a lawyer would review the result. This demo models the shape of
the work with fixed sample text, not the model and not the review.
"""

import re

# The clauses a simple services agreement is expected to carry.
REQUIRED_CLAUSES = [
    "Parties",
    "Term",
    "Payment",
    "Confidentiality",
    "Termination",
    "Governing Law",
    "Liability Cap",
]

# Words that make payment wording vague enough to flag.
VAGUE_PAYMENT_WORDS = ["promptly", "in due course", "as soon as possible"]

# Two invented sample contracts. Each clause is a short text, written
# only so the checklist and the risk checks have something to read.
CONTRACT_A = {
    "title": "Sample Services Agreement A",
    "clauses": {
        "Parties": "This agreement is between Acme Analytics LLC and "
                   "Northwind Retail Inc.",
        "Term": "The term is 12 months from the start date. It renews "
                "automatically for further 12 month periods unless either "
                "party gives 30 days written notice.",
        "Payment": "Northwind Retail Inc. pays 5000 dollars per month, "
                   "due net 30 days from invoice.",
        "Confidentiality": "Each party keeps the other party confidential "
                          "information private and does not share it with "
                          "outsiders.",
        "Termination": "Either party may end this agreement with 30 days "
                       "written notice.",
        "Governing Law": "This agreement is governed by the laws of the "
                         "State of New York.",
        "Indemnification": "Each party indemnifies the other without limit "
                           "for any loss arising from the services.",
    },
}

CONTRACT_B = {
    "title": "Sample Vendor Agreement B",
    "clauses": {
        "Parties": "This agreement is between Acme Analytics LLC and "
                   "Harbor Foods Inc.",
        "Term": "The term is 6 months from the start date.",
        "Payment": "Harbor Foods Inc. pays promptly for the services "
                   "provided.",
        "Governing Law": "This agreement is governed by the laws of the "
                         "State of California.",
    },
}


def review_checklist(contract):
    """Check which required clauses are present and which are missing.

    Returns a pair of lists, present and missing, in checklist order.
    """
    present = []
    missing = []
    for clause in REQUIRED_CLAUSES:
        if clause in contract["clauses"]:
            present.append(clause)
        else:
            missing.append(clause)
    return present, missing


def flag_risks(contract):
    """Flag risky terms in a contract.

    Returns a list of risk notes, each with a level and a reason.
    The checks read the clause text with plain string matching, so
    they only catch the wording written into the sample data.
    """
    risks = []
    clauses = contract["clauses"]
    text = " ".join(clauses.values()).lower()

    if "Liability Cap" not in clauses:
        risks.append(("high", "no liability cap, liability is uncapped"))
    if "indemnifies the other without limit" in text:
        risks.append(("high", "indemnification is unlimited"))
    if "Termination" not in clauses:
        risks.append(("medium", "no termination clause, no stated exit path"))
    elif "days" not in clauses["Termination"].lower():
        risks.append(("medium", "termination gives no notice period"))
    if "Payment" in clauses:
        payment = clauses["Payment"].lower()
        for word in VAGUE_PAYMENT_WORDS:
            if word in payment:
                risks.append(("medium", "payment wording is vague: " + word))
    if "renews automatically" in text:
        notice = re.search(r"(\d+) days written notice", text)
        if notice is None or int(notice.group(1)) < 30:
            risks.append(("medium", "auto renewal with less than 30 days notice"))
    return risks


def extract_key_terms(contract):
    """Pull the key terms out of a contract as plain text.

    The extraction is simple pattern matching over the sample text.
    It finds the parties, the term in months, the monthly fee, and
    the notice period in days, when each one is stated.
    """
    text = " ".join(contract["clauses"].values())
    terms = {}

    parties = re.search(
        r"between (.+?) and (.+?)\.", text)
    if parties:
        terms["parties"] = parties.group(1) + " and " + parties.group(2)

    term = re.search(r"term is (\d+) months", text, re.IGNORECASE)
    if term:
        terms["term"] = term.group(1) + " months"

    fee = re.search(r"pays (\d[\d,]*) dollars per month", text, re.IGNORECASE)
    if fee:
        terms["monthly fee"] = fee.group(1) + " dollars"

    notice = re.search(r"(\d+) days written notice", text, re.IGNORECASE)
    if notice:
        terms["notice period"] = notice.group(1) + " days"

    law = re.search(r"laws of the State of ([A-Za-z ]+)\.", text)
    if law:
        terms["governing law"] = law.group(1).strip()

    return terms


def generate_contract(provider, client, months, fee, state):
    """Generate a short services agreement from a template.

    The template covers every required clause, caps liability at the
    fees paid in the prior 12 months, states a clear payment term,
    and gives a 30 day notice period for termination. The generated
    text is a starting draft, not a finished agreement, and the
    review in this demo is the check that the draft is complete.
    """
    clauses = {
        "Parties": "This agreement is between %s and %s." % (provider, client),
        "Term": "The term is %d months from the start date. It does not "
                "renew automatically." % months,
        "Payment": "%s pays %d dollars per month, due net 30 days from "
                   "invoice." % (client, fee),
        "Confidentiality": "Each party keeps the other party confidential "
                          "information private and does not share it with "
                          "outsiders.",
        "Termination": "Either party may end this agreement with 30 days "
                       "written notice.",
        "Governing Law": "This agreement is governed by the laws of the "
                         "State of %s." % state,
        "Liability Cap": "Each party total liability is capped at the fees "
                         "paid in the prior 12 months.",
    }
    return {"title": "Generated Services Agreement", "clauses": clauses}


def print_review(contract):
    """Print the checklist review, the risk flags, and the key terms."""
    print(contract["title"])
    present, missing = review_checklist(contract)
    print("  Required clauses present: %d of %d" % (len(present), len(REQUIRED_CLAUSES)))
    for clause in present:
        print("    present: " + clause)
    for clause in missing:
        print("    MISSING: " + clause)
    risks = flag_risks(contract)
    print("  Risk flags: %d" % len(risks))
    for level, reason in risks:
        print("    %s risk: %s" % (level, reason))
    terms = extract_key_terms(contract)
    print("  Key terms extracted:")
    for name in ["parties", "term", "monthly fee", "notice period", "governing law"]:
        if name in terms:
            print("    %s: %s" % (name, terms[name]))
    print()
    return present, missing, risks


def main():
    print("AI legal contract generator demo")
    print("All company names, amounts, and clauses are invented sample")
    print("data, written only to exercise the pattern. This is not legal")
    print("advice, and no generated text here is a finished agreement.")
    print()

    print("Review 1: sample services agreement A")
    print("  A nearly complete agreement with two risky terms.")
    print()
    a_present, a_missing, a_risks = print_review(CONTRACT_A)

    print("Review 2: sample vendor agreement B")
    print("  A thin agreement with missing clauses and vague payment.")
    print()
    b_present, b_missing, b_risks = print_review(CONTRACT_B)

    print("Generate: a new agreement from the template")
    print("  Built for invented parties, then reviewed the same way.")
    print()
    generated = generate_contract(
        "Acme Analytics LLC", "Cedar Health Inc.", 12, 7500, "New York")
    g_present, g_missing, g_risks = print_review(generated)

    print("Summary")
    print("  Agreement A: %d of %d clauses present, %d missing, %d risk flags"
          % (len(a_present), len(REQUIRED_CLAUSES), len(a_missing), len(a_risks)))
    print("  Agreement B: %d of %d clauses present, %d missing, %d risk flags"
          % (len(b_present), len(REQUIRED_CLAUSES), len(b_missing), len(b_risks)))
    print("  Generated: %d of %d clauses present, %d missing, %d risk flags"
          % (len(g_present), len(REQUIRED_CLAUSES), len(g_missing), len(g_risks)))
    print()
    print("What the demo shows")
    print("  A contract generator is a checklist plus a risk read, not")
    print("  just text output. The template produces a complete draft,")
    print("  the review catches what is missing, and the risk flags")
    print("  catch wording that would cost money later. The generated")
    print("  draft still needs a lawyer before anyone signs it.")


if __name__ == "__main__":
    main()
