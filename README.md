# Afterkeys website

Support and privacy pages for the Afterkeys iPhone app, published with GitHub Pages:

- Support: https://noetheon.github.io/afterkeys/
- Privacy policy: https://noetheon.github.io/afterkeys/privacy.html

The pages are generated from the app's repository, so edit them there rather than here. The
provider's name and contact email aren't stored in this repository: when publishing, the workflow
in `.github/workflows/pages.yml` fills in `{{PROVIDER_NAME}}` and `{{CONTACT_EMAIL}}` from the
repository's Actions variables.
