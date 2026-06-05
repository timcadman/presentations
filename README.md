# Presentations

Slidev presentations for the MOLGENIS team.

## Prerequisites

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
| `molgenis-demonstrator` | From Data Discovery to Federated Analysis |

## Building for production

```bash
npm run build
```

The built output will be in the `dist/` directory.
