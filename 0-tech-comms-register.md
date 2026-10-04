# tech-comms-register.md

A writing register for README files and technical documentation written for a technical audience. The source material is a chapter on clear technical writing from a Hewlett-Packard era guide on data processing communication. The rules below adapt that source and add explicit prohibitions against patterns that appear by default in machine-generated prose.

## Audience and stance

Write to a working technician who will read the document once, act on it, and not return. Treat the reader as a peer who already knows the field. Do not perform expertise, and do not blame the reader for any prior confusion. Think of yourself as a communicator first and a writer second.

The second person is appropriate for instructional passages ("you run the command, then check the log"). Watch the tone, because the second person slides easily into the imperative and the imperative grates over long stretches. Reference material and explanatory prose use the third person. Either way, the writing stays informal and one-to-one rather than impersonal and product-oriented.

## Core principles

Have a purpose. Each document holds together around a single theme. State what the document is for in the opening sentences and stay on that theme.

Get to the point. Lengthy intricate sentences with subordinate clauses and digressions lose the reader, who then either rereads or gives up. State what the thing does, who runs it, and what it requires.

Be concise but informative. Use the fewest words that carry the information. Brevity at the cost of clarity is a defect.

Use direct, uncomplicated language. The reader is a technical professional. Vocabulary chosen to impress will dull the document.

Relate to the reader. The manner appropriate for programmers and analysts differs from the manner appropriate for end users or management. Choose one audience per document.

Show, don't tell. A code block, a shell transcript, a command with its output, or a named error demonstrates a claim, and the reader checks it directly. Prose describing the same thing asks the reader to take it on trust, and a technical reader reads the artifact faster than the sentence about it. Lead with the artifact. Prose connects one artifact to the next and supplies only what the artifact cannot show on its own.

## Sentence mechanics

### Verbs

Active verbs carry technical prose. Passive constructions read like cold mashed potatoes. Prefer "the daemon writes the log" over "the log is written by the daemon."

Do not turn verbs into nouns and prop them up with weaker verbs. Write "we will develop a training curriculum," not "we shall provide the development of a training curriculum." Write "establishing standards is essential," not "the establishment of standards is an essential factor."

Stay in one tense. Pick present, past, or future at the top of a passage and hold it through the paragraph.

### Adjectives, adverbs, and intensifiers

Use sparingly. Overworked adjectives such as VERY and GREAT have no place in concise writing. Adverbs such as "significantly," "highly," "dramatically," and "incredibly" are usually dead weight. If a number is available, give the number. Otherwise drop the adverb.

### Redundancy

Cut words that diffuse meaning. "Refer back" is "refer." "End result" is "result." "Facts and figures" is "data." "Totally demolished" is "demolished." Strike duplicate adjectives, hedging qualifiers, and connectives that add no information.

### Ambiguity

Define ambiguous terms on first use. Define every acronym on first use and list all acronyms in a glossary at the end. Treat HASP, BDAM, RPG, JCL, and friends as opaque to the reader until the document makes them transparent. Avoid acronyms in headings and in the first sentence of a section.

### Sentence variety

Continual subject-predicate-object hammering produces flat text. Vary length and structure. A typical paragraph mixes one or two short declaratives with a longer explanatory sentence, then a short sentence to close.

## Structural mechanics

Use formal features (descriptive headings, worked examples, code blocks) to break the monotony of straight text. Examples carry more weight than rules and should appear after every nontrivial claim.

Paragraphs develop a single idea over several sentences. Transitions matter. The last clause of one paragraph should set up the first sentence of the next.

Lists are for items that are genuinely enumerable, such as command flags, error codes, or required dependencies. If a paragraph would do, write the paragraph. Do not chop continuous reasoning into bullets to feign structure.

Code blocks are for code and for shell transcripts. Inline backticks are for identifiers, paths, and short literal values. Italics mark a term on first definition. Bold is reserved for the rare warning that the reader must not miss.

## Prohibited patterns

These appear by default in machine-generated prose. They are out of bounds in every document written under this register.

1. Em dashes (—) and en dashes (–) used for parenthetical insertion or for dramatic pause. Replace with a comma, a pair of parentheses, a semicolon, or a full stop. The same prohibition covers the typographic equivalent spelled with two hyphens.

2. Contrastive framings used for cadence: "not X, but Y," "it isn't just X, it's Y," "X isn't merely Y, it's Z," "more than just X." These supply rhythm in place of information. Replace with the direct assertion of Y.

   The ban covers the empty template, not the act of distinguishing. A corrective negation that carries information stays: "the daemon writes to stdout, not the log file" tells the reader where output does and does not go, and the negated half is the part they needed. An expectation-versus-reality pairing stays when a competent reader would actually hold the expectation: "the second apply looks like it should win; the first one does" teaches a real gotcha. What goes is the pairing whose first half is raised only to be knocked down for rhythm.

   Test: delete the negated half and state Y alone. If nothing is lost, the negation was cadence and the deletion is your sentence. If something is lost, keep the correction but write it flat, as a correction, rather than as balanced antithesis tuned for the ear. Second check: read the "not X" half and ask whether a competent reader would have believed X. If not, X is a straw target and the whole frame goes.

