# MIRACLE

**Mapping the IRES Regulatory Architecture and Conformational Landscape Engineering in Circular mRNA**

## Overview

MIRACLE is a computational pipeline for designing TNA "plug-in" oligonucleotides that stabilize functional IRES conformations in circular RNA.

⚠️ This version is **IRES-only** and does NOT include ORF regions.

## Features

- RNA secondary structure analysis (RNAfold)
- Accessibility profiling (RNAplfold)
- Binding energy prediction (RNAup)
- Duplex stability evaluation (RNAcofold)
- Automated TNA candidate ranking

## Installation

```bash
conda install -c bioconda viennarna
pip install pandas