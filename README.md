## About
A centralized repo for updating and maintaining druggable gene categories from multiple curation sources.

## Structure
Curated gene lists are stored within the data directory. There are currently two main sources of gene curations: the miller list (courtesy of Katie Miller at IGM) and the panel app lists. 

The **miller** directory contains the master list of 2217 disease-critical genes as well as additional subdirectories with sorted versions of these lists. Sample divisions thus far are: by source panel, by CGC annotation, by PCGP annotation, or by Mardis annotation. Additional curation efforts to come.

The **panelapp** directory contains all current panels from curation efforts driven by the PanelApp platform. There are two current PanelApp sources, AU and UK, and all panels from these sources have been obtained and stored within the au and uk subdirectories. Currently, the panels stored here are simplified lists containing gene symbol, gene name, and confidence levels for each gene on the panel. The confidence level field corresponds to PanelApp's 'traffic light' system, where a confidence level of 3 is equivalent to a 'green' rating and a 1 is equivalent to a 'red' rating. Additional curation efforts to come.

## Credits
Initial gene lists were pooled together by Katie Miller and her team at the Institute for Genomic Medicine (IGM) at Nationwide Children's Hospital in Columbus, OH. Additional manual curation efforts to maintain this list were done by Olivia Grischow at IGM. 