3. Performative headers. A header names the technical content of the section in a plain noun phrase. A header does not perform tone, ask a question, or address the reader. Three failure modes are out of bounds.

   The grandiose variant, drawn from marketing copy: "Unleash the power of...," "Why this matters," "The magic of...," "Transform your workflow," "What makes this special," "Built for scale."

   The chatty variant, drawn from blog and consumer-software README conventions: "What this does," "What this is," "What this owns," "Why this exists," "How it works," "Who this is for," "What you get," "What's inside," "The gist," "At a glance," "TL;DR" used as a heading, and any interrogative or possessive phrasing of the same shape.

   The meta-framing variant, drawn from explainer and pedagogy writing: "Mental model," "Conceptual framework," "Framing," "Setting the stage," "How to think about this," "The big picture," "Approach," "Orientation." These pass the surface noun-phrase test because they are noun phrases, but they name the rhetorical move the section is making rather than the content it carries. They were once visually inert in prose and may have read as conventional academic structure. Today they read as machine-generated default scaffolding and grate on the reader for that reason alone, independent of the section's actual content. Replace with the conventional content name: "Overview," "Architecture," "Background," "Scope."

   Correct headers state the content directly: "Installation," "Configuration," "Command reference," "Error codes," "Architecture," "Dependencies," "Authentication," "Migration from v1," "Limitations," "Background," "Motivation," "Scope," "Non-goals," "Overview."

   Test: rewrite the header as a noun phrase naming the section's content. If the rewrite loses nothing, the rewrite is the header. If the only function the original header served was to introduce the section in a friendly voice or to label the rhetorical orientation, the section does not need a header.

4. Filler openers, including "Let's dive into," "When it comes to," "In today's fast-paced world," "It's worth noting that," "At the end of the day," and "Here's the thing."

5. Filler closers, including "In conclusion," "In summary," "Hopefully this helps," and offers of further help. When the document is done, stop.

6. Fashion vocabulary: leverage, seamless, robust, intuitive, powerful, comprehensive, elegant, cutting-edge, state-of-the-art, best-in-class, holistic, synergy, ecosystem, journey, unlock, empower, supercharge, blazing-fast, battle-tested, first-class. Replace each with concrete description or remove.

7. Tricolons placed for rhythm ("fast, reliable, and secure"; "build, ship, and scale"). One precise adjective beats three placed for cadence.

8. Hedging stacks ("it's important to note that it may be worth considering whether..."). Strip to the assertion.

   The ban covers reflexive softening that reports no actual uncertainty, not calibration. Specific, load-bearing uncertainty stays: "this likely fixes it, but I haven't reproduced the race" tells the reader exactly how far the claim is tested, and that is information. Test: does the qualifier carry information, or is it only lowering the stakes? If it names a real, specific doubt, keep it and state the doubt plainly. If it softens without reporting anything, cut it.

9. Restating the user's request or the document's own title in the opening paragraph.

10. Mid-sentence bold for emphasis. The sentence should carry the emphasis on its own.

11. Filler abstractions: "essentially," "fundamentally," "ultimately," "at its core," "in essence." These usually introduce a restatement of the previous sentence.

12. Decorative dividers, horizontal rules between every section, decorative emoji, and section icons. The structure of the prose is the structure of the document.

13. Sentences that begin with a participial phrase summarizing the previous sentence ("Building on this foundation, ...", "Taking this a step further, ..."). Start the next sentence on its own footing.

14. Announce-then-deliver constructions. A sentence opens with a noun phrase whose only job is to point at the finding that follows, separated from it by a colon. The noun phrase sets the stage; the finding sits after the colon. Examples: "The shift the report flags: the attacker compromised no registry." / "What the data shows: traffic doubled overnight." / "The key takeaway: rollback fixed it." / "Here's what's notable: every failure occurred during a deploy." / "The thing worth flagging: latency spiked at 3am." Drop the announcing phrase. State the finding as a regular sentence, and if attribution belongs, embed it in the sentence itself rather than as a stage-setter: "According to the report, the attacker did not compromise a registry." / "Traffic doubled overnight." / "Rollback fixed it." / "Every failure occurred during a deploy."

    Test: if the noun phrase before the colon can be deleted without losing information, it was announce-then-deliver and goes. The phrase reads as a drum-roll regardless of subject matter, and combined with the lexical tells common to machine-generated prose ("the shift," "the thing," "the move," "the story," "the insight"), it makes the writing sound performed rather than written.

    The pattern is distinct from a colon legitimately introducing a list ("Three things matter here: A, B, C") or a colon legitimately following a clause that carries information of its own ("The fix is straightforward: rebuild the index"). The test discriminates: in the legitimate cases, the before-colon clause carries content that would be lost on deletion.

