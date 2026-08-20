# Administration Guide

## Installation

!!! warning "Recommendation"
    Unless you have a strong reason to build the container yourself, it is 
    recommended that you download one of the prebuilt containers.

You can install T2QC either by downloading one of the [prebuilt
containers][Container download], or by [building the container][Container
build] manually.

### Downloading the container
There are prebuilt versions of T2QC hosted on [GitHub Container Registry][GHCR]. 
You can pull any specific version of T2QC using
[Apptainer/Singularity][Apptainer] by running the following command

```bash
singularity build t2qc.sif docker://ghcr.io/harvard-nrg/t2qc:0.3.3
```

### Building the container
To build T2QC as a container, grab the latest `Dockerfile` from [the
repository][Repository] and run the following command

```bash
docker build -t t2qc:latest - < Dockerfile
```

After building the container, you should be able to execute `t2QC.py` with
docker, or build a [Apptainer/Singularity][Apptainer] image from your local
Docker daemon

```bash
docker run t2qc:latest --help
```

## XNAT Integration
The following section will describe how to integrate T2QC into your [XNAT][]
installation by building, installing, and configuring the plugin.

### Building the plugin
Clone the `xnat-1.8` branch from the [T2QC repository][Repository]

```bash
git clone -b xnat-1.8 --single-branch https://github.com/harvard-nrg/t2qc
```

XNAT plugins are built using [Gradle][]. Change your working directory into the
cloned repository directory, and compile the plugin

```bash
cd t2qc
./gradlew jar
```

Once the plugin has been successfully compiled, move the resulting `.jar` into 
your XNAT plugins directory

```bash
mv ./build/libs/t2qc-plugin-1.0.0.jar ${XNAT_HOME}/plugins/
```

[Repository]: https://github.com/harvard-nrg/t2qc
[Apptainer]: https://apptainer.org/
[GHCR]: https://ghcr.io/harvard-nrg/t2qc
[Container download]: #downloading-the-container
[Container build]: #building-the-container
[XNAT]: https://www.xnat.org
[Gradle]: https://gradle.org/install/
