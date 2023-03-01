# AnchorWave + PGGB pipeline

Hack PGGB pipeline with AnchorWave

## Software

 - [Anchorwave](https://github.com/baoxingsong/AnchorWave)
 - [PGGB](https://pggb.readthedocs.io/)

## 0. Preprocessing

Using [Pangenome Sequence Naming](https://github.com/pangenome/PanSN-spec) for fasta anf gff files.

The demos in `data` folder show some instance for the input files.

For example, `>LAp_A#1#Chr01` names Chr01 of LAp_A, while `LAp_A` means A homologous chromosome of LAp.

## 1. Run pairwise alignment for all homologous chromosomes

Generate scripts for HPC: `bash 1.pairs_anchorwave.sh`

## 2. Convert alignment results to paf format

`qsub 2.convert_paf.sh`

## 3. Combine the paf files

`for chr in Chr01 Chr02 Chr03 Chr04 Chr05 Chr06 Chr07 Chr08 Chr09 Chr10; do cat *${chr}*.paf > anchorwave.${chr}.paf; done`

## 4. Run PGGB for each chromosome

`pggb -i data/LAp.Chr01.fasta.gz -a anchorwave.Chr01.paf -p 90 -n 8 -k 11 -P asm20 -O 0.03 -G 13033,13177 -t 48 -V LAp_A:# -o LAp.k11 -m`

`-n` means the total number of homologous chromosomes.