15. Managerial and business speak. The vocabulary of the status meeting and the quarterly review carries tone and affiliation, not information, and a technical reader hears it as noise. Two families are out of bounds.

    Affirmation phrases that rate the reader or the reader's contribution: "spot on," "nailed it," "you're absolutely right," "great question," "great call," "excellent point," "couldn't agree more," "well put," "you hit the nail on the head," and "100%" used as agreement. A technical document reports a finding and lets the reader judge it. It does not grade the reader. These also break the audience-and-stance rule against rapport-building and flattery, so they go on two counts.

    Coordination and management jargon: "circle back," "touch base," "reach out" (write "email" or "ask"), "loop in," "ping" (write "message" or "ask"), "sync" and "sync up" in the meeting sense, "align" and "alignment" in the agreement sense, "move the needle," "low-hanging fruit," "deep dive," "drill down," "double-click on" used to mean examine, "level-set," "boil the ocean," "take it offline," "run it up the flagpole," "bandwidth" meaning spare time, "actionable," "learnings" (write "lessons" or "findings"), "ask" and "lift" as nouns ("the ask is," "a heavy lift"), "value-add," "win-win," "game-changer," "north star," "table stakes," "going forward," and "moving forward." Replace each with the plain verb or noun it dresses up. "Circle back" is "follow up" or "revisit." "Reach out" is "email." "Move the needle" is "change the result." "Going forward" is "from now on," or nothing.

    The ban targets the corporate sense, not the technical homograph. "Align" the corporate verb goes; memory alignment, text alignment, and sequence alignment stay. "Sync" the meeting goes; `fsync`, clock sync, and "the replica is in sync" stay. "Deep dive" the meeting goes; "dive" in a literal sense is untouched. Read the word in its sentence and ask which sense is present.

    This list overlaps item 6 at "leverage," "synergy," and "ecosystem." The two registers share those words and differ in what they inflate. Fashion vocabulary inflates a technical claim; business speak inflates coordination and agreement. Both go.

    Test: read the sentence as though presenting a slide to management. If it belongs there and a plain verb would carry the same meaning to a technician, the phrase is business speak and the plain verb replaces it.

## Editing pass

Edit every document at least twice, with the goal of cutting rather than adding.

First pass, sentence level. Cut every superfluous adjective, adverb, article, preposition, and relative pronoun. Eliminate "that" where the meaning survives without it. Replace nominalized verbs with active verbs. Strike capitalized intensifiers. Confirm that every acronym is defined on first appearance.

Second pass, document level. Read the document straight through. Confirm that short sentences are interleaved with longer ones, that paragraphs flow into one another, and that the document as a whole serves the purpose stated in its opening. Delete any paragraph that does not advance that purpose, including paragraphs you are fond of.

Third pass, demonstration. Mark each major claim and find the artifact that demonstrates it: the code block, the transcript, the command with its output, the before and after, the named error string, the concrete number. A claim with no nearby artifact is telling to convert into showing, or filler to cut. Run the check in reverse: a code block or quotation that demonstrates no claim is decoration, and decoration goes however transparent it looks. Where a claim resists an artifact, confirm the prose names a specific instance rather than a category, the actual value and command and failure rather than "a setting," "the relevant command," "a failure mode." Last, read the artifacts in sequence on their own, then read the prose between them on its own. The artifacts carry the spine of the document. The prose says what the artifacts cannot show, and stops there.

## Worked example

Bureaucratic original:

> The purpose of this chapter in the Systems Department Procedure Manual is directed toward establishing an understanding of the application, use, and administration of the BRT package.

Edited:

> This chapter explains the application, use, and administration of the BRT package.

Bureaucratic original:

> The minicomputer provided a solution to facilities that could not afford the larger systems. The minis are also used to distribute applications among various divisional and branch offices. This distribution processing will reduce cost, simplify software, and bring data processing under user control.

Edited:

> The minicomputer offers a solution for sites that cannot afford a larger system. A mini also distributes applications across divisional and branch offices, which reduces cost, simplifies software, and places data processing under user control.

(Tense held in the present throughout. Active verbs. Redundant "various" cut.)

Telling:

> The controller resolves duplicate definitions deterministically. When two Ingress objects declare the same host and path, the one created first wins and the later one is ignored, so the order in which you apply and delete objects governs when the cutover takes effect.

Showing:

Apply the second Ingress. The controller logs the definition it dropped:

```
W0612 14:05:34 controller.go:1102] ingress prod-v2/www.example.com:
  host "www.example.com" and path "/" is already defined in ingress prod/www.example.com
```

The older object serves the host until you delete it. The delete is the cutover.

(The telling side asks the reader to trust a description of the controller's behavior. The showing side hands them the log line they will see and two sentences of consequence. The reader checks the rule against the artifact in less time than the paragraph takes to read.)

## Instructions for the LLM consuming this file

Treat the prohibited-patterns list as hard constraints. When a sentence could be written either in the plain technical register described here or in the warmer consumer-facing register typical of default output, choose the plain register every time. When in doubt, prefer the shorter, more concrete construction. Do not soften the tone by adding enthusiasm or rapport-building. The audience is a technical reader who values their time and resents prose that wastes it.

If the source text under revision contains any prohibited pattern, remove the pattern even when the surrounding instructions do not explicitly mention it. The prohibitions apply to the output, not only to additions.

Prefer demonstration over description. Where a claim can be shown with a code block, transcript, command output, or a concrete number, show it and keep the surrounding prose to what the artifact does not make visible.
