---
title:
date: 2026-09-13
type: landing

sections:
  - block: hero
    content:
      title: |
        NeuroAI Lab
      image:
        filename: lab-home.png
      text: |
        <br>

        **Neuro-Artificial Intelligence Laboratory**, Department of Physiology, Pusan National University School of Medicine.
        We work at the intersection of neuroscience and artificial intelligence: biologically grounded reinforcement learning, computational models of the brain and its disorders, AI-driven drug discovery, and clinical decision support.

        We are recruiting undergraduate interns and graduate students. See [Join](join/).
      cta:
        label: Research
        url: research/
      cta_alt:
        label: People
        url: people/

  - block: markdown
    content:
      title: Research Themes
      text: |
        1. **AI-Accelerated Drug Discovery** — generative models, virtual screening and physics-based simulation for novel therapeutics.
        2. **Brain Data & Neuropsychiatry** — interpretable machine learning on electrophysiology, in-silico epilepsy models, immune–neural crosstalk.
        3. **AI-Driven Clinical Decision Support** — adverse-event prediction, procedure optimisation, clinical language intelligence with LLMs.
        4. **Hippocampus × Reinforcement Learning** — the hippocampus as a Successor Representation agent.

        {{% cta cta_link="research/" cta_text="Read more →" %}}
    design:
      columns: '1'

  - block: collection
    content:
      title: Latest News
      count: 5
      filters:
        folders:
          - post
      order: desc
      page_type: post
    design:
      view: card
      columns: '1'

  - block: collection
    content:
      title: Recent Publications
      count: 5
      filters:
        folders:
          - publication
    design:
      view: citation
      columns: '1'

  - block: markdown
    content:
      text: |
        {{% cta cta_link="people/" cta_text="Meet the team →" %}}
    design:
      columns: '1'
---
