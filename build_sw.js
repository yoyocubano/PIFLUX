const workboxBuild = require('workbox-build');

const buildSW = () => {
  return workboxBuild.generateSW({
    globDirectory: './',
    globPatterns: [
      '**/*.{html,json,js,css}',
      'assets/**/*.{png,jpg,svg}'
    ],
    swDest: './sw.js',
    runtimeCaching: [{
      urlPattern: ({url}) => url.origin === 'https://fonts.googleapis.com' || url.origin === 'https://fonts.gstatic.com' || url.origin === 'https://cdn.tailwindcss.com',
      handler: 'StaleWhileRevalidate',
    }]
  });
};

buildSW();
