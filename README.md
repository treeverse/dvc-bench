## dvc-bench
Benchmarking [dvc](https://github.com/treeverse/dvc) with pytest-benchmark.

### Viewing results

Results are rendered as a Markdown summary on each [workflow run](https://github.com/treeverse/dvc-bench/actions/workflows/build.yml).

### Setting up
```
$ uv pip install -r requirements.txt
$ dvc pull # optional, otherwise will pull datasets dynamically
```

### Running all benchmarks
```console
$ pytest --pyargs dvc.testing.benchmarks
```

### Running one benchmark
```console
$ pytest --pyargs dvc.testing.benchmarks.cli.commands.test_add
```

### CLI options
```
$ pytest -h
...
  --dataset=DATASET
                        Dataset name to use in tests (e.g. tiny/small/large/mnist/etc)
  --dvc-bin=DVC_BIN     Path to dvc binary
  --dvc-revs=DVC_REVS   Comma-separated list of DVC revisions to test (overrides `--dvc-bin`)
  --dvc-repo=DVC_GIT_REPO
                        Path or url to dvc git repo
  --dvc-bench-repo=DVC_BENCH_GIT_REPO
                        Path or url to dvc-bench git repo (for loading benchmark dataset)
  --dvc-install-deps=DVC_INSTALL_DEPS
                        Comma-separated list of DVC installation packages
  --project-rev=PROJECT_REV
                        Project revision to test
  --project-repo=PROJECT_GIT_REPO
                        Path or url to dvc project
...
```

### Comparing results
```
$ pytest-benchmark compare --histogram histograms/ --group-by name --sort name --csv results.csv
```

and if you want beautiful plots:

```
$ dvc repro
$ dvc plots show
```

### Contributing

Benchmark test definitions are now part of [dvc.testing](https://github.com/treeverse/dvc/tree/main/dvc/testing).
