# Presentations

My Slidev presentations.

## Edit in the browser

No local setup needed — open in GitHub Codespaces:

[![Open in Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?repo=timcadman/presentations&ref=master)

Then in the terminal:

```bash
cd molgenis-demonstrator   # or intro-datashield
npm run dev
```

## Local setup

### Prerequisites

- [Node.js](https://nodejs.org/) >= 22.9.0
- npm >= 11.3.0

If you use nvm:

```bash
nvm install 22
nvm use 22
```

## Setup

```bash
git clone git@github.com:timcadman/presentations.git
cd presentations
```

## Running a presentation

Each presentation is a self-contained directory. To run one locally:

```bash
cd intro-datashield   # or molgenis-demonstrator
npm install
npm run dev
```

This starts a local dev server and opens the presentation in your browser.

## Available presentations

| Directory | Topic |
|-----------|-------|
| `intro-datashield` | Introduction to DataSHIELD |
| `molgenis-armadillo` | MOLGENIS Armadillo features |
| `molgenis-demonstrator` | From Data Discovery to Federated Analysis |

## Building for production

```bash
npm run build
```

The built output will be in the `dist/` directory.
