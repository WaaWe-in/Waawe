/*
 * SITE SETTINGS — the only file you normally need to edit.
 *
 * FORMS: the homepage contact form emails Thewaawe@gmail.com through FormSubmit.co (free, no account).
 * FIRST TIME ONLY: after the site is live, submit the form once. FormSubmit emails an "Activate" link to
 * that address; click it and all future enquiries arrive in the inbox.
 *
 * To switch to another service instead, replace formEndpoint. Alternatives:
 *
 *   • Formspree  (https://formspree.io)   → formEndpoint: "https://formspree.io/f/xxxxxxxx"
 *   • Web3Forms  (https://web3forms.com)  → formEndpoint: "https://api.web3forms.com/submit"
 *                                            formFields:   { access_key: "YOUR-ACCESS-KEY" }
 *
 * The homepage contact form is the only form on the site.
 */
window.SITE_CONFIG = {
  formEndpoint: "https://formsubmit.co/ajax/Thewaawe@gmail.com",
  formFields: { _template: "table", _captcha: "false" }
};
