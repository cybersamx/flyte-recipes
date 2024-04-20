# Flyte Recipes

<p align="center">
  <img src="https://raw.githubusercontent.com/flyteorg/static-resources/main/flyte/readme/flyte_and_lf.png" alt="Flyte and LF AI & Data Logo" width="250">
</p>

## Overview

Whenever I am new to a platform or framework, I start a git project to serve as a playground and journal for learning the new stuff. This git repo is a collection of notes, learnings, and code for [Flyte](https://github.com/flyteorg/flyte), an open-source orchestrator that facilitates building data and ml pipelines. 

## Recipes

* [Set up flyte sandbox](setup-sandbox) - Set up and run Flyte as a sandbbox in a single (big) Docker container.
* [Set up flyte on a local k8s cluster](k8s-setup) - Set up and run Flyte in a local multi-node k8s cluster, includes dependencies for running flyte in k8s.
* [Flyte example project](official-example) - The official Flyte ["Getting Started"](https://docs.flyte.org/projects/cookbook/en/latest/index.html#creating-a-workflow) example code for getting started.
  * [Value passing between tasks](value-passing)
  * [Primitive passing](value-passing/primitive)

## Reference

* [Flyte Docs: Getting Started](https://docs.flyte.org/projects/cookbook/en/latest/index.html#creating-a-workflow)
