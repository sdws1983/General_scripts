# DosageGWAS

### 1. prepare genotypes

###### tped file

```bash
(base) [off_huangyumin@node47 SGG1.1]$ head -10 emmax.filtered/emmax_in.Chr01.tped | cut -f1-10
Chr01   Chr01.94344     0       94344   0.232558        0.156863        0       0.105263        0.26087 0.0645161
Chr01   Chr01.97302     0       97302   1.56522 1.13043 1.21875 1.70833 1.82143 1.39535
Chr01   Chr01.97358     0       97358   0.541667        0.666667        0.62069 0.241379        0.102564        0.561798
Chr01   Chr01.97391     0       97391   0.367347        0.789474        0.689655        0.245614        0.157895        0.518519
Chr01   Chr01.97408     0       97408   0.391304        0.873239        0.830189        0.347826        0.216867        0.627907
Chr01   Chr01.97643     0       97643   2       1.75    2       1.76471 1.82857 2
Chr01   Chr01.97693     0       97693   1.55556 1.6     2       1.61905 2       1.71429
Chr01   Chr01.97719     0       97719   1.12    1.38889 0.90566 1.06667 0.884615        1.69231
Chr01   Chr01.97837     0       97837   1.17073 0.873239        0.512821        0.26087 0.307692        1.20988
Chr01   Chr01.97883     0       97883   1.2766  1.08108 0.742857        0.645161        0.6     1.63855
```

###### tfam file

```bash
(base) [off_huangyumin@node47 SGG1.1]$ head -10 emmax.filtered/emmax_in.Chr01.tfam 
AH1803 AH1803 0 0 0 -9
B8 B8 0 0 0 -9
Badila Badila 0 0 0 -9
BC2-32 BC2-32 0 0 0 -9
BH10-12 BH10-12 0 0 0 -9
C323-68 C323-68 0 0 0 -9
C529-50 C529-50 0 0 0 -9
C86-456 C86-456 0 0 0 -9
C88-380 C88-380 0 0 0 -9
C89-147 C89-147 0 0 0 -9
```

###### split each chromosome

```bash
(base) [off_huangyumin@node47 SGG1.1]$ ls emmax.filtered/
emmax_in.Chr01.tfam  emmax_in.Chr02.tfam  emmax_in.Chr03.tfam  emmax_in.Chr04.tfam  emmax_in.Chr05.tfam  emmax_in.Chr06.tfam  emmax_in.Chr07.tfam  emmax_in.Chr08.tfam  emmax_in.Chr09.tfam  emmax_in.Chr10.tfam  emmax_in.tfam
emmax_in.Chr01.tped  emmax_in.Chr02.tped  emmax_in.Chr03.tped  emmax_in.Chr04.tped  emmax_in.Chr05.tped  emmax_in.Chr06.tped  emmax_in.Chr07.tped  emmax_in.Chr08.tped  emmax_in.Chr09.tped  emmax_in.Chr10.tped  emmax_in.tped
```

### 2. prepare kinship

```bash
python3 subsample.py emmax.filtered/emmax_in.tped emmax_in.subsample.tped 111 # "emmax.filtered/emmax_in.tped" is the tped for whole genome 
cp emmax.filtered/emmax_in.tfam emmax_in.subsample.tfam
~/software/emmax-kin-intel64 emmax_in.subsample -x -d 10 -v -o emmax_in.BN.kin
```

### 3. prepare PCs

###### calculate PCA using plink2 (for input files format, refer to "plink2.input.example")

```bash
~/software/plink2 --allow-extra-chr --double-id \
	--import-dosage SGG1.1.dosage format=1 id-delim=+ --export bgen-1.2 id-delim=+ \
	--map SGG1.1.info --psam SGG1.1.fam --threads 20 --pca 20
```

###### convert PCA result to emmax input format

```bash
(base) [off_huangyumin@node47 SGG1.1]$ head -10 emmax_in.cov.txt 
AH1803  AH1803  1       0.0153696       -0.0398399      0.111183        0.0674506       -0.0329693      0.03246 -0.216473       0.0317549       -0.0187931      -0.108505
B8      B8      1       -0.0530921      -0.036896       -0.0373901      0.0560887       -0.0274571      -0.0440858      -0.0140869      0.0290793       0.0254404       0.00511565
Badila  Badila  1       0.0163052       0.0310224       0.177057        0.0169174       0.00914525      0.00385187      -0.176333       0.00228405      -0.176517       0.10541
BC2-32  BC2-32  1       -0.156859       0.0749092       -0.041904       -0.165182       0.0715853       0.0102419       -0.0460365      -0.0501814      0.00264882      0.0266942
BH10-12 BH10-12 1       0.0813739       0.0878479       0.0708368       -0.069155       -0.110234       -0.0183929      0.0505006       -0.0125824      0.0275546       0.000844455
C323-68 C323-68 1       0.0923604       0.0964296       0.0757553       -0.0843486      -0.147167       -0.00770633     0.087313        -0.0520517      0.0377502       -0.0367384
C529-50 C529-50 1       0.0843356       0.0931523       0.0674727       -0.0581996      -0.102655       -0.0162229      0.0278162       -0.0173464      0.0112868       0.0285476
C86-456 C86-456 1       0.0125945       0.0900276       0.0272138       -0.190193       0.0487896       -0.0606795      0.0322792       0.048053        0.0857238       -0.0111665
C88-380 C88-380 1       -0.167254       0.0738998       -0.104399       0.0109833       -0.0953587      -0.0278677      -0.00265571     0.020556        -0.107618       -0.0728166
C89-147 C89-147 1       -0.0979922      0.0651423       0.054407        0.0220486       -0.0689485      -0.0259223      -0.0499778      -0.000249706    -0.0193513      0.0661616
```

### 4. prepare phenotypes

```bash
(base) [off_huangyumin@node47 SGG1.1]$ head traits.GZZTF.txt 
AH1803  AH1803  -0.39321824019312
B8      B8      0.542820779735542
Badila  Badila  NA
BC2-32  BC2-32  -1.27931056580929
BH10-12 BH10-12 -2.48932183825192
C323-68 C323-68 -2.15915652055003
C529-50 C529-50 -1.0981658104215
C86-456 C86-456 1.07110956074961
C88-380 C88-380 -0.241520661789551
C89-147 C89-147 0.798946258319673
```


### 5. run emmax for each chro

```bash
dir="emmax"
out="res"

mkdir -p $out

for i in `seq -w 1 10`;do
for t in GZZTF ZXWF TCD ZGD ZZZTF HYTF SCD ZLCD;do
#for t in Elongation2 Elongation3 Elongation4 Seedling2 Seedling3 Mature2 Mature3 Mature4;do
~/software/emmax-intel64 -t ${dir}/emmax_in.Chr${i} -o ${out}/emmax.Chr${i}.${t}.qk -p traits.${t}.txt -k emmax_in.BN.kin -c emmax_in.cov.txt -Z
done
done
```
