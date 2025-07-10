import Config

config :web, WebWeb.Endpoint,
  url: [host: System.get_env("PHX_HOST") || "example.com", port: 80],
  cache_static_manifest: "priv/static/cache_manifest.json",
  secret_key_base: System.get_env("SECRET_KEY_BASE") || "prodsecret"
