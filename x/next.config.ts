import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  trailingSlash: false,
  compiler: {
    removeConsole: false,
  }
};

export default nextConfig;
