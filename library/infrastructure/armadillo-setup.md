---
layout: content
heading: Setting up Armadillo
subheading: What you need first
---

<div class="setup-split">
<div>

<v-clicks>

- **Server or VM** running Ubuntu Server LTS
- **Java 21** and **Docker**
- **A domain name**, e.g. `armadillo.cohort.org`
- **An SSL certificate** for that domain
- **An OIDC client** from an authentication server

</v-clicks>

</div>
<div>

| Participants | Memory | Disk | Cores |
|---|---|---|---|
| 0–20,000 | 8 GB | 100 GB | 4 |
| 20,000–70,000 | 16 GB | 100 GB | 4 |
| 70,000 + | 32 GB | 150 GB | 8 |

<p class="setup-note">Larger for dsOmics — ask the team.</p>

</div>
</div>

---
layout: content
heading: Setting up Armadillo
subheading: Install
---

Install the dependencies, then run the setup script:

```bash
apt update
apt install openjdk-21-jre-headless docker.io

wget https://raw.githubusercontent.com/molgenis/\
molgenis-service-armadillo/master/scripts/install/armadillo-setup.sh
chmod u+x armadillo-setup.sh
```

<div v-click>

```bash
bash armadillo-setup.sh \
    --admin-user admin --admin-password xxxxx \
    --domain armadillo.cohort.org \
    --oidc --oidc_url https://lifecycle-auth.molgenis.org \
    --oidc_clientid clientid --oidc_clientsecret secret
```

</div>

<p class="setup-note" v-click>Armadillo is now a <code>systemd</code> service listening on port 8080.</p>

---
layout: content-two-cols
heading: Setting up Armadillo
subheading: Authentication
leftWidth: '50'
---

::left::

**You send the consortium**

<v-clicks>

- Your Armadillo domain
- The data manager's email address — they get admin rights
- Which project you belong to

</v-clicks>

::right::

**They send back**

<v-clicks>

- An OIDC service URL
- A client ID
- A client secret

</v-clicks>

<p class="setup-note" v-click>Authentication is delegated; your data manager still controls who sees what.</p>

---
layout: content
heading: Setting up Armadillo
subheading: Nginx reverse proxy
---

Armadillo listens on `localhost:8080`. Nginx puts it on your domain:

```nginx
server {
  listen 80;
  server_name armadillo.cohort.org;
  location / {
    proxy_pass http://localhost:8080;
    client_max_body_size 0;
    proxy_read_timeout 600s;
    proxy_redirect http://localhost:8080/ $scheme://$host/;
    proxy_set_header Host $host;
    proxy_http_version 1.1;
  }
}
```

<p class="setup-note" v-click>A <code>502 Bad Gateway</code> here usually means Armadillo has not finished starting.</p>

---
layout: content
heading: Setting up Armadillo
subheading: SSL certificate
---

<v-clicks>

- Nothing goes on the server until the browser shows **https**
- Get a certificate for your domain — Let's Encrypt, or your institution's
- Point Nginx at it and redirect port 80 to 443
- MOLGENIS publishes a worked `armadillo-nginx.conf` you can copy

</v-clicks>

<p class="setup-note">On SELinux hosts: <code>setsebool -P httpd_can_network_connect on</code></p>

---
layout: content
heading: Setting up Armadillo
subheading: Firewall
---

<v-clicks>

- The server should not be open to the whole internet
- Allow **the central analysis server** — where researchers run their code
- Allow **your data managers' IP addresses** — for uploading and managing data
- Everything else is refused

</v-clicks>

<p class="setup-note" v-click>Only aggregate results ever leave, but the fewer doors the better.</p>

---
layout: content-two-cols
heading: Setting up Armadillo
subheading: Running it
leftWidth: '50'
---

::left::

**Day to day**

```bash
systemctl status armadillo
systemctl stop armadillo
systemctl start armadillo
```

::right::

**Back up**

<v-clicks>

- `/usr/share/armadillo` — the data
- `/etc/armadillo` — the configuration
- Your own `datadir`, if you set one

</v-clicks>

<p class="setup-note" v-click>Guide: <a href="https://molgenis.github.io/molgenis-service-armadillo/">molgenis.github.io/molgenis-service-armadillo</a></p>
