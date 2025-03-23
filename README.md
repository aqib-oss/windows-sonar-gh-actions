# windows-sonar-gh-actions

## Table of Contents

- [windows-sonar-gh-actions](#windows-sonar-gh-actions)

  - [Table of Contents](#table-of-contents)
  - [Purpose of this repository](#purpose-of-this-repository)
    - [The issue](#the-issue)
    - [The solution](#the-solution)
  - [Links and stats](#links-and-stats)
  - [Next steps](#next-steps)

## Purpose of this repository

Demonstrating how to use Sonar scan for GitHub Actions using the Windows OS (`windows-latest`).
This is for CI-based analysis, not automatic analysis by SonarQube.

### The issue

- The official SonarCloud GitHub action only works with Ubuntu (Linux) OS (`ubuntu-latest`).
  - <https://github.com/SonarSource/sonarqube-scan-action>
  - <https://github.com/SonarSource/sonarcloud-github-action> (deprecated)
- However, your production environment may use Windows OS, so, you would want to run your tests and analysis using the same. There can also be packages and code that only runs on Windows OS.

### The solution

- So, we use install and use SonarScanner CLI directly in our GitHub Actions workflows. :bulb:
- We also use the GitHub cache action so that we don't have to install the Sonar scanner CLI every time and can just get it from the cache.
  - <https://github.com/actions/cache>

## Links and stats

- This project on SonarQube Cloud: <https://sonarcloud.io/project/configuration?id=aqib-oss_windows-sonar-gh-actions>
- [How to contribute - setup, PR, etc.](CONTRIBUTING.md)

| Source                        | Status                                                                                                                                                                                                                |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| GitHub Actions main workflow  | [![main-workflow](https://github.com/aqib-oss/windows-sonar-gh-actions/actions/workflows/main-workflow.yaml/badge.svg)](https://github.com/aqib-oss/windows-sonar-gh-actions/actions/workflows/main-workflow.yaml)    |
| GitHub Action PR workflow     | [![pr-workflow](https://github.com/aqib-oss/windows-sonar-gh-actions/actions/workflows/pr-workflow.yaml/badge.svg)](https://github.com/aqib-oss/windows-sonar-gh-actions/actions/workflows/pr-workflow.yaml)          |
| SonarQube Quality Gate status | [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=aqib-oss_windows-sonar-gh-actions&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=aqib-oss_windows-sonar-gh-actions) |
| SonarQube Code Coverage       | [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=aqib-oss_windows-sonar-gh-actions&metric=coverage)](https://sonarcloud.io/summary/new_code?id=aqib-oss_windows-sonar-gh-actions)                |

## Next steps

- Convert this into a GitHub action that anyone can easily use as a step in their GitHub workflow just like the official action that uses Ubuntu.
