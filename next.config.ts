import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  output: 'standalone',
  trailingSlash: false,
  experimental: {
    optimizeCss: true,
  },
  compiler: {
    removeConsole: false,
  }
};

export default nextConfig;
