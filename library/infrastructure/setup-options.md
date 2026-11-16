---
layout: content
heading: Setting up Armadillo
subheading: Two options
clicks: 1
---

<FocusCards :items="[
  { title: 'Run it yourself', color: 'var(--c-blue)', body: ['Install Armadillo on your own server or VM', '<strong>Requirements:</strong> Ubuntu LTS, 8–32 GB memory, Java 21, Docker, a domain', '<strong>Configure:</strong> Nginx with SSL, firewall, OIDC login', '<strong>Docs:</strong> <a href=&quot;https://molgenis.github.io/molgenis-service-armadillo/&quot; target=&quot;_blank&quot; style=&quot;color: inherit&quot;>molgenis.github.io/molgenis-service-armadillo</a>'] },
  { title: 'We run it for you', color: 'var(--c-teal)', body: ['MOLGENIS hosts Armadillo on the UMCG Azure cloud', 'Set up and maintained by the team', 'Only you can see and manage the data', 'support@molgenis.org'] },
]" />

<style>
:deep(.tint-card p) { margin-bottom: 0.7rem; }
:deep(.fq-grid .tint-card) { justify-content: flex-start; }
:deep(.tint-card h3) { margin-bottom: 1rem; }
</style>
