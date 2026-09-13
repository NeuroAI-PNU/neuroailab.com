---
title: Research
date: 2026-09-13
type: landing

sections:
  - block: markdown
    content:
      title: Research
      text: |
        <img class="research-map-wide" src="research-map.svg" alt="Research map: molecule to behavior × computational model to clinical data" data-zoomable>
        <img class="research-map-mobile" src="research-map-mobile.svg" alt="Research map: molecule to behavior × computational model to clinical data" data-zoomable>
        <p style="text-align:center;font-size:0.85em;color:#666">Figures: FAK activator graphical abstract ([Comput Biol Chem 2025](../publication/yoon-2025/), © Elsevier), KMU-11342 ([Pharmaceuticals 2026](../publication/jeon-2026/), CC BY 4.0), ACh-gain landscape, Supplementary Fig. S1 ([Cognitive Neurodynamics 2026](../publication/seo-2026/), open access), T-maze and cumulative-reward curves ([Sensors 2024](../publication/seo-2024/), CC BY 4.0), CASCADE ([Bioinformatics 2026](../publication/avila-2026/), CC BY 4.0), SNOMED-CT mapping ([Med Biol Eng Comput 2026](../publication/oh-2026/), open access), symbolic regression vs machine-learning classifiers, ROC ([Biomedicines 2026](../publication/oh-2026-2/), CC BY 4.0).</p>

        ## 1. AI-Accelerated Drug Discovery

        We combine virtual screening, AI-based property prediction and physics-based simulation to find and explain new therapeutic candidates, then close the loop with wet-lab collaborators. Our FAK-activator study coupled similarity-based screening, docking and deep-learning predictors with molecular dynamics to select compounds with better binding profiles than the reference ligand ([Comput Biol Chem 2025](../publication/yoon-2025/)). With Keimyung University we characterised two indolin-2-one kinase inhibitors: KMU-11342 suppresses proliferation, migration and stemness of colorectal cancer cells in 2D, 3D spheroid and patient-derived organoid models, with kinase profiling and docking pointing to GSK3β/CDK1 regulation through p53/NF-κB and FoxO1 signalling ([Pharmaceuticals 2026](../publication/jeon-2026/)); KMU-11361 attenuates rheumatoid arthritis by inhibiting the TAK1–NF-κB–NLRP3 axis ([Inflammation Research 2026](../publication/baek-2026/)). Ongoing work targets nervous-system disorders, including selective modulators of the lysosomal ion channel TMEM175 and drug discovery for REM sleep behaviour disorder.

        ## 2. Brain Data & Neuropsychiatry

        We build interpretable analysis pipelines across scales, from single-cell electrophysiology to population recordings. We showed that a neuron's transgenic marker can be predicted from its electrophysiological properties alone ([Brain Res Bull 2019](../publication/seo-2019/)), and human cortical recordings revealed that the net synaptic drive onto fast-spiking interneurons is inverted towards inhibition in FCD type I epilepsy ([Nature Communications 2024](../publication/cho-2024/)). Because every multi-electrode array manufacturer ships its own closed software, we released CASCADE, an open-source Python pipeline that reads recordings from five MEA platforms and computes standard network metrics together with criticality and avalanche statistics ([Bioinformatics 2026](../publication/avila-2026/)). We also analyse immune–neural crosstalk in Alzheimer's disease with immune cell-enriched single-cell RNA-seq ([J Neuroimmunol 2025](../publication/kang-2025/)), benchmark end-to-end EEG-based stress detection ([IEEE Access 2026](../publication/kim-2026/)), and are constructing in-silico epilepsy models with NEURON and NetPyNE, including mechanistic analysis of Nav1.2 variants linked to developmental and epileptic encephalopathy. Earlier work links neurogenesis-driven pattern separation to mood disorders ([J Korean Soc Biol Ther Psychiatry 2020](../publication/lee-2020/)).

        ## 3. AI-Driven Clinical Decision Support

        Our clinical work favours models that clinicians can read. We fine-tuned ClinicalBERT to map free-text diagnosis spans in electronic medical records to SNOMED-CT concepts and analysed how the latent space separates ambiguous from clearly distinct diagnoses ([Med Biol Eng Comput 2026](../publication/oh-2026/)). For liver-transplant recipients we derived an intuitive risk equation for post-transplant bloodstream infection with symbolic regression, and SHAP analysis highlighted EBV/HBV serological markers as candidate risk factors beyond routine laboratory values ([Biomedicines 2026](../publication/oh-2026-2/)). Earlier studies used machine learning to distinguish cytomegalovirus from herpes simplex esophagitis on endoscopy ([Scientific Reports 2021](../publication/lee-2021/)), tested whether endoscopists can tell GAN-generated gastroscopy images from real ones ([J Digit Imaging 2023](../publication/shin-2023/)), and examined the obesity paradox in colorectal cancer with TCGA cohorts ([J Cancer 2023](../publication/lim-2023-2/)). Our early perspective on ChatGPT in medical education is among the most cited papers on the topic ([Anat Sci Educ 2024](../publication/lee-2024/)).

        ## 4. Hippocampus × Reinforcement Learning

        We test the hypothesis that the hippocampus implements the successor representation and ask how neuromodulators shape its learning rules ([Biosystems 2022](../publication/lee-2022/); [Front Comput Neurosci 2025](../publication/lee-daou-2025/)). Simulation studies showed how weight initialisation affects successor-feature learning ([Electronics 2023](../publication/lee-2023/)), how predecessor and successor features transfer in noisy T-maze tasks ([Sensors 2024](../publication/seo-2024/)), and how both algorithms tolerate noise in one- and two-dimensional environments ([Sensors 2025](../publication/lee-2025/)). Most recently we proposed an acetylcholine-modulated predecessor-feature model in which eligibility-trace–gated depression lets an agent keep exploring after reward; in n-arm radial maze simulations it outperforms the standard model within an effective range of modulation that narrows as environments grow more complex ([Cognitive Neurodynamics 2026](../publication/seo-2026/)).

        > "From synapse to silicon, insight travels — and patient care transforms."

        {{% cta cta_link="../publication/" cta_text="All publications →" %}}
    design:
      columns: '1'
---
