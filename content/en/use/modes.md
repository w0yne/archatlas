---
title: Autonomous or guided
---
# Autonomous or guided

Both modes use the same evidence and quality standards. They differ in who makes the intermediate choices.

## Autonomous

The agent chooses sensible defaults, states assumptions and proceeds. It still asks if a wrong guess would change an important boundary, deployment target or interpretation. Non-interactive runs default to autonomous unless told otherwise.

> Autonomous mode. Draw a logical view of this service for developers. Use the declared configuration, and distinguish inferred connections.

## Guided

The agent asks one consequential question at a time, recommends an option, and waits for wireframe approval before rendering.

**Agent:** Who is the reader: business stakeholders or developers? I recommend a context view for the former and a container view for the latter.

**You:** Developers joining the team.

**Agent:** I recommend a container view showing runnable units and their dependencies. Should we show the current implementation or a proposed design?

## Missing answers are not consent

If a required answer is unavailable, the agent reports the question as needing input. A timeout does not approve a design. No special host-specific question tool is required: ordinary chat works.

## Revising a diagram

Explain what is unclear—ownership, reading order, boundaries or amount of detail. The agent should answer questions in your feedback before redrawing and retain previously accepted decisions.
