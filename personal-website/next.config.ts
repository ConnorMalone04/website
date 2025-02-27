import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  experimental: {
    serverActions: {
      bodySizeLimit: 5 * 1024 * 1024, // 5MB limit
    },
  },
};

export default nextConfig;
