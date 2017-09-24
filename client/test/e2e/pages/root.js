import { URL } from 'url';

module.exports = {
  url: (devServerUrl) => {
    return new URL('/', devServerUrl);
  },
  elements: {
    console: '#console',
    header: '#header',
    breadcrumb: '#breadcrumb',
    main: '#main',
    footer: '#footer',
  },
};
