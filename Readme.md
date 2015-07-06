# PyImageQualityRanking 
## An Image quality ranking tool for Microscopy

*PyImageQualityRanking* is a small software utility that allows the ordering/sorting of image datasets, according to image-quality-related statistical parameters. The software is distributed under BSD open source license.

### How does it work?
The purpose of this tool is to extract image-quality-related statistics, and to use them to rank the quality of images within that dataset. Such tool could be used for example to find the highest-quality images in a dataset, or to identify and discard low-quality images. Instead  of trying to estimate image quality. The purpose of the software is to figure out, whether certain images were clearly better than the rest in the dataset, or vice versa.

Our aim was to develop a simple tool that would not involve any complex mathematical models or training schemes – but that could still provide robust quality-related measures, that could be taken advantage of in a variety of applications. The analysis was also intended to be simple and fast, to allow its easy integration to any image-processing workflow – including online during-acquisition analysis. 

*PyImageQualityRanking* software implements two kinds of parameters to rank image quality. 

1. The quality of the image histogram (contrast) is estimated by a Shannon entropy measure, that is calculated at a masked region of an image, to allow the comparison of images with varying content. 
2. The image detail is estimated in the frequency domain, by calculating a number of parameters from the power spectrum. The calculations focus on the power spectrum tail (>40% of Nyquist frequency), because that allowed us to focus exclusively on the fine detail, which is strongly affected by noise and blur.

### How do I install it?
*PyImageQualityRanking* was written in Python, utilizing standard SciPy scientific libraries. The software should thus work on all the common operating systems. *PyImageQualityRanking* does not, at the moment require any installation as such, but it can be run directly from the source code directory. However, one should make sure that the [SciPy libraries](http://www.scipy.org/install.html) have been installed on the computer's Python environment. Typically, if using Anaconda distribution etc. these libraries should have been installed by default.

Please refer to the Wiki page for usage examples.

### Contribution guidelines ###

The *PyImageQualityRanking* is distributed under BSD open-source license. You can use the software in any way you like; we would just ask you to aknowledge our work:

publication here

All kinds of contributions: new features, bug fixes, documentation, usage examples etc. are welcome.

### Contacts ###

Sami Koho <sami.koho@gmail.com>

