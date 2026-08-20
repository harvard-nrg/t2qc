# Developer Guide

## Dependencies
T2QC is built upon [MRIQC][] and [volumetric navigators][vNav] software 
packages. The [container][Container] is based on Rocky Linux.

| Package         | Version    | Download                              |
|-----------------|------------|---------------------------------------|
| [Rocky Linux][] | `8`        | [:material-download:][Rocky Linux DL] |
| [Freeview][]    | `6.0.0`    | [:material-download:][Freeview DL]    |
| [MRIQC][]       | `0.16.1`   | [:material-download:][MRIQC DL]       |
| [FSL][]         | `6.0.4`    | [:material-download:][FSL DL]         |
| [AFNI][]        | `latest`   | [:material-download:][AFNI DL]        |
| [ANTs][]        | `2.2.0`    | [:material-download:][ANTs DL]        |
| [dcm2niix][]    | `1.0.20200331` | [:material-download:][dcm2niix DL] |
| [vNav][]        | `0.3.1`    | [:material-download:][vNav DL]        |

## Pipeline overview
### MRIQC
[MRIQC][] is a well-known tool designed to automate quality control and 
extraction of image quality metrics from MRI brain images. MRIQC generates an
HTML report that contains mosaic views of the brain, and computes a comprehensive 
set of image quality metrics.

#### `mriqc`
T2QC runs the main `mriqc` command at the `participant` level

```bash
mriqc --participant_label ${SUBJECT} --session-id ${SESSION} --run-id ${RUN}
--work-dir ${WORKING_DIR} --verbose-reports --float32 --n_procs 2 --no-sub
${INPUT_DIR} ${OUTPUT_DIR} participant
```

### vNav
[Volumetric navigators][vNav], or "vNavs", are rapid, low-resolution 3D volume 
scans slotted into the natural pauses within a longer T1- or T2-weighted 
structural MRI sequence. These navigator volumes are used to track and correct 
for head motion, in real time, without needing additional hardware.

#### `parse_vNav_Motion.py`
The `parse_vNav_Motion.py` command extracts vNav tracking data from the metadata
(DICOM headers) of T2-weighted MRI data, and generates useful head 
motion metrics and plots. These motion metrics and plots reflect millimeter 
shifts (RMS and Max) over the timeline of the sequence

```bash
parse_vNav_Motion.py --tr ${TR} --rms --max --plot --input-dir ${DICOM_DIR} --output-dir ${OUTPUT_DIR}
```

### Snapshots
T2QC generates an axial mosaic image of the T2-weighted scan using [Freeview][].
The pipeline uses [FSL][]'s `bet2` to create a brain mask, determines the 
brain boundaries, then captures evenly-spaced axial slices using Freeview in 
headless mode (via `xvfb-run`). Each slice is cropped, captioned with its 
slice number, and assembled into a mosaic image.

```bash
bet2 ${T2W_IMAGE} ${OUTPUT_ROOT} -m -n
```

```bash
xvfb-run freeview -v ${T2W_IMAGE} -layout 1 -cc -nocursor -viewsize ${X} ${Y}
-viewport axial -slice ${X} ${Y} ${Z} -ss ${OUTPUT_FILE}
```

[Freeview]: https://surfer.nmr.mgh.harvard.edu/
[Freeview DL]: https://github.com/freesurfer/freesurfer/releases/tag/v6.0.0
[MRIQC]: https://mriqc.readthedocs.io/en/latest/
[MRIQC DL]: https://github.com/nipreps/mriqc/releases/tag/0.16.1
[vNav]: https://github.com/harvard-nrg/vnav
[vNav DL]: https://pypi.org/project/vnav/0.3.1/
[FSL]: https://fsl.fmrib.ox.ac.uk/fsl/
[FSL DL]: https://fsl.fmrib.ox.ac.uk/fsldownloads_registration
[AFNI]: https://afni.nimh.nih.gov/
[AFNI DL]: https://afni.nimh.nih.gov/pub/dist/doc/htmldoc/background_install/main_toc.html
[ANTs]: http://stnava.github.io/ANTs/
[ANTs DL]: https://github.com/ANTsX/ANTs/releases/tag/v2.2.0
[dcm2niix]: https://github.com/rordenlab/dcm2niix
[dcm2niix DL]: https://github.com/rordenlab/dcm2niix/releases/tag/v1.0.20200331
[Rocky Linux]: https://rockylinux.org/
[Rocky Linux DL]: https://hub.docker.com/layers/library/rockylinux/8
[Container]: ../admin#downloading-the-container
