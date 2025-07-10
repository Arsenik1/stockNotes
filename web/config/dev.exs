import Config

config :web, WebWeb.Endpoint,
  http: [port: 4000],
  check_origin: false,
  code_reloader: true,
  debug_errors: true,
  secret_key_base: String.duplicate("abcdefgh", 8),
  watchers: []

config :web, dev_routes: true
